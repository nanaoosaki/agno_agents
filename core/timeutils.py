"""
Time utilities for health data management.

This module provides robust date/time parsing and formatting utilities
optimized for health logging and recall scenarios.
"""

from datetime import datetime, timedelta, timezone
from typing import Tuple, Optional, Union
import re
from dateutil import parser
from dateutil.relativedelta import relativedelta

# Default timezone for health logging
DEFAULT_TIMEZONE = timezone.utc

def parse_date_range(time_expression: str, reference_date: Optional[datetime] = None) -> Tuple[datetime, datetime]:
    """
    Parse natural language time expressions into date ranges.
    
    This function handles various time expressions commonly used in health logging:
    - "yesterday", "today", "last week"
    - "past 3 days", "last 2 weeks"
    - "since Monday", "this month"
    - Specific dates: "2025-01-15", "January 15th"
    
    Args:
        time_expression: Natural language time expression
        reference_date: Reference date for relative expressions (defaults to now)
        
    Returns:
        Tuple of (start_date, end_date) as timezone-aware datetime objects
        
    Examples:
        >>> start, end = parse_date_range("yesterday")
        >>> start, end = parse_date_range("past 7 days")
        >>> start, end = parse_date_range("last week")
    """
    if reference_date is None:
        reference_date = datetime.now(DEFAULT_TIMEZONE)
    
    # Ensure reference_date is timezone-aware
    if reference_date.tzinfo is None:
        reference_date = reference_date.replace(tzinfo=DEFAULT_TIMEZONE)
    
    expr = time_expression.lower().strip()
    
    # Today
    if expr in ["today", "now", "current"]:
        start = reference_date.replace(hour=0, minute=0, second=0, microsecond=0)
        end = start + timedelta(days=1) - timedelta(microseconds=1)
        return start, end
    
    # Yesterday  
    if expr in ["yesterday", "last day"]:
        start = reference_date.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)
        end = start + timedelta(days=1) - timedelta(microseconds=1)
        return start, end
    
    # This week
    if expr in ["this week", "current week"]:
        days_since_monday = reference_date.weekday()
        start = reference_date.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=days_since_monday)
        end = start + timedelta(days=7) - timedelta(microseconds=1)
        return start, end
    
    # Last week
    if expr in ["last week", "previous week"]:
        days_since_monday = reference_date.weekday()
        this_week_start = reference_date.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=days_since_monday)
        start = this_week_start - timedelta(days=7)
        end = this_week_start - timedelta(microseconds=1)
        return start, end
    
    # This month
    if expr in ["this month", "current month"]:
        start = reference_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        next_month = start + relativedelta(months=1)
        end = next_month - timedelta(microseconds=1)
        return start, end
    
    # Last month
    if expr in ["last month", "previous month"]:
        this_month_start = reference_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        start = this_month_start - relativedelta(months=1)
        end = this_month_start - timedelta(microseconds=1)
        return start, end
    
    # Past N days/weeks/months pattern
    past_match = re.search(r'(?:past|last)\s+(\d+)\s+(day|week|month)s?', expr)
    if past_match:
        num = int(past_match.group(1))
        unit = past_match.group(2)
        
        if unit == "day":
            start = reference_date.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=num)
            end = reference_date.replace(hour=23, minute=59, second=59, microsecond=999999)
        elif unit == "week":
            start = reference_date.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(weeks=num)
            end = reference_date.replace(hour=23, minute=59, second=59, microsecond=999999)
        elif unit == "month":
            start = reference_date.replace(hour=0, minute=0, second=0, microsecond=0) - relativedelta(months=num)
            end = reference_date.replace(hour=23, minute=59, second=59, microsecond=999999)
        
        return start, end
    
    # Since pattern (since Monday, since January, etc.)
    since_match = re.search(r'since\s+(.+)', expr)
    if since_match:
        since_expr = since_match.group(1)
        try:
            since_date = parser.parse(since_expr, default=reference_date)
            if since_date.tzinfo is None:
                since_date = since_date.replace(tzinfo=DEFAULT_TIMEZONE)
            start = since_date.replace(hour=0, minute=0, second=0, microsecond=0)
            end = reference_date.replace(hour=23, minute=59, second=59, microsecond=999999)
            return start, end
        except (ValueError, parser.ParserError):
            pass
    
    # Try to parse as specific date
    try:
        specific_date = parser.parse(time_expression, default=reference_date)
        if specific_date.tzinfo is None:
            specific_date = specific_date.replace(tzinfo=DEFAULT_TIMEZONE)
        start = specific_date.replace(hour=0, minute=0, second=0, microsecond=0)
        end = start + timedelta(days=1) - timedelta(microseconds=1)
        return start, end
    except (ValueError, parser.ParserError):
        pass
    
    # Default: last 7 days if nothing else matches
    start = reference_date.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=7)
    end = reference_date.replace(hour=23, minute=59, second=59, microsecond=999999)
    return start, end

def normalize_timezone(dt: Union[datetime, str], target_tz: timezone = DEFAULT_TIMEZONE) -> datetime:
    """
    Normalize a datetime to a specific timezone.
    
    Args:
        dt: Datetime object or ISO string
        target_tz: Target timezone (defaults to UTC)
        
    Returns:
        Timezone-aware datetime in target timezone
    """
    if isinstance(dt, str):
        try:
            dt = parser.parse(dt)
        except (ValueError, parser.ParserError):
            raise ValueError(f"Could not parse datetime string: {dt}")
    
    if dt.tzinfo is None:
        # Assume local timezone if no timezone info
        dt = dt.replace(tzinfo=DEFAULT_TIMEZONE)
    
    return dt.astimezone(target_tz)

def format_health_date(dt: datetime, include_time: bool = True) -> str:
    """
    Format datetime for health logging display.
    
    Args:
        dt: Datetime to format
        include_time: Whether to include time component
        
    Returns:
        Formatted date string optimized for health contexts
        
    Examples:
        >>> format_health_date(datetime.now())
        '2025-01-15 10:30 AM'
        >>> format_health_date(datetime.now(), include_time=False)
        '2025-01-15 (Wed)'
    """
    if include_time:
        return dt.strftime("%Y-%m-%d %I:%M %p")
    else:
        return dt.strftime("%Y-%m-%d (%a)")

def get_relative_time_description(dt: datetime, reference_date: Optional[datetime] = None) -> str:
    """
    Get human-friendly relative time description.
    
    Args:
        dt: Target datetime
        reference_date: Reference datetime (defaults to now)
        
    Returns:
        Human-friendly description like "2 hours ago", "yesterday", "next week"
        
    Examples:
        >>> get_relative_time_description(datetime.now() - timedelta(hours=2))
        '2 hours ago'
        >>> get_relative_time_description(datetime.now() - timedelta(days=1))
        'yesterday'
    """
    if reference_date is None:
        reference_date = datetime.now(DEFAULT_TIMEZONE)
    
    # Ensure both are timezone-aware
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=DEFAULT_TIMEZONE)
    if reference_date.tzinfo is None:
        reference_date = reference_date.replace(tzinfo=DEFAULT_TIMEZONE)
    
    diff = reference_date - dt
    
    if diff.total_seconds() < 0:
        # Future time
        future_diff = dt - reference_date
        if future_diff.days > 0:
            return f"in {future_diff.days} day{'s' if future_diff.days != 1 else ''}"
        elif future_diff.seconds > 3600:
            hours = future_diff.seconds // 3600
            return f"in {hours} hour{'s' if hours != 1 else ''}"
        else:
            minutes = future_diff.seconds // 60
            return f"in {minutes} minute{'s' if minutes != 1 else ''}"
    
    # Past time
    if diff.days > 0:
        if diff.days == 1:
            return "yesterday"
        elif diff.days < 7:
            return f"{diff.days} days ago"
        elif diff.days < 14:
            return "last week"
        elif diff.days < 30:
            weeks = diff.days // 7
            return f"{weeks} week{'s' if weeks != 1 else ''} ago"
        else:
            months = diff.days // 30
            return f"{months} month{'s' if months != 1 else ''} ago"
    
    # Same day
    hours = diff.seconds // 3600
    if hours > 0:
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    
    minutes = diff.seconds // 60
    if minutes > 0:
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
    
    return "just now"

def is_within_time_window(target_dt: datetime, window_start: datetime, window_end: datetime) -> bool:
    """
    Check if a datetime falls within a time window.
    
    Args:
        target_dt: Datetime to check
        window_start: Start of time window
        window_end: End of time window
        
    Returns:
        True if target_dt is within the window
    """
    # Ensure all are timezone-aware
    if target_dt.tzinfo is None:
        target_dt = target_dt.replace(tzinfo=DEFAULT_TIMEZONE)
    if window_start.tzinfo is None:
        window_start = window_start.replace(tzinfo=DEFAULT_TIMEZONE)
    if window_end.tzinfo is None:
        window_end = window_end.replace(tzinfo=DEFAULT_TIMEZONE)
    
    return window_start <= target_dt <= window_end

def get_day_boundaries(dt: datetime) -> Tuple[datetime, datetime]:
    """
    Get the start and end of the day for a given datetime.
    
    Args:
        dt: Target datetime
        
    Returns:
        Tuple of (day_start, day_end)
    """
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=DEFAULT_TIMEZONE)
    
    day_start = dt.replace(hour=0, minute=0, second=0, microsecond=0)
    day_end = day_start + timedelta(days=1) - timedelta(microseconds=1)
    
    return day_start, day_end