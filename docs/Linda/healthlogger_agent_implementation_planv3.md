\[Inference]

Here’s a single, consolidated plan you can hand to Gemini 2.5 Pro to implement **with Agno’s library**, blending their v3 workflow proposal with the gaps I flagged (episode candidates, candidate-aware linker, and disambiguation). I’m keeping this API-agnostic but **Agno-native** (agents, workflow steps, tools, session state). Where I’m unsure of exact method names, I describe intent, I/O, and state so Gemini can map to Agno’s actual APIs.

---

# Health Logger v3 — Agno Workflow Plan (Router + Deterministic Core + Disambiguation)

## Goals

* Turn messy conversational input into **clean, linked health data** (episodes, observations, interventions).
* Maintain **episode continuity** across turns using **stateful context** (not stateless LLM calls).
* Ask for **clarification** when linkage is ambiguous instead of guessing.

---

## High-Level Architecture

**Workflow (Agno):** three steps + shared state.

1. **Extract (Router Agent)** — LLM with short memory + open-episode context → emits a strict JSON proposal.
2. **Process (Deterministic Core)** — validates/links/commits; may emit a clarification payload instead of committing.
3. **Reply (Tone Agent)** — renders confirmations or a concise question for the user.

**Shared state:** `workflow_session_state` holds:

* `open_episode_id` (soft preference)
* `pending_disambiguation` (if we paused to ask the user)
* `last_router_confidence` and small audit fields

**Storage:** JSON or SQLite (same APIs) with an **event log** and **episodes** (+ interventions; observations optional).

---

## Step 0 — Tools & Shared Utilities (Agno “tools”)

Define these as Agno tools so the Router and Processor can call them deterministically.

1. **`fetch_open_episode_candidates(window_hours=24)`**

   * Input: `window_hours`, `now_local_date`, `ontology`
   * Output: list of compact candidates (most recent ≤ 24h), each:

     ```
     {
       "episode_id": "ep_2025-08-15_migraine_ab12cd3",
       "condition": "migraine",
       "started_at": "...", "last_updated_at": "...",
       "current_severity": 5,
       "salient": "right temple; photophobia; heat therapy helped"
     }
     ```
   * Purpose: provide the Extractor with realistic, stateful context.

2. **`normalize_condition(text)`**

   * Input: user text
   * Output: canonical label (e.g., “migraine”) + family (see ontology).
   * Internals: synonyms + body-region hints.

3. **`resolve_link(proposal, candidates, session_pref, now, policy)`**

   * Input:

     * `proposal` = Extractor JSON (intent, condition, fields, episode\_link suggestion, interventions, confidence)
     * `candidates` = output of fetch tool
     * `session_pref` = `open_episode_id` from session (optional)
     * `now` = timestamp
     * `policy` = time windows, day boundary, ambiguity thresholds
   * Output:

     ```
     {
       "final_action": "create" | "update" | "observation" | "intervention" | "query" | "clarify",
       "episode_id": "ep_..." | null,
       "needs_disambiguation": true/false,
       "disambiguation": {
         "message": "Update existing migraine episode from 07:10, or create a new one?",
         "options": [
           {"label": "Update ep_...ab12cd3", "action": "update", "episode_id": "ep_...ab12cd3"},
           {"label": "Create new migraine episode", "action": "create", "episode_id": null}
         ]
       },
       "override_reason": "router_suggested_same_but_stale" | null
     }
     ```
   * Deterministic rules (see “Policies” below).

4. **Storage tools**

   * `append_event(user_text, parsed_json, action, model, confidence, episode_id)`
   * `latest_open_episode(condition, date)` (optional convenience)
   * `create_episode(condition, now, fields) -> episode_id`
   * `update_episode(episode_id, now, fields)`
   * `add_intervention(episode_id, now, iv)`
   * `save_observation(date, category, fields)`
   * (Optional) `rollup_day(date)` for daily canonical view

5. **Telemetry tool (optional)**

   * `log_router_metrics(model, latency_ms, confidence, overrides, disambiguation_used)`

---

## Step 1 — Extract (Router Agent)

**Agno agent** with:

* `response_model` = `RouterOutput` (Pydantic schema below)
* `add_history_to_messages=True`, `num_history_runs=3–5`
* **Context injection**: prepend a tool message (or system context) containing **top N open episode candidates** (e.g., ≤3) from `fetch_open_episode_candidates()`. This is crucial.

**System instructions (sketch):**

* You’re a clinical logging router for a holistic health journal.
* Consider the **recent conversation** and the provided **open episode candidates**.
* Output **only JSON** per RouterOutput; no prose.
* Normalize the condition, extract fields, list interventions.
* Episode linking suggestion:

  * Prefer `same_episode` and include a concrete candidate `episode_id` when continuity is implied and a candidate fits.
  * Use `new_episode` when the message clearly starts something new.
  * Use `unknown` on ambiguity.
* Include `confidence` 0–1; low (<0.6) when unsure.

**RouterOutput (strict JSON)**

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
    "episode_id": "ep_2025-08-15_migraine_ab12cd3",
    "rationale": "User said 'still/now'; candidate is migraine updated 20m ago"
  },
  "interventions": [
    {"type": "heat therapy", "dose": null, "timing": "now", "notes": "on neck"}
  ],
  "confidence": 0.82
}
```

When ambiguous:

```json
{
  "intent": "episode_update",
  "condition": "migraine",
  "fields": {"severity": 5, "notes": "same spot"},
  "episode_link": {"link_strategy": "unknown", "episode_id": null, "rationale": "Two plausible candidates"},
  "interventions": [],
  "confidence": 0.55
}
```

---

## Step 2 — Process (Deterministic Core)

**Agno workflow step** (Python executor) that:

1. **Reads** the Extractor JSON + `workflow_session_state` (e.g., `open_episode_id`).

2. **Fetches** the same candidate list used for context to avoid drift.

3. **Calls** `resolve_link(...)` with:

   * proposal, candidates, session\_pref, now, policy

4. **Branches:**

   * If `final_action == "clarify"` → set `pending_disambiguation` in session state and **emit a clarification payload** (return content suited for the Reply step).
   * Else:

     * **Append event** (audit).
     * **Create/Update** episode deterministically.
     * **Attach interventions** (if any; if no episode chosen on intervention-only, pick best candidate within window; else create minimal episode).
     * **Save observation** path for `intent="observation"`.
     * **Update** `open_episode_id` to the chosen episode, if any.

5. **Return** a compact, deterministic confirmation string for the Reply step, e.g.:

   * “Episode: migraine — created.”
   * “Episode: migraine — updated; intervention recorded: heat therapy.”
   * “Observation saved: sleep 7h.”
   * Or a **clarification prompt** string if needed.

---

## Step 3 — Reply (Tone Agent)

**Agno agent** that paraphrases confirmations or **asks the disambiguation question** concisely and empathetically. Keep deterministic content intact; this is tone only.

Examples:

* Confirmation input: `Episode: migraine — updated; intervention recorded: heat therapy.`
  Output: `Got it — I’ve updated your migraine episode and noted the heat therapy.`

* Clarification input: `Clarify: Update ep_...ab12cd3 from 07:10 today, or create a new migraine episode?`
  Output: `This looks related to your migraine from 07:10. Should I update that episode, or start a new one?`

---

## Disambiguation UX (Gradio)

When the Processor returns a clarification string and sets `pending_disambiguation`, the UI should render **two buttons**:

* **Update \<short\_id>**
* **Create new episode**

On click, call the same workflow with a small control message:

```
/resolve { "choice": "update", "episode_id": "ep_...ab12cd3" }
```

The Processor:

* Detects `/resolve`, reads `pending_disambiguation`, commits deterministically, clears it, and replies with a standard confirmation.

---

## Policies (Deterministic Rules in `resolve_link`)

* **Time window:** default **12h** recency to count as same episode.
* **Day boundary:** entering a new local date defaults to **new episode**, unless Extractor strongly signals continuation **and** a candidate fits within window.
* **Family match:** a proposal for “pain/neck/temple” can map to **migraine family**; candidates from that family are eligible.
* **Session preference:** prefer `open_episode_id` if it also passes window/family checks.
* **Ambiguity threshold:** clarification if:

  * Extractor `confidence < 0.6`, **or**
  * Two candidates within **0.1** score margin, **or**
  * Router suggests `same_episode` but policy rejects due to staleness or mismatch.

**Intervention-only messages:** attach to most recent **eligible** candidate in same family within window; else **create minimal episode** and attach.

**Auto-close:** close open episodes after **24–48h** idle (`ended_at`, `status="closed"`). New messages after closure will normally create new episodes; Extractor may still suggest same episode, but policy decides.

---

## Condition Ontology (minimum viable)

Families and hints (editable JSON/dict used by both Extractor context and Processor):

```
FAMILIES = {
  "migraine": ["migraine", "headache", "head pain", "temple pain", "behind eye", "neck-related head pain"],
  "sleep": ["sleep", "insomnia", "sleep quality", "nap"],
  "reflux": ["reflux", "heartburn", "gerd", "acid"],
  "asthma": ["asthma", "wheeze", "wheezing", "shortness of breath"]
}

BODY_REGION_HINTS = {
  "migraine": ["temple", "behind eye", "photophobia", "nausea", "throbbing", "neck"],
  "reflux": ["burning chest", "acid", "sour taste"],
  "asthma": ["wheeze", "short of breath", "tight chest"]
}
```

---

## Data Schema (persisted)

* **events.jsonl** (append-only): `{event_id, ts, user_text, parsed, action, model, confidence, episode_id, event_hash}`
* **episodes.json** (or table keyed by `episode_id`):

  ```
  {
    "episode_id": "...",
    "condition": "migraine",
    "started_at": "...", "ended_at": null, "status": "open",
    "current_severity": 5, "max_severity": 8,
    "severity_points": [{"ts":"...", "level":5}, ...],
    "notes_log": [{"ts":"...", "text":"..."}, ...],
    "interventions": [{"ts":"...", "type":"heat therapy", "notes":"on neck"}],
    "last_updated_at": "..."
  }
  ```
* **interventions.json** (optional mirror list for export)
* **observations.json** (optional list; `{date, category, fields}`)

**Idempotency:** hash `(normalized_text + minute_bucket)` to avoid double commits on resubmits.

---

## Session & Timezone

* Use a **per-conversation `session_id`** (store in `gr.State`), pass to Agno Workflow so `workflow_session_state` is user-scoped.
* Resolve **local date/time** from user timezone before linking or creating episodes (day boundary logic depends on this).

---

## Failure Modes & Fallbacks

* If Extractor JSON parse fails → return `intent="observation"`, `episode_link.link_strategy="unknown"`, `confidence=0.0`, and trigger **clarification**.
* If storage write fails → abort commit, **do not** update `open_episode_id`, return a clear error string for Reply Agent.
* If user ignores a clarification and sends new content → clear `pending_disambiguation` and treat next turn normally.

---

## Telemetry & Tests

* **Log per turn:** model, latency\_ms, router confidence, overrides (policy vs router), disambiguation\_used (bool).
* **Tests:**

  * Router few-shot JSON validity and key field extraction.
  * Linker policy across time gaps and families.
  * Intervention-only attach behavior.
  * Observation path (no episode changes).
  * Disambiguation: low confidence produces options; user choice commits correctly.

---

## Acceptance Criteria

* Sequential migraine-related messages on the same day **update a single episode** ≥ 90% of the time without prompting.
* Intervention-only messages **attach to the correct episode** (same family, within window) ≥ 90%.
* Ambiguity flow triggers with clear options when confidence is low or candidates tie, and user choice is honored.
* No duplicate commits on UI resubmits (idempotency working).

---

## Integration Notes (Gradio)

* Replace the dropdown agent with “Health Logger (Workflow)”.
* Maintain a per-tab `session_id` via `gr.State`.
* When the Reply step asks a question, render **two buttons**; on click, send `/resolve {json}` to the Workflow; Processor finalizes and clears `pending_disambiguation`.

---

### Hand-off summary for Gemini

* Implement the **Extractor Agent** with history and **candidate context injection**.
* Implement `fetch_open_episode_candidates`, `normalize_condition`, `resolve_link`, and storage tools as Agno tools callable from the Workflow.
* Make `resolve_link` **candidate-aware** (not just `open_episode_id`).
* Add **disambiguation** branch with session-state persistence and UI buttons.
* Enforce the **policies** above (12h window, day boundary, family match, auto-close).
* Keep Router output **strict JSON** (Pydantic model) and Processor **deterministic**.

If you want, I can also provide a tiny set of **few-shot examples** (one per intent) tailored to your real transcripts to seed the Extractor’s behavior.

## Gemini's Agno library recommendations 
Excellent. The issue analysis is spot on, the v2 implementation report is clear, and the v3 high-level plan is the correct path forward. The core problem is indeed the lack of conversational context and state management, which is precisely what Agno's Workflow and session_state are designed to solve.

Here is a comprehensive implementation plan that translates your v3 proposal into a concrete, Agno-native architecture. This plan leverages the Agno library's features to directly address the issues you've identified.

Revised Implementation Plan (v3) - Agno Native Architecture

We will refactor the system into a stateful Agno Workflow. This workflow will manage the conversation state, orchestrate the specialized agents, and handle the deterministic logic, providing a robust and observable process.

High-Level Agno Workflow:

Step 1: Extractor Agent (Agent): This agent's responsibility is to understand the user's intent within the context of the conversation. It will now receive chat history.

Step 2: Process & Log (Custom Function): This is the deterministic core. It will be a Python function acting as a workflow step. It will receive the structured data from the Extractor, apply your business logic from linker.py and storage.py, and update the workflow's shared state.

Step 3: Reply Agent (Agent): This agent's role is to craft a user-friendly response based on the outcome of the processing step (e.g., a confirmation or a clarifying question).

This structure gives us the best of both worlds: LLM-based understanding and deterministic, testable Python code for the critical business logic.

Step 1: The Stateful Extractor Agent (with Conversational Context)

The key to fixing the episode continuity issue is to make the extractor agent aware of the conversation history.

File: healthlogger/router_llm.py (or integrated into agents.py)

Implementation using agno.agent.Agent:

code
Python
download
content_copy
expand_less

# healthlogger/agents.py (or a new file)

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from .schema import RouterOutput # Your Pydantic model for the LLM's output
from .prompts import get_system_prompt, get_few_shot_examples # Your prompt helpers

extractor_agent = Agent(
    name="ExtractorAgent",
    model=OpenAIChat(id="gpt-4o"),
    # Enforce the strict JSON output using Agno's built-in feature
    response_model=RouterOutput,
    
    # CRITICAL FIX: This passes the last few conversation turns to the agent.
    add_history_to_messages=True,
    num_history_runs=5, # Number of previous user/agent turns to include
    
    instructions=[
        get_system_prompt(),
        "You must analyze the user's LATEST message in the context of the RECENT CHAT HISTORY.",
        "Your primary goal is to determine if the user is updating an existing episode or creating a new one.",
        "Use the `episode_link.link_strategy` field for this. If the user says 'the pain is still going on', it's an UPDATE.",
        "You must ONLY return a valid JSON object matching the RouterOutput schema."
    ],
    few_shot_examples=get_few_shot_examples(),
)

What this solves:

Lack of Conversational Context: The agent now sees previous messages, allowing it to understand phrases like "it's still ongoing."

Improved Condition Normalization: With context, the LLM is much more likely to correctly associate "the pain" with the previously mentioned "migraine."

Step 2: The Deterministic Core as a Workflow Step

This step will be a custom Python function that takes the output of the Extractor Agent and applies your business logic. It will interact with the workflow's shared memory (workflow_session_state).

File: healthlogger/workflow_steps.py

code
Python
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# healthlogger/workflow_steps.py
from agno.workflow.v2 import StepInput, StepOutput
from .schema import RouterOutput
from . import storage, linker, rules
from datetime import datetime

def process_and_log_step(step_input: StepInput) -> StepOutput:
    """
    Deterministic step to process extracted health data, link episodes,
    and commit to storage.
    """
    parsed_data: RouterOutput = step_input.previous_step_content
    now = datetime.utcnow()
    
    # Get the currently open episode from the workflow's shared memory
    open_episode_id = step_input.workflow_session_state.get("open_episode_id")
    last_open_episode = storage._episodes().get(open_episode_id) if open_episode_id else None

    # Use the linker to decide the action
    action, episode_id_to_update = linker.resolve_episode_action(
        parsed_data, now, last_open_episode
    )
    
    # Your logic to create/update episodes and log interventions...
    # ... (This logic can be ported from your v2 plan) ...

    # CRITICAL: Update the workflow's shared state
    if episode_id:
        step_input.workflow_session_state["open_episode_id"] = episode_id
    
    # Return a structured payload for the Reply agent
    confirmation_payload = {
        "action_taken": action,
        "condition": parsed_data.condition,
        "details": confirmations # A list of strings like "Severity updated to 5/10."
    }
    return StepOutput(content=confirmation_payload)

What this solves:

Stateful Episode Tracking: workflow_session_state provides a reliable way to remember the active episode between user messages.

Step 3: The User-Facing Reply Agent

This agent's job is to take the structured confirmation from the processing step and turn it into a natural, empathetic response.

File: healthlogger/agents.py

code
Python
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# healthlogger/agents.py

reply_agent = Agent(
    name="ReplyAgent",
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions=[
        "You are a friendly and empathetic health companion.",
        "You will receive a structured summary of actions taken.",
        "Convert this summary into a warm, natural, and brief confirmation message for the user.",
        "For example, if the action was 'update' for a 'migraine', say something like: 'Thanks for the update, I've added that to your ongoing migraine log. Hope you're feeling a bit better.'"
    ]
)
Step 4: The Agno Workflow (agents.py)

Now, we wrap these components in an agno.workflow.v2.Workflow. This becomes the main entry point called by the Gradio UI.

code
Python
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# agents.py (the final orchestrator)

from agno.workflow.v2 import Workflow, Step
from .healthlogger.workflow_steps import process_and_log_step
from .healthlogger.agents import extractor_agent, reply_agent

# Define the steps for our workflow
steps = [
    Step(name="Extract", agent=extractor_agent),
    Step(name="Process", executor=process_and_log_step),
    Step(name="Reply", agent=reply_agent),
]

# Define the main workflow
health_logger_workflow = Workflow(
    name="Health Logger Workflow V3",
    steps=steps,
    # The session state is automatically managed per session_id by Agno
    workflow_session_state={} 
)

# Wrapper class to interface with the existing Gradio app
class HealthLoggerWorkflowWrapper:
    name = "Health Logger (v3)"

    def run(self, prompt: str, files: Optional[list] = None) -> ChatResult:
        # Each user has a unique, persistent session_id
        session_id = "user_main_session" # In a real app, this would be dynamic per user
        
        response = health_logger_workflow.run(
            message=prompt,
            session_id=session_id
        )
        return ChatResult(text=response.content)

# Update the AGENTS dictionary in agents.py
AGENTS = {
    "Health Logger (v3)": HealthLoggerWorkflowWrapper(),
    # ... other agents
}
How this Plan Solves the Key Issues:

Fragmented Episodes: Solved by workflow_session_state, which tracks the open_episode_id across turns. The linker.py now receives this stateful context.

Lack of Conversational Context: Solved by add_history_to_messages=True on the ExtractorAgent. It can now correctly interpret "it's still ongoing" because it sees the previous message about the migraine.

Condition Normalization: The conversational context dramatically improves the LLM's ability to link "pain" or "neck pain" back to "migraine". You can further enhance this by explicitly instructing the agent in its prompt to use the context to normalize conditions.

No User Confirmation: The v3 plan's disambiguation logic can be implemented inside the process_and_log_step. If resolve_link returns "clarify", this step can set a flag in workflow_session_state and return a StepOutput with the clarification question, which the ReplyAgent will then ask the user. The next run of the workflow will see the flag and handle the user's response accordingly.

This Agno-native architecture is robust, scalable, and directly implements the intelligent, hybrid approach outlined in your v3 plan.