# healthlogger/storage.py
# Storage layer implemented as Agno tools for Health Logger v3

from __future__ import annotations
import json
import os
import uuid
import hashlib
from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any
from pathlib import Path

try:
    from agno.tools import tool
except ImportError:
    # Fallback for development
    tool = lambda x: x

from .schema import (
    EpisodeData, EpisodeCandidate, ObservationData, InterventionData,
    CONDITION_FAMILIES, BODY_REGION_HINTS
)

# Data directory and files
DATA_DIR = Path("data")
EPISODES_FILE = DATA_DIR / "episodes.json"
OBSERVATIONS_FILE = DATA_DIR / "observations.json"
INTERVENTIONS_FILE = DATA_DIR / "interventions.json"
EVENTS_FILE = DATA_DIR / "events.jsonl"

def _ensure_data_dir():
    """Ensure data directory and files exist"""
    DATA_DIR.mkdir(exist_ok=True)
    
    # Initialize files if they don't exist
    if not EPISODES_FILE.exists():
        EPISODES_FILE.write_text(json.dumps({}, indent=2))
    if not OBSERVATIONS_FILE.exists():
        OBSERVATIONS_FILE.write_text(json.dumps([], indent=2))
    if not INTERVENTIONS_FILE.exists():
        INTERVENTIONS_FILE.write_text(json.dumps([], indent=2))
    if not EVENTS_FILE.exists():
        EVENTS_FILE.touch()

def _load_episodes() -> Dict[str, Dict[str, Any]]:
    """Load episodes from storage"""
    _ensure_data_dir()
    try:
        with open(EPISODES_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def _save_episodes(episodes: Dict[str, Dict[str, Any]]):
    """Save episodes to storage"""
    _ensure_data_dir()
    with open(EPISODES_FILE, 'w') as f:
        json.dump(episodes, f, indent=2, default=str)

@tool
def fetch_open_episode_candidates(window_hours: int = 24) -> List[EpisodeCandidate]:
    """
    Fetch recent open episodes as candidates for linking.
    This tool provides context to the Extractor Agent.
    
    Args:
        window_hours: How far back to look for candidates
        
    Returns:
        List of episode candidates with salient information
    """
    episodes = _load_episodes()
    now = datetime.utcnow()
    candidates = []
    
    for episode_id, ep_data in episodes.items():
        if ep_data.get("status") != "open":
            continue
            
        # Parse last_updated_at
        last_updated_str = ep_data.get("last_updated_at", ep_data.get("started_at"))
        if isinstance(last_updated_str, str):
            try:
                last_updated = datetime.fromisoformat(last_updated_str.replace('Z', '+00:00'))
            except ValueError:
                continue
        else:
            last_updated = last_updated_str
            
        # Check if within time window
        if (now - last_updated).total_seconds() <= window_hours * 3600:
            # Create salient summary
            salient_parts = []
            if ep_data.get("current_severity"):
                salient_parts.append(f"severity {ep_data['current_severity']}")
            if ep_data.get("notes_log"):
                # Get most recent note
                latest_note = ep_data["notes_log"][-1].get("text", "")[:50]
                if latest_note:
                    salient_parts.append(latest_note)
            
            candidate = EpisodeCandidate(
                episode_id=episode_id,
                condition=ep_data["condition"],
                started_at=ep_data["started_at"],
                last_updated_at=last_updated_str,
                current_severity=ep_data.get("current_severity"),
                salient="; ".join(salient_parts) or "recent episode"
            )
            candidates.append(candidate)
    
    # Sort by most recent first
    candidates.sort(key=lambda x: x.last_updated_at, reverse=True)
    return candidates[:5]  # Limit to top 5 candidates

@tool
def normalize_condition(text: str) -> Optional[str]:
    """
    Normalize condition text to canonical form using condition families.
    
    Args:
        text: User's description of condition
        
    Returns:
        Normalized condition name or None
    """
    if not text:
        return None
        
    text_lower = text.lower()
    
    # Direct family matching
    for condition, synonyms in CONDITION_FAMILIES.items():
        if any(synonym in text_lower for synonym in synonyms):
            return condition
    
    # Body region hints
    for condition, hints in BODY_REGION_HINTS.items():
        if any(hint in text_lower for hint in hints):
            return condition
    
    return None

@tool
def create_episode(condition: str, fields: Dict[str, Any], now: Optional[str] = None) -> str:
    """
    Create a new health episode.
    
    Args:
        condition: Normalized condition name
        fields: Health data fields (severity, location, etc.)
        now: Timestamp (optional, defaults to current time)
        
    Returns:
        Episode ID of created episode
    """
    if now is None:
        timestamp = datetime.utcnow()
    else:
        timestamp = datetime.fromisoformat(now) if isinstance(now, str) else now
    
    episodes = _load_episodes()
    
    # Generate episode ID
    date_str = timestamp.date().isoformat()
    episode_id = f"ep_{date_str}_{condition}_{uuid.uuid4().hex[:8]}"
    
    # Create episode data
    episode = {
        "episode_id": episode_id,
        "condition": condition,
        "started_at": timestamp.isoformat(),
        "ended_at": None,
        "status": "open",
        "current_severity": fields.get("severity"),
        "max_severity": fields.get("severity"),
        "severity_points": [{"ts": timestamp.isoformat(), "level": fields["severity"]}] if fields.get("severity") else [],
        "notes_log": [{"ts": timestamp.isoformat(), "text": fields.get("notes")}] if fields.get("notes") else [],
        "interventions": [],
        "last_updated_at": timestamp.isoformat()
    }
    
    episodes[episode_id] = episode
    _save_episodes(episodes)
    
    return episode_id

@tool
def update_episode(episode_id: str, fields: Dict[str, Any], now: Optional[str] = None) -> bool:
    """
    Update an existing episode with new data.
    
    Args:
        episode_id: ID of episode to update
        fields: New health data fields
        now: Timestamp (optional)
        
    Returns:
        True if update successful
    """
    if now is None:
        timestamp = datetime.utcnow()
    else:
        timestamp = datetime.fromisoformat(now) if isinstance(now, str) else now
    
    episodes = _load_episodes()
    
    if episode_id not in episodes:
        return False
    
    episode = episodes[episode_id]
    
    # Update severity if provided
    if fields.get("severity") is not None:
        new_severity = fields["severity"]
        episode["current_severity"] = new_severity
        episode["max_severity"] = max(new_severity, episode.get("max_severity", 0))
        
        # Add severity point
        if "severity_points" not in episode:
            episode["severity_points"] = []
        episode["severity_points"].append({
            "ts": timestamp.isoformat(),
            "level": new_severity
        })
    
    # Add notes if provided
    if fields.get("notes"):
        if "notes_log" not in episode:
            episode["notes_log"] = []
        episode["notes_log"].append({
            "ts": timestamp.isoformat(),
            "text": fields["notes"]
        })
    
    episode["last_updated_at"] = timestamp.isoformat()
    
    episodes[episode_id] = episode
    _save_episodes(episodes)
    
    return True

@tool
def add_intervention(episode_id: str, intervention: Dict[str, Any], now: Optional[str] = None) -> str:
    """
    Add an intervention to an episode.
    
    Args:
        episode_id: Target episode ID
        intervention: Intervention data (type, dose, timing, notes)
        now: Timestamp (optional)
        
    Returns:
        Intervention ID
    """
    if now is None:
        timestamp = datetime.utcnow()
    else:
        timestamp = datetime.fromisoformat(now) if isinstance(now, str) else now
    
    intervention_id = f"int_{uuid.uuid4().hex[:8]}"
    
    # Load interventions file
    try:
        with open(INTERVENTIONS_FILE, 'r') as f:
            interventions = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        interventions = []
    
    # Create intervention record
    intervention_record = {
        "intervention_id": intervention_id,
        "episode_id": episode_id,
        "timestamp": timestamp.isoformat(),
        "type": intervention.get("type"),
        "dose": intervention.get("dose"),
        "timing": intervention.get("timing"),
        "notes": intervention.get("notes")
    }
    
    interventions.append(intervention_record)
    
    # Save interventions
    with open(INTERVENTIONS_FILE, 'w') as f:
        json.dump(interventions, f, indent=2, default=str)
    
    # Also add to episode
    episodes = _load_episodes()
    if episode_id in episodes:
        episode = episodes[episode_id]
        if "interventions" not in episode:
            episode["interventions"] = []
        episode["interventions"].append({
            "ts": timestamp.isoformat(),
            "type": intervention.get("type"),
            "dose": intervention.get("dose"),
            "timing": intervention.get("timing"),
            "notes": intervention.get("notes")
        })
        episode["last_updated_at"] = timestamp.isoformat()
        _save_episodes(episodes)
    
    return intervention_id

@tool
def save_observation(category: str, fields: Dict[str, Any], now: Optional[str] = None) -> str:
    """
    Save a general health observation.
    
    Args:
        category: Observation category (sleep, mood, diet, etc.)
        fields: Observation data
        now: Timestamp (optional)
        
    Returns:
        Observation ID
    """
    if now is None:
        timestamp = datetime.utcnow()
    else:
        timestamp = datetime.fromisoformat(now) if isinstance(now, str) else now
    
    observation_id = f"obs_{uuid.uuid4().hex[:8]}"
    
    # Load observations
    try:
        with open(OBSERVATIONS_FILE, 'r') as f:
            observations = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        observations = []
    
    # Create observation record
    observation_record = {
        "observation_id": observation_id,
        "timestamp": timestamp.isoformat(),
        "category": category,
        "value": fields.get("value"),
        "notes": fields.get("notes")
    }
    
    observations.append(observation_record)
    
    # Save observations
    with open(OBSERVATIONS_FILE, 'w') as f:
        json.dump(observations, f, indent=2, default=str)
    
    return observation_id

@tool
def append_event(user_text: str, parsed_data: Dict[str, Any], action: str, 
                model: Optional[str] = None, confidence: Optional[float] = None,
                episode_id: Optional[str] = None) -> str:
    """
    Append event to audit log for tracking and debugging.
    
    Args:
        user_text: Original user message
        parsed_data: Structured data from extraction
        action: Action taken (create, update, observation, etc.)
        model: Model used for extraction
        confidence: Extraction confidence
        episode_id: Associated episode ID
        
    Returns:
        Event ID
    """
    timestamp = datetime.utcnow()
    event_id = f"evt_{uuid.uuid4().hex[:8]}"
    
    # Create event hash for idempotency
    bucket = timestamp.replace(second=0, microsecond=0).isoformat()
    event_hash = hashlib.sha1((user_text.strip() + bucket).encode()).hexdigest()
    
    event = {
        "event_id": event_id,
        "timestamp": timestamp.isoformat(),
        "user_text": user_text,
        "parsed_data": parsed_data,
        "action": action,
        "model": model,
        "confidence": confidence,
        "episode_id": episode_id,
        "event_hash": event_hash
    }
    
    # Append to JSONL file
    _ensure_data_dir()
    with open(EVENTS_FILE, 'a') as f:
        f.write(json.dumps(event, default=str) + '\n')
    
    return event_id

@tool
def get_episode_by_id(episode_id: str) -> Optional[Dict[str, Any]]:
    """
    Retrieve episode by ID.
    
    Args:
        episode_id: Episode ID to retrieve
        
    Returns:
        Episode data or None if not found
    """
    episodes = _load_episodes()
    return episodes.get(episode_id)