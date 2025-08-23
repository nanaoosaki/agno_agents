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
    def deactivate_condition(self, user_id: str, condition_name: str, source: str) -> None:
        """Soft delete condition with audit trail"""
        pass
    
    @abstractmethod
    def add_or_update_routine(self, user_id: str, routine: Routine, source: str) -> None:
        """Add or update routine with audit trail"""
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
            
            # Handle Windows file replacement
            if self.profile_file.exists():
                self.profile_file.unlink()
            temp_file.rename(self.profile_file)
        except Exception as e:
            if temp_file.exists():
                try:
                    temp_file.unlink()
                except:
                    pass
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
    
    def add_or_update_medication(self, user_id: str, medication: Medication, source: str) -> None:
        """Add or update medication with audit trail"""
        profile = self.get_profile(user_id)
        if not profile:
            profile = UserProfile(user_id=user_id)
        
        # Find existing medication by name
        existing_med = None
        for i, med in enumerate(profile.medications):
            if med.name.lower() == medication.name.lower() and med.status == "active":
                existing_med = i
                break
        
        medication_dict = medication.model_dump()
        idempotency_key = self._generate_idempotency_key(user_id, "medication", medication_dict)
        
        if existing_med is not None:
            # Update existing
            before_state = profile.medications[existing_med].model_dump()
            profile.medications[existing_med] = medication
            action = "update"
        else:
            # Add new
            before_state = None
            profile.medications.append(medication)
            action = "add"
        
        # Save profile
        self.save_profile(profile, source)
        
        # Create medication-specific event
        event = ProfileEvent(
            user_id=user_id,
            kind=action,
            entity="medication",
            before=before_state,
            after=medication_dict,
            source=source,
            idempotency_key=idempotency_key
        )
        self.append_event(event)
    
    def deactivate_medication(self, user_id: str, med_name: str, source: str) -> None:
        """Soft delete medication with audit trail"""
        profile = self.get_profile(user_id)
        if not profile:
            return
        
        # Find and deactivate medication
        for medication in profile.medications:
            if medication.name.lower() == med_name.lower() and medication.status == "active":
                before_state = medication.model_dump()
                medication.status = "inactive"
                medication.stopped_at = datetime.now(timezone.utc)
                
                # Save profile
                self.save_profile(profile, source)
                
                # Create deactivation event
                event = ProfileEvent(
                    user_id=user_id,
                    kind="deactivate",
                    entity="medication",
                    before=before_state,
                    after=medication.model_dump(),
                    source=source,
                    idempotency_key=self._generate_idempotency_key(
                        user_id, "medication_deactivate", {"name": med_name}
                    )
                )
                self.append_event(event)
                break
    
    def add_or_update_condition(self, user_id: str, condition: Condition, source: str) -> None:
        """Add or update condition with audit trail"""
        profile = self.get_profile(user_id)
        if not profile:
            profile = UserProfile(user_id=user_id)
        
        # Find existing condition by name
        existing_condition = None
        for i, cond in enumerate(profile.conditions):
            if cond.name.lower() == condition.name.lower() and cond.status == "active":
                existing_condition = i
                break
        
        condition_dict = condition.model_dump()
        idempotency_key = self._generate_idempotency_key(user_id, "condition", condition_dict)
        
        if existing_condition is not None:
            # Update existing
            before_state = profile.conditions[existing_condition].model_dump()
            profile.conditions[existing_condition] = condition
            action = "update"
        else:
            # Add new
            before_state = None
            profile.conditions.append(condition)
            action = "add"
        
        # Save profile
        self.save_profile(profile, source)
        
        # Create condition-specific event
        event = ProfileEvent(
            user_id=user_id,
            kind=action,
            entity="condition",
            before=before_state,
            after=condition_dict,
            source=source,
            idempotency_key=idempotency_key
        )
        self.append_event(event)
    
    def deactivate_condition(self, user_id: str, condition_name: str, source: str) -> None:
        """Soft delete condition with audit trail"""
        profile = self.get_profile(user_id)
        if not profile:
            return
        
        # Find and deactivate condition
        for condition in profile.conditions:
            if condition.name.lower() == condition_name.lower() and condition.status == "active":
                before_state = condition.model_dump()
                condition.status = "inactive"
                condition.ended_at = datetime.now(timezone.utc)
                
                # Save profile
                self.save_profile(profile, source)
                
                # Create deactivation event
                event = ProfileEvent(
                    user_id=user_id,
                    kind="deactivate",
                    entity="condition",
                    before=before_state,
                    after=condition.model_dump(),
                    source=source,
                    idempotency_key=self._generate_idempotency_key(
                        user_id, "condition_deactivate", {"name": condition_name}
                    )
                )
                self.append_event(event)
                break
    
    def add_or_update_routine(self, user_id: str, routine: Routine, source: str) -> None:
        """Add or update routine with audit trail"""
        profile = self.get_profile(user_id)
        if not profile:
            profile = UserProfile(user_id=user_id)
        
        # Find existing routine by category
        existing_routine = None
        for i, rout in enumerate(profile.routines):
            if rout.category == routine.category:
                existing_routine = i
                break
        
        routine_dict = routine.model_dump()
        idempotency_key = self._generate_idempotency_key(user_id, "routine", routine_dict)
        
        if existing_routine is not None:
            # Update existing
            before_state = profile.routines[existing_routine].model_dump()
            profile.routines[existing_routine] = routine
            action = "update"
        else:
            # Add new
            before_state = None
            profile.routines.append(routine)
            action = "add"
        
        # Save profile
        self.save_profile(profile, source)
        
        # Create routine-specific event
        event = ProfileEvent(
            user_id=user_id,
            kind=action,
            entity="routine",
            before=before_state,
            after=routine_dict,
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