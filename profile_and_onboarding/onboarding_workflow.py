# profile_and_onboarding/onboarding_workflow.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from typing import Dict, Any, Optional
from .schema import (
    OnboardConditionsResponse, OnboardMedicationsResponse, OnboardRoutinesResponse,
    OnboardingPreviewResponse, Condition, Medication, Routine
)
from .tools import save_onboarding_progress, finalize_onboarding, get_onboarding_progress
from .storage import get_profile_store
from core.ontology import normalize_condition
from datetime import datetime, timezone

# Onboarding agents with structured outputs
conditions_agent = Agent(
    name="ConditionsOnboardingAgent",
    model=OpenAIChat(id="gpt-4o-mini-2024-07-18"),
    response_model=OnboardConditionsResponse,
    instructions=[
        "Extract health conditions from user input with confidence scoring.",
        "Use medical terminology and normalize condition names.",
        "Only include conditions explicitly mentioned by the user.",
        "If unsure about any condition, set needs_clarification=True and ask a specific question.",
        "Common conditions include: Migraine, Tension Headache, Cluster Headache, Asthma, Acid Reflux, Sleep Disorders.",
        "Be precise and don't assume conditions not explicitly mentioned."
    ]
)

medications_agent = Agent(
    name="MedicationsOnboardingAgent", 
    model=OpenAIChat(id="gpt-4o-mini-2024-07-18"),
    response_model=OnboardMedicationsResponse,
    instructions=[
        "Extract medications from user input. Accept partial information and don't over-clarify.",
        "Examples: 'ubrelvy' → name='Ubrelvy', type='abortive' (assume common medication types)",
        "Examples: 'Ubrelvy 25mg' → name='Ubrelvy', dose='25mg', type='abortive'",
        "Examples: 'Pantoprazole morning' → name='Pantoprazole', schedule='morning', type='other'",
        "If user provides just a medication name, extract it and set reasonable defaults.",
        "Common migraine medications like Ubrelvy, Nurtec, Imitrex are typically 'abortive' type.",
        "Preventative medications include propranolol, topiramate, amitriptyline.",
        "Only set needs_clarification=True if the input is truly unclear or not medication-related.",
        "Always create at least one medication entry if user mentions any medication name."
    ]
)

routines_agent = Agent(
    name="RoutinesOnboardingAgent",
    model=OpenAIChat(id="gpt-4o-mini-2024-07-18"),
    response_model=OnboardRoutinesResponse,
    instructions=[
        "Extract health-related routines from user input.",
        "Categorize routines as: sleep, hydration, exercise, stress, nutrition.",
        "Create clear pattern descriptions (e.g., 'Sleep 22:00-06:00', 'Water 8 glasses daily').",
        "If routine details are vague, set needs_clarification=True.",
        "Focus on regular, health-maintaining activities.",
        "Include frequency information when provided."
    ]
)

preview_agent = Agent(
    name="OnboardingPreviewAgent",
    model=OpenAIChat(id="gpt-4o-mini-2024-07-18"),
    response_model=OnboardingPreviewResponse,
    instructions=[
        "Present a summary of collected profile information for user confirmation.",
        "Allow user to confirm or request edits to specific sections.",
        "Respond with appropriate action based on user feedback.",
        "If user says 'confirm', 'yes', 'yes please', 'looks good', 'that's right', 'correct', respond with action='confirm'.",
        "If user wants to edit conditions, respond with action='edit_conditions'.",
        "If user wants to edit medications, respond with action='edit_medications'.",
        "If user wants to edit routines, respond with action='edit_routines'."
    ]
)

class OnboardingWorkflow:
    """Complete onboarding workflow with resumable state"""
    
    def __init__(self):
        self.current_step = 0
        self.session_state = {}
        self.steps = [
            "conditions",
            "medications", 
            "routines",
            "preview"
        ]
    
    def run(self, message: str = None, session_id: str = "anonymous", **kwargs) -> dict:
        """Run onboarding workflow with state management"""
        try:
            # Initialize or load session state
            if not hasattr(self, 'session_state') or not self.session_state:
                self.session_state = {
                    "step_index": 0,
                    "partial_profile": {},
                    "user_id": session_id,
                    "completed": False
                }
            
            # Determine current step
            current_step_name = self.steps[self.session_state.get("step_index", 0)]
            
            # Route to appropriate step handler
            if current_step_name == "conditions":
                return self._handle_conditions_step(message)
            elif current_step_name == "medications":
                return self._handle_medications_step(message)
            elif current_step_name == "routines":
                return self._handle_routines_step(message)
            elif current_step_name == "preview":
                return self._handle_preview_step(message)
            else:
                return {
                    "content": "Onboarding completed! You can now start logging your health data.",
                    "metadata": {"onboarding_completed": True}
                }
                
        except Exception as e:
            return {
                "content": f"Error during onboarding: {str(e)}. Please try again.",
                "metadata": {"error": True}
            }
    
    def _handle_conditions_step(self, message: str) -> dict:
        """Step 1: Collect health conditions"""
        if not message:
            return {
                "content": "Welcome to the Health Companion onboarding! Let's start by learning about your health conditions. What health conditions are you currently managing? (e.g., migraines, asthma, etc.)",
                "metadata": {"step": "conditions", "awaiting_input": True}
            }
        
        # Run conditions extraction
        agent_response = conditions_agent.run(message)
        
        # Extract structured data from RunResponse object
        if hasattr(agent_response, 'content') and hasattr(agent_response.content, 'needs_clarification'):
            # Agno v2 RunResponse with structured content
            result = agent_response.content
        elif hasattr(agent_response, 'needs_clarification'):
            # Direct structured response (fallback/mock mode)
            result = agent_response
        else:
            # Fallback if structure is unexpected
            return {
                "content": "I had trouble processing your conditions. Could you please list your health conditions again?",
                "metadata": {"error": True, "step": "conditions"}
            }
        
        if result.needs_clarification:
            return {
                "content": result.clarification_question or "Could you provide more details about your conditions?",
                "metadata": {"needs_clarification": True, "step": "conditions"}
            }
        
        # Save progress
        self.session_state["partial_profile"]["conditions"] = [
            {
                "name": normalize_condition(condition) or condition,
                "status": "active",
                "source": "onboarding",
                "started_at": datetime.now(timezone.utc).isoformat()
            }
            for condition in result.conditions
        ]
        self.session_state["step_index"] = 1
        
        conditions_list = ', '.join(result.conditions) if result.conditions else "none mentioned"
        return {
            "content": f"Thank you! I've noted these conditions: {conditions_list}. Now, what medications are you currently taking? Please include dosages if you know them.",
            "metadata": {"confidence": result.confidence, "step_completed": "conditions"}
        }
    
    def _handle_medications_step(self, message: str) -> dict:
        """Step 2: Collect medications"""
        if not message:
            return {
                "content": "What medications are you currently taking? Please include dosages and schedules if you know them.",
                "metadata": {"step": "medications", "awaiting_input": True}
            }
        
        agent_response = medications_agent.run(message)
        
        # Extract structured data from RunResponse object
        if hasattr(agent_response, 'content') and hasattr(agent_response.content, 'needs_clarification'):
            # Agno v2 RunResponse with structured content
            result = agent_response.content
        elif hasattr(agent_response, 'needs_clarification'):
            # Direct structured response (fallback/mock mode)
            result = agent_response
        else:
            # Fallback if structure is unexpected
            return {
                "content": "I had trouble processing your medications. Could you please list your current medications again?",
                "metadata": {"error": True, "step": "medications"}
            }
        
        if result.needs_clarification:
            return {
                "content": result.clarification_question or "Could you provide more details about your medications?",
                "metadata": {"needs_clarification": True, "step": "medications"}
            }
        
        # Save progress and ensure medications were extracted
        if not result.medications:
            return {
                "content": "I didn't find any medications in your response. Could you please tell me what medications you're currently taking? (You can just list the names if you don't know dosages)",
                "metadata": {"needs_clarification": True, "step": "medications"}
            }
        
        medications_data = []
        for med in result.medications:
            med_dict = med.dict() if hasattr(med, 'dict') else med.model_dump()
            med_dict.update({
                "source": "onboarding", 
                "started_at": datetime.now(timezone.utc).isoformat()
            })
            medications_data.append(med_dict)
        
        self.session_state["partial_profile"]["medications"] = medications_data
        self.session_state["step_index"] = 2
        
        med_count = len(result.medications)
        return {
            "content": f"Got it! I've recorded {med_count} medications. Finally, do you have any daily routines that help manage your health? (e.g., sleep schedule, exercise, hydration habits)",
            "metadata": {"confidence": result.confidence, "step_completed": "medications"}
        }
    
    def _handle_routines_step(self, message: str) -> dict:
        """Step 3: Collect routines"""
        if not message:
            return {
                "content": "Do you have any daily routines that help manage your health? (e.g., sleep schedule, exercise, hydration habits)",
                "metadata": {"step": "routines", "awaiting_input": True}
            }
        
        agent_response = routines_agent.run(message)
        
        # Extract structured data from RunResponse object
        if hasattr(agent_response, 'content') and hasattr(agent_response.content, 'needs_clarification'):
            # Agno v2 RunResponse with structured content
            result = agent_response.content
        elif hasattr(agent_response, 'needs_clarification'):
            # Direct structured response (fallback/mock mode)
            result = agent_response
        else:
            # Fallback if structure is unexpected
            return {
                "content": "I had trouble processing your routines. Could you please describe your daily health routines again?",
                "metadata": {"error": True, "step": "routines"}
            }
        
        if result.needs_clarification:
            return {
                "content": result.clarification_question or "Could you provide more details about your routines?",
                "metadata": {"needs_clarification": True, "step": "routines"}
            }
        
        # Save progress (routines can be empty - user might not have specific routines)
        routines_data = []
        for routine in result.routines:
            routine_dict = routine.dict() if hasattr(routine, 'dict') else routine.model_dump()
            routine_dict.update({"last_confirmed_at": datetime.now(timezone.utc).isoformat()})
            routines_data.append(routine_dict)
        
        self.session_state["partial_profile"]["routines"] = routines_data
        self.session_state["step_index"] = 3
        
        # Immediately transition to preview and show summary
        return self._handle_preview_step(None)
    
    def _handle_preview_step(self, message: str) -> dict:
        """Step 4: Preview profile and get confirmation"""
        partial_profile = self.session_state.get("partial_profile", {})
        
        # If message is None, show the summary (first time in preview)
        if message is None:
            # Show profile summary for confirmation
            summary_parts = ["Here's your health profile summary:"]
            
            conditions = partial_profile.get("conditions", [])
            if conditions:
                condition_names = [c["name"] for c in conditions]
                summary_parts.append(f"**Conditions:** {', '.join(condition_names)}")
            
            medications = partial_profile.get("medications", [])
            if medications:
                med_descriptions = []
                for m in medications:
                    med_desc = m["name"]
                    if m.get("dose"):
                        med_desc += f" ({m['dose']})"
                    med_descriptions.append(med_desc)
                summary_parts.append(f"**Medications:** {', '.join(med_descriptions)}")
            
            routines = partial_profile.get("routines", [])
            if routines:
                routine_desc = [f"{r['category']}: {r['pattern']}" for r in routines]
                summary_parts.append(f"**Routines:** {', '.join(routine_desc)}")
            
            summary = "\n\n".join(summary_parts)
            summary += "\n\nWould you like to **confirm** this profile, or **edit** any section (conditions, medications, routines)?"
            
            return {
                "content": summary,
                "metadata": {"awaiting_confirmation": True, "step": "preview"}
            }
        
        # User is responding to the summary - process their confirmation response
        agent_response = preview_agent.run(f"User response to profile summary: {message}")
        
        # Extract structured data from RunResponse object
        if hasattr(agent_response, 'content') and hasattr(agent_response.content, 'action'):
            # Agno v2 RunResponse with structured content
            result = agent_response.content
        elif hasattr(agent_response, 'action'):
            # Direct structured response (fallback/mock mode)
            result = agent_response
        else:
            # Fallback if structure is unexpected
            return {
                "content": "I didn't understand that response. Please say 'confirm' to save your profile, or 'edit conditions/medications/routines' to modify a section.",
                "metadata": {"error": True, "step": "preview"}
            }
        
        if result.action == "confirm":
            # Finalize onboarding
            return self._finalize_profile()
            
        elif result.action == "edit_conditions":
            self.session_state["step_index"] = 0
            return {
                "content": "Let's update your conditions. What health conditions are you currently managing?",
                "metadata": {"editing_section": "conditions", "step": "conditions"}
            }
            
        elif result.action == "edit_medications":
            self.session_state["step_index"] = 1
            return {
                "content": "Let's update your medications. What medications are you currently taking?",
                "metadata": {"editing_section": "medications", "step": "medications"}
            }
            
        elif result.action == "edit_routines":
            self.session_state["step_index"] = 2
            return {
                "content": "Let's update your routines. What daily health routines do you follow?",
                "metadata": {"editing_section": "routines", "step": "routines"}
            }
        
        return {
            "content": "I didn't understand that response. Please say 'confirm' to save your profile, or 'edit conditions/medications/routines' to modify a section.",
            "metadata": {"needs_clarification": True, "step": "preview"}
        }
    
    def _finalize_profile(self) -> dict:
        """Complete onboarding and create final user profile"""
        try:
            partial_profile = self.session_state.get("partial_profile", {})
            user_id = self.session_state.get("user_id", "anonymous")
            
            # Create profile components
            conditions = []
            for cond_data in partial_profile.get("conditions", []):
                conditions.append(Condition(**cond_data))
            
            medications = []
            for med_data in partial_profile.get("medications", []):
                medications.append(Medication(**med_data))
            
            routines = []
            for routine_data in partial_profile.get("routines", []):
                routines.append(Routine(**routine_data))
            
            # Create and save profile
            from .schema import UserProfile
            profile = UserProfile(
                user_id=user_id,
                onboarding_completed=True,
                onboarding_completed_at=datetime.now(timezone.utc),
                conditions=conditions,
                medications=medications,
                routines=routines
            )
            
            profile_store = get_profile_store()
            profile_store.save_profile(profile, source="onboarding")
            
            # Clear session state
            self.session_state = {"completed": True}
            
            return {
                "content": f"Excellent! Your health profile has been created successfully with {len(conditions)} conditions, {len(medications)} medications, and {len(routines)} routines. You're all set to start logging your health data with the Health Companion!",
                "metadata": {"onboarding_completed": True, "profile_created": True}
            }
            
        except Exception as e:
            return {
                "content": f"Error creating profile: {str(e)}. Please try again.",
                "metadata": {"error": True}
            }

# Workflow wrapper for agent registry integration
class ProfileOnboardingWrapper:
    """Wrapper for Gradio integration following existing patterns"""
    
    name = "Profile & Onboarding"
    description = "Complete health profile setup and management using structured onboarding workflow"
    
    def __init__(self):
        self.workflows = {}  # Session-based workflow storage
    
    def run(self, prompt: str, files=None, session_id: str = "anonymous"):
        """Run method following existing ChatResult pattern"""
        try:
            # Get or create workflow for this session
            if session_id not in self.workflows:
                self.workflows[session_id] = OnboardingWorkflow()
            
            workflow = self.workflows[session_id]
            result = workflow.run(message=prompt, session_id=session_id)
            
            # Add standard metadata
            if "metadata" not in result:
                result["metadata"] = {}
            
            result["metadata"].update({
                "agent_name": self.name,
                "workflow_type": "onboarding",
                "supports_files": False,
                "session_id": session_id
            })
            
            # CRITICAL FIX: Return ChatResult object instead of raw dict
            from dataclasses import dataclass
            from typing import Dict, Any, Optional
            
            @dataclass
            class ChatResult:
                text: str
                meta: Optional[Dict[str, Any]] = None
            
            return ChatResult(
                text=result.get("content", "Onboarding response error"),
                meta=result.get("metadata", {})
            )
            
        except Exception as e:
            # Import ChatResult for error case
            from dataclasses import dataclass
            from typing import Dict, Any, Optional
            
            @dataclass
            class ChatResult:
                text: str
                meta: Optional[Dict[str, Any]] = None
            
            return ChatResult(
                text=f"Error during onboarding: {str(e)}",
                meta={
                    "error": True,
                    "agent_name": self.name
                }
            )