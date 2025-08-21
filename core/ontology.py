"""
Health condition ontology and normalization utilities.

This module provides centralized health condition mapping and normalization
to ensure consistent data representation across the health companion system.
"""

from typing import Set, Optional, Dict, List
import re

# Will be populated after CONDITION_MAP is defined
CONDITION_FAMILIES = {}


# Core condition families and their aliases
CONDITION_MAP = {
    "migraine": {
        "aliases": ["migraine", "migraines", "headache", "head pain", "cephalgia"],
        "family": "neurological",
        "severity_scale": "1-10",
        "typical_triggers": ["stress", "food", "weather", "sleep", "hormones"]
    },
    "back_pain": {
        "aliases": ["back pain", "backache", "lower back", "upper back", "spinal pain"],
        "family": "musculoskeletal", 
        "severity_scale": "1-10",
        "typical_triggers": ["posture", "lifting", "sitting", "exercise", "stress"]
    },
    "joint_pain": {
        "aliases": ["joint pain", "arthritis", "knee pain", "shoulder pain", "hip pain"],
        "family": "musculoskeletal",
        "severity_scale": "1-10", 
        "typical_triggers": ["weather", "activity", "inflammation", "overuse"]
    },
    "fatigue": {
        "aliases": ["fatigue", "tired", "exhausted", "energy", "weakness"],
        "family": "general",
        "severity_scale": "1-10",
        "typical_triggers": ["sleep", "stress", "diet", "activity", "illness"]
    },
    "anxiety": {
        "aliases": ["anxiety", "anxious", "worry", "stress", "panic"],
        "family": "mental_health",
        "severity_scale": "1-10",
        "typical_triggers": ["stress", "caffeine", "social", "work", "health"]
    },
    "depression": {
        "aliases": ["depression", "depressed", "sad", "mood", "low"],
        "family": "mental_health", 
        "severity_scale": "1-10",
        "typical_triggers": ["stress", "isolation", "sleep", "seasonal", "health"]
    },
    "insomnia": {
        "aliases": ["insomnia", "sleep", "sleepless", "awake", "sleep problems"],
        "family": "sleep",
        "severity_scale": "hours_affected",
        "typical_triggers": ["stress", "caffeine", "screens", "schedule", "pain"]
    },
    "nausea": {
        "aliases": ["nausea", "nauseous", "sick", "queasy", "stomach"],
        "family": "gastrointestinal",
        "severity_scale": "1-10",
        "typical_triggers": ["food", "medication", "motion", "stress", "hormones"]
    }
}

# Build reverse lookup for fast normalization
_ALIAS_TO_CONDITION = {}
for condition, data in CONDITION_MAP.items():
    for alias in data["aliases"]:
        _ALIAS_TO_CONDITION[alias.lower()] = condition

def normalize_condition(user_input: str) -> Optional[str]:
    """
    Normalize user input to a standard condition name.
    
    Args:
        user_input: Raw user input describing a condition
        
    Returns:
        Normalized condition name or None if not recognized
        
    Examples:
        >>> normalize_condition("my head hurts")
        'migraine'
        >>> normalize_condition("back ache")
        'back_pain' 
        >>> normalize_condition("feeling anxious")
        'anxiety'
    """
    if not user_input:
        return None
        
    # Clean and lowercase input
    clean_input = re.sub(r'[^\w\s]', '', user_input.lower())
    
    # Direct alias match
    if clean_input in _ALIAS_TO_CONDITION:
        return _ALIAS_TO_CONDITION[clean_input]
    
    # Partial matching for phrases
    for alias, condition in _ALIAS_TO_CONDITION.items():
        if alias in clean_input or clean_input in alias:
            return condition
    
    # Word-based matching
    words = clean_input.split()
    for word in words:
        if word in _ALIAS_TO_CONDITION:
            return _ALIAS_TO_CONDITION[word]
    
    return None

def get_condition_family(condition: str) -> Optional[str]:
    """
    Get the condition family for a normalized condition.
    
    Args:
        condition: Normalized condition name
        
    Returns:
        Condition family or None if condition not found
        
    Examples:
        >>> get_condition_family("migraine")
        'neurological'
        >>> get_condition_family("anxiety") 
        'mental_health'
    """
    if condition in CONDITION_MAP:
        return CONDITION_MAP[condition]["family"]
    return None

def get_condition_triggers(condition: str) -> List[str]:
    """
    Get typical triggers for a condition.
    
    Args:
        condition: Normalized condition name
        
    Returns:
        List of typical triggers for the condition
    """
    if condition in CONDITION_MAP:
        return CONDITION_MAP[condition]["typical_triggers"]
    return []

def get_severity_scale(condition: str) -> str:
    """
    Get the appropriate severity scale for a condition.
    
    Args:
        condition: Normalized condition name
        
    Returns:
        Severity scale description
    """
    if condition in CONDITION_MAP:
        return CONDITION_MAP[condition]["severity_scale"]
    return "1-10"

def get_all_conditions() -> Set[str]:
    """Get all normalized condition names."""
    return set(CONDITION_MAP.keys())

def get_conditions_by_family(family: str) -> Set[str]:
    """
    Get all conditions in a specific family.
    
    Args:
        family: Condition family name
        
    Returns:
        Set of conditions in that family
    """
    return {
        condition for condition, data in CONDITION_MAP.items()
        if data["family"] == family
    }

def expand_condition_query(query: str) -> Set[str]:
    """
    Expand a general condition query to include related specific conditions.
    
    Useful for search queries where user says "pain" but we want to include
    "migraine", "back_pain", "joint_pain", etc.
    
    Args:
        query: User query that might be a general term
        
    Returns:
        Set of specific conditions that match the query
        
    Examples:
        >>> expand_condition_query("pain")
        {'migraine', 'back_pain', 'joint_pain'}
        >>> expand_condition_query("mental health")
        {'anxiety', 'depression'}
    """
    query_lower = query.lower()
    matching_conditions = set()
    
    # Direct condition match
    normalized = normalize_condition(query)
    if normalized:
        matching_conditions.add(normalized)
    
    # Family-based expansion
    if "pain" in query_lower:
        matching_conditions.update(get_conditions_by_family("neurological"))
        matching_conditions.update(get_conditions_by_family("musculoskeletal"))
    
    if "mental" in query_lower or "mood" in query_lower:
        matching_conditions.update(get_conditions_by_family("mental_health"))
    
    if "sleep" in query_lower:
        matching_conditions.update(get_conditions_by_family("sleep"))
    
    if "stomach" in query_lower or "digestive" in query_lower:
        matching_conditions.update(get_conditions_by_family("gastrointestinal"))
    
    return matching_conditions

# Medical severity mapping for standardization
SEVERITY_LEVELS = {
    "none": 0,
    "minimal": 1,
    "mild": 2, 
    "low": 3,
    "moderate": 4,
    "medium": 5,
    "significant": 6,
    "high": 7,
    "severe": 8,
    "extreme": 9,
    "unbearable": 10
}

def normalize_severity(severity_input: str) -> Optional[int]:
    """
    Normalize severity input to a 0-10 scale.
    
    Args:
        severity_input: User input describing severity
        
    Returns:
        Severity level (0-10) or None if not parseable
        
    Examples:
        >>> normalize_severity("mild")
        2
        >>> normalize_severity("7")
        7
        >>> normalize_severity("severe pain")
        8
    """
    if not severity_input:
        return None
    
    # Try to parse as number first
    try:
        level = float(severity_input)
        if 0 <= level <= 10:
            return int(round(level))
    except ValueError:
        pass
    
    # Text-based severity matching
    clean_input = severity_input.lower().strip()
    
    for severity_text, level in SEVERITY_LEVELS.items():
        if severity_text in clean_input:
            return level

    return None

# Populate CONDITION_FAMILIES for backward compatibility
CONDITION_FAMILIES = {
    condition: data["aliases"] 
    for condition, data in CONDITION_MAP.items()
}

def get_related_conditions(condition: str) -> List[str]:
    """
    Get related conditions for a given condition.
    
    Args:
        condition: The condition name to find related conditions for
    
    Returns:
        List of related condition names
    """
    normalized = normalize_condition(condition)
    if normalized and normalized in CONDITION_MAP:
        return CONDITION_MAP[normalized]["aliases"]
    return [condition]  # Return original if not found