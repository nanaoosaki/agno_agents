This will be our "North Star" for all subsequent development, including the CoachAgent and the future enhancements you've outlined.

Definitive Implementation Plan (v3.2): The Modular, Stateful Health Companion

This plan formalizes the Layered Architecture and incorporates the best practices from all previous discussions.

1. Core Architectural Philosophy

Layered Architecture: We will strictly adhere to the separation of concerns:

core: Shared, app-wide primitives (ontology, time utils, policies).

data: Storage abstractions and persistence logic.

profile_and_onboarding: Manages static user data.

healthlogger: The workflow for writing dynamic, time-series health events.

health_advisor: The layer for reading and analyzing data to provide insights (Recall & Coach).

Agno Workflows as Orchestrators: Complex, stateful processes like logging and onboarding will be managed by agno.workflow.v2.Workflow.

Agno Agents as Specialists: Simpler, read-only tasks like recall and coaching will be handled by single agno.agent.Agent instances equipped with powerful toolkits.

Deterministic Core: Critical business logic (episode linking, safety checks, data commits) will always be in deterministic Python functions (@tools or workflow steps), not left to LLM interpretation.

Stateful by Design: We will use Agno's workflow_session_state and a per-conversation session_id to manage context and implement advanced features like disambiguation and user confirmation.

2. Finalized File Structure Blueprint

This is the structure we will build towards.

code
Code
download
content_copy
expand_less

agno-chat/
  ├── app.py                      # Gradio UI
  ├── agents.py                   # Main Agent Registry & UI Wrappers
  │
  ├── core/                       # --- SHARED PRIMITIVES ---
  │   ├── __init__.py
  │   ├── ontology.py             # Condition families, normalization rules
  │   ├── timeutils.py            # Timezone handling, date parsing
  │   └── policies.py             # App-wide constants (e.g., 12h window)
  │
  ├── data/                       # --- PERSISTENCE LAYER ---
  │   ├── __init__.py
  │   ├── storage_interface.py    # Defines the abstract Storage API
  │   ├── json_store.py           # Implements the Storage API for JSON files
  │   └── schemas/
  │       ├── episodes.py         # Pydantic models for persisted data
  │       └── ...
  │
  ├── profile_and_onboarding/     # --- PROFILE LAYER ---
  │   ├── __init__.py
  │   ├── workflow.py             # 5-question onboarding Agno workflow
  │   └── storage.py              # CRUD for user_profiles.json
  │
  ├── healthlogger/               # --- DATA CAPTURE LAYER ---
  │   ├── __init__.py
  │   ├── workflow.py             # The 3-step (Extract, Process, Reply) Agno workflow
  │   └── schema.py               # Pydantic models for the Router's output
  │
  └── health_advisor/             # --- INSIGHTS LAYER (Read-Only on logs) ---
      ├── __init__.py
      ├── recall/
      │   ├── agent.py
      │   └── tools.py
      ├── coach/                  # <-- THIS IS WHERE WE WILL BUILD NEXT
      │   ├── agent.py
      │   └── tools.py
      └── knowledge/
          ├── migraine_handout.md
          └── loader.py
3. The Refactor Action Plan (Immediate Next Steps)

Before implementing the CoachAgent, we will perform this minimal, low-risk refactor.

Create Directories: Create the core/, data/, health_advisor/, and profile_and_onboarding/ directories with their __init__.py files.

Centralize Primitives:

Create core/ontology.py and move COND_MAP and _normalize_condition from rules.py into it.

Create core/timeutils.py for any date/time logic.

Delete the old rules.py.

Abstract Storage:

Move the existing storage.py to data/json_store.py.

Create a data/storage_interface.py that defines the function signatures (create_episode, find_latest_open_episode, etc.) as an abstract base class or protocol. This makes it easy to add a SQLiteStore later.

Relocate Modules:

Move the RecallAgent logic (agent.py, tools.py) into health_advisor/recall/.

Move the HealthLoggerAgentV2 logic into healthlogger/workflow.py.

Update Imports: Fix all imports across the moved files to reflect the new structure (e.g., from core.ontology import normalize_condition).

Verify: Run the app and test the Logger and Recall agents thoroughly. They should function identically, but the code is now organized for the future.

4. Coach Agent Implementation Plan (To be done after the refactor)

With the new structure in place, implementing the CoachAgent is clean and logical.

a. Knowledge Ingestion (health_advisor/knowledge/loader.py)

Create the migraine_knowledge_base using agno.knowledge.MarkdownKnowledgeBase.

This module will have a load_knowledge() function that is called once on app startup.

The loaded knowledge base will be imported and used by the Coach's tools.

b. Coach Toolkit (health_advisor/coach/tools.py)

This file will contain the deterministic tools as planned:

fetch_active_episode_snapshot(agent: Agent) -> Optional[dict]: Reads from data.json_store.

get_coaching_snippets(agent: Agent, topic: str) -> List[str]: Queries the migraine_knowledge_base.

apply_safety_guardrails(agent: Agent, proposed_advice: str) -> str: A simple, rule-based filter.

c. Coach Agent (health_advisor/coach/agent.py)

An agno.agent.Agent that uses the toolkit above.

Its instructions will enforce the "Plan -> Fetch -> Synthesize -> Guardrail -> Reply" logic.

It will be stateful via add_history_to_messages=True.

5. Future Enhancements: The "Propose -> Confirm -> Commit" Pattern

Your plan for interactive features like medication tracking and guided exercises is excellent. The new architecture supports this perfectly. Here’s how it will work:

The Proposer: An agent (e.g., the CoachAgent) identifies an opportunity.

The Proposal: Instead of returning a simple text response, the agent's workflow step will return a special StepOutput containing a pending_action object.

The State: The main app.py logic will see this pending_action and store it in Gradio's session state (gr.State).

The UI: The UI will render buttons based on the pending_action options ("Add to Profile", "Not Now").

The Resolver: When a button is clicked, a special message (e.g., /resolve {"action": "profile_add_med", ...}) is sent back to the agent.

The Committer: A dedicated, deterministic tool or workflow step receives this resolved action and safely writes the data to the appropriate store (profile_storage.py or healthlogger/storage.py).

This pattern is robust, secure, and can be reused for every interactive feature you build, from reminders to profile updates. It fits naturally into the health_advisor and profile_and_onboarding layers.

This refined plan provides a clear, scalable, and maintainable path forward. It addresses the immediate need to organize the code before adding the Coach Agent and sets up a robust foundation for all the advanced features you've envisioned.