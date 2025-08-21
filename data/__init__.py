"""
Data layer for the health companion system.

This module provides storage abstractions and implementations for health data,
user profiles, and session management.
"""

from .storage_interface import HealthDataStorage
from .json_store import JsonStore

__all__ = [
    "HealthDataStorage",
    "JsonStore"
]