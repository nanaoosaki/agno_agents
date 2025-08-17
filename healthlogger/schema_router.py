"""
Router-specific schemas for the Health Logger workflow.

These schemas are used specifically for LLM extraction and routing,
separate from the persistence layer schemas.
"""

from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Dict, Any
from data.schemas.episodes import Intent, LinkStrategy, Fields, EpisodeLink, InterventionIn

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
    confidence: Optional[float] = None

class RouterOutput(BaseModel):
    """Complete router output with nested models for internal processing"""
    intent: Intent
    condition: Optional[str] = None
    fields: Fields
    episode_link: EpisodeLink
    interventions: List[InterventionIn] = Field(default_factory=list)
    confidence: Optional[float] = None
    
    @classmethod
    def from_simple(cls, simple: SimpleRouterOutput) -> 'RouterOutput':
        """Convert SimpleRouterOutput to full RouterOutput structure"""
        
        # Build fields object
        fields = Fields(
            severity=simple.severity,
            location=simple.location,
            triggers=simple.triggers,
            start_time=simple.start_time,
            end_time=simple.end_time,
            notes=simple.notes
        )
        
        # Build episode link object
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