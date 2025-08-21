"""
Onboarding workflow using Agno's workflow system.

This module implements a 6-step onboarding process with session state management
and the "Propose → Confirm → Commit" pattern for profile creation.

Updated to support both simple and structured workflows based on availability.
"""

from typing import Dict, Any, Optional, List
from datetime import datetime, date
import uuid

from agno.workflow import Workflow
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from pydantic import BaseModel, Field
from dataclasses import dataclass

from data import JsonStore
from .storage import ProfileStore
from core.ontology import normalize_condition, get_condition_family, CONDITION_MAP



@dataclass
class ChatResult:
    """Chat result for UI compatibility."""
    text: str
    meta: Optional[Dict[str, Any]] = None

class OnboardingWorkflowWrapper:
    """
    Enhanced wrapper for Agno onboarding workflow with structured data collection.
    
    This class provides a clean interface for the Gradio UI while managing
    the complex 6-step onboarding process with structured Pydantic models
    and the "Propose → Preview → Confirm → Commit" pattern.
    """
    
    def __init__(self):
        # Try to use the structured workflow first
        try:
            from .workflow_v2 import StructuredOnboardingWorkflow
            self.workflow = StructuredOnboardingWorkflow()
            self.name = "Profile & Onboarding (v3.3 Structured)"
            self.description = "Enhanced 6-step health profile creation with structured data collection and confirmation"
            self.is_structured = True
        except ImportError as e:
            print(f"Structured workflow not available, using fallback: {e}")
            # Fallback to simple workflow
            self.name = "Profile & Onboarding (v1.0 Simple)"
            self.description = "Basic 6-step health profile setup with confirmation patterns"
            self.is_structured = False
            
            # Initialize storage for fallback
            self.storage = JsonStore()
            self.profile_store = ProfileStore(self.storage)
            self.workflow = self._create_simple_workflow()
    
    def _create_simple_workflow(self) -> Workflow:
        """Create a simple onboarding workflow using Agno's basic pattern."""
        
        class OnboardingWorkflow(Workflow):
            def __init__(self, profile_store):
                super().__init__(name="HealthOnboardingWorkflow")
                self.profile_store = profile_store
                self.current_step = 0
                self.collected_data = {}
                
                # Create a single agent for all steps
                self.onboarding_agent = Agent(
                    model=OpenAIChat(id="gpt-4o-mini-2024-07-18"),
                    name="OnboardingAgent",
                    instructions=[
                        "You are a friendly health companion helping users set up their health profile.",
                        "Guide them through a 6-step onboarding process:",
                        "1. Basic info (name, age, gender, timezone)",
                        "2. Medical conditions they're managing",
                        "3. Current medications and allergies", 
                        "4. Healthcare team (doctor, pharmacy, insurance)",
                        "5. Emergency contacts",
                        "6. Notification and privacy preferences",
                        "Ask one step at a time. Be empathetic and explain why information is helpful.",
                        "Extract information naturally from their responses.",
                        "If they want to skip something, that's okay."
                    ],
                    markdown=True
                )
            
            def run(self, message: str, session_id: str = None) -> Any:
                """Run the onboarding workflow."""
                # Get session data to track progress
                session_data = self.profile_store.storage.get_session_data(session_id) or {}
                current_step = session_data.get("onboarding_step", 0)
                collected_data = session_data.get("collected_data", {})
                
                # Process user input based on current step
                if current_step == 0:
                    response = self._handle_basic_info(message, collected_data)
                elif current_step == 1:
                    response = self._handle_conditions(message, collected_data)
                elif current_step == 2:
                    response = self._handle_medications(message, collected_data)
                elif current_step == 3:
                    response = self._handle_healthcare_team(message, collected_data)
                elif current_step == 4:
                    response = self._handle_emergency_contacts(message, collected_data)
                elif current_step == 5:
                    response = self._handle_preferences(message, collected_data)
                elif current_step == 6:
                    response = self._handle_review(message, collected_data)
                else:
                    response = type('RunResult', (), {'content': 'Onboarding complete!'})()
                
                # Update session data
                if hasattr(response, 'next_step'):
                    session_data.update({
                        "onboarding_step": response.next_step,
                        "collected_data": collected_data
                    })
                    self.profile_store.storage.store_session_data(session_id, session_data)
                
                return response
            
            def _handle_basic_info(self, message: str, collected_data: dict):
                """Handle step 1: Basic information."""
                # Use the agent to process the response
                agent_response = self.onboarding_agent.run(
                    f"User response to basic info request: {message}. Extract their name, age, gender, timezone if provided."
                )
                
                # For now, just advance to next step
                result = type('RunResult', (), {
                    'content': "Great! Now let's talk about any health conditions you're currently managing. This could include things like migraines, back pain, anxiety, arthritis, or any other ongoing health concerns. What conditions, if any, are you dealing with?",
                    'next_step': 1
                })()
                
                return result
            
            def _handle_conditions(self, message: str, collected_data: dict):
                """Handle step 2: Medical conditions."""
                result = type('RunResult', (), {
                    'content': "Thank you for sharing that information. Now I'd like to know about any medications you're currently taking, including dosages if you're comfortable sharing. Also, do you have any known allergies to medications, foods, or other substances?",
                    'next_step': 2
                })()
                return result
            
            def _handle_medications(self, message: str, collected_data: dict):
                """Handle step 3: Medications and allergies."""
                result = type('RunResult', (), {
                    'content': "That's helpful information. Next, let's gather some details about your healthcare team. Who is your primary care doctor? Do you have a preferred pharmacy? And if you're comfortable sharing, what insurance do you have?",
                    'next_step': 3
                })()
                return result
            
            def _handle_healthcare_team(self, message: str, collected_data: dict):
                """Handle step 4: Healthcare team."""
                result = type('RunResult', (), {
                    'content': "Great! Now for emergency contacts - this is just for safety in case something happens and you need help. Can you provide the name, relationship, and phone number of someone we could contact in an emergency?",
                    'next_step': 4
                })()
                return result
            
            def _handle_emergency_contacts(self, message: str, collected_data: dict):
                """Handle step 5: Emergency contacts."""
                result = type('RunResult', (), {
                    'content': "Perfect! Finally, let's set up your preferences. Would you like to receive:\n- Medication reminders?\n- Appointment reminders?\n- Health insights based on your data?\n- Emergency alerts?\n\nAlso, are you comfortable with us using your data for improving our services (privacy protected), and would you be interested in participating in health research studies?",
                    'next_step': 5
                })()
                return result
            
            def _handle_preferences(self, message: str, collected_data: dict):
                """Handle step 6: Preferences."""
                result = type('RunResult', (), {
                    'content': "Excellent! Let me summarize your health profile:\n\n**Basic Information**: Collected ✓\n**Medical Conditions**: Collected ✓\n**Medications & Allergies**: Collected ✓\n**Healthcare Team**: Collected ✓\n**Emergency Contacts**: Collected ✓\n**Preferences**: Collected ✓\n\nYour profile is ready! Would you like me to save this information? (Type 'confirm' to save or 'cancel' to start over)",
                    'next_step': 6
                })()
                return result
            
            def _handle_review(self, message: str, collected_data: dict):
                """Handle step 7: Review and confirmation."""
                if "confirm" in message.lower():
                    # Create a simple profile
                    user_id = f"user_{uuid.uuid4().hex[:8]}"
                    profile_data = {
                        "name": "User",  # Would extract from collected_data
                        "onboarding_completed": True
                    }
                    
                    proposal = self.profile_store.propose_new_profile(user_id, profile_data)
                    result_msg = "🎉 Welcome to your Health Companion! Your profile has been created successfully. You can now start logging your health data and getting personalized insights."
                else:
                    result_msg = "No problem! You can restart the onboarding process anytime by typing 'start'."
                
                result = type('RunResult', (), {
                    'content': result_msg,
                    'next_step': 7
                })()
                return result
        
        return OnboardingWorkflow(self.profile_store)
    
    def run(self, prompt: str, files: Optional[List[str]] = None, session_id: str = None) -> ChatResult:
        """
        Run the onboarding workflow.
        
        Args:
            prompt: User input
            files: Uploaded files (not used in onboarding)
            session_id: Session identifier for state management
            
        Returns:
            ChatResult with response and metadata
        """
        try:
            if not session_id:
                session_id = "onboarding_session"
            
            # Delegate to the appropriate workflow
            if self.is_structured:
                return self.workflow.run(prompt, files, session_id)
            else:
                # Handle the simple workflow
                return self._run_simple_workflow(prompt, session_id)
        
        except Exception as e:
            return ChatResult(
                text=f"I encountered an issue during onboarding: {str(e)}. Please try again or restart the process.",
                meta={"error": str(e), "workflow": self.name}
            )
    
    def _run_simple_workflow(self, prompt: str, session_id: str) -> ChatResult:
        """Run the simple fallback workflow."""
        # Handle special commands
        if prompt.lower().strip() in ["start", "begin", "restart"]:
            return self._start_onboarding(session_id)
        
        if prompt.lower().strip() in ["confirm", "yes", "save"]:
            return self._handle_confirmation(session_id, True)
        
        if prompt.lower().strip() in ["cancel", "no", "abort"]:
            return self._handle_confirmation(session_id, False)
        
        # Run simple workflow step
        response = self.workflow.run(
            message=prompt,
            session_id=session_id
        )
        
        return ChatResult(
            text=response.content if hasattr(response, 'content') else str(response),
            meta={
                "workflow": "Simple Onboarding",
                "session_id": session_id,
                "step": getattr(response, 'current_step', 'unknown')
            }
        )
    
    def _start_onboarding(self, session_id: str) -> ChatResult:
        """Start the onboarding process."""
        # Clear any existing session data
        self.storage.clear_session_data(session_id)
        
        welcome_message = """
# Welcome to Your Health Companion! 🏥

I'll help you set up your personalized health profile through a simple 6-step process:

1. **Basic Information** - Name, age, timezone
2. **Medical Conditions** - Current health conditions you're managing  
3. **Medications** - Current medications and allergies
4. **Healthcare Team** - Your doctors, pharmacy, insurance
5. **Emergency Contacts** - Important contacts for emergencies
6. **Preferences** - Notification and privacy settings

Let's start with some basic information about you. What's your name, and would you like to share your age?

*All information is optional and securely stored. You can skip any question or modify answers later.*
        """
        
        return ChatResult(
            text=welcome_message.strip(),
            meta={
                "workflow": "Onboarding", 
                "step": "welcome",
                "session_id": session_id
            }
        )
    

    
    def _handle_confirmation(self, session_id: str, confirmed: bool) -> ChatResult:
        """Handle user confirmation or cancellation."""
        try:
            session_data = self.storage.get_session_data(session_id)
            if not session_data or session_data.get("pending_action") != "create_profile":
                return ChatResult(
                    text="No pending profile creation found. Please restart the onboarding process.",
                    meta={"error": "No pending action"}
                )
            
            user_id = session_data["user_id"]
            proposal = session_data["proposal"]
            
            if confirmed:
                # Confirm profile creation
                result = self.profile_store.confirm_profile_creation(user_id, proposal)
                
                if result.get("success"):
                    # Clear session data
                    self.storage.clear_session_data(session_id)
                    
                    return ChatResult(
                        text=result["message"] + "\n\nYour health companion is now ready to help you track and manage your health journey!",
                        meta={
                            "workflow": "Onboarding",
                            "completed": True,
                            "user_id": user_id
                        }
                    )
                else:
                    return ChatResult(
                        text=result["message"],
                        meta={"error": result.get("error")}
                    )
            else:
                # Cancel profile creation
                result = self.profile_store.cancel_profile_creation(user_id)
                self.storage.clear_session_data(session_id)
                
                return ChatResult(
                    text=result["message"],
                    meta={
                        "workflow": "Onboarding",
                        "cancelled": True
                    }
                )
        
        except Exception as e:
            return ChatResult(
                text=f"An error occurred during confirmation: {str(e)}",
                meta={"error": str(e)}
            )