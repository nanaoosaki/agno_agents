"""
App-wide policies and constants for the health companion application.

This module centralizes configuration values, business rules, and 
policy constants used throughout the application.
"""

from typing import Dict, Any

# === EPISODE LINKING POLICIES ===

# Time window for linking related health events (in hours)
EPISODE_LINKING_WINDOW_HOURS = 12

# Maximum episode duration before auto-closing (in hours)
MAX_EPISODE_DURATION_HOURS = 72

# Minimum severity change to trigger episode update
MIN_SEVERITY_CHANGE_THRESHOLD = 1


# === DATA RETENTION POLICIES ===

# Maximum number of events to keep in memory for processing
MAX_EVENTS_IN_MEMORY = 1000

# Maximum age of events to consider for correlation analysis (in days)
MAX_CORRELATION_ANALYSIS_DAYS = 90


# === VALIDATION POLICIES ===

# Valid severity scale range
MIN_SEVERITY = 1
MAX_SEVERITY = 10

# Maximum length for text fields
MAX_TEXT_FIELD_LENGTH = 1000

# Required fields for episode creation
REQUIRED_EPISODE_FIELDS = ["condition", "started_at", "current_severity"]

# Required fields for observation creation
REQUIRED_OBSERVATION_FIELDS = ["timestamp", "type", "value"]


# === SAFETY AND GUARDRAILS ===

# Keywords that trigger safety warnings in coaching advice
SAFETY_WARNING_KEYWORDS = [
    "emergency", "urgent", "severe", "911", "hospital", "doctor",
    "chest pain", "difficulty breathing", "unconscious", "seizure",
    "suicidal", "self-harm", "overdose", "allergic reaction"
]

# Disclaimer text for health advice
HEALTH_ADVICE_DISCLAIMER = (
    "Warning: This advice is for informational purposes only and should not replace "
    "professional medical consultation. If you have severe symptoms or concerns, "
    "please contact your healthcare provider."
)


# === UI AND INTERACTION POLICIES ===

# Default timezone for new users
DEFAULT_USER_TIMEZONE = "UTC"

# Maximum number of suggestions to show in UI
MAX_UI_SUGGESTIONS = 5

# Session timeout for user interactions (in minutes)
SESSION_TIMEOUT_MINUTES = 60


# === RECALL AGENT POLICIES ===

# Default time window for recall queries when not specified
DEFAULT_RECALL_WINDOW_DAYS = 7

# Maximum number of episodes to return in recall queries
MAX_RECALL_RESULTS = 50

# Correlation analysis window (hours before/after episode)
CORRELATION_WINDOW_HOURS = 24


# === COACH AGENT POLICIES ===

# Maximum length of coaching responses
MAX_COACHING_RESPONSE_LENGTH = 500

# Confidence threshold for knowledge base matches
KNOWLEDGE_MATCH_CONFIDENCE_THRESHOLD = 0.7

# Maximum number of knowledge snippets to include in coaching
MAX_KNOWLEDGE_SNIPPETS = 3


# === FILE STORAGE POLICIES ===

# Data file paths
DATA_FILES = {
    "episodes": "data/episodes.json",
    "observations": "data/observations.json", 
    "interventions": "data/interventions.json",
    "events": "data/events.jsonl",
    "user_profiles": "data/user_profiles.json"
}

# Backup retention policy
BACKUP_RETENTION_DAYS = 30

# Auto-save interval for data files (in seconds)
AUTO_SAVE_INTERVAL_SECONDS = 300


def get_policy_value(policy_name: str, default: Any = None) -> Any:
    """
    Get a policy value by name with optional default.
    
    Args:
        policy_name: The name of the policy constant
        default: Default value if policy not found
        
    Returns:
        Policy value or default
    """
    return globals().get(policy_name, default)


def validate_severity(severity: int) -> bool:
    """
    Validate that a severity value is within acceptable range.
    
    Args:
        severity: The severity value to validate
        
    Returns:
        True if valid, False otherwise
    """
    return MIN_SEVERITY <= severity <= MAX_SEVERITY


def is_safety_sensitive_content(text: str) -> bool:
    """
    Check if text contains safety-sensitive keywords.
    
    Args:
        text: The text to check
        
    Returns:
        True if safety-sensitive content detected
    """
    if not text:
        return False
        
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in SAFETY_WARNING_KEYWORDS)