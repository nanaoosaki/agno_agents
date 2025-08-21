"""
Enhanced onboarding workflow following the v3.3 implementation plan.

This module implements the structured "Propose → Preview → Confirm → Commit" pattern
for robust, auditable user profile creation with full Agno workflow integration.
"""

from typing import Dict, Any, Optional, List
from datetime import datetime
import uuid

try:
    from agno.workflow.v2 import Workflow, Step, StepInput, StepOutput
    from agno.workflow.v2.workflow import Workflow as WorkflowClass
    AGNO_V2_AVAILABLE = True
except ImportError:
    try:
        from agno.workflow import Workflow as WorkflowClass
        AGNO_V2_AVAILABLE = False
        # Create compatibility classes
        class StepInput:
            def __init__(self, message="", session_id=None, workflow_session_state=None, previous_step_content=""):
                self.message = message
                self.session_id = session_id
                self.workflow_session_state = workflow_session_state or {}
                self.previous_step_content = previous_step_content
            
            def get_step_content(self, step_name):
                return self.workflow_session_state.get(f"{step_name}_result")
        
        class StepOutput:
            def __init__(self, content=""):
                self.content = content
        
        class Step:
            def __init__(self, name, agent=None, executor=None, description=""):
                self.name = name
                self.agent = agent
                self.executor = executor
                self.description = description
    except ImportError:
        AGNO_V2_AVAILABLE = False
        WorkflowClass = object

from agno.models.openai import OpenAIChat
from agno.agent import Agent
from dataclasses import dataclass

from data import JsonStore
from .storage import ProfileStore
from .agents import (
    create_conditions_agent, create_goals_agent, create_symptoms_agent,
    create_medications_agent, create_routines_agent, create_style_agent
)
from data.schemas import (
    UserProfile, OnboardingConditions, OnboardingGoals, OnboardingSymptoms,
    OnboardingMedications, OnboardingRoutines, OnboardingStyle
)
from core.ontology import normalize_condition, CONDITION_MAP

@dataclass
class ChatResult:
    """Chat result for UI compatibility."""
    text: str
    meta: Optional[Dict[str, Any]] = None

def preview_and_confirm_step(step_input: StepInput) -> StepOutput:
    """
    Consolidates all structured answers into a summary for user review.
    
    This implements the "Preview" part of the Propose → Preview → Confirm → Commit pattern.
    """
    try:
        # Retrieve structured output from each step
        conditions_data = step_input.get_step_content("AskConditions")
        goals_data = step_input.get_step_content("AskGoals") 
        symptoms_data = step_input.get_step_content("AskSymptoms")
        medications_data = step_input.get_step_content("AskMedications")
        routines_data = step_input.get_step_content("AskRoutines")
        style_data = step_input.get_step_content("AskStyle")
        
        # Build comprehensive summary
        summary_parts = [
            "# 📋 Your Health Profile Summary",
            "",
            "Please review the information I've collected. This will be saved as your health profile:",
            ""
        ]
        
        if conditions_data and hasattr(conditions_data, 'conditions'):
            summary_parts.extend([
                "## 🏥 Health Conditions",
                f"- Conditions: {', '.join(conditions_data.conditions) if conditions_data.conditions else 'None specified'}",
                f"- Primary concern: {conditions_data.primary_condition or 'Not specified'}",
                ""
            ])
        
        if goals_data and hasattr(goals_data, 'goals'):
            summary_parts.extend([
                "## 🎯 Health Goals", 
                f"- Primary goal: {goals_data.goals}",
                f"- Specific targets: {', '.join(goals_data.specific_targets) if hasattr(goals_data, 'specific_targets') and goals_data.specific_targets else 'None specified'}",
                ""
            ])
        
        if symptoms_data and hasattr(symptoms_data, 'symptoms_description'):
            summary_parts.extend([
                "## 🩺 Symptoms & Triggers",
                f"- Symptoms: {symptoms_data.symptoms_description or 'No symptoms specified'}",
                f"- Known triggers: {', '.join(symptoms_data.trigger_patterns) if hasattr(symptoms_data, 'trigger_patterns') and symptoms_data.trigger_patterns else 'None identified'}",
                ""
            ])
        
        if medications_data and hasattr(medications_data, 'medications_list'):
            summary_parts.extend([
                "## 💊 Medications & Treatments",
                f"- Medications: {medications_data.medications_list or 'No medications'}",
                f"- Allergies: {', '.join(medications_data.allergies) if hasattr(medications_data, 'allergies') and medications_data.allergies else 'None known'}",
                ""
            ])
        
        if routines_data and hasattr(routines_data, 'routines_description'):
            summary_parts.extend([
                "## 🔄 Daily Routines",
                f"- Routines: {routines_data.routines_description or 'No routines specified'}",
                f"- Exercise: {routines_data.exercise_habits if hasattr(routines_data, 'exercise_habits') and routines_data.exercise_habits else 'Not specified'}",
                ""
            ])
        
        if style_data and hasattr(style_data, 'communication_style'):
            summary_parts.extend([
                "## 💬 Communication Preferences",
                f"- Style: {style_data.communication_style}",
                f"- Privacy level: {style_data.privacy_level if hasattr(style_data, 'privacy_level') and style_data.privacy_level else 'Not specified'}",
                ""
            ])
        
        summary_parts.extend([
            "---",
            "",
            "**Does this look correct?**",
            "- Type **'confirm'** to save your profile",
            "- Type **'edit'** to make changes to any section", 
            "- Type **'cancel'** to start over",
            "",
            "*Your information is stored securely and privately. You can update it anytime.*"
        ])
        
        summary = "\n".join(summary_parts)
        
        # Store the consolidated profile data in session state for potential commit
        profile_data = {
            "conditions_data": conditions_data,
            "goals_data": goals_data,
            "symptoms_data": symptoms_data,
            "medications_data": medications_data,
            "routines_data": routines_data,
            "style_data": style_data
        }
        
        step_input.workflow_session_state["pending_profile"] = profile_data
        step_input.workflow_session_state["profile_summary"] = summary
        
        return StepOutput(content=summary)
        
    except Exception as e:
        return StepOutput(content=f"I encountered an issue creating your profile summary: {str(e)}. Let's try again.")

def commit_profile_step(step_input: StepInput) -> StepOutput:
    """
    Saves the profile if the user confirms, implementing the "Commit" part of the pattern.
    """
    try:
        user_response = step_input.previous_step_content.lower()
        
        if "confirm" not in user_response:
            # Clear pending state
            step_input.workflow_session_state.pop("pending_profile", None)
            step_input.workflow_session_state.pop("profile_summary", None)
            
            if "cancel" in user_response:
                return StepOutput(content="❌ Profile creation cancelled. You can restart the onboarding process anytime by selecting 'Profile & Onboarding' again.")
            elif "edit" in user_response:
                return StepOutput(content="✏️ To edit your profile, please restart the onboarding process. I'll ask all the questions again so you can provide updated information.")
            else:
                return StepOutput(content="Please respond with 'confirm' to save, 'edit' to make changes, or 'cancel' to abort.")
        
        # User confirmed - proceed with commit
        profile_data = step_input.workflow_session_state.get("pending_profile")
        if not profile_data:
            return StepOutput(content="❌ Something went wrong - I don't have a profile to save. Please restart the onboarding process.")
        
        # Convert structured data to UserProfile format
        user_id = step_input.session_id or f"user_{uuid.uuid4().hex[:8]}"
        
        # Process conditions
        processed_conditions = []
        conditions_data = profile_data.get("conditions_data")
        if conditions_data and hasattr(conditions_data, 'conditions'):
            for condition in conditions_data.conditions:
                normalized = normalize_condition(condition)
                processed_conditions.append({
                    "name": normalized or condition.lower(),
                    "display_name": condition,
                    "status": "active"
                })
        
        # Process medications (simplified for compatibility)
        processed_medications = []
        medications_data = profile_data.get("medications_data")
        if medications_data and hasattr(medications_data, 'medications_list') and medications_data.medications_list:
            # Convert medication text to simple list format
            medications_text = medications_data.medications_list
            if medications_text.strip():
                processed_medications.append({
                    "name": medications_text,
                    "source": "user_entered",
                    "status": "active"
                })
        
        # Process routines (simplified)
        processed_routines = []
        routines_data = profile_data.get("routines_data")
        if routines_data and hasattr(routines_data, 'routines_description') and routines_data.routines_description:
            processed_routines.append({
                "type": "general",
                "description": routines_data.routines_description
            })
        
        # Create comprehensive UserProfile
        goals_data = profile_data.get("goals_data")
        style_data = profile_data.get("style_data")
        
        new_profile = UserProfile(
            user_id=user_id,
            conditions=processed_conditions,
            goals=goals_data.goals if goals_data and hasattr(goals_data, 'goals') else "",
            medications=processed_medications,
            daily_routines=processed_routines,
            communication_style=style_data.communication_style if style_data and hasattr(style_data, 'communication_style') else "supportive",
            last_updated_at=datetime.now().isoformat(),
            last_updated_by="user",
            onboarding_completed=True
        )
        
        # Save to storage using ProfileStore
        from data import JsonStore
        storage = JsonStore()
        profile_store = ProfileStore(storage)
        
        success = storage.create_user_profile(user_id, new_profile.dict())
        
        if success:
            # Clear the pending state
            step_input.workflow_session_state.pop("pending_profile", None)
            step_input.workflow_session_state.pop("profile_summary", None)
            
            return StepOutput(content=f"""🎉 **Welcome to your Health Companion!**

Your health profile has been created successfully with:
- **{len(processed_conditions)}** health condition(s) tracked
- **{len(processed_medications)}** medication(s) logged  
- **{len(processed_routines)}** daily routine(s) established

You can now start logging your health data, and I'll provide personalized insights based on your profile. 

**What's next?**
- Use the **Health Logger** to track symptoms and episodes
- Try the **Recall Agent** to review your health history
- Ask the **Coach Agent** for personalized health advice

Your health journey starts now! 🌟""")
        else:
            return StepOutput(content="❌ I encountered an issue saving your profile. Please try again or contact support if the problem persists.")
            
    except Exception as e:
        return StepOutput(content=f"❌ An error occurred while saving your profile: {str(e)}. Please try again.")

class StructuredOnboardingWorkflow:
    """
    Enhanced onboarding workflow implementing the v3.3 specification.
    
    Features:
    - Structured data collection with Pydantic models
    - Step-by-step progression with session state management
    - Preview and confirmation before commitment
    - Robust error handling and recovery
    """
    
    def __init__(self):
        self.name = "Profile & Onboarding (v3.3 Structured)"
        self.description = "Comprehensive 6-step health profile creation with structured data collection and confirmation"
        
        # Initialize storage
        self.storage = JsonStore()
        self.profile_store = ProfileStore(self.storage)
        
        # Create workflow with structured steps
        if AGNO_V2_AVAILABLE:
            self.workflow = self._create_v2_workflow()
        else:
            self.workflow = self._create_fallback_workflow()
    
    def _create_v2_workflow(self):
        """Create workflow using Agno v2 workflow system."""
        return Workflow(
            name="StructuredOnboardingWorkflowV2",
            steps=[
                Step(
                    name="AskConditions",
                    agent=create_conditions_agent(),
                    description="Collect health conditions with structured output"
                ),
                Step(
                    name="AskGoals", 
                    agent=create_goals_agent(),
                    description="Collect health management goals"
                ),
                Step(
                    name="AskSymptoms",
                    agent=create_symptoms_agent(), 
                    description="Collect symptoms and trigger patterns"
                ),
                Step(
                    name="AskMedications",
                    agent=create_medications_agent(),
                    description="Collect medications and treatments"
                ),
                Step(
                    name="AskRoutines",
                    agent=create_routines_agent(),
                    description="Collect daily routines and lifestyle"
                ),
                Step(
                    name="AskStyle",
                    agent=create_style_agent(),
                    description="Collect communication preferences"
                ),
                Step(
                    name="PreviewAndConfirm",
                    executor=preview_and_confirm_step,
                    description="Summarize collected data and ask for confirmation"
                ),
                Step(
                    name="SaveProfile",
                    executor=commit_profile_step,
                    description="Save confirmed profile to storage"
                )
            ]
        )
    
    def _create_fallback_workflow(self):
        """Create simplified workflow for compatibility."""
        class SimpleWorkflow:
            def __init__(self, profile_store):
                self.profile_store = profile_store
                self.steps = [
                    "conditions", "goals", "symptoms", "medications", "routines", "style", "confirm"
                ]
            
            def run(self, message: str, session_id: str = None):
                # Simple fallback implementation
                return type('RunResult', (), {
                    'content': "Structured onboarding requires Agno v2. Please use the basic onboarding instead."
                })()
        
        return SimpleWorkflow(self.profile_store)
    
    def run(self, prompt: str, files: Optional[List[str]] = None, session_id: str = None) -> ChatResult:
        """
        Run the structured onboarding workflow.
        
        Args:
            prompt: User input
            files: Uploaded files (not used in onboarding)
            session_id: Session identifier for state management
            
        Returns:
            ChatResult with response and metadata
        """
        try:
            if not session_id:
                session_id = str(uuid.uuid4())
            
            # Handle special commands
            if prompt.lower().strip() in ["start", "begin", "restart"]:
                return self._start_onboarding(session_id)
            
            # Run the structured workflow
            if AGNO_V2_AVAILABLE:
                response = self.workflow.run(
                    message=prompt,
                    session_id=session_id
                )
                
                return ChatResult(
                    text=response.content if hasattr(response, 'content') else str(response),
                    meta={
                        "workflow": "Structured Onboarding v3.3",
                        "session_id": session_id,
                        "architecture": "agno_v2_structured"
                    }
                )
            else:
                # Fallback for non-v2 environments
                response = self.workflow.run(prompt, session_id)
                return ChatResult(
                    text=response.content if hasattr(response, 'content') else str(response),
                    meta={
                        "workflow": "Onboarding (Compatibility Mode)",
                        "session_id": session_id,
                        "architecture": "fallback"
                    }
                )
        
        except Exception as e:
            return ChatResult(
                text=f"I encountered an issue during onboarding: {str(e)}. Please try restarting the process.",
                meta={"error": str(e), "session_id": session_id}
            )
    
    def _start_onboarding(self, session_id: str) -> ChatResult:
        """Start the structured onboarding process."""
        # Clear any existing session data
        self.storage.clear_session_data(session_id)
        
        welcome_message = """
# 🏥 Welcome to Your Health Profile Setup!

I'll guide you through creating a comprehensive health profile in **6 structured steps**:

1. **🏥 Health Conditions** - What conditions do you manage?
2. **🎯 Goals** - What are your health management goals? 
3. **🩺 Symptoms & Triggers** - What symptoms do you experience?
4. **💊 Medications** - Current medications and treatments
5. **🔄 Daily Routines** - Health habits and lifestyle factors
6. **💬 Communication Style** - How you prefer to interact

**Why structured?** This approach ensures I capture complete, accurate information for personalized health insights.

**Let's start with Step 1:**

What health conditions are you currently managing or would like to track? This could include things like migraines, back pain, anxiety, diabetes, arthritis, or any other ongoing health concerns.

*Feel free to list as many as apply - I'll help organize them.*
        """
        
        return ChatResult(
            text=welcome_message.strip(),
            meta={
                "workflow": "Structured Onboarding v3.3",
                "step": "welcome", 
                "session_id": session_id,
                "next_step": "conditions"
            }
        )

# Create the workflow wrapper for backward compatibility
class OnboardingWorkflowWrapper:
    """Backward compatible wrapper that delegates to the appropriate workflow."""
    
    def __init__(self):
        self.structured_workflow = StructuredOnboardingWorkflow()
        self.name = self.structured_workflow.name
        self.description = self.structured_workflow.description
    
    def run(self, prompt: str, files: Optional[List[str]] = None, session_id: str = None) -> ChatResult:
        """Delegate to the structured workflow."""
        return self.structured_workflow.run(prompt, files, session_id)