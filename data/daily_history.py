"""Utilities for compiling and retrieving daily health history.

This module aggregates raw health logs into a per-day summary so that the
UI and Recall Agent can query compact daily snapshots instead of scanning
all raw data files.  Each record contains pain statistics and counts of
logged episodes and observations for that day.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Optional

DATA_DIR = Path("data")
DAILY_HISTORY_FILE = DATA_DIR / "daily_history.json"
EPISODES_FILE = DATA_DIR / "episodes.json"
OBSERVATIONS_FILE = DATA_DIR / "observations.json"


@dataclass
class DailyHistory:
    """Aggregated health metrics for a single day."""

    date: str  # YYYY-MM-DD
    avg_pain: Optional[float] = None
    max_pain: Optional[int] = None
    episodes: int = 0
    observations: int = 0


def _read_json(path: Path, default):
    if path.exists():
        try:
            return json.loads(path.read_text())
        except json.JSONDecodeError:
            return default
    return default


def _load_history() -> List[DailyHistory]:
    """Load existing daily history records."""
    records = _read_json(DAILY_HISTORY_FILE, [])
    return [DailyHistory(**r) for r in records]

# Public alias
load_history = _load_history


def _save_history(records: List[DailyHistory]):
    DATA_DIR.mkdir(exist_ok=True)
    DAILY_HISTORY_FILE.write_text(json.dumps([asdict(r) for r in records], indent=2))


def compile_day(date: Optional[str] = None) -> DailyHistory:
    """Compile daily history for the given date (UTC)."""
    if date is None:
        date = datetime.utcnow().date().isoformat()
    day_start = datetime.fromisoformat(date)
    day_end = day_start + timedelta(days=1)

    episodes = _read_json(EPISODES_FILE, {})
    observations = _read_json(OBSERVATIONS_FILE, [])

    severities: List[int] = []
    for ep in episodes.values():
        try:
            ts = datetime.fromisoformat(ep["started_at"])
        except Exception:
            continue
        if day_start <= ts < day_end and ep.get("max_severity") is not None:
            severities.append(int(ep["max_severity"]))

    episode_count = len(severities)
    max_pain = max(severities) if severities else None
    avg_pain = sum(severities) / episode_count if episode_count else None

    observation_count = 0
    for ob in observations:
        try:
            ts = datetime.fromisoformat(ob["timestamp"])
        except Exception:
            continue
        if day_start <= ts < day_end:
            observation_count += 1

    record = DailyHistory(
        date=date,
        avg_pain=avg_pain,
        max_pain=max_pain,
        episodes=episode_count,
        observations=observation_count,
    )

    records = [r for r in _load_history() if r.date != date]
    records.append(record)
    records.sort(key=lambda r: r.date)
    _save_history(records)
    return record


def get_history(start_date: Optional[str] = None, end_date: Optional[str] = None) -> List[DailyHistory]:
    """Retrieve compiled daily history records within an optional date range."""
    records = _load_history()
    if start_date and end_date:
        return [r for r in records if start_date <= r.date <= end_date]
    if start_date:
        return [r for r in records if r.date >= start_date]
    if end_date:
        return [r for r in records if r.date <= end_date]
    return records
