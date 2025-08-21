"""
JSON-based storage implementation for health data.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Any
from pathlib import Path
import uuid

from .storage_interface import HealthDataStorage

class JsonStore(HealthDataStorage):
    """Simple JSON file-based storage implementation."""
    
    def __init__(self, base_path: str = "data"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(exist_ok=True)
        
        self.episodes_file = self.base_path / "episodes.json"
        self.observations_file = self.base_path / "observations.json"
        self.interventions_file = self.base_path / "interventions.json"
        self.profiles_file = self.base_path / "user_profiles.json"
        self.sessions_file = self.base_path / "session_data.json"
        
        self._initialize_files()
    
    def _initialize_files(self):
        """Initialize empty data files."""
        for file_path in [self.episodes_file, self.observations_file, self.interventions_file]:
            if not file_path.exists():
                with open(file_path, 'w') as f:
                    json.dump([], f)
        
        for file_path in [self.profiles_file, self.sessions_file]:
            if not file_path.exists():
                with open(file_path, 'w') as f:
                    json.dump({}, f)
    
    def _load_data(self, file_path: Path):
        """Load data from JSON file."""
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return [] if "profiles" not in file_path.name else {}
    
    def _save_data(self, file_path: Path, data):
        """Save data to JSON file."""
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2, default=str)
    
    # Episode methods
    def create_episode(self, episode_data: Dict[str, Any]) -> str:
        episodes = self._load_data(self.episodes_file)
        episode_id = str(uuid.uuid4())
        episode = {"id": episode_id, "created_at": datetime.now().isoformat(), **episode_data}
        episodes.append(episode)
        self._save_data(self.episodes_file, episodes)
        return episode_id
    
    def update_episode(self, episode_id: str, updates: Dict[str, Any]) -> bool:
        episodes = self._load_data(self.episodes_file)
        for episode in episodes:
            if episode["id"] == episode_id:
                episode.update(updates)
                self._save_data(self.episodes_file, episodes)
                return True
        return False
    
    def find_episodes(self, user_id=None, condition=None, start_date=None, end_date=None, active_only=False):
        episodes = self._load_data(self.episodes_file)
        return [ep for ep in episodes if not user_id or ep.get("user_id") == user_id]
    
    def get_episode(self, episode_id: str) -> Optional[Dict[str, Any]]:
        episodes = self._load_data(self.episodes_file)
        for episode in episodes:
            if episode["id"] == episode_id:
                return episode
        return None
    
    # Observation methods
    def create_observation(self, observation_data: Dict[str, Any]) -> str:
        observations = self._load_data(self.observations_file)
        obs_id = str(uuid.uuid4())
        observation = {"id": obs_id, "created_at": datetime.now().isoformat(), **observation_data}
        observations.append(observation)
        self._save_data(self.observations_file, observations)
        return obs_id
    
    def find_observations(self, user_id=None, observation_type=None, start_date=None, end_date=None):
        observations = self._load_data(self.observations_file)
        return [obs for obs in observations if not user_id or obs.get("user_id") == user_id]
    
    # Intervention methods
    def create_intervention(self, intervention_data: Dict[str, Any]) -> str:
        interventions = self._load_data(self.interventions_file)
        int_id = str(uuid.uuid4())
        intervention = {"id": int_id, "created_at": datetime.now().isoformat(), **intervention_data}
        interventions.append(intervention)
        self._save_data(self.interventions_file, interventions)
        return int_id
    
    def find_interventions(self, user_id=None, intervention_type=None, start_date=None, end_date=None):
        interventions = self._load_data(self.interventions_file)
        return [inter for inter in interventions if not user_id or inter.get("user_id") == user_id]
    
    # User profile methods
    def create_user_profile(self, user_id: str, profile_data: Dict[str, Any]) -> bool:
        profiles = self._load_data(self.profiles_file)
        profiles[user_id] = {"user_id": user_id, "created_at": datetime.now().isoformat(), **profile_data}
        self._save_data(self.profiles_file, profiles)
        return True
    
    def get_user_profile(self, user_id: str) -> Optional[Dict[str, Any]]:
        profiles = self._load_data(self.profiles_file)
        return profiles.get(user_id)
    
    def update_user_profile(self, user_id: str, updates: Dict[str, Any]) -> bool:
        profiles = self._load_data(self.profiles_file)
        if user_id not in profiles:
            return False
        profiles[user_id].update(updates)
        self._save_data(self.profiles_file, profiles)
        return True
    
    # Session methods
    def store_session_data(self, session_id: str, data: Dict[str, Any]) -> bool:
        sessions = self._load_data(self.sessions_file)
        sessions[session_id] = {"session_id": session_id, "data": data}
        self._save_data(self.sessions_file, sessions)
        return True
    
    def get_session_data(self, session_id: str) -> Optional[Dict[str, Any]]:
        sessions = self._load_data(self.sessions_file)
        session = sessions.get(session_id)
        return session.get("data") if session else None
    
    def clear_session_data(self, session_id: str) -> bool:
        sessions = self._load_data(self.sessions_file)
        if session_id in sessions:
            del sessions[session_id]
            self._save_data(self.sessions_file, sessions)
            return True
        return False
    
    # Analysis methods
    def get_correlation_data(self, user_id: str, conditions: List[str], start_date: datetime, end_date: datetime):
        return {"episodes": [], "observations": [], "interventions": []}
    
    def backup_user_data(self, user_id: str) -> Dict[str, Any]:
        return {"user_id": user_id, "timestamp": datetime.now().isoformat()}
    
    def restore_user_data(self, user_id: str, backup_data: Dict[str, Any]) -> bool:
        return True
    
    def health_check(self) -> Dict[str, Any]:
        return {"status": "ok", "timestamp": datetime.now().isoformat()}
    
    def fetch_open_episode_candidates(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Fetch open episodes for coaching context."""
        try:
            episodes = self._load_data(self.episodes_file)
            open_episodes = [
                ep for ep in episodes 
                if ep.get("status") == "active"
            ]
            # Sort by created_at descending and limit
            open_episodes.sort(key=lambda x: x.get("created_at", ""), reverse=True)
            return open_episodes[:limit]
        except Exception as e:
            print(f"Error fetching open episodes: {e}")
            return []