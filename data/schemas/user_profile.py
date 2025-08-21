"""
User profile schema for health companion system.

This module defines the Pydantic models for user profiles, including
medical conditions, medications, emergency contacts, and structured onboarding models.
"""

from datetime import datetime, date
from typing import List, Optional, Dict, Any, Literal
from pydantic import BaseModel, Field, validator
from enum import Enum

# --- Structured Onboarding Models ---

class OnboardingConditions(BaseModel):
    """Step 1: Health conditions the user wants to manage."""
    conditions: List[str] = Field(default=[], description="A list of health conditions the user wants to manage")
    primary_condition: Optional[str] = Field(default=None, description="The most concerning or primary condition")

class OnboardingGoals(BaseModel):
    """Step 2: User's health management goals."""
    goals: str = Field(default="", description="The user's primary goals for health management")
    specific_targets: List[str] = Field(default=[], description="Specific measurable targets")

class OnboardingSymptoms(BaseModel):
    """Step 3: Symptoms and their patterns."""
    symptoms_description: str = Field(default="", description="Description of symptoms and patterns")
    trigger_patterns: List[str] = Field(default=[], description="Known trigger patterns")

class OnboardingMedications(BaseModel):
    """Step 4: Current medications and treatments."""
    medications_list: str = Field(default="", description="Current medications with details as text")
    allergies: List[str] = Field(default=[], description="Known allergies")
    treatments: List[str] = Field(default=[], description="Non-medication treatments")

class OnboardingRoutines(BaseModel):
    """Step 5: Daily routines and lifestyle factors."""
    routines_description: str = Field(default="", description="Daily health routines description")
    exercise_habits: Optional[str] = Field(default=None, description="Exercise and activity patterns")
    sleep_patterns: Optional[str] = Field(default=None, description="Sleep schedule and quality")

class OnboardingStyle(BaseModel):
    """Step 6: Communication and interaction preferences."""
    communication_style: str = Field(default="supportive", description="Preferred communication style")
    notification_preferences_text: str = Field(default="", description="Notification preferences as text")
    privacy_level: str = Field(default="moderate", description="Privacy comfort level")

class ProfileStatus(str, Enum):
    """Profile status enumeration."""
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"

class MedicalCondition(BaseModel):
    """Medical condition information."""
    name: str = Field(..., description="Condition name (normalized)")
    display_name: str = Field(..., description="Human-readable condition name")
    family: str = Field(..., description="Condition family (e.g., neurological)")
    severity: Optional[int] = Field(None, ge=0, le=10, description="Base severity level")
    diagnosed_date: Optional[date] = Field(None, description="Date of diagnosis")
    status: ProfileStatus = Field(default=ProfileStatus.ACTIVE, description="Condition status")
    notes: Optional[str] = Field(None, description="Additional notes")
    triggers: List[str] = Field(default_factory=list, description="Known triggers")
    
    class Config:
        use_enum_values = True

class Medication(BaseModel):
    """Medication information with enhanced tracking."""
    name: str = Field(..., description="Medication name")
    dosage: Optional[str] = Field(None, description="Dosage information")
    frequency: Optional[str] = Field(None, description="Frequency of administration")
    schedule: Optional[str] = Field(None, description="Specific timing schedule")
    condition: Optional[str] = Field(None, description="Associated condition")
    prescribing_doctor: Optional[str] = Field(None, description="Prescribing physician")
    start_date: Optional[date] = Field(None, description="Start date")
    end_date: Optional[date] = Field(None, description="End date (if applicable)")
    status: ProfileStatus = Field(default=ProfileStatus.ACTIVE, description="Medication status")
    source: Literal["user_entered", "inferred", "imported"] = Field(default="user_entered", description="Data source")
    notes: Optional[str] = Field(None, description="Additional notes")
    
    class Config:
        use_enum_values = True

class EmergencyContact(BaseModel):
    """Emergency contact information."""
    name: str = Field(..., description="Contact name")
    relationship: str = Field(..., description="Relationship to user")
    phone: str = Field(..., description="Primary phone number")
    email: Optional[str] = Field(None, description="Email address")
    is_primary: bool = Field(default=False, description="Is primary emergency contact")
    notes: Optional[str] = Field(None, description="Additional notes")

class UserProfile(BaseModel):
    """
    Complete user profile for health companion with enhanced structure.
    
    This schema represents the structured user profile created through
    the onboarding process and maintained throughout the user's journey.
    Follows the v3.3 specification for robust, auditable health data management.
    """
    # Core Identity
    user_id: str = Field(..., description="Unique user identifier")
    schema_version: int = Field(default=2, description="Profile schema version")
    
    # Basic Information
    name: Optional[str] = Field(None, description="User's name")
    date_of_birth: Optional[date] = Field(None, description="Date of birth")
    gender: Optional[str] = Field(None, description="Gender identity")
    user_timezone: str = Field(default="UTC", description="User's timezone")
    
    # Core Health Profile Data (from structured onboarding)
    conditions: List[Dict[str, str]] = Field(
        default_factory=list, 
        description="Health conditions with status (e.g., {'name': 'migraine', 'status': 'active'})"
    )
    goals: str = Field(default="", description="Primary health management goals")
    symptoms: Dict[str, List[str]] = Field(
        default_factory=dict,
        description="Symptoms organized by condition"
    )
    medications: List[Medication] = Field(
        default_factory=list,
        description="List of current medications with detailed tracking"
    )
    daily_routines: List[Dict[str, str]] = Field(
        default_factory=list,
        description="Daily health routines and habits"
    )
    communication_style: str = Field(default="supportive", description="Preferred communication style")
    
    # Legacy fields for backward compatibility
    allergies: List[str] = Field(
        default_factory=list,
        description="Known allergies"
    )
    
    # Healthcare Information
    primary_doctor: Optional[str] = Field(None, description="Primary care physician")
    pharmacy: Optional[str] = Field(None, description="Preferred pharmacy")
    insurance: Optional[str] = Field(None, description="Insurance information")
    emergency_contacts: List[EmergencyContact] = Field(
        default_factory=list,
        description="Emergency contacts"
    )
    
    # Preferences and Settings
    timezone: str = Field(default="UTC", description="User's timezone")
    notification_preferences: Dict[str, bool] = Field(
        default_factory=lambda: {
            "medication_reminders": True,
            "appointment_reminders": True,
            "health_insights": True,
            "emergency_alerts": True
        },
        description="Notification preferences"
    )
    privacy_settings: Dict[str, Any] = Field(
        default_factory=lambda: {
            "data_sharing": False,
            "analytics": True,
            "research_participation": False
        },
        description="Privacy settings"
    )
    
    # Audit and Metadata (following v3.3 specification)
    status: ProfileStatus = Field(default=ProfileStatus.ACTIVE, description="Profile status")
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat(), description="Profile creation time")
    last_updated_at: str = Field(default_factory=lambda: datetime.now().isoformat(), description="Last update time")
    last_updated_by: Literal["user", "system", "agent"] = Field(default="user", description="Who made the last update")
    last_login: Optional[datetime] = Field(None, description="Last login time")
    
    # Onboarding Progress
    onboarding_completed: bool = Field(default=False, description="Onboarding completion status")
    onboarding_step: int = Field(default=0, description="Current onboarding step")
    onboarding_data: Dict[str, Any] = Field(
        default_factory=dict,
        description="Temporary onboarding data"
    )
    
    class Config:
        use_enum_values = True
        json_encoders = {
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat()
        }
    
    @validator('date_of_birth')
    def validate_birth_date(cls, v):
        """Validate that birth date is not in the future."""
        if v and v > date.today():
            raise ValueError("Birth date cannot be in the future")
        return v
    
    @validator('emergency_contacts')
    def validate_emergency_contacts(cls, v):
        """Ensure only one primary emergency contact."""
        primary_count = sum(1 for contact in v if contact.is_primary)
        if primary_count > 1:
            raise ValueError("Only one emergency contact can be marked as primary")
        return v
    
    @validator('conditions')
    def validate_conditions(cls, v):
        """Validate condition names are unique."""
        if not v:
            return v
        active_names = []
        for condition in v:
            if isinstance(condition, dict):
                if condition.get("status", "active") == "active":
                    active_names.append(condition.get("name", ""))
        if len(active_names) != len(set(active_names)):
            raise ValueError("Active condition names must be unique")
        return v
    
    @validator('medications')
    def validate_medications(cls, v):
        """Validate active medications."""
        if not v:
            return v
        # Medication validation logic can be added here if needed
        return v
    
    def add_condition(self, condition_name: str, display_name: str = None, status: str = "active") -> None:
        """Add a new medical condition."""
        # Check for existing condition
        for existing in self.conditions:
            if isinstance(existing, dict) and existing.get("name") == condition_name and existing.get("status") == "active":
                raise ValueError(f"Active condition '{condition_name}' already exists")
        
        self.conditions.append({
            "name": condition_name,
            "display_name": display_name or condition_name,
            "status": status
        })
        self.last_updated_at = datetime.now().isoformat()
    
    def deactivate_condition(self, condition_name: str) -> bool:
        """Deactivate a medical condition."""
        for condition in self.conditions:
            if isinstance(condition, dict) and condition.get("name") == condition_name and condition.get("status") == "active":
                condition["status"] = "inactive"
                self.last_updated_at = datetime.now().isoformat()
                return True
        return False
    
    def add_medication(self, medication: Medication) -> None:
        """Add a new medication."""
        self.medications.append(medication)
        self.last_updated_at = datetime.now().isoformat()
    
    def deactivate_medication(self, medication_name: str) -> bool:
        """Deactivate a medication."""
        for medication in self.medications:
            if medication.name == medication_name and medication.status == ProfileStatus.ACTIVE:
                medication.status = ProfileStatus.INACTIVE
                medication.end_date = date.today()
                self.last_updated_at = datetime.now().isoformat()
                return True
        return False
    
    def add_emergency_contact(self, contact: EmergencyContact) -> None:
        """Add an emergency contact."""
        # If this is marked as primary, unmark others
        if contact.is_primary:
            for existing in self.emergency_contacts:
                existing.is_primary = False
        
        self.emergency_contacts.append(contact)
        self.last_updated_at = datetime.now().isoformat()
    
    def get_active_conditions(self) -> List[Dict[str, str]]:
        """Get all active medical conditions."""
        return [condition for condition in self.conditions 
                if isinstance(condition, dict) and condition.get("status") == "active"]
    
    def get_active_medications(self) -> List[Medication]:
        """Get all active medications."""
        return [medication for medication in self.medications 
                if medication.status == ProfileStatus.ACTIVE]
    
    def get_primary_emergency_contact(self) -> Optional[EmergencyContact]:
        """Get the primary emergency contact."""
        for contact in self.emergency_contacts:
            if contact.is_primary:
                return contact
        return None
    
    def update_onboarding_progress(self, step: int, data: Dict[str, Any] = None) -> None:
        """Update onboarding progress."""
        self.onboarding_step = step
        if data:
            self.onboarding_data.update(data)
        
        # Mark as completed if we've reached the final step
        if step >= 6:  # Assuming 6-step onboarding
            self.onboarding_completed = True
            self.onboarding_data = {}  # Clear temporary data
        
        self.last_updated_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert profile to dictionary for storage."""
        return self.dict(by_alias=True)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "UserProfile":
        """Create profile from dictionary."""
        return cls(**data)
    
    def get_summary(self) -> Dict[str, Any]:
        """Get a summary of the user profile for display."""
        active_conditions = self.get_active_conditions()
        active_medications = self.get_active_medications()
        primary_contact = self.get_primary_emergency_contact()
        
        return {
            "user_id": self.user_id,
            "name": self.name,
            "conditions_count": len(active_conditions),
            "medications_count": len(active_medications),
            "has_emergency_contact": primary_contact is not None,
            "onboarding_completed": self.onboarding_completed,
            "last_updated": self.last_updated_at
        }