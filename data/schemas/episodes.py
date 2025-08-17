"""
Pydantic models for episode and health data persistence.

These models define the structure of data stored in the persistence layer.
"""

from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Dict, Any
from datetime import datetime

# Core data types
Intent = Literal["episode_create", "episode_update", "observation", "intervention", "query"]
LinkStrategy = Literal["same_episode", "new_episode", "unknown"]

class Fields(BaseModel):
    """Health data fields extracted from user message"""
    severity: Optional[int] = None  # Severity level 0-10
    location: Optional[str] = None  # Body location  
    triggers: Optional[List[str]] = None  # Potential triggers
    start_time: Optional[str] = None  # When symptoms started
    end_time: Optional[str] = None  # When symptoms ended
    notes: Optional[str] = None  # Additional notes

class EpisodeLink(BaseModel):
    """Episode linking strategy and reasoning"""
    link_strategy: LinkStrategy  # Linking approach
    episode_id: Optional[str] = None  # Target episode ID if updating
    rationale: Optional[str] = None  # Reasoning for linking decision

class InterventionIn(BaseModel):
    """Intervention/treatment taken"""
    type: str  # Type of intervention
    dose: Optional[str] = None  # Dose or quantity
    timing: Optional[str] = None  # When intervention was taken
    notes: Optional[str] = None  # Additional notes

class EpisodeCandidate(BaseModel):
    """Lightweight episode info for context injection"""
    episode_id: str
    condition: str
    started_at: str
    last_updated_at: str
    current_severity: Optional[int] = None
    salient: str  # Brief summary for LLM context

class ProcessingResult(BaseModel):
    """Result from deterministic processing step"""
    action_taken: str  # "create", "update", "observation", "intervention"
    condition: Optional[str] = None
    episode_id: Optional[str] = None
    details: List[str] = Field(default_factory=list)  # List of changes made
    needs_clarification: bool = False
    clarification_options: Optional[List[Dict[str, Any]]] = None

class EpisodeData(BaseModel):
    """Complete episode record"""
    episode_id: str
    condition: str
    started_at: datetime
    ended_at: Optional[datetime] = None
    current_severity: int
    peak_severity: Optional[int] = None
    location: Optional[str] = None
    triggers: Optional[List[str]] = None
    interventions: List[Dict[str, Any]] = Field(default_factory=list)
    notes: Optional[str] = None
    status: Literal["active", "resolved"] = "active"

class ObservationData(BaseModel):
    """Health observation record"""
    observation_id: str
    timestamp: datetime
    type: str  # sleep, mood, activity, etc.
    value: str
    location: Optional[str] = None
    notes: Optional[str] = None

class InterventionData(BaseModel):
    """Intervention/treatment record"""
    intervention_id: str
    episode_id: str
    type: str
    timestamp: datetime
    dosage: Optional[str] = None
    notes: Optional[str] = None

# === RECALL AGENT SCHEMAS ===

class TimeRange(BaseModel):
    """Structured time range for historical queries"""
    start_utc_iso: str  # Start time in UTC ISO format
    end_utc_iso: str   # End time in UTC ISO format  
    label: str         # Human-readable label e.g., "last 7 days", "yesterday"

class EpisodeSummary(BaseModel):
    """Summary of an episode for recall purposes"""
    episode_id: str
    condition: str
    started_at: str
    max_severity: Optional[int] = None
    interventions: List[str] = Field(default_factory=list)

class CorrelationDetail(BaseModel):
    """Detailed correlation information between observation and episode"""
    observation_timestamp: str
    matched_episode_id: str
    hours_difference: float

class CorrelationResult(BaseModel):
    """Result of correlation analysis between observations and episodes"""
    observation_total: int
    episodes_with_correlation: int
    correlation_found: bool
    details: List[CorrelationDetail] = Field(default_factory=list)
    conclusion: str