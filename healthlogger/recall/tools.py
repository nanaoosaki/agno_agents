# healthlogger/recall/tools.py
# Recall Agent Tools - Following docs/agno/tools/writing_your_own_tools.md patterns
# Author: Claude (Anthropic AI Assistant)
# Date: January 15, 2025

import json
import os
from agno.tools import tool
from agno.agent import Agent
from .. import storage
from ..schema import TimeRange, EpisodeSummary, CorrelationResult, CorrelationDetail, CONDITION_FAMILIES
from datetime import datetime, timedelta
from typing import List, Optional
import dateparser

# Get the data directory path
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")

def _normalize_condition(condition: str) -> Optional[str]:
    """
    Normalize condition text using existing CONDITION_FAMILIES logic
    Reuses the logic from storage.normalize_condition but as a standalone function
    """
    condition_lower = condition.lower().strip()
    
    for canonical_condition, synonyms in CONDITION_FAMILIES.items():
        if any(synonym in condition_lower for synonym in synonyms):
            return canonical_condition
    
    return None

def _load_episodes() -> dict:
    """Load episodes from JSON file"""
    episodes_file = os.path.join(DATA_DIR, "episodes.json")
    if os.path.exists(episodes_file):
        try:
            with open(episodes_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
    return {}

def _load_observations() -> dict:
    """Load observations from JSON file"""
    observations_file = os.path.join(DATA_DIR, "observations.json")
    if os.path.exists(observations_file):
        try:
            with open(observations_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
    return {}

@tool
def parse_time_range(agent: Agent, query: str, user_timezone: str = "UTC") -> TimeRange:
    """
    Parses a natural language query to identify a time range (e.g., 'last week', 'yesterday', 'since August 1st').
    Returns a structured start and end time in UTC ISO format. This should be the first step in any historical query.
    
    Args:
        agent: The calling agent (automatically provided by Agno)
        query: Natural language query containing time references
        user_timezone: User's timezone (defaults to UTC)
    
    Returns:
        TimeRange: Structured time range with start, end, and label
    """
    now = datetime.utcnow()
    query_lower = query.lower()
    
    # Enhanced date parsing with more patterns
    if "last week" in query_lower or "past week" in query_lower:
        end_date = now
        start_date = now - timedelta(days=7)
        label = "the last 7 days"
    elif "yesterday" in query_lower:
        start_date = now - timedelta(days=1)
        start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = start_date + timedelta(days=1) - timedelta(microseconds=1)
        label = "yesterday"
    elif "last month" in query_lower or "past month" in query_lower:
        end_date = now
        start_date = now - timedelta(days=30)
        label = "the last 30 days"
    elif "last 3 days" in query_lower or "past 3 days" in query_lower:
        end_date = now
        start_date = now - timedelta(days=3)
        label = "the last 3 days"
    elif "today" in query_lower:
        start_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = start_date + timedelta(days=1) - timedelta(microseconds=1)
        label = "today"
    else:
        # Default to last 7 days if no specific range is found
        end_date = now
        start_date = now - timedelta(days=7)
        label = "the last 7 days (default range)"

    return TimeRange(
        start_utc_iso=start_date.isoformat(),
        end_utc_iso=end_date.isoformat(),
        label=label
    )

@tool
def find_episodes_in_range(agent: Agent, condition: str, start_date_iso: str, end_date_iso: str) -> List[EpisodeSummary]:
    """
    Finds episodes for a given condition within a specific UTC date range.
    Always normalize the condition using the shared rules first.
    
    Args:
        agent: The calling agent (automatically provided by Agno)
        condition: Health condition to search for (will be normalized)
        start_date_iso: Start date in ISO format
        end_date_iso: End date in ISO format
    
    Returns:
        List[EpisodeSummary]: Episodes matching the criteria
    """
    # Normalize the condition
    normalized_condition = _normalize_condition(condition)
    if not normalized_condition:
        return []
    
    # Load episodes
    episodes = _load_episodes()
    
    # Parse date range
    try:
        start_dt = datetime.fromisoformat(start_date_iso.replace('Z', '+00:00'))
        end_dt = datetime.fromisoformat(end_date_iso.replace('Z', '+00:00'))
    except ValueError:
        return []
    
    matching_episodes = []
    
    for episode_id, episode_data in episodes.items():
        # Check condition match
        if episode_data.get("condition") != normalized_condition:
            continue
            
        # Check date range
        episode_start = episode_data.get("started_at")
        if not episode_start:
            continue
            
        try:
            episode_dt = datetime.fromisoformat(episode_start.replace('Z', '+00:00'))
            if start_dt <= episode_dt <= end_dt:
                # Extract interventions
                interventions = []
                for intervention in episode_data.get("interventions", []):
                    intervention_type = intervention.get("type", "unknown")
                    interventions.append(intervention_type)
                
                matching_episodes.append(EpisodeSummary(
                    episode_id=episode_id,
                    condition=episode_data.get("condition", "unknown"),
                    started_at=episode_start,
                    max_severity=episode_data.get("peak_severity") or episode_data.get("current_severity"),
                    interventions=interventions
                ))
        except ValueError:
            continue
    
    return matching_episodes

@tool
def correlate_observation_to_episodes(agent: Agent, observation_keyword: str, condition: str, 
                                    start_date_iso: str, end_date_iso: str, 
                                    window_hours: int = 24) -> CorrelationResult:
    """
    Analyzes if a specific observation (e.g., 'tofu') is correlated with a health condition (e.g., 'migraine')
    within a given time range and window.
    
    Args:
        agent: The calling agent (automatically provided by Agno)
        observation_keyword: Keyword to search for in observations
        condition: Health condition to correlate with
        start_date_iso: Start date in ISO format
        end_date_iso: End date in ISO format
        window_hours: Time window in hours to look for correlations (default 24)
    
    Returns:
        CorrelationResult: Analysis of correlations found
    """
    # Normalize the condition
    normalized_condition = _normalize_condition(condition)
    if not normalized_condition:
        return CorrelationResult(
            observation_total=0,
            episodes_with_correlation=0,
            correlation_found=False,
            details=[],
            conclusion=f"Could not normalize condition '{condition}' to a known condition family."
        )
    
    # Load data
    observations = _load_observations()
    episodes = _load_episodes()
    
    # Parse date range
    try:
        start_dt = datetime.fromisoformat(start_date_iso.replace('Z', '+00:00'))
        end_dt = datetime.fromisoformat(end_date_iso.replace('Z', '+00:00'))
    except ValueError:
        return CorrelationResult(
            observation_total=0,
            episodes_with_correlation=0,
            correlation_found=False,
            details=[],
            conclusion="Invalid date format provided."
        )
    
    # Find matching observations in the date range
    matching_observations = []
    keyword_lower = observation_keyword.lower()
    
    for obs_id, obs_data in observations.items():
        obs_timestamp = obs_data.get("timestamp")
        if not obs_timestamp:
            continue
            
        try:
            obs_dt = datetime.fromisoformat(obs_timestamp.replace('Z', '+00:00'))
            if start_dt <= obs_dt <= end_dt:
                # Check if observation contains the keyword
                obs_text = obs_data.get("notes", "").lower()
                obs_category = obs_data.get("category", "").lower()
                
                if keyword_lower in obs_text or keyword_lower in obs_category:
                    matching_observations.append((obs_id, obs_data, obs_dt))
        except ValueError:
            continue
    
    # Find episodes of the specified condition in the date range
    condition_episodes = []
    for episode_id, episode_data in episodes.items():
        if episode_data.get("condition") != normalized_condition:
            continue
            
        episode_start = episode_data.get("started_at")
        if not episode_start:
            continue
            
        try:
            episode_dt = datetime.fromisoformat(episode_start.replace('Z', '+00:00'))
            # Extend search range by window_hours to catch episodes that might have started outside range
            extended_start = start_dt - timedelta(hours=window_hours)
            extended_end = end_dt + timedelta(hours=window_hours)
            
            if extended_start <= episode_dt <= extended_end:
                condition_episodes.append((episode_id, episode_data, episode_dt))
        except ValueError:
            continue
    
    # Find correlations: observations within window_hours of episodes
    correlations = []
    window_delta = timedelta(hours=window_hours)
    
    for obs_id, obs_data, obs_dt in matching_observations:
        for episode_id, episode_data, episode_dt in condition_episodes:
            time_diff = abs((obs_dt - episode_dt).total_seconds() / 3600)  # Convert to hours
            
            if time_diff <= window_hours:
                correlations.append(CorrelationDetail(
                    observation_timestamp=obs_dt.isoformat(),
                    matched_episode_id=episode_id,
                    hours_difference=time_diff
                ))
    
    # Generate conclusion
    total_observations = len(matching_observations)
    episodes_with_correlation = len(set(detail.matched_episode_id for detail in correlations))
    correlation_found = len(correlations) > 0
    
    if total_observations == 0:
        conclusion = f"No observations containing '{observation_keyword}' found in the specified time period."
    elif not correlation_found:
        conclusion = f"Found {total_observations} observation(s) containing '{observation_keyword}', but none were within {window_hours} hours of a {normalized_condition} episode."
    else:
        correlation_rate = episodes_with_correlation / len(condition_episodes) if condition_episodes else 0
        conclusion = f"Found {len(correlations)} correlation(s): {total_observations} observation(s) containing '{observation_keyword}' were within {window_hours} hours of {episodes_with_correlation} different {normalized_condition} episode(s). This suggests a potential correlation (rate: {correlation_rate:.1%})."
    
    return CorrelationResult(
        observation_total=total_observations,
        episodes_with_correlation=episodes_with_correlation,
        correlation_found=correlation_found,
        details=correlations,
        conclusion=conclusion
    )