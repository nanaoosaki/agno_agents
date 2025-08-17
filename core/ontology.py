"""
Core ontology definitions for health conditions and normalization rules.

This module centralizes the health domain knowledge used across the application
for consistent condition classification and matching.
"""

from typing import Optional, Dict, List

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
    
    return None


def get_related_conditions(condition: str) -> List[str]:
    """
    Get related conditions for broader searching.
    For generic terms like 'pain', returns all pain-related conditions.
    
    Args:
        condition: The condition to find related conditions for
        
    Returns:
        List of related condition names including the original
    """
    normalized = normalize_condition(condition)
    if not normalized:
        return []
    
    # If searching for generic "pain", include all pain-related conditions
    if normalized == "pain":
        pain_related = ["pain", "migraine", "back_pain", "neck_pain"]
        return [cond for cond in pain_related if cond in CONDITION_FAMILIES]
    
    # Otherwise, return just the normalized condition
    return [normalized]


def get_condition_synonyms(canonical_condition: str) -> List[str]:
    """
    Get all known synonyms for a canonical condition.
    
    Args:
        canonical_condition: The canonical condition name
        
    Returns:
        List of synonyms for the condition
    """
    return CONDITION_FAMILIES.get(canonical_condition, [])


def get_body_region_hints(condition: str) -> List[str]:
    """
    Get body region hints for a condition to help with classification.
    
    Args:
        condition: The condition name
        
    Returns:
        List of body region hints
    """
    return BODY_REGION_HINTS.get(condition, [])