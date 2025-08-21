"""
Core module for shared primitives and utilities.

This module provides shared functionality used across the health companion system,
including health condition ontology and time utilities.
"""

from .ontology import CONDITION_MAP, normalize_condition, get_condition_family
from .timeutils import parse_date_range, normalize_timezone, format_health_date

__all__ = [
    "CONDITION_MAP",
    "normalize_condition", 
    "get_condition_family",
    "parse_date_range",
    "normalize_timezone",
    "format_health_date"
]