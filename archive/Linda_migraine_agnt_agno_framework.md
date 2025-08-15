# 0) Install the few extras

From your `uv` venv, run:

```bash
pip install -U agno fastapi uvicorn pydantic pytest ruff black python-dotenv
```

# 1) Milestone A — make the renderer bulletproof

Create two files and one test. This gives you guaranteed table order and blanks, independent of any LLM.

## `linda_core/schemas.py`

```python
from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Literal, List, Dict, Optional

# Canonical orders used everywhere
TABLE_FIELDS: List[str] = [
    "Date","Time","Bed time (HH:MM)","Wake time (HH:MM)","Sleep hours + Quality (1-10)",
    "Night wakes (#)","Morning light (min)","AM-feel refreshed (1-10)",
    "Meals & times (food, caffeine, alcohol)","Hydration (oz)","Stress (0-10)","Mood / emotions",
    "Exercise / Activity","Posture breaks / Neck exercises","Notes (weather change, hormones, travel, etc.)",
    "Protein (g)","Fiber (g)","Vitamin D (IU)","Calcium (mg)","Calories (kcal)",
    "Carbohydrates (g)","Added sugars (g)","Supplements list",
    "Pantoprazole (Y/N time)","Famotidine (Y/N time)","Amitriptyline (Y/N time)","Emgality – injection date",
    "Doxylamine (mg + brand)","Acetaminophen (mg + brand)",
    "Right-side migraine pain (0-10)","Left-headache pain (0-10)","Scalp-pain (0-10)",
    "Asthma symptoms (none / cough / tight)","Reflux symptoms (burn / lump / cool 0-5)",
    "Episode ID link",
    "PT Before pain / tightness (0-10)","PT During comfort (0-10)","PT After relief (0-10)",
    "Dry-mouth (0-5)","Motivation (0-5)","Appetite (↓ / ↔ / ↑)",
    "Maintenance inhaler (name + puffs)","Rescue inhaler uses",
]
EPISODE_COLUMNS: List[str] = ["ID","Symptom","Start","End/dur","Init","Peak","Relief","Env/Pillow"]

class RowDelta(BaseModel):
    field: str
    value: str
    source_msg_id: Optional[str] = None

class EpisodeDelta(BaseModel):
    id: str
    op: Literal["upsert","close"]
    fields: Dict[str, str] = Field(default_factory=dict)

class Counters(BaseModel):
    data: Dict[str, int] = Field(default_factory=dict)

class PayloadReply(BaseModel):
    markdown: str
    mode: Literal["log","full_table","qa"]

class PayloadData(BaseModel):
    date: str                    # the resolved record_date (echoed back)
    row_deltas: List[RowDelta] = Field(default_factory=list)
    episodes_delta: List[EpisodeDelta] = Field(default_factory=list)
    counters: Dict[str, int] = Field(default_factory=dict)
    profile_delta: List[Dict[str, str]] = Field(default_factory=list)
    alerts: List[Dict[str, str]] = Field(default_factory=list)

class TurnPayload(BaseModel):
    reply: PayloadReply
    data: PayloadData
```

## `linda_core/tools/rendering.py`

```python
from __future__ import annotations
from typing import List, Dict
from ..schemas import TABLE_FIELDS, EPISODE_COLUMNS, RowDelta

def _md_table(rows: List[List[str]]) -> str:
    if not rows:
        return "| Field | Details |\n|---|---|\n"
    header = ["Field","Details"]
    lines = ["| " + " | ".join(header) + " |",
             "| " + " | ".join(["---","---"]) + " |"]
    lines += [f"| {r[0]} | {r[1]} |" for r in rows]
    return "\n".join(lines)

def full_table(day_rows: Dict[str, str], episodes: List[Dict[str, str]] | None = None) -> str:
    rows = [[f, day_rows.get(f, "") or ""] for f in TABLE_FIELDS]
    md = _md_table(rows)
    if episodes:
        md += "\n\n**Episode sub-table**\n"
        hdr = ["| " + " | ".join(EPISODE_COLUMNS) + " |",
               "| " + " | ".join(["---"]*len(EPISODE_COLUMNS)) + " |"]
        body = ["| " + " | ".join([e.get(k,"") or "" for k in EPISODE_COLUMNS]) + " |" for e in episodes]
        md += "\n".join(hdr + body)
    return md

def delta_table(deltas: List[RowDelta]) -> str:
    val_by_field = {d.field: d.value for d in deltas}
    rows = [[f, val_by_field[f]] for f in TABLE_FIELDS if f in val_by_field]
    return _md_table(rows)
```

## `tests/test_rendering.py`

```python
from linda_core.schemas import TABLE_FIELDS, RowDelta
from linda_core.tools.rendering import full_table, delta_table

def test_delta_table_order_and_blanks():
    deltas = [RowDelta(field="Hydration (oz)", value="24"),
              RowDelta(field="Wake time (HH:MM)", value="6:10")]
    md = delta_table(deltas)
    assert "| Wake time (HH:MM) | 6:10 |" in md
    assert md.index("Wake time (HH:MM)") < md.index("Hydration (oz)")

def test_full_table_all_fields_present():
    day_rows = {"Date":"2025-08-07","Hydration (oz)":"24"}
    md = full_table(day_rows, episodes=[])
    for f in TABLE_FIELDS:
        assert f in md
    assert "| Hydration (oz) | 24 |" in md
```

Run: `pytest -q`.

# 2) Milestone B — storage with idempotency

## `linda_core/tools/log_store.py`

```python
import sqlite3, time
from typing import List, Dict
from ..schemas import RowDelta, TABLE_FIELDS

class LogStore:
    def __init__(self, db_path="tmp/linda.db"):
        self.db = db_path
        with sqlite3.connect(self.db) as c:
            c.execute("""CREATE TABLE IF NOT EXISTS day_rows(
                date TEXT, field TEXT, value TEXT, source_msg_id TEXT, ts REAL,
                PRIMARY KEY(date, field, source_msg_id)
            )""")

    def write_rows(self, date: str, deltas: List[RowDelta]) -> None:
        now = time.time()
        with sqlite3.connect(self.db) as c:
            for d in deltas:
                c.execute("""INSERT OR IGNORE INTO day_rows(date,field,value,source_msg_id,ts)
                             VALUES(?,?,?,?,?)""",
                          (date, d.field, d.value, d.source_msg_id or "", now))

    def read_rows(self, date: str) -> Dict[str, str]:
        with sqlite3.connect(self.db) as c:
            cur = c.execute("""SELECT field, value, MAX(ts) FROM day_rows
                               WHERE date=? GROUP BY field""", (date,))
            out = {f: v for (f, v, _) in cur.fetchall()}
        return {f: out.get(f, "") for f in TABLE_FIELDS}
```

## `tests/test_idempotency.py`

```python
from linda_core.schemas import RowDelta
from linda_core.tools.log_store import LogStore

def test_idempotent_writes(tmp_path):
    db = tmp_path / "test.db"
    store = LogStore(str(db))
    date = "2025-08-07"
    d = RowDelta(field="Hydration (oz)", value="24", source_msg_id="m1")
    store.write_rows(date, [d])
    store.write_rows(date, [d])  # same msg again
    rows = store.read_rows(date)
    assert rows["Hydration (oz)"] == "24"
```

Run: `pytest -q`.

# 3) Milestone C — **ActiveDayResolver** (prevents day bleed) + tests

Add a deterministic resolver that picks a **record\_date** for every turn before the workflow runs.

## `linda_core/utils/day_resolver.py`  \[Unverified]

```python
from __future__ import annotations
from datetime import datetime, timedelta
from typing import Optional
import re
import zoneinfo

RELATIVE_PATTERNS = {
    "yesterday": -1,
    "last night": -1,
    "today": 0,
    "this morning": 0,
}

def resolve_record_date(
    message: str,
    timezone: str,
    client_local_time: Optional[str] = None,   # ISO string from UI
    active_date: Optional[str] = None,         # YYYY-MM-DD from UI (wins if present)
) -> tuple[str, Optional[str]]:
    """
    Returns (record_date, clarification_prompt?). If clarification is needed, returns
    (proposed_date, "question text") and the caller should NOT write until confirmed.
    """
    if active_date:
        return active_date, None

    tz = zoneinfo.ZoneInfo(timezone)
    now = datetime.fromisoformat(client_local_time) if client_local_time else datetime.now(tz)

    # 1) explicit relative terms
    low = message.lower()
    for key, offset in RELATIVE_PATTERNS.items():
        if key in low:
            day = (now.date() + timedelta(days=offset)).isoformat()
            return day, None

    # 2) grace window 00:00–04:00 and sleep-ish content → propose yesterday
    if 0 <= now.hour < 4 and re.search(r"\b(bed|slept|sleep|woke|wake|last night)\b", low):
        yday = (now.date() - timedelta(days=1)).isoformat()
        return yday, f"Log this to yesterday ({yday}) or today ({now.date().isoformat()})?"

    # 3) default to today's date
    return now.date().isoformat(), None
```

## `tests/test_day_resolver.py`  \[Unverified]

```python
from linda_core.utils.day_resolver import resolve_record_date

def test_yesterday_phrase_anytime():
    d, clar = resolve_record_date("yesterday I took Ubrelvy 50 mg at 18:10",
                                  timezone="America/New_York",
                                  client_local_time="2025-08-08T14:00:00")
    assert d == "2025-08-07" and clar is None

def test_grace_window_prompts():
    d, clar = resolve_record_date("went to bed at 21:15 and woke at 4",
                                  timezone="America/New_York",
                                  client_local_time="2025-08-08T00:30:00")
    assert d == "2025-08-07" and clar  # proposes yesterday and asks
```

# 4) Milestone D — thin workflow + API (no LLM yet), **date-scoped**

Wire the resolver into the workflow so every write/read is keyed to a single `record_date`.

## `linda_core/workflow.py`  \[Unverified]

```python
from typing import Dict, Any
from .schemas import TurnPayload, PayloadReply, PayloadData, RowDelta
from .tools.log_store import LogStore
from .tools.rendering import full_table, delta_table
from .utils.day_resolver import resolve_record_date

store = LogStore()

def _stub_extract(message: str) -> Dict[str, Any]:
    # tiny demo: capture "24 oz" and "wake 6:10"
    deltas = []
    import re
    if m := re.search(r"(\d+)\s*oz", message, re.I):
        deltas.append(RowDelta(field="Hydration (oz)", value=m.group(1)))
    if m := re.search(r"wake\s+(\d{1,2}:\d{2})", message, re.I):
        deltas.append(RowDelta(field="Wake time (HH:MM)", value=m.group(1)))
    return {"intent":"log","row_deltas":deltas,"episodes_delta":[], "profile_delta":[]}

class MigraineDayWorkflow:
    def run(self, message: str, user_id: str="demo",
            timezone: str="America/New_York",
            client_local_time: str | None = None,
            active_date: str | None = None) -> TurnPayload:

        record_date, clarify = resolve_record_date(message, timezone, client_local_time, active_date)
        if clarify:
            reply = PayloadReply(
                markdown=f"{clarify}\n\nStretch, deep breath, quick walk?",
                mode="qa"
            )
            data = PayloadData(date=record_date)  # do not write yet
            return TurnPayload(reply=reply, data=data)

        ext = _stub_extract(message)

        if ext["intent"] == "full_table":
            table = full_table(store.read_rows(record_date), [])
            reply = PayloadReply(markdown=table + "\n\nStretch, deep breath, quick walk?", mode="full_table")
            data = PayloadData(date=record_date)
            return TurnPayload(reply=reply, data=data)

        store.write_rows(record_date, ext["row_deltas"])
        table = delta_table(ext["row_deltas"])
        reflections = "\n\n**Reflections**\n- Nice job logging early.\n\nStretch, deep breath, quick walk?"
        reply = PayloadReply(markdown=table + reflections, mode="log")
        data = PayloadData(date=record_date, row_deltas=ext["row_deltas"])
        return TurnPayload(reply=reply, data=data)
```

## `server/api.py`  \[Unverified]

```python
from fastapi import FastAPI
from linda_core.workflow import MigraineDayWorkflow

app = FastAPI()
wf = MigraineDayWorkflow()

@app.post("/api/linda/turn")
def turn(body: dict):
    return wf.run(
        message=body.get("message",""),
        user_id=body.get("userId","demo"),
        timezone=body.get("timezone","America/New_York"),
        client_local_time=body.get("clientLocalTime"),
        active_date=body.get("activeDate"),
    )
```

Run the service:

```bash
uvicorn server.api:app --reload
```

Smoke test with explicit context:

```bash
curl -s localhost:8000/api/linda/turn \
 -H "Content-Type: application/json" \
 -d '{"message":"Slept 7h, wake 6:10, drank 24 oz water",
      "timezone":"America/New_York",
      "clientLocalTime":"2025-08-08T14:05:00"}' | jq .
```

# 5) Milestone E — swap stub for the **Agno agent** (extraction only)

Add your Agno `Agent` in `linda_core/agent.py` with `ReasoningTools(add_instructions=True)`, `add_datetime_to_instructions=True`, `add_history_to_messages=True` (num\_history\_runs=3). Replace `_stub_extract()` with an agent call that returns strictly typed JSON for `row_deltas`, `episodes_delta`, `profile_delta`. Everything else stays deterministic and date-scoped.

# 6) Milestone F — expand in tiny bites

* Add **EpisodeManager** (open/update/close + Summary row anchored to **start date**).
* Add **Counters** you care about first (Ubrelvy 30d, amine 7d, acetaminophen-days 30d).
* Add the **Safety gate** and minimal Reflections.
* Add full-table requests if not done.
* Only then consider image nutrition parsing (text first; OCR later).

---

If you want, I can generate a smarter `_stub_extract()` for your most common phrases so you get an immediately satisfying end-to-end loop while we wire the Agno extractor.
