"""
Time utilities for handling dates, timezones, and temporal parsing.

This module centralizes all date/time logic used across the application
for consistent temporal operations.
"""

from datetime import datetime, timedelta
from typing import Tuple, Optional
import re


def parse_natural_time_range(query: str, user_timezone: str = "UTC") -> Tuple[datetime, datetime, str]:
    """
    Parse natural language time expressions into structured date ranges.
    
    Args:
        query: Natural language query containing time expressions
        user_timezone: User's timezone (currently defaults to UTC)
        
    Returns:
        Tuple of (start_datetime, end_datetime, human_readable_label)
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

    return start_date, end_date, label


def format_timestamp(dt: datetime, include_seconds: bool = False) -> str:
    """
    Format a datetime object for consistent display.
    
    Args:
        dt: The datetime to format
        include_seconds: Whether to include seconds in the output
        
    Returns:
        Formatted timestamp string
    """
    if include_seconds:
        return dt.strftime("%Y-%m-%d %H:%M:%S UTC")
    return dt.strftime("%Y-%m-%d %H:%M UTC")


def parse_iso_timestamp(timestamp_str: str) -> Optional[datetime]:
    """
    Parse an ISO format timestamp string into a datetime object.
    
    Args:
        timestamp_str: ISO format timestamp string
        
    Returns:
        Parsed datetime object or None if parsing fails
    """
    if not timestamp_str:
        return None
        
    try:
        # Handle Z suffix and various ISO formats
        clean_timestamp = timestamp_str.replace('Z', '+00:00')
        return datetime.fromisoformat(clean_timestamp)
    except ValueError:
        return None


def get_current_utc_iso() -> str:
    """
    Get the current time as an ISO format string in UTC.
    
    Returns:
        Current timestamp in ISO format
    """
    return datetime.utcnow().isoformat()


def time_since(start_time: datetime, end_time: Optional[datetime] = None) -> str:
    """
    Calculate human-readable time difference.
    
    Args:
        start_time: The start time
        end_time: The end time (defaults to now)
        
    Returns:
        Human-readable time difference
    """
    if end_time is None:
        end_time = datetime.utcnow()
    
    diff = end_time - start_time
    
    if diff.days > 0:
        return f"{diff.days} day{'s' if diff.days != 1 else ''} ago"
    elif diff.seconds > 3600:
        hours = diff.seconds // 3600
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    elif diff.seconds > 60:
        minutes = diff.seconds // 60
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
    else:
        return "just now"