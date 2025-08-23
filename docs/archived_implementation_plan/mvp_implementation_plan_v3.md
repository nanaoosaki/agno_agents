\[Inference]

Great—since your **Extractor** is in place (Agno workflow + structured JSON + history-aware) and behaving per the v3 report, the lean MVP now needs just **two more agents** to complete the core value loop:

* a **Recall Agent** to answer “what happened when…?” questions from the structured log, and
* a **Coach Agent** to deliver safe, actionable tips or brief emotional support grounded in the user’s recent data.&#x20;

Below is a crisp, high-level agentic framework you can keep in Cursor as the project’s north star.

---

# MVP Agentic Framework (Agno)

## 1) Health Logger (already built)

Purpose: convert messy input into clean, linked data and confirm what was saved.

Architecture: Agno **Workflow** with three steps
• **Extract (Router Agent)** → structured JSON (intent, condition, fields, link suggestion, interventions, confidence) with conversation history and open-episode context.
• **Process (Deterministic Step)** → apply policies (time window, family match, day boundary), create/update episode, attach interventions, persist event/episode. If ambiguous, produce a short clarification prompt instead of guessing.
• **Reply (Tone Agent)** → a concise, empathetic confirmation or clarification.&#x20;

Core outputs: `events.jsonl`, `episodes.json`, `interventions.json`, `observations.json` + user-facing confirmation.&#x20;

---

## 2) Recall Agent (to build now)

Purpose: let the user query their history in plain language, e.g., “Did I get migraines whenever I had tofu?” “When was my last attack?” “Show me sleep vs. headache severity last week.”

How it works (Agno):

* **Inputs:** user question + short conversation memory.
* **Tools:**

  1. `search_events(query)` — keyword/date filters over events and episodes (JSON or SQLite).
  2. `aggregate(pattern)` — small helpers for “count per day,” “co-occurrence,” “time window before/after X.”
  3. `fetch_episode_summaries(range)` — compact tables for the LLM to cite.
* **Agent behavior:**

  * Parses the question into a simple **query plan** (e.g., entity = tofu, condition = migraine, window = same day ± 12h).
  * Calls tools deterministically, never “imagines” results.
  * Produces a **brief answer + one supporting snippet/table**; if evidence is thin, it says “I can’t verify” and suggests what to log next \[Unverified].
* **Outputs:** short natural-language answer plus an optional tiny table; no schema changes.

Success criteria:

* Answers are reproducible from stored data, with no hallucination.
* Handles the top 5 queries you care about (last episode, frequency in a range, food co-occurrence, trend line, interventions tried before relief).
* Falls back gracefully with “need more data” when logs are sparse.

---

## 3) Coach Agent (to build now)

Purpose: turn the just-logged context (and, when helpful, recent history) into **one or two** safe, practical suggestions or a brief coping script—nothing clinical or diagnostic.

How it works (Agno):

* **Inputs:** latest **ProcessingResult** (condition, severity, notes, interventions just taken), plus a **very small** profile/context slice (e.g., known triggers, typical bedtime).
* **Tools:**

  1. `fetch_recent_episode_snapshot()` — last 24–72h for the active condition.
  2. `safety_rules()` — a static map of guardrails (“do not recommend beyond OTC; avoid dosage advice; when severity ≥ X with red flags, suggest seeking care”).
  3. (Optional) `habits_catalog()` — tiny library of evidence-based micro-actions (hydration break, dark/quiet room, paced breathing, gentle neck heat/ice guidance).
* **Agent behavior:**

  * Reads the snapshot and picks **at most two** suggestions, clearly labeled as general support.
  * If something is already being tried (e.g., heat therapy), it acknowledges and avoids repeating advice; may suggest a complementary step (hydration, light stretch).
  * Uses cautious language and encourages tracking outcomes (“If you try this, I’ll note it so we can see if it helps next time”).
* **Outputs:** one paragraph, maximum two bullets; never prescriptive medical guidance.

Success criteria:

* Helpful tone, tiny and actionable; aligns with what was just logged.
* No dosage, no diagnoses, no false certainty.
* Encourages continued logging and recalls (“If it worsens or new symptoms appear, tell me so I can update the episode.”).

---

## Orchestration at the UI level

Keep it simple for the MVP:

* **Single entry point:** the existing chat.
* Default route = **Health Logger**. If the user asks a historical question (“did I…”, “when…”, “show…”, “how often…”) → call **Recall Agent**. If they ask “what can I do right now?” or express distress → call **Coach Agent**.
* You can keep a temporary dropdown in dev builds to manually force a call route while testing.

---

## Minimal interfaces (I/O contracts)

* **Recall Agent → Reply:**

  * “From 2025-08-01 to 2025-08-15, you logged 4 migraine episodes. On days you ate tofu, 0/2 had migraines within 12h. I can’t verify a link yet.” \[Unverified]

* **Coach Agent → Reply:**

  * “I’ve updated your migraine episode. Since heat helped a bit, you could try a brief hydration break and a dark, quiet room for 20–30 minutes. If symptoms change, tell me and I’ll update the log.”

Both agents should return a short, deterministic `meta` block (e.g., filters applied, episode\_id considered) for debugging, but only the concise prose goes to the user.

---

## Guardrails and policies shared across agents

* **Time window for continuity:** default 12h; day boundary starts a new episode unless strongly indicated otherwise.
* **Condition families & hints:** common synonyms and body-region cues live in one shared map.
* **Ambiguity handling:** when unsure, ask a **one-tap** question rather than guessing; respect user choice.
* **Idempotency:** hash `(normalized_text + minute bucket)` to avoid double commits on resubmits.
* **Safety:** no clinical claims; encourage help-seeking when severity/red flags appear.

---

## What’s “done” for the MVP

* Health Logger Workflow (Extractor → Process → Reply) behaves as in your v3 report.&#x20;
* Recall Agent answers the top 5 history questions reliably from logs.
* Coach Agent provides one-paragraph, safe guidance tied to the latest episode.
* The chat routes to Recall/Coach when appropriate; otherwise logs by default.
* Basic tests pass for: episode continuity, tofu-style co-occurrence, intervention attach, and ambiguity prompts.

If you want, I can sketch the **Recall query patterns** and the **Coach micro-suggestion catalog** next, so Gemini has crisp tool signatures to implement inside Agno.
