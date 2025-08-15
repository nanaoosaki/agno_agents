\[Inference]

Here’s a clean, Cursor-ready implementation plan you can drop in as `HealthLogger_Revised_Plan.md`.

---

# Health Logger — Revised Implementation Plan (Hybrid LLM + Deterministic Core)

## Purpose

Create a **conversational health logger** that turns messy user input into **clean, queryable data** while staying simple enough for an MVP.
Core idea: **LLM judges & extracts; code validates & commits.**
Pipeline: *User text → LLM JSON → Guardrails/linking → Append event → Upsert episode → (optional) interventions → User reply.*

---

## 0) Repo layout (proposed)

```
agno-chat/
  app.py
  agents.py
  healthlogger/
    __init__.py
    router_llm.py          # calls LLM, returns strict JSON
    linker.py              # decide same-episode vs new-episode using small rules
    storage.py             # JSON/SQLite store, upserts, indexes
    schema.py              # Pydantic models for parsed JSON and persisted rows
    prompts/
      router.system.md     # the system prompt
      router.fewshot.json  # a few labeled examples to anchor behavior
    rules.py               # regex lists for continuity/reset + normalizers
    tests/
      test_router.py
      test_linker.py
      test_storage.py
  data/
    events.jsonl
    episodes.json
    interventions.json
    observations.json
```

SQLite is optional; JSON files are fine for MVP.

---

## 1) JSON contract (LLM → backend)

**LLM must emit only this JSON** (no prose). Validate with Pydantic before use.

```json
{
  "intent": "episode_update",
  "condition": "migraine",
  "fields": {
    "severity": 5,
    "location": "right temple",
    "triggers": ["wine"],
    "start_time": null,
    "end_time": null,
    "notes": "throbbing"
  },
  "episode_link": {
    "link_strategy": "same_episode",
    "episode_key_hint": {"condition": "migraine", "local_date": "YYYY-MM-DD"},
    "rationale": "User said 'now it's 5', implies continuation"
  },
  "interventions": [
    {"type": "heat therapy", "dose": null, "timing": "now", "notes": "on neck"}
  ],
  "confidence": 0.84
}
```

**Intents**: `observation | episode_create | episode_update | intervention | query`.

---

## 2) Prompts

### `prompts/router.system.md`

* Role: *“clinical logging router for holistic health journal.”*
* Tasks: classify intent, normalize condition, extract fields, suggest episode linking, list interventions, set confidence.
* Rules:

  * Prefer `episode_update` when text signals continuity (still, now, same, helped…).
  * Prefer `episode_create` for new/separate (another, new, next day…).
  * Return **only valid JSON** per schema.
  * If unsure, `intent="observation"`, `link_strategy="unknown"`, confidence < 0.6.

### `prompts/router.fewshot.json`

3–6 examples from your own transcripts covering: new migraine, severity update, sleep observation, intervention-only (“took sumatriptan 50mg”), pattern query.

---

## 3) LLM router

`healthlogger/router_llm.py`

* `route_with_llm(text: str, now: dt, model) -> ParsedRouterOutput`

  * Builds prompt from system + few-shot + user text.
  * Calls model; parses JSON; validates via Pydantic model (`schema.RouterOutput`).
  * If parsing fails → raise `RouterParseError`.

* `normalize_condition(s: str) -> str`

  * Map common aliases (headache → migraine, stomach acid → reflux, etc.).
  * Keep tiny and editable.

---

## 4) Linking guardrails (deterministic)

`healthlogger/linker.py`

* Inputs: `ParsedRouterOutput`, `now`, `store.latest_open_episode(cond, date)`
* Regex sets from `rules.py`:

  * `CONTINUITY_RE = r"\b(still|same|now|update|helped|relieve|therapy|patch|took|ice|heat)\b"`
  * `RESET_RE      = r"\b(another|new|again|later that|next day)\b"`
* Policy:

  1. If router says `same_episode` **and** an open episode exists **and** `(now - last_updated) <= 12h`, choose **update**.
  2. Else if router says `new_episode` → **create**.
  3. Else (unknown/ambiguous):

     * If an open episode exists and **either** continuity regex hits **or** within 12h → **update**.
     * Otherwise → **create**.

Returns: `("update"|"create", episode_id_or_None)`.

---

## 5) Storage layer

`healthlogger/storage.py`

* Files (JSON MVP):

  * `events.jsonl` (append-only): `{event_id, ts, user_text, parsed_json, action, model, confidence, ep_id?}`
  * `episodes.json` (dict keyed by `episode_id`):

    ```
    {
      "ep_2025-08-15_migraine_x1": {
        "episode_id": "...",
        "condition": "migraine",
        "started_at": "...",
        "ended_at": null,             # optional
        "status": "open",
        "current_severity": 5,
        "max_severity": 8,
        "severity_points": [{"ts": "...", "level": 5}, ...],
        "notes_log": [{"ts": "...", "text": "..."}, ...],
        "interventions": [{"ts":"...", "type":"heat therapy", "notes":"on neck"}]
      }
    }
    ```
  * `interventions.json` (list) — optional duplication for easy export.
  * `observations.json` (list) — generic non-episode facts (sleep, mood).

* API:

  * `append_event(...) -> event_id`
  * `latest_open_episode(cond, date) -> episode|None`
  * `create_episode(cond, now, fields) -> episode_id`
  * `update_episode(episode_id, fields) -> None`
  * `add_intervention(episode_id, intervention) -> None`
  * `save_observation(date, category, fields) -> None`
  * `rollup_day(date) -> dict` (optional daily canonical view)

* Performance: maintain an **in-memory index** `{(cond, date): episode_id}` hydrated on startup; update it on create/close.

---

## 6) HealthLogger agent (MVP v3)

`agents.py`

* `HealthLoggerAgent.run(text, files=None)`:

  1. Build `enhanced_text` (attach file mentions if any).
  2. `parsed = router_llm.route_with_llm(enhanced_text, now, model)`
  3. `action, ep_id = linker.resolve(parsed, now, store)`
  4. `event_id = store.append_event(text, parsed, action, ep_id)`
  5. If `action == "create"` → `ep_id = store.create_episode(parsed.condition, now, parsed.fields)`
  6. If `action == "update"` → `store.update_episode(ep_id, parsed.fields)`
  7. For each `iv in parsed.interventions` → `store.add_intervention(ep_id, iv)`
  8. If `parsed.intent == "observation"` → `store.save_observation(...)`
  9. Return user-facing message:

     * “**Episode: migraine — updated**; severity 5; **intervention recorded: heat therapy**.”
     * Or “**Episode: migraine — created**.”
     * Or “**Observation saved: sleep** 7h.”

* **Idempotency**: compute `event_hash = sha1(norm_text + minute_bucket)`; if duplicate within 60s, drop.

---

## 7) UX copy (deterministic)

* Update: “Episode: **{condition}** — **updated**; severity {n}{; interventions recorded: …}”
* Create: “Episode: **{condition}** — **created**.”
* Observation: “Observation saved: **{category}**.”
* Override notice (when guardrails change router’s suggestion):
  “Linked to your ongoing **{condition}** episode (within 12h). Say ‘new episode’ if that’s wrong.”

---

## 8) Tests (minimal but meaningful)

* `test_router.py` — feed few-shot strings, assert it returns valid JSON with correct `intent/condition/fields`.
* `test_linker.py` — simulate time gaps and keyword hints; assert update vs create decisions.
* `test_storage.py` — create/update episodes, add interventions, ensure indexes and rollups are correct.

---

## 9) Telemetry & safety

* Log `model_name`, `latency_ms`, `confidence`, `overrides` count (router said same, guardrail created new, etc.).
* If `confidence < 0.55`, return a gentle **clarifying question** instead of committing:
  “Do you want me to update today’s migraine episode or start a new one?”

---

## 10) Rollout steps

1. Implement `schema.py` Pydantic models for `RouterOutput`, `Episode`, `Event`, `Intervention`.
2. Implement `rules.py` (regex + normalizers).
3. Implement `router_llm.py` (uses your existing OpenAI client, same `.env`).
4. Implement `storage.py` (JSON MVP + in-memory index).
5. Implement `linker.py` guardrails.
6. Wire into `HealthLoggerAgent.run()` and your existing Gradio UI.
7. Add 4–6 few-shot examples and iterate.

---

## 11) Later extensions (nice-to-have)

* Switch storage to SQLite (same API) for stronger indexing and concurrency.
* Add an **Episode closer**: close open episodes after 24–48h of no updates.
* Add **pattern queries** (separate Recall Agent using the same store).
* Add **reminders** and **profile updates** once the logging loop is solid.

---

### Acceptance Criteria (MVP)

* LLM returns valid JSON ≥ 95% of the time on your test set.
* Guardrails reduce mis-links; two related migraine messages on same day → **one episode updated**.
* Interventions like “heat therapy” are **attached to the correct episode**.
* events.jsonl, episodes.json update on every turn; UI message reflects action taken.

---

If you want, I can generate the actual code stubs for `schema.py`, `router_llm.py`, `linker.py`, and `storage.py` to paste into Cursor next.
# what gemini2.5pro recommend for Agno library usage 

Of course. The revised plan is excellent and adopts a robust hybrid strategy: using an LLM for its strength in natural language understanding and deterministic code for validation and state management. This is a best practice for building reliable agentic systems.

You are right to ask how the Agno library can be leveraged here. Agno is perfectly suited to implement this plan in a cleaner, more powerful, and more maintainable way.

Here is a comprehensive revised plan that maps the "GPT-5" proposal directly onto Agno's features.

Revised Implementation Plan: Leveraging Agno for the Hybrid Health Logger

The core idea remains the same: LLM extracts, and deterministic code commits. Agno streamlines this by using its built-in features for structured outputs (response_model) and custom tools (@tool).

Instead of a single large HealthLoggerAgent.run() method that does everything, we'll create a more modular system within the Agno framework:

The Extractor Agent: This will be an AgnoAgent whose sole purpose is to perform the task of router_llm.py. It will take raw user text and output a structured RouterOutput Pydantic object. This is Agno's specialty.

The Orchestrator Tool: We will create a single, powerful custom tool, process_health_data, that acts as the "deterministic core." It will receive the structured RouterOutput from the Extractor Agent and perform all the linking and storage logic by calling helpers from your linker.py and storage.py files.

The Orchestrator Agent: This will be the main agent the user interacts with. It will have a simple two-step goal:
a. First, call the Extractor Agent to parse the user's message.
b. Second, call the Orchestrator Tool with the structured data from the first step.

This creates a clean, observable, and highly reliable "extract-then-commit" chain of thought.

Step 1: Define the Schemas (healthlogger/schema.py)

This file is critical. It defines the Pydantic models that ensure type-safe data flow between the LLM and your code.

code
Python
download
content_copy
expand_less

# healthlogger/schema.py
from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class Intervention(BaseModel):
    type: str = Field(..., description="Type of intervention, e.g., 'medication', 'heat therapy'.")
    notes: Optional[str] = Field(None, description="Details about the intervention.")

class EpisodeLink(BaseModel):
    link_strategy: Literal["same_episode", "new_episode", "unknown"]
    rationale: str

class RouterOutput(BaseModel):
    """The structured JSON output from the initial LLM call."""
    intent: Literal["observation", "episode_create", "episode_update", "intervention", "query"]
    condition: Optional[str] = Field(None, description="Normalized condition like 'migraine'.")
    fields: dict = Field(default_factory=dict, description="Extracted fields like severity, location, triggers.")
    interventions: List[Intervention] = Field(default_factory=list)
    episode_link: EpisodeLink
    confidence: float
Step 2: Implement the "Deterministic Core" as a Tool

We will create a new file, healthlogger/tools.py, to house our main orchestrator tool. This tool will use your existing storage.py and a new linker.py.

healthlogger/linker.py (You can create this from your plan)

code
Python
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# healthlogger/linker.py
from datetime import datetime
from typing import Tuple, Optional, Dict, Any
import storage # Assumes storage.py is in the same directory

# Simplified rules for the linker
def resolve_episode_action(
    parsed_output, now: datetime, last_open_episode: Optional[Dict[str, Any]]
) -> Tuple[str, Optional[str]]:
    """Decides whether to 'update' an existing episode or 'create' a new one."""
    if parsed_output.episode_link.link_strategy == "same_episode" and last_open_episode:
        return "update", last_open_episode["episode_id"]
    if parsed_output.episode_link.link_strategy == "new_episode":
        return "create", None
    
    # Fallback logic if LLM is unsure
    if last_open_episode and (now - datetime.fromisoformat(last_open_episode["started_at"].replace("Z",""))).total_seconds() <= 12 * 3600:
        return "update", last_open_episode["episode_id"]

    return "create", None

healthlogger/tools.py

code
Python
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# healthlogger/tools.py
from datetime import datetime
from agno.tools import tool
from .schema import RouterOutput
from . import storage, linker

@tool
def process_and_log_health_data(parsed_data: RouterOutput) -> str:
    """
    Takes the structured output from the extractor agent, applies linking logic,
    and commits the data to storage. This is the main business logic function.
    """
    now = datetime.utcnow()
    confirmations = []

    action, episode_id = "create", None

    if parsed_data.intent in ["episode_create", "episode_update"]:
        condition = parsed_data.condition or "unknown"
        last_open = storage.find_latest_open_episode(condition, now.strftime("%Y-%m-%d"))
        action, episode_id = linker.resolve_episode_action(parsed_data, now, last_open)

        if action == "create":
            new_episode = storage.create_episode(condition, notes=parsed_data.fields.get("notes"))
            episode_id = new_episode["episode_id"]
            confirmations.append(f"Started a new '{condition}' episode.")
        else:
            confirmations.append(f"Updating your ongoing '{condition}' episode.")

        if episode_id:
            storage.update_episode(episode_id, **parsed_data.fields)
            if parsed_data.fields.get("severity"):
                storage.update_episode_severity(episode_id, parsed_data.fields["severity"])
                confirmations.append(f"Severity logged as {parsed_data.fields['severity']}/10.")
    
    for iv in parsed_data.interventions:
        intervention_obj = storage.log_intervention(iv.model_dump())
        confirmations.append(f"Logged intervention: {iv.type}.")
        if episode_id:
            storage.link_to_episode(episode_id, "intervention", intervention_obj["action_id"], "relief")
            
    return " ".join(confirmations)
Step 3: Revise agents.py to use the New Agno-centric Structure

Your agents.py file will now define and orchestrate the two key agents.

code
Python
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# agents.py
import os
from dataclasses import dataclass
from typing import Dict, Any, Optional, List

# --- Agno & Pydantic Imports ---
from agno.agent import Agent as AgnoAgent
from agno.models.openai import OpenAIChat
from agno.tools import tool

# --- Import our custom logic and new schemas/tools ---
from healthlogger.schema import RouterOutput
from healthlogger.tools import process_and_log_health_data
from healthlogger.prompts.router import get_system_prompt, get_few_shot_examples # Assuming prompts are here

# --- Define the Agent Classes ---

@dataclass
class ChatResult:
    text: str
    meta: Optional[Dict[str, Any]] = None

class HealthLoggerAgentV2:
    """
    A multi-step agent that first extracts structured data, then processes it.
    """
    name = "Health Logger (Hybrid)"
    extractor_agent: AgnoAgent
    orchestrator_agent: AgnoAgent

    def __init__(self):
        # 1. The Extractor Agent: Its only job is to return a valid RouterOutput JSON.
        self.extractor_agent = AgnoAgent(
            model=OpenAIChat(id="gpt-4o"),
            response_model=RouterOutput,
            instructions=[
                get_system_prompt(), # Your detailed system prompt
                "You must only return a valid JSON object matching the RouterOutput schema.",
            ],
            # Add few-shot examples for better performance
            few_shot_examples=get_few_shot_examples(),
        )

        # 2. The Orchestrator Agent: Its only job is to call the tool.
        self.orchestrator_agent = AgnoAgent(
            model=OpenAIChat(id="gpt-4o"),
            tools=[process_and_log_health_data],
            instructions=[
                "You will be given a structured JSON object with health data.",
                "You must call the `process_and_log_health_data` tool with this data.",
                "Return the confirmation message from the tool to the user.",
            ],
        )

    def run(self, prompt: str, files: Optional[list] = None) -> ChatResult:
        print("--- Step 1: Extracting structured data from text ---")
        extraction_response = self.extractor_agent.run(prompt)
        
        if not isinstance(extraction_response.content, RouterOutput):
            return ChatResult(text="Sorry, I had trouble understanding that. Could you rephrase?")

        structured_data = extraction_response.content
        print(f"--- Extracted Data (Confidence: {structured_data.confidence:.2f}) ---")
        print(structured_data.model_dump_json(indent=2))

        if structured_data.confidence < 0.55:
             return ChatResult(text="I'm not quite sure what to do with that. Could you be more specific? Are you trying to log a symptom, an observation, or something else?")

        print("\n--- Step 2: Processing and logging data ---")
        orchestration_response = self.orchestrator_agent.run(
            message=structured_data.model_dump() # Pass the Pydantic model directly
        )
        
        return ChatResult(text=orchestration_response.content)

# ... (Other agents like EchoAgent can remain)
class EchoAgent:
    name = "EchoAgent"
    def run(self, prompt: str, files: Optional[list] = None) -> ChatResult:
        file_info = f" ({len(files)} files attached)" if files else ""
        return ChatResult(text=f"Echo: {prompt}{file_info}")

# --- Agent Registry ---
AGENTS: Dict[str, Any] = {
    "Health Logger (Hybrid)": HealthLoggerAgentV2(),
    "EchoAgent": EchoAgent(),
}

def call_agent(agent_name: str, user_text: str, filepaths: Optional[List[str]]) -> ChatResult:
    agent = AGENTS.get(agent_name)
    if not agent:
        return ChatResult(text=f"Unknown agent: {agent_name}")
    
    return agent.run(user_text, files=filepaths)
How to Test This Revised Plan

Your testing flow remains almost identical, but the underlying process is now more robust.

Run the App: python app.py

Select Agent: Choose "Health Logger (Hybrid)".

Provide Input:

Woke up with a bad migraine, maybe a 7/10. I think it was the wine last night.

Observe Console Output: You will now see two distinct steps logged:

The structured JSON output from the ExtractorAgent.

The tool call to process_and_log_health_data.

Check UI and Files: The UI will show the final confirmation, and your data/ directory will be updated correctly.

This Agno-native implementation directly translates your advanced design into a clean, testable, and scalable agentic system.