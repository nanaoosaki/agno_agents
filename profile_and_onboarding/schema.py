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

class OnboardRoutinesResponse(BaseModel):
    routines: List[RoutineChange]
    confidence: float = Field(ge=0.0, le=1.0)
    needs_clarification: bool = False
    clarification_question: Optional[str] = None

class OnboardingPreviewResponse(BaseModel):
    action: Literal["confirm", "edit_conditions", "edit_medications", "edit_routines"]
    feedback: Optional[str] = None
    summary: str  # Summary of what will be saved