# Profile & Onboarding Agent Implementation Plan v2.0

**Author**: Claude (Anthropic AI Assistant - Claude Code)  
**Date**: August 21, 2025  
**Framework**: Agno v2.0 with layered architecture integration  
**Integration**: Health Companion Auto-Router orchestration  

---

## 1. Repository Alignment & Architectural Integration

This implementation plan aligns with the **existing Health Companion layered architecture** and integrates seamlessly with the production-ready Router Agent and MasterAgent orchestration system. The Profile & Onboarding system will:

- **Leverage existing infrastructure**: Reuse `core/`, `data/`, and orchestration patterns
- **Follow established patterns**: Use the same Agno Workflow v2.0, storage interfaces, and agent patterns
- **Integrate with Router Agent**: Extend the existing RouterDecision schema and orchestration logic
- **Maintain consistency**: Use shared primitives from `core/ontology.py`, `core/timeutils.py`, and `core/policies.py`

This approach ensures the Profile & Onboarding system is production-grade, following the same atomic, idempotent, and auditable principles as the existing health logging, recall, and coaching agents.

## 2. Implementation Architecture Following Agno v2.0 Patterns

### **Data Layer Integration** (`profile_and_onboarding/schema.py`)

**Following existing patterns from `data/schemas/episodes.py`:**
- Use identical Pydantic patterns with `Field(default_factory=list)` for safety
- Timezone-aware UTC timestamps using `datetime.now(timezone.utc)`
- Consistent event modeling following `data/json_store.py` patterns
- Integration with existing condition normalization from `core/ontology.py`

**Key Models:**
```python
class UserProfile(BaseModel):
    user_id: str
    schema_version: int = 1
    user_tz: str = "UTC"
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    conditions: List[Condition] = Field(default_factory=list)
    medications: List[Medication] = Field(default_factory=list)
    routines: List[Routine] = Field(default_factory=list)

class ProfileEvent(BaseModel):
    event_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    ts: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    user_id: str
    kind: Literal["add", "update", "deactivate", "create"]
    entity: Literal["condition", "medication", "routine", "profile"]
    before: Optional[dict] = None
    after: Optional[dict] = None
    source: Literal["onboarding", "chat", "import"]
    idempotency_key: str
```

### **Storage Layer Extension** (`profile_and_onboarding/storage.py`)

**Extending `data/storage_interface.py` pattern:**
```python
class ProfileStorageInterface(ABC):
    """Abstract interface following data/storage_interface.py pattern"""
    @abstractmethod
    def get_profile(self, user_id: str) -> Optional[UserProfile]: ...
    
    @abstractmethod
    def save_profile(self, profile: UserProfile, source: str) -> None: ...
    
    # Additional profile-specific operations...

class JsonProfileStore(ProfileStorageInterface):
    """JSON implementation following data/json_store.py atomic patterns"""
    def __init__(self, storage_path: Path = Path("data")):
        self.profile_file = storage_path / "user_profiles.json"
        self.events_file = storage_path / "profile_events.jsonl"
```

### **Onboarding Workflow** (`profile_and_onboarding/onboarding_workflow.py`)

**Following Agno v2.0 workflow patterns from existing health logger implementation:**

```python
from agno.workflow.v2 import Workflow, Step, StepInput, StepOutput
from agno.agent import Agent
from agno.models.openai import OpenAIChat

# Step-specific response models for structured outputs
class OnboardConditionsResponse(BaseModel):
    conditions: List[str]
    confidence: float = Field(ge=0.0, le=1.0)

class OnboardMedicationsResponse(BaseModel):
    medications: List[Medication]
    confidence: float = Field(ge=0.0, le=1.0)

class OnboardingPreviewResponse(BaseModel):
    action: Literal["confirm", "edit_conditions", "edit_medications", "edit_routines"]
    feedback: Optional[str] = None

# Agents with structured response models
conditions_agent = Agent(
    name="ConditionsOnboardingAgent",
    model=OpenAIChat(id="gpt-4o-mini-2024-07-18"),
    response_model=OnboardConditionsResponse,
    instructions=[
        "Extract health conditions from user input with confidence scoring.",
        "Use medical terminology and normalize condition names.",
        "Only suggest conditions explicitly mentioned by the user."
    ]
)

# Workflow steps following health logger pattern
def onboard_conditions_step(step_input: StepInput) -> StepOutput:
    """Step 1: Collect health conditions with workflow_session_state persistence"""
    workflow = step_input.workflow
    
    # Initialize session state following Agno patterns
    if workflow.workflow_session_state is None:
        workflow.workflow_session_state = {}
    
    if "onboarding_progress" not in workflow.workflow_session_state:
        workflow.workflow_session_state["onboarding_progress"] = {
            "step_index": 0,
            "partial_profile": {},
            "user_id": workflow.session_id or "anonymous"
        }
    
    # Run conditions agent
    result = conditions_agent.run(step_input.message or "Please tell me about your health conditions")
    
    # Store in session state for resumability
    progress = workflow.workflow_session_state["onboarding_progress"]
    progress["partial_profile"]["conditions"] = [{
        "name": condition,
        "status": "active",
        "source": "onboarding"
    } for condition in result.conditions]
    progress["step_index"] = 1
    
    return StepOutput(
        content=f"Great! I've noted your conditions: {', '.join(result.conditions)}. Now, what medications are you currently taking?",
        metadata={"confidence": result.confidence, "step_completed": "conditions"}
    )
```

### **Profile Update Agent** (`profile_and_onboarding/updater_agent.py`)

**Following structured output patterns from existing health logger agents:**

```python
# Structured response models for profile updates
class ProposedProfileChange(BaseModel):
    intent: Literal["profile_update"]
    changes: List[ProfileChangeDetail] = Field(default_factory=list)
    clarifications: List[str] = Field(default_factory=list)
    overall_confidence: float = Field(ge=0.0, le=1.0)
    requires_confirmation: bool = True

class ProfileChangeDetail(BaseModel):
    entity: Literal["medication", "condition", "routine"]
    action: Literal["add", "update", "deactivate"]
    data: Union[MedicationChange, ConditionChange, RoutineChange]
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str

# Profile updater agent with confidence thresholds
profile_updater_agent = Agent(
    name="ProfileUpdaterAgent",
    model=OpenAIChat(id="gpt-4o-mini-2024-07-18"),
    response_model=ProposedProfileChange,
    add_history_to_messages=True,  # Context awareness
    num_history_runs=3,
    instructions=[
        "Analyze user messages for profile updates with high confidence.",
        "Only propose changes with confidence >= 0.7.",
        "For low confidence items, add clarification questions instead.",
        "Use existing condition families from core.ontology for normalization.",
        "Ensure all medication changes include proper dosage and timing."
    ]
)
```

### **Profile Commit Logic** (`profile_and_onboarding/commit_step.py`)

**Following deterministic processing patterns from `healthlogger/workflow_steps.py`:**

```python
def commit_profile_changes(
    user_id: str,
    proposed_changes: ProposedProfileChange,
    user_choice: str,
    profile_store: ProfileStorageInterface
) -> str:
    """Deterministic profile commit function following health logger patterns"""
    
    if user_choice.lower() != "confirm":
        return f"Profile update cancelled. No changes made."
    
    # Load existing profile
    current_profile = profile_store.get_profile(user_id)
    if not current_profile:
        current_profile = UserProfile(user_id=user_id)
    
    # Apply changes atomically with audit trail
    for change_detail in proposed_changes.changes:
        try:
            # Generate idempotency key
            change_key = generate_idempotency_key(
                user_id, 
                change_detail.entity, 
                change_detail.data.model_dump()
            )
            
            # Apply change with audit event
            _apply_profile_change(current_profile, change_detail, change_key)
            
        except Exception as e:
            logger.error(f"Failed to apply profile change: {e}")
            return f"Error applying changes: {str(e)}"
    
    # Atomic save
    profile_store.save_profile(current_profile, source="chat")
    
    return f"Successfully updated your profile with {len(proposed_changes.changes)} changes."
```

### **Router Agent Integration** (`health_advisor/router/schema.py` updates)

**Extending existing RouterDecision schema to include profile intents:**

```python
# Update existing RouterDecision to include profile intents
class RouterDecision(BaseModel):
    primary_intent: Literal[
        "log", "recall", "coach", "profile_update", "onboarding",  # Added profile intents
        "clarify_response", "control_action", "unknown"
    ]
    secondary_intent: Optional[Literal[
        "log", "recall", "coach", "profile_update"
    ]] = None
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str
    profile_action: Optional[Literal["start_onboarding", "update_profile", "view_profile"]] = None
```

### **MasterAgent Orchestration** (`agents.py` updates)

**Extending existing MasterAgent to handle profile intents:**

```python
# Update existing MasterAgent orchestration logic
def handle_profile_intent(
    router_decision: RouterDecision,
    message: str,
    session_state: Dict[str, Any]
) -> ChatResult:
    """Handle profile-related intents in existing MasterAgent"""
    
    # Short-circuit for profile confirmations
    if message.lower().startswith("/resolve") and "pending_profile_change" in session_state:
        pending_change = session_state.pop("pending_profile_change")
        result = commit_profile_changes(
            user_id=session_state.get("user_id", "anonymous"),
            proposed_changes=pending_change,
            user_choice="confirm",
            profile_store=get_profile_store()
        )
        return ChatResult(content=result)
    
    # Route to appropriate profile handler
    if router_decision.profile_action == "start_onboarding":
        return onboarding_workflow.run(message)
    elif router_decision.profile_action == "update_profile":
        return handle_profile_update(message, session_state)
    elif router_decision.profile_action == "view_profile":
        return handle_profile_view(session_state.get("user_id"))
    
    return ChatResult(content="I'm not sure how to help with that profile request.")

# Integration with existing AGENTS registry
AGENTS = {
    "Health Companion (Auto-Router)": master_agent,  # Updated with profile support
    "Profile & Onboarding": ProfileOnboardingWrapper(),  # New specialized access
    "Health Logger (v3.1 Multi-Modal)": health_logger_v31,
    "Recall Agent": recall_agent_wrapper,
    "Coach Agent": coach_agent_wrapper,
    # ... existing agents
}
```

## 3. Implementation Files & Code Structure

### **File Organization Following Existing Architecture**

```
profile_and_onboarding/
├── __init__.py                 # Package initialization
├── schema.py                   # Pydantic models (following data/schemas/ pattern)
├── storage.py                  # Storage interface & JSON implementation
├── agents.py                   # Profile-related agents
├── onboarding_workflow.py      # Agno Workflow v2.0 implementation
├── updater_agent.py           # Profile update agent with tools
├── commit_step.py             # Deterministic commit functions
└── tools.py                   # Profile management tools
```

### **Complete Schema Implementation** (`profile_and_onboarding/schema.py`)

```python
# profile_and_onboarding/schema.py
from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Union
from datetime import datetime, timezone
import uuid

# Core data models with consistent patterns
class Condition(BaseModel):
    name: str
    status: Literal["active", "inactive"] = "active"
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None
    severity: Optional[int] = Field(None, ge=1, le=10)
    source: Literal["user", "inferred", "imported"] = "user"

class Medication(BaseModel):
    name: str
    type: Literal["preventative", "abortive", "supplement", "other"]
    dose: Optional[str] = None
    schedule: Optional[str] = None
    status: Literal["active", "inactive"] = "active"
    started_at: Optional[datetime] = None
    stopped_at: Optional[datetime] = None
    prescriber: Optional[str] = None
    source: Literal["user", "inferred", "imported"] = "user"

class Routine(BaseModel):
    category: Literal["sleep", "hydration", "exercise", "stress", "nutrition"]
    pattern: str  # "Sleep 22:00-06:00", "Water 8 glasses daily"
    frequency: Optional[str] = None  # "daily", "weekly", etc.
    last_confirmed_at: Optional[datetime] = None
    effectiveness: Optional[int] = Field(None, ge=1, le=5)  # User-rated effectiveness

class UserProfile(BaseModel):
    user_id: str
    schema_version: int = 1
    user_tz: str = "UTC"
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    last_updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    last_updated_by: str = "system"
    onboarding_completed: bool = False
    onboarding_completed_at: Optional[datetime] = None
    
    # Health profile data
    conditions: List[Condition] = Field(default_factory=list)
    medications: List[Medication] = Field(default_factory=list)
    routines: List[Routine] = Field(default_factory=list)
    
    # Preferences and settings
    notification_preferences: dict = Field(default_factory=dict)
    privacy_settings: dict = Field(default_factory=dict)

# Audit trail following existing event patterns
class ProfileEvent(BaseModel):
    event_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    ts: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    user_id: str
    kind: Literal["add", "update", "deactivate", "create", "onboard"]
    entity: Literal["condition", "medication", "routine", "profile"]
    before: Optional[dict] = None
    after: Optional[dict] = None
    source: Literal["onboarding", "chat", "import", "system"]
    idempotency_key: str
    metadata: dict = Field(default_factory=dict)

# Change proposal models for agent structured outputs
class MedicationChange(BaseModel):
    name: str
    type: Literal["preventative", "abortive", "supplement", "other"]
    dose: Optional[str] = None
    schedule: Optional[str] = None
    prescriber: Optional[str] = None

class ConditionChange(BaseModel):
    name: str
    severity: Optional[int] = Field(None, ge=1, le=10)
    started_at: Optional[str] = None  # Natural language date

class RoutineChange(BaseModel):
    category: Literal["sleep", "hydration", "exercise", "stress", "nutrition"]
    pattern: str
    frequency: Optional[str] = None

# Agent response models
class ProfileChangeDetail(BaseModel):
    entity: Literal["medication", "condition", "routine"]
    action: Literal["add", "update", "deactivate"]
    data: Union[MedicationChange, ConditionChange, RoutineChange]
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str

class ProposedProfileChange(BaseModel):
    intent: Literal["profile_update"]
    changes: List[ProfileChangeDetail] = Field(default_factory=list)
    clarifications: List[str] = Field(default_factory=list)
    overall_confidence: float = Field(ge=0.0, le=1.0)
    requires_confirmation: bool = True

# Onboarding step response models
class OnboardConditionsResponse(BaseModel):
    conditions: List[str]
    confidence: float = Field(ge=0.0, le=1.0)
    needs_clarification: bool = False
    clarification_question: Optional[str] = None

class OnboardMedicationsResponse(BaseModel):
    medications: List[MedicationChange]
    confidence: float = Field(ge=0.0, le=1.0)
    needs_clarification: bool = False
    clarification_question: Optional[str] = None

class OnboardingPreviewResponse(BaseModel):
    action: Literal["confirm", "edit_conditions", "edit_medications", "edit_routines"]
    feedback: Optional[str] = None
    summary: str  # Summary of what will be saved
```
    ```

### **Storage Implementation** (`profile_and_onboarding/storage.py`)

```python
# profile_and_onboarding/storage.py
import json
import uuid
import hashlib
from abc import ABC, abstractmethod
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, List
from .schema import UserProfile, ProfileEvent, Medication, Condition, Routine

class ProfileStorageInterface(ABC):
    """Abstract storage interface following data/storage_interface.py patterns"""
    
    @abstractmethod
    def get_profile(self, user_id: str) -> Optional[UserProfile]:
        """Get user profile by ID"""
        pass
    
    @abstractmethod
    def save_profile(self, profile: UserProfile, source: str) -> None:
        """Save user profile with audit trail"""
        pass
    
    @abstractmethod
    def add_or_update_medication(self, user_id: str, medication: Medication, source: str) -> None:
        """Add or update medication with audit trail"""
        pass
    
    @abstractmethod
    def deactivate_medication(self, user_id: str, med_name: str, source: str) -> None:
        """Soft delete medication with audit trail"""
        pass
    
    @abstractmethod
    def add_or_update_condition(self, user_id: str, condition: Condition, source: str) -> None:
        """Add or update condition with audit trail"""
        pass
    
    @abstractmethod
    def append_event(self, event: ProfileEvent) -> None:
        """Append event to audit log"""
        pass

class JsonProfileStore(ProfileStorageInterface):
    """JSON implementation following data/json_store.py atomic patterns"""
    
    def __init__(self, storage_path: Path = Path("data")):
        self.profile_file = storage_path / "user_profiles.json"
        self.events_file = storage_path / "profile_events.jsonl"
        storage_path.mkdir(exist_ok=True)
        
        # Load existing profiles
        self.profiles = self._load_profiles()
    
    def _load_profiles(self) -> dict:
        """Load profiles with error handling"""
        if not self.profile_file.exists():
            return {}
        try:
            with open(self.profile_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading profiles: {e}")
            return {}
    
    def _generate_idempotency_key(self, user_id: str, entity: str, payload: dict) -> str:
        """Generate idempotency key following existing patterns"""
        payload_str = json.dumps(payload, sort_keys=True, default=str)
        raw_string = f"{user_id}:{entity}:{payload_str}"
        return hashlib.sha256(raw_string.encode()).hexdigest()
    
    def _atomic_save_profiles(self) -> None:
        """Atomic save following data/json_store.py patterns"""
        temp_file = self.profile_file.with_suffix(".tmp")
        try:
            with open(temp_file, 'w') as f:
                json.dump(self.profiles, f, indent=2, default=str)
            temp_file.rename(self.profile_file)
        except Exception as e:
            if temp_file.exists():
                temp_file.unlink()
            raise e
    
    def get_profile(self, user_id: str) -> Optional[UserProfile]:
        """Get user profile with error handling"""
        profile_data = self.profiles.get(user_id)
        if not profile_data:
            return None
        try:
            return UserProfile(**profile_data)
        except Exception as e:
            print(f"Error parsing profile for {user_id}: {e}")
            return None
    
    def save_profile(self, profile: UserProfile, source: str) -> None:
        """Save profile with audit trail and idempotency"""
        # Get before state for audit
        before_state = self.profiles.get(profile.user_id)
        
        # Update timestamps
        profile.last_updated_at = datetime.now(timezone.utc)
        profile.last_updated_by = source
        
        # Generate idempotency key
        profile_dict = profile.model_dump(mode='json')
        idempotency_key = self._generate_idempotency_key(
            profile.user_id, "profile", profile_dict
        )
        
        # Check for duplicate operations (basic deduplication)
        recent_events = self._get_recent_events(profile.user_id, minutes=5)
        if any(event.get("idempotency_key") == idempotency_key for event in recent_events):
            print(f"Duplicate profile save operation detected for {profile.user_id}")
            return
        
        # Atomic save
        self.profiles[profile.user_id] = profile_dict
        self._atomic_save_profiles()
        
        # Create audit event
        event = ProfileEvent(
            user_id=profile.user_id,
            kind="update" if before_state else "create",
            entity="profile",
            before=before_state,
            after=profile_dict,
            source=source,
            idempotency_key=idempotency_key
        )
        self.append_event(event)
    
    def append_event(self, event: ProfileEvent) -> None:
        """Append event to audit log following events.jsonl pattern"""
        try:
            with open(self.events_file, "a") as f:
                f.write(event.model_dump_json() + "\n")
        except IOError as e:
            print(f"Error writing event: {e}")
    
    def _get_recent_events(self, user_id: str, minutes: int = 5) -> List[dict]:
        """Get recent events for deduplication"""
        # Simplified implementation - in production, would use more efficient approach
        if not self.events_file.exists():
            return []
        
        cutoff_time = datetime.now(timezone.utc).timestamp() - (minutes * 60)
        recent_events = []
        
        try:
            with open(self.events_file, "r") as f:
                for line in f:
                    try:
                        event = json.loads(line.strip())
                        if (event.get("user_id") == user_id and 
                            datetime.fromisoformat(event.get("ts", "")).timestamp() > cutoff_time):
                            recent_events.append(event)
                    except (json.JSONDecodeError, ValueError):
                        continue
        except IOError:
            pass
        
        return recent_events

# Factory function for dependency injection
def get_profile_store() -> ProfileStorageInterface:
    """Factory function following existing patterns"""
    return JsonProfileStore()
```

### **Onboarding Workflow Tools** (`profile_and_onboarding/tools.py`)

```python
# profile_and_onboarding/tools.py
from agno import Agent, tool
from typing import Optional, List, Dict, Any
from .storage import get_profile_store, ProfileStorageInterface
from .schema import UserProfile, Condition, Medication, Routine
from core.ontology import normalize_condition
from core.timeutils import parse_natural_time

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
    
    if profile.conditions:
        conditions = [c.name for c in profile.conditions if c.status == "active"]
        summary_parts.append(f"Conditions: {', '.join(conditions)}")
    
    if profile.medications:
        meds = [f"{m.name} ({m.dose})" for m in profile.medications if m.status == "active"]
        summary_parts.append(f"Medications: {', '.join(meds)}")
    
    if profile.routines:
        routines = [f"{r.category}: {r.pattern}" for r in profile.routines]
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
def finalize_onboarding(agent: Agent) -> str:
    """Complete onboarding and create final user profile"""
    if not agent.workflow_session_state or "onboarding_progress" not in agent.workflow_session_state:
        return "No onboarding in progress"
    
    progress = agent.workflow_session_state["onboarding_progress"]
    partial_profile = progress.get("partial_profile", {})
    user_id = progress.get("user_id", "anonymous")
    
    # Create full profile
    profile = UserProfile(
        user_id=user_id,
        onboarding_completed=True,
        conditions=[Condition(**c) for c in partial_profile.get("conditions", [])],
        medications=[Medication(**m) for m in partial_profile.get("medications", [])],
        routines=[Routine(**r) for r in partial_profile.get("routines", [])]
    )
    
    # Save to storage
    profile_store = get_profile_store()
    profile_store.save_profile(profile, source="onboarding")
    
    # Clear onboarding state
    agent.workflow_session_state.pop("onboarding_progress", None)
    
    return f"Onboarding completed! Created profile with {len(profile.conditions)} conditions, {len(profile.medications)} medications, and {len(profile.routines)} routines."
```

### **Complete Onboarding Workflow** (`profile_and_onboarding/onboarding_workflow.py`)

```python
# profile_and_onboarding/onboarding_workflow.py
from agno.workflow.v2 import Workflow, Step, StepInput, StepOutput
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from typing import Dict, Any, Optional
from .schema import (
    OnboardConditionsResponse, OnboardMedicationsResponse, 
    OnboardingPreviewResponse, Condition, Medication, Routine
)
from .tools import save_onboarding_progress, finalize_onboarding
from core.ontology import normalize_condition

# Onboarding agents with structured outputs
conditions_agent = Agent(
    name="ConditionsOnboardingAgent",
    model=OpenAIChat(id="gpt-4o-mini-2024-07-18"),
    response_model=OnboardConditionsResponse,
    instructions=[
        "Extract health conditions from user input with confidence scoring.",
        "Use medical terminology and normalize condition names.",
        "Only include conditions explicitly mentioned by the user.",
        "If unsure about any condition, set needs_clarification=True and ask a specific question."
    ]
)

medications_agent = Agent(
    name="MedicationsOnboardingAgent", 
    model=OpenAIChat(id="gpt-4o-mini-2024-07-18"),
    response_model=OnboardMedicationsResponse,
    instructions=[
        "Extract medications from user input including dosage and schedule.",
        "Categorize medications as preventative, abortive, supplement, or other.",
        "If dosage or schedule information is missing, set needs_clarification=True.",
        "Focus on current medications, not past ones."
    ]
)

preview_agent = Agent(
    name="OnboardingPreviewAgent",
    model=OpenAIChat(id="gpt-4o-mini-2024-07-18"),
    response_model=OnboardingPreviewResponse,
    instructions=[
        "Present a summary of collected profile information for user confirmation.",
        "Allow user to confirm or request edits to specific sections.",
        "Respond with appropriate action based on user feedback."
    ]
)

# Workflow step functions
def onboard_conditions_step(step_input: StepInput) -> StepOutput:
    """Step 1: Collect health conditions"""
    workflow = step_input.workflow
    
    # Initialize session state
    if workflow.workflow_session_state is None:
        workflow.workflow_session_state = {}
    
    if "onboarding_progress" not in workflow.workflow_session_state:
        workflow.workflow_session_state["onboarding_progress"] = {
            "step_index": 0,
            "partial_profile": {},
            "user_id": workflow.session_id or "anonymous"
        }
    
    # Run conditions extraction
    message = step_input.message or "What health conditions are you currently managing?"
    result = conditions_agent.run(message)
    
    if result.needs_clarification:
        return StepOutput(
            content=result.clarification_question or "Could you provide more details about your conditions?",
            metadata={"needs_clarification": True, "step": "conditions"}
        )
    
    # Save progress
    progress = workflow.workflow_session_state["onboarding_progress"]
    progress["partial_profile"]["conditions"] = [
        {
            "name": normalize_condition(condition) or condition,
            "status": "active",
            "source": "onboarding"
        }
        for condition in result.conditions
    ]
    progress["step_index"] = 1
    
    conditions_list = ', '.join(result.conditions) if result.conditions else "none mentioned"
    return StepOutput(
        content=f"Thank you! I've noted these conditions: {conditions_list}. Now, what medications are you currently taking?",
        metadata={"confidence": result.confidence, "step_completed": "conditions"}
    )

def onboard_medications_step(step_input: StepInput) -> StepOutput:
    """Step 2: Collect medications"""
    workflow = step_input.workflow
    
    result = medications_agent.run(step_input.message or "Please list your current medications")
    
    if result.needs_clarification:
        return StepOutput(
            content=result.clarification_question or "Could you provide more details about your medications?",
            metadata={"needs_clarification": True, "step": "medications"}
        )
    
    # Save progress
    progress = workflow.workflow_session_state["onboarding_progress"]
    progress["partial_profile"]["medications"] = [
        med.model_dump() for med in result.medications
    ]
    progress["step_index"] = 2
    
    med_count = len(result.medications)
    return StepOutput(
        content=f"Got it! I've recorded {med_count} medications. Finally, do you have any daily routines that help manage your health?",
        metadata={"confidence": result.confidence, "step_completed": "medications"}
    )

def onboard_routines_step(step_input: StepInput) -> StepOutput:
    """Step 3: Collect routines (simplified for this example)"""
    workflow = step_input.workflow
    
    # Simple routine extraction (could use another agent)
    message = step_input.message or ""
    routines = []
    
    # Basic keyword extraction for routines
    if "sleep" in message.lower():
        routines.append({"category": "sleep", "pattern": "User-defined sleep routine"})
    if "water" in message.lower() or "hydration" in message.lower():
        routines.append({"category": "hydration", "pattern": "User-defined hydration routine"})
    if "exercise" in message.lower() or "workout" in message.lower():
        routines.append({"category": "exercise", "pattern": "User-defined exercise routine"})
    
    # Save progress
    progress = workflow.workflow_session_state["onboarding_progress"]
    progress["partial_profile"]["routines"] = routines
    progress["step_index"] = 3
    
    return StepOutput(
        content="Perfect! Let me show you a summary of your profile for confirmation.",
        metadata={"step_completed": "routines"}
    )

def preview_and_confirm_step(step_input: StepInput) -> StepOutput:
    """Step 4: Preview profile and get confirmation"""
    workflow = step_input.workflow
    progress = workflow.workflow_session_state.get("onboarding_progress", {})
    partial_profile = progress.get("partial_profile", {})
    
    # Create summary
    summary_parts = ["Here's your health profile summary:"]
    
    conditions = partial_profile.get("conditions", [])
    if conditions:
        condition_names = [c["name"] for c in conditions]
        summary_parts.append(f"Conditions: {', '.join(condition_names)}")
    
    medications = partial_profile.get("medications", [])
    if medications:
        med_names = [f"{m['name']} ({m.get('dose', 'no dose specified')})" for m in medications]
        summary_parts.append(f"Medications: {', '.join(med_names)}")
    
    routines = partial_profile.get("routines", [])
    if routines:
        routine_desc = [f"{r['category']}: {r['pattern']}" for r in routines]
        summary_parts.append(f"Routines: {', '.join(routine_desc)}")
    
    summary = "\n\n".join(summary_parts)
    summary += "\n\nWould you like to confirm this profile, or edit any section?"
    
    # Check for user response
    if step_input.message:
        result = preview_agent.run(f"User response to profile summary: {step_input.message}")
        
        if result.action == "confirm":
            # Finalize onboarding
            final_result = finalize_onboarding.execute(workflow=workflow)
            return StepOutput(
                content=f"Excellent! {final_result} You're all set to start logging your health data.",
                metadata={"onboarding_completed": True}
            )
        elif result.action.startswith("edit_"):
            # Route back to appropriate step
            section = result.action.replace("edit_", "")
            progress["step_index"] = {"conditions": 0, "medications": 1, "routines": 2}.get(section, 0)
            return StepOutput(
                content=f"Let's update your {section}. Please provide the new information.",
                metadata={"editing_section": section}
            )
    
    return StepOutput(content=summary, metadata={"awaiting_confirmation": True})

# Main onboarding workflow
class OnboardingWorkflow(Workflow):
    """Complete onboarding workflow with resumable state"""
    
    def __init__(self):
        super().__init__(
            name="Health Profile Onboarding",
            steps=[
                Step(name="CollectConditions", executor=onboard_conditions_step),
                Step(name="CollectMedications", executor=onboard_medications_step), 
                Step(name="CollectRoutines", executor=onboard_routines_step),
                Step(name="PreviewAndConfirm", executor=preview_and_confirm_step)
            ]
        )
    
    def run(self, message: str = None, **kwargs) -> str:
        """Run onboarding workflow with state management"""
        try:
            result = super().run(message=message, **kwargs)
            return result.content if hasattr(result, 'content') else str(result)
        except Exception as e:
            return f"Error during onboarding: {str(e)}. Please try again."

# Workflow wrapper for agent registry integration
class ProfileOnboardingWrapper:
    """Wrapper for Gradio integration following existing patterns"""
    
    name = "Profile & Onboarding"
    description = "Complete health profile setup and management using structured onboarding workflow"
    
    def __init__(self):
        self.workflow = OnboardingWorkflow()
    
    def run(self, prompt: str, files=None) -> dict:
        """Run method following existing ChatResult pattern"""
        try:
            content = self.workflow.run(message=prompt)
            return {
                "content": content,
                "metadata": {
                    "agent_name": self.name,
                    "workflow_type": "onboarding",
                    "supports_files": False
                }
            }
        except Exception as e:
            return {
                "content": f"Error during onboarding: {str(e)}",
                "metadata": {"error": True}
            }
```

## 4. Integration with Existing Health Companion Architecture

### **Router Agent Updates** (Extending `health_advisor/router/schema.py`)

```python
# Add to existing RouterDecision schema
class RouterDecision(BaseModel):
    primary_intent: Literal[
        "log", "recall", "coach", 
        "profile_update", "onboarding", "profile_view",  # NEW: Profile intents
        "clarify_response", "control_action", "unknown"
    ]
    # ... existing fields ...
    profile_action: Optional[Literal[
        "start_onboarding", "update_profile", "view_profile", "edit_profile"
    ]] = None
```

### **MasterAgent Orchestration Updates** (Extending `agents.py`)

```python
# Add profile handling to existing MasterAgent
from profile_and_onboarding.storage import get_profile_store
from profile_and_onboarding.onboarding_workflow import ProfileOnboardingWrapper
from profile_and_onboarding.updater_agent import profile_updater_agent
from profile_and_onboarding.commit_step import commit_profile_changes

def handle_profile_routing(
    router_decision: RouterDecision,
    message: str,
    session_state: Dict[str, Any]
) -> Any:
    """Handle profile intents within existing orchestration"""
    
    # Short-circuit for profile confirmations (following existing /resolve pattern)
    if message.lower().startswith("/resolve profile") and "pending_profile_change" in session_state:
        pending_change = session_state.pop("pending_profile_change")
        user_id = session_state.get("user_id", "anonymous")
        
        result = commit_profile_changes(
            user_id=user_id,
            proposed_changes=pending_change,
            user_choice="confirm",
            profile_store=get_profile_store()
        )
        return result
    
    # Route based on profile action
    if router_decision.profile_action == "start_onboarding":
        onboarding_wrapper = ProfileOnboardingWrapper()
        return onboarding_wrapper.run(message)
    
    elif router_decision.profile_action == "update_profile":
        result = profile_updater_agent.run(message)
        if result.overall_confidence >= 0.7 and not result.clarifications:
            # High confidence - prepare for confirmation
            session_state["pending_profile_change"] = result
            return {
                "content": f"I'd like to update your profile with these changes:\n" +
                          f"\n".join([f"- {change.rationale}" for change in result.changes]) +
                          f"\n\nType '/resolve profile' to confirm these changes.",
                "metadata": {"requires_confirmation": True}
            }
        else:
            # Low confidence or clarifications needed
            clarifications = "\n".join([f"- {q}" for q in result.clarifications])
            return {
                "content": f"I need some clarification:\n{clarifications}",
                "metadata": {"requires_clarification": True}
            }
    
    elif router_decision.profile_action == "view_profile":
        from profile_and_onboarding.tools import get_profile_summary
        user_id = session_state.get("user_id", "anonymous")
        summary = get_profile_summary.execute(user_id=user_id)
        return {"content": summary, "metadata": {"profile_view": True}}
    
    return {"content": "I'm not sure how to help with that profile request."}

# Update existing AGENTS registry
AGENTS = {
    "Health Companion (Auto-Router)": master_agent,  # Enhanced with profile support
    "Profile & Onboarding": ProfileOnboardingWrapper(),  # New dedicated access
    "Health Logger (v3.1 Multi-Modal)": health_logger_v31,
    "Recall Agent": recall_agent_wrapper,
    "Coach Agent": coach_agent_wrapper,
    # ... existing agents
}
```
## 5. Implementation Validation Checklist

### **✅ Agno Framework Compliance**
- [ ] **Workflow v2.0 Pattern**: Uses proper Step, StepInput, StepOutput structures
- [ ] **Session State Management**: Implements workflow_session_state following documented patterns
- [ ] **Structured Outputs**: All agents use response_model with Pydantic schemas
- [ ] **Tool Decoration**: Profile management tools properly decorated with @tool
- [ ] **Agent Instructions**: Clear, specific instructions following existing agent patterns

### **✅ Architecture Integration**
- [ ] **Layered Architecture**: Follows existing core/, data/, health_advisor/ structure
- [ ] **Shared Primitives**: Uses core/ontology.py, core/timeutils.py, core/policies.py
- [ ] **Storage Interface**: Extends data/storage_interface.py pattern
- [ ] **Router Integration**: Properly extends health_advisor/router/schema.py
- [ ] **MasterAgent Integration**: Seamlessly integrates with existing orchestration

### **✅ Data Consistency & Safety**
- [ ] **Atomic Operations**: JsonProfileStore performs atomic writes with temp files
- [ ] **Audit Trail**: Every mutation generates ProfileEvent with idempotency_key
- [ ] **Soft Deletes**: Uses status="inactive" instead of actual deletion
- [ ] **Idempotency**: Duplicate operations detected and prevented
- [ ] **UTC Timestamps**: All timestamps use timezone-aware UTC datetime

### **✅ Workflow Requirements**
- [ ] **Resumable Onboarding**: workflow_session_state persists progress across sessions
- [ ] **Structured Data Capture**: Each step uses specific response_model (OnboardConditionsResponse, etc.)
- [ ] **Edit Capability**: PreviewConfirm step allows /edit commands to return to specific steps
- [ ] **Confidence Thresholds**: Low confidence triggers clarification instead of proceeding
- [ ] **Error Handling**: Graceful fallbacks for all failure modes

### **✅ Agent Behavior**
- [ ] **Profile Updater**: Returns strongly-typed ProposedProfileChange with confidence scoring
- [ ] **Clarification Logic**: confidence < 0.7 generates specific clarification questions
- [ ] **Context Awareness**: Uses add_history_to_messages=True for conversation context
- [ ] **Medical Safety**: Integrates with existing safety guardrails from Coach Agent
- [ ] **Condition Normalization**: Uses normalize_condition from core/ontology.py

### **✅ Orchestration & Control Flow**
- [ ] **/resolve Command**: Short-circuits router to call deterministic commit_profile_changes
- [ ] **Multi-Intent Support**: Supports profile + coach chaining ("update my meds and give advice")
- [ ] **Session Management**: Proper user_id handling and session isolation
- [ ] **State Cleanup**: Clears onboarding_progress after completion
- [ ] **Error Recovery**: Handles workflow failures without data corruption

### **✅ User Experience**
- [ ] **Progressive Disclosure**: Onboarding asks for information step-by-step
- [ ] **Clear Confirmations**: Profile changes require explicit user confirmation
- [ ] **Edit Flexibility**: Users can modify any section during onboarding preview
- [ ] **Consistent Terminology**: Uses same health terms as existing agents
- [ ] **Helpful Feedback**: Clear success/error messages following existing patterns

### **✅ Testing Requirements**
- [ ] **Unit Tests**: ProfileStore idempotency, atomic writes, soft deletes
- [ ] **Workflow Tests**: Onboarding resume paths, step transitions
- [ ] **Integration Tests**: Router decisions, MasterAgent orchestration
- [ ] **Data Tests**: Profile serialization, event audit trails
- [ ] **Edge Cases**: Malformed input, API failures, storage errors

## 6. Implementation Timeline

### **Phase 1: Core Infrastructure (Week 1)**
- Implement ProfileStorageInterface and JsonProfileStore
- Create complete schema.py with all Pydantic models
- Set up basic profile management tools
- Create unit tests for storage layer

### **Phase 2: Onboarding Workflow (Week 2)**
- Implement OnboardingWorkflow with all steps
- Create onboarding agents with structured outputs
- Implement workflow_session_state management
- Test resumable onboarding scenarios

### **Phase 3: Profile Updates (Week 3)**
- Implement ProfileUpdaterAgent with confidence scoring
- Create commit_profile_changes deterministic function
- Implement /resolve command handling
- Test profile update and confirmation flows

### **Phase 4: Integration & Testing (Week 4)**
- Integrate with existing Router Agent and MasterAgent
- Update Gradio UI with ProfileOnboardingWrapper
- Comprehensive testing with existing health companion features
- Performance testing and optimization

This implementation plan ensures the Profile & Onboarding system integrates seamlessly with the existing Health Companion architecture while following Agno v2.0 best practices and maintaining the same level of reliability and user experience as the existing production-ready agents.

---

## Summary

This updated implementation plan provides a comprehensive, production-ready approach to implementing Profile & Onboarding functionality within the existing Health Companion architecture. The plan follows established Agno v2.0 patterns, integrates seamlessly with existing agents and storage systems, and maintains the same high standards for reliability, safety, and user experience.

**Key improvements over the original plan:**
- **Full Agno v2.0 compliance** with proper workflow patterns and session state management
- **Architectural consistency** with existing health companion layered structure
- **Enhanced error handling** and graceful degradation following established patterns
- **Comprehensive validation checklist** ensuring production-ready implementation
- **Detailed integration points** with Router Agent and MasterAgent orchestration

The implementation maintains the atomic, idempotent, and auditable principles while leveraging the existing infrastructure for maximum reliability and maintainability.

---

**Plan Updated:** August 21, 2025  
**Status:** Ready for Implementation  
**Integration:** Health Companion Auto-Router v1.0  
**Framework:** Agno v2.0 with layered architecture patterns


code
Python
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# profile_and_onboarding/profile_store.py
import json
import uuid
import hashlib
from abc import ABC, abstractmethod
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from .schema import UserProfile, ProfileEvent, Medication

class ProfileStore(ABC):
    @abstractmethod
    def get(self, user_id: str) -> Optional[UserProfile]: ...
    
    @abstractmethod
    def save(self, profile: UserProfile, source: str) -> None: ...
    
    @abstractmethod
    def add_or_update_med(self, user_id: str, med_data: Medication, source: str) -> None: ...
    
    @abstractmethod
    def deactivate_med(self, user_id: str, med_name: str, source: str) -> None: ...

    @abstractmethod
    def append_event(self, event: ProfileEvent) -> None: ...

class JsonProfileStore(ProfileStore):
    def __init__(self, storage_path: Path):
        self.profile_file = storage_path / "user_profiles.json"
        self.events_file = storage_path / "profile_events.jsonl"
        self.profiles = self._load_profiles()

    def _generate_idempotency_key(self, user_id: str, entity: str, payload: dict) -> str:
        payload_str = json.dumps(payload, sort_keys=True)
        return hashlib.sha256(f"{user_id}:{entity}:{payload_str}".encode()).hexdigest()

    def _atomic_save(self):
        temp_file = self.profile_file.with_suffix(".tmp")
        temp_file.write_text(json.dumps(self.profiles, indent=2, default=str))
        temp_file.rename(self.profile_file)

    def get(self, user_id: str) -> Optional[UserProfile]:
        data = self.profiles.get(user_id)
        return UserProfile(**data) if data else None

    def save(self, profile: UserProfile, source: str):
        # In a real app, you would fetch the 'before' state for the event
        before_state = self.profiles.get(profile.user_id)

        profile.last_updated_at = datetime.now(timezone.utc)
        profile.last_updated_by = source
        self.profiles[profile.user_id] = profile.model_dump(mode='json')
        self._atomic_save()

        event = ProfileEvent(
            event_id=str(uuid.uuid4()),
            user_id=profile.user_id,
            kind="update" if before_state else "create",
            entity="profile",
            before=before_state,
            after=profile.model_dump(mode='json'),
            source=source,
            idempotency_key=self._generate_idempotency_key(profile.user_id, "profile", profile.model_dump(mode='json'))
        )
        self.append_event(event)

    def append_event(self, event: ProfileEvent):
        with open(self.events_file, "a") as f:
            f.write(event.model_dump_json() + "\n")
            
    # ... Implement other methods like add_or_update_med with soft deletes and event generation

3. workflows/orchestrator.py (Updated with /resolve short-circuit)

code
Python
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# workflows/orchestrator.py
# (Showing only the updated execution function)

from profile_and_onboarding.commit_step import commit_profile_changes

def route_and_dispatch_logic(step_input: StepInput) -> StepOutput:
    workflow = step_input.workflow
    message = step_input.message
    session_state = workflow.workflow_session_state or {}
    user_id = session_state.get("user_id")

    # 1. Handle short-circuiting for pending profile changes
    if message.lower().startswith("/resolve") and "pending_profile_change" in session_state:
        choice = message.split(" ", 1) if " " in message else "confirm"
        result = commit_profile_changes(
            user_id=user_id,
            pending_change=session_state.pop("pending_profile_change"),
            user_choice=choice
        )
        return StepOutput(content=result, stop=True)

    # ... (rest of the routing and dispatching logic as before) ...
4. Validation Checklist

Onboarding: Is the OnboardingWorkflow resumable using workflow_session_state? Does it use response_model for each step? Does the PreviewConfirm step allow for editing before the final atomic save?

Updater Agent: Does the ProfileUpdaterAgent return strongly-typed ProposedChanges? Does it correctly generate a clarification question when confidence is low (< 0.7) instead of setting pending_profile_change?

Storage: Is the JsonProfileStore performing atomic writes? Is every mutation generating a complete ProfileEvent with an idempotency_key? Are "deletes" implemented as soft deletes (status="inactive")?

Orchestrator: Does the /resolve command correctly short-circuit the router and call the deterministic commit_step function? Does it support chaining intents (e.g., profile then coach)?

Core Utilities: Are shared utilities for normalization (normalize_med_name) and time (user_tz) being used consistently?

Shadow Routing: In dev mode, is the router's prediction logged against the gold standard when a specialist agent is run directly?

Tests: Have unit tests for ProfileStore (idempotency, soft delete) and the onboarding resume path been added?

This comprehensive plan addresses the identified gaps and provides a solid foundation for a production-ready, safe, and maintainable Profile & Onboarding system within the Agno framework.