"""
Profile storage operations with "Propose → Confirm → Commit" pattern.

This module provides safe profile CRUD operations that implement the
confirmation pattern required for healthcare data management.
"""

from typing import Dict, Any, Optional, List
from datetime import datetime
import json
from pathlib import Path

from data.storage_interface import HealthDataStorage
from data.schemas.user_profile import UserProfile, MedicalCondition, Medication, EmergencyContact, ProfileStatus

class ProfileStore:
    """
    Profile storage with confirmation pattern support.
    
    This class implements the "Propose → Confirm → Commit" pattern for
    all profile operations, ensuring users review changes before they
    are permanently stored.
    """
    
    def __init__(self, storage: HealthDataStorage):
        """
        Initialize profile store.
        
        Args:
            storage: Storage backend for persisting profiles
        """
        self.storage = storage
    
    def propose_new_profile(self, user_id: str, profile_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Propose a new user profile for confirmation.
        
        Args:
            user_id: User identifier
            profile_data: Profile information from onboarding
            
        Returns:
            Proposed profile data for user review
        """
        try:
            # Create UserProfile object for validation
            profile = UserProfile(user_id=user_id, **profile_data)
            
            # Return proposed profile data
            return {
                "action": "create_profile",
                "user_id": user_id,
                "profile": profile.to_dict(),
                "summary": profile.get_summary(),
                "confirmation_required": True,
                "message": self._format_profile_confirmation_message(profile)
            }
        
        except Exception as e:
            return {
                "action": "create_profile",
                "user_id": user_id,
                "error": str(e),
                "confirmation_required": False
            }
    
    def confirm_profile_creation(self, user_id: str, proposed_profile: Dict[str, Any]) -> Dict[str, Any]:
        """
        Confirm and commit a proposed profile.
        
        Args:
            user_id: User identifier
            proposed_profile: Previously proposed profile data
            
        Returns:
            Result of profile creation
        """
        try:
            # Extract profile data from proposal
            profile_data = proposed_profile.get("profile", {})
            
            # Create and validate profile
            profile = UserProfile.from_dict(profile_data)
            profile.onboarding_completed = True
            profile.last_updated_at = datetime.now().isoformat()
            
            # Store in backend
            success = self.storage.create_user_profile(user_id, profile.to_dict())
            
            if success:
                return {
                    "success": True,
                    "message": f"Welcome, {profile.name or 'user'}! Your health profile has been created successfully.",
                    "profile_summary": profile.get_summary()
                }
            else:
                return {
                    "success": False,
                    "message": "Failed to save profile. Please try again.",
                    "error": "Storage operation failed"
                }
        
        except Exception as e:
            return {
                "success": False,
                "message": "An error occurred while creating your profile.",
                "error": str(e)
            }
    
    def cancel_profile_creation(self, user_id: str) -> Dict[str, Any]:
        """
        Cancel a proposed profile creation.
        
        Args:
            user_id: User identifier
            
        Returns:
            Cancellation confirmation
        """
        return {
            "success": True,
            "message": "Profile creation cancelled. You can restart the onboarding process anytime.",
            "action": "cancelled"
        }
    
    def get_profile(self, user_id: str) -> Optional[UserProfile]:
        """
        Get existing user profile.
        
        Args:
            user_id: User identifier
            
        Returns:
            UserProfile object or None if not found
        """
        profile_data = self.storage.get_user_profile(user_id)
        if profile_data:
            try:
                return UserProfile.from_dict(profile_data)
            except Exception as e:
                print(f"Error loading profile for {user_id}: {e}")
        return None
    
    def propose_profile_update(self, user_id: str, updates: Dict[str, Any]) -> Dict[str, Any]:
        """
        Propose profile updates for confirmation.
        
        Args:
            user_id: User identifier
            updates: Fields to update
            
        Returns:
            Proposed update data for review
        """
        try:
            current_profile = self.get_profile(user_id)
            if not current_profile:
                return {
                    "error": "Profile not found",
                    "confirmation_required": False
                }
            
            # Create updated profile for validation
            updated_data = current_profile.to_dict()
            updated_data.update(updates)
            updated_profile = UserProfile.from_dict(updated_data)
            
            return {
                "action": "update_profile",
                "user_id": user_id,
                "current_profile": current_profile.get_summary(),
                "proposed_updates": updates,
                "updated_profile": updated_profile.get_summary(),
                "confirmation_required": True,
                "message": self._format_update_confirmation_message(current_profile, updated_profile, updates)
            }
        
        except Exception as e:
            return {
                "action": "update_profile",
                "error": str(e),
                "confirmation_required": False
            }
    
    def confirm_profile_update(self, user_id: str, updates: Dict[str, Any]) -> Dict[str, Any]:
        """
        Confirm and commit profile updates.
        
        Args:
            user_id: User identifier
            updates: Confirmed updates
            
        Returns:
            Result of profile update
        """
        try:
            updates["last_updated_at"] = datetime.now().isoformat()
            success = self.storage.update_user_profile(user_id, updates)
            
            if success:
                updated_profile = self.get_profile(user_id)
                return {
                    "success": True,
                    "message": "Your profile has been updated successfully.",
                    "profile_summary": updated_profile.get_summary() if updated_profile else None
                }
            else:
                return {
                    "success": False,
                    "message": "Failed to update profile. Please try again.",
                    "error": "Storage operation failed"
                }
        
        except Exception as e:
            return {
                "success": False,
                "message": "An error occurred while updating your profile.",
                "error": str(e)
            }
    
    def propose_add_condition(self, user_id: str, condition_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Propose adding a medical condition.
        
        Args:
            user_id: User identifier
            condition_data: Condition information
            
        Returns:
            Proposed condition for confirmation
        """
        try:
            profile = self.get_profile(user_id)
            if not profile:
                return {"error": "Profile not found", "confirmation_required": False}
            
            # Create and validate condition
            condition = MedicalCondition(**condition_data)
            
            # Check for conflicts
            for existing in profile.get_active_conditions():
                if existing.name == condition.name:
                    return {
                        "error": f"You already have an active condition: {existing.display_name}",
                        "confirmation_required": False
                    }
            
            return {
                "action": "add_condition",
                "user_id": user_id,
                "condition": condition.dict(),
                "confirmation_required": True,
                "message": f"Add '{condition.display_name}' to your medical conditions?"
            }
        
        except Exception as e:
            return {
                "action": "add_condition",
                "error": str(e),
                "confirmation_required": False
            }
    
    def confirm_add_condition(self, user_id: str, condition_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Confirm and add a medical condition.
        
        Args:
            user_id: User identifier
            condition_data: Confirmed condition data
            
        Returns:
            Result of adding condition
        """
        try:
            profile = self.get_profile(user_id)
            if not profile:
                return {"success": False, "error": "Profile not found"}
            
            condition = MedicalCondition(**condition_data)
            profile.add_condition(condition)
            
            success = self.storage.update_user_profile(user_id, profile.to_dict())
            
            if success:
                return {
                    "success": True,
                    "message": f"Added '{condition.display_name}' to your medical conditions."
                }
            else:
                return {
                    "success": False,
                    "message": "Failed to add condition. Please try again."
                }
        
        except Exception as e:
            return {
                "success": False,
                "message": "An error occurred while adding the condition.",
                "error": str(e)
            }
    
    def _format_profile_confirmation_message(self, profile: UserProfile) -> str:
        """Format confirmation message for new profile."""
        message_parts = [
            "Please review your health profile:",
            "",
            f"Name: {profile.name or 'Not provided'}",
            f"Conditions: {len(profile.get_active_conditions())} active",
            f"Medications: {len(profile.get_active_medications())} active",
            f"Emergency contacts: {len(profile.emergency_contacts)}",
            "",
            "Would you like to save this profile?"
        ]
        
        return "\n".join(message_parts)
    
    def _format_update_confirmation_message(self, current: UserProfile, updated: UserProfile, changes: Dict[str, Any]) -> str:
        """Format confirmation message for profile updates."""
        message_parts = [
            "Please review the changes to your profile:",
            ""
        ]
        
        # Show specific changes
        for field, new_value in changes.items():
            if field in ["last_updated_at", "schema_version"]:
                continue
            
            old_value = getattr(current, field, "Not set")
            message_parts.append(f"{field.replace('_', ' ').title()}: {old_value} → {new_value}")
        
        message_parts.extend([
            "",
            "Would you like to save these changes?"
        ])
        
        return "\n".join(message_parts)
    
    def backup_profile(self, user_id: str) -> Dict[str, Any]:
        """
        Create a backup of user profile.
        
        Args:
            user_id: User identifier
            
        Returns:
            Profile backup data
        """
        profile = self.get_profile(user_id)
        if profile:
            return {
                "user_id": user_id,
                "backup_timestamp": datetime.now().isoformat(),
                "profile_data": profile.to_dict()
            }
        return {}
    
    def restore_profile(self, user_id: str, backup_data: Dict[str, Any]) -> bool:
        """
        Restore profile from backup.
        
        Args:
            user_id: User identifier
            backup_data: Backup data to restore
            
        Returns:
            True if successful
        """
        try:
            profile_data = backup_data.get("profile_data", {})
            profile = UserProfile.from_dict(profile_data)
            profile.last_updated_at = datetime.now().isoformat()
            
            return self.storage.create_user_profile(user_id, profile.to_dict())
        
        except Exception as e:
            print(f"Error restoring profile for {user_id}: {e}")
            return False