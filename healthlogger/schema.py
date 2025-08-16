# healthlogger/schema.py
# Pydantic schemas for Health Logger v3 - Pure Agno Implementation

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

# Flattened schema for OpenAI compatibility (no nested models, no Field descriptions)
class SimpleRouterOutput(BaseModel):
    """Flattened schema for OpenAI structured output - avoids $ref description errors"""
    intent: Intent
    condition: Optional[str] = None
    severity: Optional[int] = None
    location: Optional[str] = None
    triggers: Optional[List[str]] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    notes: Optional[str] = None
    link_strategy: LinkStrategy
    episode_id: Optional[str] = None
    rationale: Optional[str] = None
    intervention_types: Optional[List[str]] = None
    intervention_doses: Optional[List[Optional[str]]] = None
    intervention_timings: Optional[List[Optional[str]]] = None
    intervention_notes: Optional[List[Optional[str]]] = None
    confidence: float = 0.0

class RouterOutput(BaseModel):
    """Full structured output with nested models - for internal use after LLM call"""
    intent: Intent
    condition: Optional[str] = None
    fields: Fields
    episode_link: EpisodeLink
    interventions: List[InterventionIn] = Field(default_factory=list)
    confidence: float = 0.0
    
    @classmethod
    def from_simple(cls, simple: SimpleRouterOutput) -> "RouterOutput":
        """Convert flattened SimpleRouterOutput to full RouterOutput structure"""
        
        # Build fields
        fields = Fields(
            severity=simple.severity,
            location=simple.location,
            triggers=simple.triggers,
            start_time=simple.start_time,
            end_time=simple.end_time,
            notes=simple.notes
        )
        
        # Build episode link
        episode_link = EpisodeLink(
            link_strategy=simple.link_strategy,
            episode_id=simple.episode_id,
            rationale=simple.rationale
        )
        
        # Build interventions
        interventions = []
        if simple.intervention_types:
            for i, int_type in enumerate(simple.intervention_types):
                intervention = InterventionIn(
                    type=int_type,
                    dose=simple.intervention_doses[i] if simple.intervention_doses and i < len(simple.intervention_doses) else None,
                    timing=simple.intervention_timings[i] if simple.intervention_timings and i < len(simple.intervention_timings) else None,
                    notes=simple.intervention_notes[i] if simple.intervention_notes and i < len(simple.intervention_notes) else None
                )
                interventions.append(intervention)
        
        return cls(
            intent=simple.intent,
            condition=simple.condition,
            fields=fields,
            episode_link=episode_link,
            interventions=interventions,
            confidence=simple.confidence
        )

# Storage schemas
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
    status: Literal["open", "closed"] = "open"
    current_severity: Optional[int] = None
    max_severity: Optional[int] = None
    severity_points: List[Dict[str, Any]] = Field(default_factory=list)
    notes_log: List[Dict[str, Any]] = Field(default_factory=list)
    interventions: List[Dict[str, Any]] = Field(default_factory=list)
    last_updated_at: datetime

class ObservationData(BaseModel):
    """Observation record"""
    observation_id: str
    timestamp: datetime
    category: str
    value: Optional[str] = None
    notes: Optional[str] = None

class InterventionData(BaseModel):
    """Intervention record"""
    intervention_id: str
    episode_id: Optional[str] = None
    timestamp: datetime
    type: str
    dose: Optional[str] = None
    timing: Optional[str] = None
    notes: Optional[str] = None

# Condition families for semantic matching
CONDITION_FAMILIES = {
    "migraine": ["migraine", "headache", "head pain", "temple pain", "behind eye", "neck-related head pain"],
    "sleep": ["sleep", "insomnia", "sleep quality", "nap", "tired", "fatigue"],
    "reflux": ["reflux", "heartburn", "gerd", "acid", "indigestion"],
    "asthma": ["asthma", "wheeze", "wheezing", "shortness of breath"],
    "anxiety": ["anxiety", "anxious", "panic", "worry", "stress"],
    "depression": ["depression", "depressed", "sad", "down", "low mood"],
    "back_pain": ["back pain", "backache", "lower back", "spine pain"],
    "neck_pain": ["neck pain", "neck ache", "stiff neck"],
    "pain": ["pain", "ache", "hurt", "sore"]  # Generic pain family
}

BODY_REGION_HINTS = {
    "migraine": ["temple", "behind eye", "photophobia", "nausea", "throbbing", "neck", "head"],
    "reflux": ["burning chest", "acid", "sour taste", "chest"],
    "asthma": ["wheeze", "short of breath", "tight chest", "chest"],
    "back_pain": ["lower back", "spine", "back"],
    "neck_pain": ["neck", "cervical", "stiff neck"]
}

# === RECALL AGENT SCHEMAS ===
# Following docs/agno/tools/writing_your_own_tools.md patterns

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