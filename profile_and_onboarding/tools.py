# profile_and_onboarding/tools.py
try:
    from agno import Agent, tool
except ImportError:
    print("Warning: Agno imports not available, using mock classes")
    class Agent:
        def __init__(self):
            self.workflow_session_state = None
    
    def tool(func):
        """Mock tool decorator"""
        func.func = func  # Store original function
        return func
from typing import Optional, List, Dict, Any
from .storage import get_profile_store, ProfileStorageInterface
from .schema import UserProfile, Condition, Medication, Routine
try:
    from core.ontology import normalize_condition
except ImportError:
    def normalize_condition(condition):
        return condition
        
try:
    from core.timeutils import parse_natural_time
except ImportError:
    def parse_natural_time(time_str):
        return None

# Profile management tools using workflow_session_state
@tool
def get_profile_summary(agent: Agent, user_id: str) -> str:
    """Get a summary of the user's current profile"""
    profile_store = get_profile_store()
    profile = profile_store.get_profile(user_id)
    
    if not profile:
        return "No profile found. Would you like to start the onboarding process?"
    
    summary_parts = []
    summary_parts.append(f"Profile for {user_id}:")
    summary_parts.append(f"Created: {profile.created_at.strftime('%Y-%m-%d')}")
    summary_parts.append(f"Onboarding completed: {'Yes' if profile.onboarding_completed else 'No'}")
    
    if profile.conditions:
        conditions = [c.name for c in profile.conditions if c.status == "active"]
        if conditions:
            summary_parts.append(f"Conditions: {', '.join(conditions)}")
    
    if profile.medications:
        meds = []
        for m in profile.medications:
            if m.status == "active":
                med_str = f"{m.name}"
                if m.dose:
                    med_str += f" ({m.dose})"
                meds.append(med_str)
        if meds:
            summary_parts.append(f"Medications: {', '.join(meds)}")
    
    if profile.routines:
        routines = [f"{r.category}: {r.pattern}" for r in profile.routines]
        if routines:
            summary_parts.append(f"Routines: {', '.join(routines)}")
    
    return "\n".join(summary_parts)

@tool
def save_onboarding_progress(agent: Agent, step_data: Dict[str, Any]) -> str:
    """Save onboarding progress to workflow session state"""
    if agent.workflow_session_state is None:
        agent.workflow_session_state = {}
    
    if "onboarding_progress" not in agent.workflow_session_state:
        agent.workflow_session_state["onboarding_progress"] = {
            "step_index": 0,
            "partial_profile": {},
            "user_id": step_data.get("user_id", "anonymous")
        }
    
    # Update progress
    progress = agent.workflow_session_state["onboarding_progress"]
    progress["partial_profile"].update(step_data)
    
    return f"Saved progress for step {progress.get('step_index', 0)}"

@tool
def get_onboarding_progress(agent: Agent) -> Optional[Dict[str, Any]]:
    """Get current onboarding progress from workflow session state"""
    if not agent.workflow_session_state or "onboarding_progress" not in agent.workflow_session_state:
        return None
    
    return agent.workflow_session_state["onboarding_progress"]

@tool
def finalize_onboarding(agent: Agent) -> str:
    """Complete onboarding and create final user profile"""
    if not agent.workflow_session_state or "onboarding_progress" not in agent.workflow_session_state:
        return "No onboarding in progress"
    
    progress = agent.workflow_session_state["onboarding_progress"]
    partial_profile = progress.get("partial_profile", {})
    user_id = progress.get("user_id", "anonymous")
    
    # Create conditions from onboarding data
    conditions = []
    for cond_data in partial_profile.get("conditions", []):
        if isinstance(cond_data, dict):
            conditions.append(Condition(**cond_data))
        elif isinstance(cond_data, str):
            conditions.append(Condition(name=cond_data, source="onboarding"))
    
    # Create medications from onboarding data
    medications = []
    for med_data in partial_profile.get("medications", []):
        if isinstance(med_data, dict):
            medications.append(Medication(**med_data))
    
    # Create routines from onboarding data
    routines = []
    for routine_data in partial_profile.get("routines", []):
        if isinstance(routine_data, dict):
            routines.append(Routine(**routine_data))
    
    # Create full profile
    profile = UserProfile(
        user_id=user_id,
        onboarding_completed=True,
        onboarding_completed_at=datetime.now(timezone.utc),
        conditions=conditions,
        medications=medications,
        routines=routines
    )
    
    # Save to storage
    profile_store = get_profile_store()
    profile_store.save_profile(profile, source="onboarding")
    
    # Clear onboarding state
    agent.workflow_session_state.pop("onboarding_progress", None)
    
    return f"Onboarding completed! Created profile with {len(profile.conditions)} conditions, {len(profile.medications)} medications, and {len(profile.routines)} routines."

@tool
def check_profile_exists(agent: Agent, user_id: str) -> bool:
    """Check if a user profile already exists"""
    profile_store = get_profile_store()
    profile = profile_store.get_profile(user_id)
    return profile is not None

@tool
def update_profile_medication(agent: Agent, user_id: str, medication_data: Dict[str, Any]) -> str:
    """Update a specific medication in the user's profile"""
    try:
        medication = Medication(**medication_data)
        profile_store = get_profile_store()
        profile_store.add_or_update_medication(user_id, medication, source="chat")
        return f"Successfully updated medication: {medication.name}"
    except Exception as e:
        return f"Error updating medication: {str(e)}"

@tool
def update_profile_condition(agent: Agent, user_id: str, condition_data: Dict[str, Any]) -> str:
    """Update a specific condition in the user's profile"""
    try:
        condition = Condition(**condition_data)
        profile_store = get_profile_store()
        profile_store.add_or_update_condition(user_id, condition, source="chat")
        return f"Successfully updated condition: {condition.name}"
    except Exception as e:
        return f"Error updating condition: {str(e)}"

@tool
def update_profile_routine(agent: Agent, user_id: str, routine_data: Dict[str, Any]) -> str:
    """Update a specific routine in the user's profile"""
    try:
        routine = Routine(**routine_data)
        profile_store = get_profile_store()
        profile_store.add_or_update_routine(user_id, routine, source="chat")
        return f"Successfully updated routine: {routine.category} - {routine.pattern}"
    except Exception as e:
        return f"Error updating routine: {str(e)}"

@tool
def deactivate_profile_medication(agent: Agent, user_id: str, medication_name: str) -> str:
    """Deactivate a medication in the user's profile"""
    try:
        profile_store = get_profile_store()
        profile_store.deactivate_medication(user_id, medication_name, source="chat")
        return f"Successfully deactivated medication: {medication_name}"
    except Exception as e:
        return f"Error deactivating medication: {str(e)}"

@tool
def deactivate_profile_condition(agent: Agent, user_id: str, condition_name: str) -> str:
    """Deactivate a condition in the user's profile"""
    try:
        profile_store = get_profile_store()
        profile_store.deactivate_condition(user_id, condition_name, source="chat")
        return f"Successfully deactivated condition: {condition_name}"
    except Exception as e:
        return f"Error deactivating condition: {str(e)}"

# Import datetime for finalize_onboarding
from datetime import datetime, timezone