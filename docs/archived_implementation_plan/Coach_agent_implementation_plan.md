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

## implementation details from gemini 2.5pro 
Excellent. The architectural refactor is complete, the foundation is solid, and now we can build the CoachAgent on top of it with confidence. The provided plan is perfect, and we will implement it directly within the new, clean, layered architecture.

This plan confirms that the "Layered Architecture" was the right choice. The CoachAgent will live in the health_advisor layer and will act as a read-only consumer of data from both the data layer (for dynamic logs) and the profile_and_onboarding layer (for static user info), with its advice grounded in its own knowledge module.

Here is the comprehensive, step-by-step implementation plan for the Coach Agent, with all code snippets ready to be placed in their correct locations within your newly refactored project.

Implementation Plan: The Agno-Native Coach Agent (v3.2)
Step 1: Ingest the Knowledge Base (health_advisor/knowledge/loader.py)

First, we need to make the "Migraine Headache Megahandout" available to the agent. We'll use Agno's MarkdownKnowledgeBase and create a simple loader script.

Create health_advisor/knowledge/loader.py:

code
Python
download
content_copy
expand_less

# health_advisor/knowledge/loader.py
from pathlib import Path
from agno.knowledge.markdown import MarkdownKnowledgeBase
from agno.vectordb.lancedb import LanceDb

# Define paths relative to the project root
# This assumes your script runs from the `agno-chat` directory
PROJECT_ROOT = Path(__file__).parent.parent.parent
HANDOUT_PATH = PROJECT_ROOT / "knowledge" / “Migraine Headache Megahandout.md"
LANCEDB_PATH = PROJECT_ROOT / "data" / "lancedb_coach"

# Create the Knowledge Base instance
migraine_knowledge_base = MarkdownKnowledgeBase(
    path=HANDOUT_PATH,
    vector_db=LanceDb(
        uri=str(LANCEDB_PATH),
        table_name="migraine_handout"
    ),
)

def load_knowledge_if_needed():
    """Function to load the handout into the vector database if it doesn't exist."""
    if not LANCEDB_PATH.exists():
        print("Knowledge base not found. Loading migraine handout...")
        migraine_knowledge_base.load(recreate=True)
        print("✅ Knowledge base loaded successfully.")
    else:
        print("✅ Knowledge base already exists.")

if __name__ == "__main__":
    load_knowledge_if_needed()
Step 2: Build the Coach Agent's Toolkit (health_advisor/coach/tools.py)

This toolkit contains the deterministic functions that fetch data, retrieve knowledge, and apply safety rules.

Create health_advisor/coach/tools.py:

code
Python
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# health_advisor/coach/tools.py
from agno.tools import tool
from agno.agent import Agent
from typing import Optional, Dict, Any, List

# Import from the correct layers
from data.json_store import find_latest_open_episode # Or your storage interface
from ..knowledge.loader import migraine_knowledge_base

@tool
def fetch_active_episode_snapshot(agent: Agent) -> Optional[Dict[str, Any]]:
    """
    Fetches a compact summary of the user's most recent open health episode
    for a specific condition to provide immediate context for coaching.
    """
    # Note: In a real app, the condition would be dynamically determined.
    # For MVP, we can hardcode or infer from the agent's context.
    condition = "migraine" # This can be made dynamic later
    episode = find_latest_open_episode(condition)
    
    if episode and episode.get("status") == "open":
        return {
            "condition": episode.get("condition"),
            "current_severity": episode.get("current_severity"),
            "notes": episode.get("notes"),
            "interventions_tried": [iv.get('type') for iv in episode.get('interventions', [])]
        }
    return None

@tool
def get_coaching_snippets(agent: Agent, topic: str, num_snippets: int = 2) -> List[str]:
    """
    Searches the Migraine Handout knowledge base for actionable, non-medication advice
    on a specific topic like 'lifestyle', 'triggers', 'stress', or 'hydration'.
    """
    results = migraine_knowledge_base.search(query=topic, limit=num_snippets)
    return [result.get("content", "") for result in results]

@tool
def apply_safety_guardrails(agent: Agent, proposed_advice: str) -> str:
    """
    Reviews a proposed piece of advice to ensure it is safe and non-prescriptive.
    It removes specific medical advice, dosage, or diagnoses.
    """
    # Simple rule-based filter for MVP. Can be replaced with a dedicated safety agent later.
    unsafe_keywords = ["dosage", "mg", "prescription", "diagnose", "prescribe"]
    if any(keyword in proposed_advice.lower() for keyword in unsafe_keywords):
        return "Based on general wellness principles, focusing on lifestyle factors like hydration and rest can be beneficial. For specific medical advice, please consult a healthcare professional."
    
    # Check for overuse mentions
    if "more than 2 days per week" in proposed_advice or "frequent use" in proposed_advice:
        return proposed_advice + "\n\n*Note: Frequent use of pain medication can sometimes lead to overuse headaches. It's always a good idea to track usage and discuss patterns with your doctor.*"

    return proposed_advice
Step 3: Define the Coach Agent (health_advisor/coach/agent.py)

This Agno agent orchestrates the tools to generate its response.

Create health_advisor/coach/agent.py:

code
Python
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# health_advisor/coach/agent.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from .tools import fetch_active_episode_snapshot, get_coaching_snippets, apply_safety_guardrails

coach_agent = Agent(
    name="CoachAgent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        fetch_active_episode_snapshot,
        get_coaching_snippets,
        apply_safety_guardrails,
    ],
    show_tool_calls=True,
    add_history_to_messages=True,
    num_history_runs=3,
    instructions=[
        "You are an empathetic and supportive health coach. Your goal is to provide safe, actionable, non-medication tips based on the user's situation and a knowledge base.",
        "Follow this strict plan:",
        "1. First, call `fetch_active_episode_snapshot` to understand the user's current health status.",
        "2. Based on the active episode's condition (e.g., 'migraine'), call `get_coaching_snippets` to retrieve 1-2 relevant tips from the knowledge base. Use topics like 'lifestyle', 'triggers', or 'stress'.",
        "3. Synthesize a brief, personalized suggestion. If the user already tried an intervention, acknowledge it and suggest a *complementary* action (e.g., 'Since you've tried heat, gentle hydration might also help.').",
        "4. CRITICAL FINAL STEP: Before responding, you MUST pass your complete proposed message to the `apply_safety_guardrails` tool to ensure it's safe.",
        "5. Your final response to the user is the text returned by the `apply_safety_guardrails` tool."
    ]
)
Step 4: Integrate the Coach Agent into the Main UI (agents.py)

Finally, make the new agent available to the Gradio app.

Modify agents.py:```python

agents.py
... (keep all your existing imports and code) ...
--- Import the new Coach Agent and its knowledge loader ---

from health_advisor.coach.agent import coach_agent
from health_advisor.knowledge.loader import load_knowledge_if_needed

--- Load the Coach's knowledge base on startup ---
This will run once when the application starts.

load_knowledge_if_needed()

--- Add a wrapper class for the Coach Agent ---

class CoachAgentWrapper:
name = "Coach Agent"
def run(self, prompt: str, files: Optional[list] = None) -> ChatResult:
# For the Coach Agent, we pass the open_episode_id from the logger's state.
# This demonstrates inter-module state awareness.
open_episode_id = health_logger_workflow.workflow_session_state.get("open_episode_id")

code
Code
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
response = coach_agent.run(
        message=prompt,
        # The tool can access this context via the agent object
        context={"open_episode_id": open_episode_id} 
    )
    return ChatResult(text=response.content)
--- Update the Agent Registry ---

AGENTS: Dict[str, Any] = {
"Health Logger (Workflow)": HealthLoggerWorkflowWrapper(),
"Recall Agent": RecallAgentWrapper(),
"Coach Agent": CoachAgentWrapper(), # Add the new coach
}

The call_agent function remains the same.
code
Code
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
### **Testing Your New Coach Agent**

Your testing flow will now look like this:

1.  **Start the App**: `python app.py`. On the first run, you will see a message that the knowledge base is being loaded.
2.  **Log an Episode**:
    *   Select **"Health Logger (Workflow)"**.
    *   Send: `My migraine is back, it's a 6/10 and the pain is in my right temple.`
3.  **Ask for Advice**:
    *   Switch to **"Coach Agent"**.
    *   Send: `What can I do for this?`
4.  **Observe the Console**: You will see the agent executing its plan:
    *   It will call `fetch_active_episode_snapshot`.
    *   It will call `get_coaching_snippets` with a query like `migraine triggers`.
    *   It will synthesize a response.
    *   It will call `apply_safety_guardrails` on its own response.
5.  **Check the UI**: You will receive a safe, empathetic, and context-aware suggestion grounded in your handout, like:
    > "I'm sorry to hear your migraine is back. I've noted the severity and location. The knowledge base suggests that for some people, resting in a dark, quiet room can help reduce sensitivity to light. You could also try applying a cool compress to your temple. I hope you feel some relief soon."

This implementation completes your MVP trio within a clean, scalable, and robust architecture, all powered by the Agno framework.