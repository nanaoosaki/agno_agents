"""
Abstract storage interface for health data persistence.

This module defines the contract that all storage backends must implement,
allowing for easy swapping between JSON files, SQLite, PostgreSQL, etc.
"""

from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any
from datetime import datetime


class HealthDataStorage(ABC):
    """
    Abstract base class for health data storage backends.
    
    Defines the standard interface that all storage implementations
    must provide for episodes, observations, and interventions.
    """
    
    # === EPISODE OPERATIONS ===
    
    @abstractmethod
    def create_episode(self, condition: str, started_at: str, current_severity: int, 
                      location: Optional[str] = None, notes: Optional[str] = None) -> str:
        """
        Create a new health episode.
        
        Args:
            condition: The health condition (normalized)
            started_at: ISO timestamp when episode began
            current_severity: Initial severity (1-10)
            location: Optional location information
            notes: Optional additional notes
            
        Returns:
            The generated episode ID
        """
        pass
    
    @abstractmethod
    def get_episode_by_id(self, episode_id: str) -> Optional[Dict[str, Any]]:
        """Get an episode by its ID."""
        pass
    
    @abstractmethod
    def update_episode(self, episode_id: str, **updates) -> bool:
        """Update an existing episode with new data."""
        pass
    
    @abstractmethod
    def find_latest_open_episode(self, condition: str, window_hours: int = 12) -> Optional[Dict[str, Any]]:
        """Find the most recent open episode for a condition within a time window."""
        pass
    
    @abstractmethod
    def fetch_open_episode_candidates(self, window_hours: int = 24) -> List[Dict[str, Any]]:
        """Fetch episodes that might be candidates for linking new data."""
        pass
    
    @abstractmethod
    def close_episode(self, episode_id: str, ended_at: Optional[str] = None) -> bool:
        """Close an episode and mark it as resolved."""
        pass
    
    # === OBSERVATION OPERATIONS ===
    
    @abstractmethod
    def save_observation(self, timestamp: str, observation_type: str, value: str,
                        location: Optional[str] = None, notes: Optional[str] = None) -> str:
        """Save a health observation."""
        pass
    
    @abstractmethod
    def get_observations_in_range(self, start_time: str, end_time: str) -> List[Dict[str, Any]]:
        """Get all observations within a time range."""
        pass
    
    # === INTERVENTION OPERATIONS ===
    
    @abstractmethod
    def add_intervention(self, episode_id: str, intervention_type: str, 
                        dosage: Optional[str] = None, timing: Optional[str] = None,
                        notes: Optional[str] = None) -> bool:
        """Add an intervention to an episode."""
        pass
    
    @abstractmethod
    def get_episode_interventions(self, episode_id: str) -> List[Dict[str, Any]]:
        """Get all interventions for a specific episode."""
        pass
    
    # === EVENT LOG OPERATIONS ===
    
    @abstractmethod
    def append_event(self, event_type: str, data: Dict[str, Any], 
                    episode_id: Optional[str] = None) -> bool:
        """Append an event to the audit log."""
        pass
    
    @abstractmethod
    def get_recent_events(self, limit: int = 100) -> List[Dict[str, Any]]:
        """Get the most recent events from the audit log."""
        pass
    
    # === QUERY OPERATIONS ===
    
    @abstractmethod
    def get_episodes_in_range(self, start_time: str, end_time: str, 
                             condition: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get episodes within a time range, optionally filtered by condition."""
        pass
    
    @abstractmethod
    def search_episodes_by_keyword(self, keyword: str) -> List[Dict[str, Any]]:
        """Search episodes by keyword in notes or other text fields."""
        pass
    
    # === MAINTENANCE OPERATIONS ===
    
    @abstractmethod
    def backup_data(self, backup_path: str) -> bool:
        """Create a backup of all data."""
        pass
    
    @abstractmethod
    def get_storage_stats(self) -> Dict[str, Any]:
        """Get statistics about the stored data."""
        pass