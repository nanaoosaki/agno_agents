# profile_and_onboarding/__init__.py
"""
Profile and Onboarding System for Health Companion

This module provides user profile management and onboarding workflows
for the Health Companion AI system, following Agno v2.0 patterns.
"""

from .schema import (
    UserProfile,
    ProfileEvent,
    Condition,
    Medication,
    Routine,
    ProfileChangeDetail,
    ProposedProfileChange,
    OnboardConditionsResponse,
    OnboardMedicationsResponse,
    OnboardRoutinesResponse,
    OnboardingPreviewResponse
)

from .storage import (
    ProfileStorageInterface,
    JsonProfileStore,
    get_profile_store
)

from .tools import (
    get_profile_summary,
    save_onboarding_progress,
    get_onboarding_progress,
    finalize_onboarding,
    check_profile_exists,
    update_profile_medication,
    update_profile_condition,
    update_profile_routine,
    deactivate_profile_medication,
    deactivate_profile_condition
)

__all__ = [
    # Schema models
    "UserProfile",
    "ProfileEvent", 
    "Condition",
    "Medication",
    "Routine",
    "ProfileChangeDetail",
    "ProposedProfileChange",
    "OnboardConditionsResponse",
    "OnboardMedicationsResponse", 
    "OnboardRoutinesResponse",
    "OnboardingPreviewResponse",
    
    # Storage interfaces
    "ProfileStorageInterface",
    "JsonProfileStore",
    "get_profile_store",
    
    # Tools
    "get_profile_summary",
    "save_onboarding_progress",
    "get_onboarding_progress", 
    "finalize_onboarding",
    "check_profile_exists",
    "update_profile_medication",
    "update_profile_condition",
    "update_profile_routine",
    "deactivate_profile_medication",
    "deactivate_profile_condition"
]