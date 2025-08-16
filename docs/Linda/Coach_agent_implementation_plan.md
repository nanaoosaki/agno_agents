\[Inference]

awesome—since your **Extractor** and **Recall Agent** are now live, the last core piece for the MVP is the **Coach Agent**. Below is a high-level, Agno-native plan you can hand to Gemini 2.5 Pro. It keeps things simple, stateful, and safe, and it leans on your existing logs plus your migraine megahandout for non-medication guidance.

---

# Coach Agent — High-Level Plan (Agno)

## Purpose

Provide brief, personalized, **non-medication** suggestions that can help users relieve pain or reduce risk (e.g., heat/ice, stretches, pacing, hydration, sleep hygiene, stress/mindfulness, trigger management), grounded in the user’s most recent episode and history. The agent must be empathetic, concise, and strictly evidence-informed from your provided handout content.&#x20;

This completes your MVP trio:

* **Logger Workflow** → clean, linked data
* **Recall Agent** → answers about the past
* **Coach Agent** → next best small step right now &#x20;

---

## Inputs (to the Coach Agent)

* **Conversation context**: last 2–3 user turns (Agno `add_history_to_messages=True`).
* **Active episode snapshot** (tool): current condition, started/last\_updated, current/max severity, body location, notes, recent interventions tried.
* **Recent history** (tool): last 48–72h summary for that condition (severity trend, common triggers observed, what helped).
* **User profile slice** (tool, optional): known sensitivities (e.g., caffeine), sleep patterns.
* **Knowledge snippets**: compact sections from the **Migraine Headache Megahandout** transformed into short, reusable guidance blocks (lifestyle, trigger avoidance, sleep regularity, hydration, exercise warm-up, stress reduction).&#x20;

---

## Outputs

* A **single short paragraph** plus at most **two bullets** with actionable, non-pharmacologic tips tailored to the episode and recent history (e.g., “short dark-room break,” “warm compress 10–15 min,” “hydration and gentle neck mobility”).
* Optional: a small, neutral **nudging line** to keep logging and, if helpful, track whether the action reduced severity.

No dosing guidance, no diagnosis, and no prescriptive medical directives.

---

## Agent Design (Agno)

**Pattern:** Single **Coach Agent** with a small **toolkit** (deterministic helpers). The agent plans briefly, calls tools, and composes advice snippets that map to the handout content.

### Tools (deterministic)

1. `fetch_active_episode_snapshot(window_hours=72)`
   Returns the last open episode (or most recent closed within window) with severity trajectory, notes, and interventions.

2. `fetch_recent_triggers(condition, start, end)`
   Returns common triggers observed recently (e.g., irregular sleep, bright light exposure, specific foods). This should align with your Logger ontology; the handout enumerates common triggers to map against.&#x20;

3. `knowledge_snippets(condition)`
   Returns a curated set of **non-medication** micro-interventions sourced from the handout (e.g., keep **regular sleep** and **meals**, avoid **bright/harsh lights**, **hydrate**, **gentle aerobic activity with warm-up**, **stress reduction/mindfulness**).&#x20;

4. `safety_filters()`
   Enforces house rules:

   * No med dosing; flag **medication overuse** risk gently if user mentions frequent OTCs (reference: overuse can worsen headaches; if using pain meds >2–3 days/week, consider reducing/seek guidance). Suggestions should remain neutral and educational.&#x20;

5. `compose_plan(episode, recent_triggers, snippets)`
   Deterministically picks **≤2** tips that are: a) not already tried in last few hours, b) compatible with triggers and context, c) simple and low-effort.

---

## Agent Instructions (essentials)

* Start with the **active episode snapshot**. If none is open, use the most recent episode today; otherwise fall back to a short general tip set.
* Prefer **adjacent, low-effort** actions first (e.g., dark/quiet room; hydration; warm or cool compress; brief paced breathing/mindfulness) and **sleep regularity** coaching, drawn from the handout’s lifestyle and trigger sections.&#x20;
* If the user already tried something (e.g., heat), acknowledge it and suggest one **complementary** option (e.g., hydration + quiet break).
* Keep it short: **one paragraph + up to two bullets**.
* Always be supportive and non-judgmental.
* Do **not** speculate or diagnose. If you lack details, say what you need the user to log next.

---

## Minimal Workflow (inside the Coach Agent)

1. **Plan**: identify condition and whether there’s an active episode.
2. **Call tools**:

   * `fetch_active_episode_snapshot(72h)`
   * `fetch_recent_triggers(condition, last_72h)`
   * `knowledge_snippets(condition)`
3. **Pick tips** with `compose_plan(...)`:

   * Avoid duplicates from the last few hours,
   * Prefer tips aligned to observed triggers (e.g., if irregular sleep is present, emphasize routine + short wind-down).
4. **Run `safety_filters()`**:

   * If the user hints at frequent analgesic use, include a **gentle** one-line reminder about medication overuse headaches and to keep usage below common thresholds; avoid specific medical instructions.&#x20;
5. **Generate the response** (tone: kind, brief, practical).

---

## Content grounding (from the Megahandout)

Use as your authoritative source for non-medication guidance highlights:

* **Lifestyle & triggers** to reduce frequency/severity: maintain **regular sleep** and **meals**, manage **stress**, **exercise regularly** with **warm-up**, **avoid/limit triggers** like bright lights, certain foods (e.g., **tyramine/nitrates/MSG**, alcohol/red wine), excessive **caffeine**, dehydration, and environmental changes where possible.&#x20;
* **Migraine diet guidance** (allowed vs avoid lists) when the user asks for food ideas or mentions diet-linked headaches. Emphasize experimentation and tracking, not absolutes.&#x20;
* **Medication-overuse** risk education (brief, neutral) if relevant.&#x20;

---

## Disambiguation & Gaps

* If no episode is active and context is vague, the agent should ask **one** clarifying question (e.g., “Is this about your current headache, or would you like general tips?”) and then proceed.
* If the user requests clinical dosing or prescription guidance, respond with a **gentle limit** and pivot to non-medication strategies.

---

## Acceptance Criteria (MVP)

* For an active migraine episode, the agent produces **one paragraph + ≤2 bullets** that reflect the episode’s latest details and **do not** repeat the same tip within a short window.
* Advice maps to the **handout’s** lifestyle/trigger content and is phrased as *supportive suggestions*, not medical directives.&#x20;
* When recent OTC overuse is implied, the reply includes one neutral sentence about **overuse headaches** and encourages tracking/safer patterns (without dosing).&#x20;
* If insufficient context, asks **one** concise question before advising.

---

## Tiny Example (shape, not verbatim)

* “I’ve updated your migraine entry. Since screens and bright light can aggravate symptoms, try 20–30 minutes in a dark, quiet room, and sip water. If your neck/temple is tight, a warm compress for 10–15 minutes can help you relax.”

  * Bullets:

    * “Short wind-down tonight: consistent bedtime, gentle stretching before sleep.”
    * “If possible, reduce screen brightness and take brief vision breaks.”
      (Lifestyle, light/trigger reduction, sleep regularity. )

---

## Hand-off to Gemini (what to implement)

* Agno **Coach Agent** with `add_history_to_messages=True`.
* Implement the 4 tools above; keep outputs small and deterministic.
* Build a compact **knowledge\_snippets** map from the handout’s lifestyle/trigger/diet sections.&#x20;
* Reuse the Recall/Logger condition ontology and time policies so wording like “head pain” still resolves to migraine family.&#x20;
* Enforce the **one paragraph + ≤2 bullets** rule and run `safety_filters()` last.

That’s it—lean, grounded, and ready for Agno wiring.
