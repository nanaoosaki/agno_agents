This is an outstanding set of recommendations. The feedback from "gpt5" is not just an iteration; it's a blueprint for building a production-grade, enterprise-ready feature. It correctly identifies that a simple conversational flow is not enough and pushes for a robust, structured, and auditable process.

Let's integrate this feedback into a definitive, final implementation plan for the Profile & Onboarding module. This will be our guide.

Definitive Implementation Plan: Proactive, Structured, & Resumable Onboarding (v3.3)
1. Core Architectural Philosophy (Reinforced)

Structured First: Every step of the onboarding process will be a structured interaction. We will use Pydantic response_models for each of the six questions to eliminate ambiguity and avoid parsing free-form text at the end.

Propose → Preview → Confirm → Commit: We will formalize this pattern. The workflow will gather structured data, present a summary for user review, and only commit to permanent storage after explicit user confirmation.

Single Source of Truth: The user_profiles.json file (or a future database table) will be the canonical source of truth for a user's profile. Agno's Memory will be used as a semantic cache for this data, enabling other agents to perform natural language queries against it.

Stateful and Resumable: The entire onboarding process will be stateful, managed by Agno's workflow_session_state, allowing users to pause and resume without losing progress.

Step 1: Enhance the Schemas for Robustness

We will upgrade the Pydantic models to be more detailed and production-ready.

File: data/schemas/user_profile.py

code
Python
download
content_copy
expand_less

# data/schemas/user_profile.py
from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Dict
from datetime import datetime

# --- Per-Step Structured Models for Onboarding ---
class OnboardConditions(BaseModel):
    conditions: List[str] = Field(..., description="A list of health conditions the user wants to manage.")

class OnboardGoals(BaseModel):
    goals: str = Field(..., description="The user's primary goals for health management.")
# ... Define similar Pydantic models for Symptoms, Meds, Routines, and Style ...

# --- The Canonical UserProfile Model (with enhancements) ---
class Medication(BaseModel):
    name: str
    dosage: Optional[str] = None
    schedule: Optional[str] = None
    status: Literal["active", "inactive"] = "active"
    started_at: Optional[str] = None
    stopped_at: Optional[str] = None
    source: Literal["user_entered", "inferred"] = "user_entered"

class UserProfile(BaseModel):
    user_id: str
    _schema_version: int = 1
    
    # Core Profile Data
    conditions: List[Dict[str, str]] = Field(default_factory=list) # e.g., {"name": "migraine", "status": "active"}
    goals: str
    symptoms: Dict[str, List[str]] = Field(default_factory=dict)
    medications: List[Medication] = Field(default_factory=list)
    routines: List[Dict[str, str]] = Field(default_factory=dict)
    communication_style: str
    
    # Metadata
    user_timezone: str = "UTC"
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    last_updated_at: str
    last_updated_by: Literal["user", "system"]
Step 2: Upgrade the Onboarding Workflow

The workflow will now manage a multi-step, structured, and resumable conversation.

File: profile_and_onboarding/workflow.py

code
Python
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# profile_and_onboarding/workflow.py
from agno.workflow.v2 import Workflow, Step, StepInput, StepOutput
from agno.agent import Agent
from .agents import create_onboarding_agent # We'll create this helper
from .storage import profile_storage
from data.schemas.user_profile import UserProfile, OnboardConditions, OnboardGoals # and others

# --- The Onboarding Workflow ---
onboarding_workflow = Workflow(
    name="OnboardingWorkflowV2",
    steps=[
        Step(name="AskConditions", agent=create_onboarding_agent("Ask what conditions they manage.", OnboardConditions)),
        Step(name="AskGoals", agent=create_onboarding_agent("Ask for their main health goals.", OnboardGoals)),
        # ... steps for questions 3, 4, 5, 6, each with its own response_model ...
        
        # New Step: Preview and Confirm
        Step(
            name="PreviewAndConfirm",
            executor=preview_and_confirm_step,
            description="Summarize the collected data and ask for user confirmation."
        ),
        
        # Final Step: Commit to storage
        Step(
            name="SaveProfile",
            executor=commit_profile_step,
            description="Save the confirmed profile to the canonical store and semantic memory."
        ),
    ]
)

def preview_and_confirm_step(step_input: StepInput) -> StepOutput:
    """Consolidates all structured answers into a summary for the user to review."""
    # Use `get_step_content` to retrieve structured output from each step
    conditions_data = step_input.get_step_content("AskConditions")
    goals_data = step_input.get_step_content("AskGoals")
    
    # Build a summary string from the structured data
    summary = f"Great! Here's what I've got so far:\n"
    summary += f"- Conditions: {', '.join(conditions_data.conditions)}\n"
    summary += f"- Your Goal: {goals_data.goals}\n"
    summary += "\nDoes this look correct? Please say 'confirm' to save, or tell me what to change."
    
    # Store the partial, unconfirmed profile in the session state
    step_input.workflow_session_state["pending_profile"] = {
        "conditions": conditions_data.conditions,
        "goals": goals_data.goals,
        # ... other data
    }
    
    return StepOutput(content=summary)

def commit_profile_step(step_input: StepInput) -> StepOutput:
    """Saves the profile if the user confirms."""
    user_response = step_input.previous_step_content
    if "confirm" not in user_response.lower():
        step_input.workflow_session_state.pop("pending_profile", None)
        return StepOutput(content="Okay, I've discarded that. We can start over whenever you're ready.")

    profile_data = step_input.workflow_session_state.get("pending_profile")
    if not profile_data:
        return StepOutput(content="Something went wrong, I don't have a profile to save. Let's try again.")

    # Create and save the full UserProfile object
    user_id = step_input.session_id or "default_user"
    new_profile = UserProfile(
        user_id=user_id,
        last_updated_at=datetime.utcnow().isoformat(),
        last_updated_by="user",
        **profile_data
    )
    profile_storage.save_user_profile(new_profile)
    
    # ... (Logic to update Agno Memory as planned) ...
    
    # Clear the pending state
    step_input.workflow_session_state.pop("pending_profile", None)
    
    return StepOutput(content="Perfect, your profile has been saved!")
Step 3: Update UI and Main Agent Registry

The UI (app.py) and main agents.py need to be aware of this more sophisticated, multi-turn workflow.

File: app.py

The onboarding_state in gr.State becomes more important for tracking progress.

The unified_submit handler will now manage the back-and-forth of the onboarding conversation, calling the workflow step-by-step and passing the session_id and onboarding_state on each turn.

File: agents.py

The MasterAgent (your router) needs to be enhanced. When it detects an onboarding intent, it shouldn't just run a one-shot agent. It should initiate the onboarding_workflow and hand over control of the conversation to it until the workflow completes.

code
Python
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# agents.py - inside MasterAgent.run()

# ... (router logic)
final_intent = decision.primary_intent

if final_intent == "onboarding":
    print("--> Initiating Onboarding Workflow")
    # This call starts the multi-turn workflow. The UI will manage subsequent steps.
    return onboarding_workflow.run(message=prompt, session_id=session_id)
# ... (rest of the routing)

This updated plan provides a clear path to building the robust, user-friendly, and scalable onboarding system you envisioned. It directly incorporates the expert feedback, leveraging Agno's best features for state management and structured data handling.