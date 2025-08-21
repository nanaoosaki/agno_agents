"""
Abstract storage interface for health data management.

This module defines the abstract interface that all storage implementations
must follow, enabling easy migration between storage backends.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any, Union
from datetime import datetime
from enum import Enum

class HealthDataType(Enum):
    """Types of health data that can be stored."""
    EPISODE = "episode"
    OBSERVATION = "observation" 
    INTERVENTION = "intervention"
    USER_PROFILE = "user_profile"
    SESSION_DATA = "session_data"

class HealthDataStorage(ABC):
    """
    Abstract interface for health data storage.
    
    This interface provides a consistent API for storing and retrieving
    health data regardless of the underlying storage backend (JSON, SQL, etc.).
    """
    
    @abstractmethod
    def create_episode(self, episode_data: Dict[str, Any]) -> str:
        """
        Create a new health episode.
        
        Args:
            episode_data: Episode information including condition, severity, etc.
            
        Returns:
            Episode ID
        """
        pass
    
    @abstractmethod
    def update_episode(self, episode_id: str, updates: Dict[str, Any]) -> bool:
        """
        Update an existing episode.
        
        Args:
            episode_id: ID of episode to update
            updates: Dictionary of fields to update
            
        Returns:
            True if update was successful
        """
        pass
    
    @abstractmethod
    def find_episodes(self, 
                     user_id: Optional[str] = None,
                     condition: Optional[str] = None,
                     start_date: Optional[datetime] = None,
                     end_date: Optional[datetime] = None,
                     active_only: bool = False) -> List[Dict[str, Any]]:
        """
        Find episodes matching criteria.
        
        Args:
            user_id: User ID to filter by
            condition: Condition type to filter by  
            start_date: Earliest episode start date
            end_date: Latest episode start date
            active_only: Only return active episodes
            
        Returns:
            List of episode dictionaries
        """
        pass
    
    @abstractmethod
    def get_episode(self, episode_id: str) -> Optional[Dict[str, Any]]:
        """
        Get a specific episode by ID.
        
        Args:
            episode_id: Episode identifier
            
        Returns:
            Episode data or None if not found
        """
        pass
    
    @abstractmethod
    def create_observation(self, observation_data: Dict[str, Any]) -> str:
        """
        Create a new health observation.
        
        Args:
            observation_data: Observation information
            
        Returns:
            Observation ID
        """
        pass
    
    @abstractmethod
    def find_observations(self,
                         user_id: Optional[str] = None,
                         observation_type: Optional[str] = None,
                         start_date: Optional[datetime] = None,
                         end_date: Optional[datetime] = None) -> List[Dict[str, Any]]:
        """
        Find observations matching criteria.
        
        Args:
            user_id: User ID to filter by
            observation_type: Type of observation to filter by
            start_date: Earliest observation date
            end_date: Latest observation date
            
        Returns:
            List of observation dictionaries
        """
        pass
    
    @abstractmethod
    def create_intervention(self, intervention_data: Dict[str, Any]) -> str:
        """
        Create a new health intervention.
        
        Args:
            intervention_data: Intervention information
            
        Returns:
            Intervention ID
        """
        pass
    
    @abstractmethod
    def find_interventions(self,
                          user_id: Optional[str] = None,
                          intervention_type: Optional[str] = None,
                          start_date: Optional[datetime] = None,
                          end_date: Optional[datetime] = None) -> List[Dict[str, Any]]:
        """
        Find interventions matching criteria.
        
        Args:
            user_id: User ID to filter by
            intervention_type: Type of intervention to filter by
            start_date: Earliest intervention date
            end_date: Latest intervention date
            
        Returns:
            List of intervention dictionaries
        """
        pass
    
    @abstractmethod
    def create_user_profile(self, user_id: str, profile_data: Dict[str, Any]) -> bool:
        """
        Create or update a user profile.
        
        Args:
            user_id: User identifier
            profile_data: Profile information
            
        Returns:
            True if successful
        """
        pass
    
    @abstractmethod
    def get_user_profile(self, user_id: str) -> Optional[Dict[str, Any]]:
        """
        Get user profile by ID.
        
        Args:
            user_id: User identifier
            
        Returns:
            Profile data or None if not found
        """
        pass
    
    @abstractmethod
    def update_user_profile(self, user_id: str, updates: Dict[str, Any]) -> bool:
        """
        Update user profile.
        
        Args:
            user_id: User identifier
            updates: Fields to update
            
        Returns:
            True if successful
        """
        pass
    
    @abstractmethod
    def store_session_data(self, session_id: str, data: Dict[str, Any]) -> bool:
        """
        Store session-specific data.
        
        Args:
            session_id: Session identifier
            data: Session data to store
            
        Returns:
            True if successful
        """
        pass
    
    @abstractmethod
    def get_session_data(self, session_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve session data.
        
        Args:
            session_id: Session identifier
            
        Returns:
            Session data or None if not found
        """
        pass
    
    @abstractmethod
    def clear_session_data(self, session_id: str) -> bool:
        """
        Clear session data.
        
        Args:
            session_id: Session identifier
            
        Returns:
            True if successful
        """
        pass
    
    @abstractmethod
    def get_correlation_data(self, 
                           user_id: str,
                           conditions: List[str],
                           start_date: datetime,
                           end_date: datetime) -> Dict[str, Any]:
        """
        Get data for correlation analysis.
        
        Args:
            user_id: User identifier
            conditions: List of conditions to analyze
            start_date: Analysis start date
            end_date: Analysis end date
            
        Returns:
            Correlation analysis data
        """
        pass
    
    @abstractmethod
    def backup_user_data(self, user_id: str) -> Dict[str, Any]:
        """
        Create a backup of all user data.
        
        Args:
            user_id: User identifier
            
        Returns:
            Complete user data backup
        """
        pass
    
    @abstractmethod
    def restore_user_data(self, user_id: str, backup_data: Dict[str, Any]) -> bool:
        """
        Restore user data from backup.
        
        Args:
            user_id: User identifier
            backup_data: Backup data to restore
            
        Returns:
            True if successful
        """
        pass
    
    @abstractmethod
    def health_check(self) -> Dict[str, Any]:
        """
        Perform storage health check.
        
        Returns:
            Health status information
        """
        pass