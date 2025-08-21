Revised Implementation Plan (v3.3): The "Stateful & Intelligent" Orchestrator

This plan refines the MasterAgent into a more sophisticated orchestrator that handles multi-intent turns, manages conversational state, and uses confidence thresholds for safer routing.

Step 1: Enhance the Router's Schema and Logic

The router needs to become more expressive. We'll expand its Pydantic model to handle multiple intents and control messages.

Update health_advisor/router/schema.py:

code
Python
download
content_copy
expand_less

# health_advisor/router/schema.py
from pydantic import BaseModel, Field
from typing import List, Literal, Optional

class RouterDecision(BaseModel):
    """The structured output from the Router Agent."""
    primary_intent: Literal["log", "recall", "coach", "clarify_response", "control_action", "unknown"] = Field(
        ...,
        description="The primary intent of the user's message."
    )
    secondary_intent: Optional[Literal["log", "recall", "coach"]] = Field(
        None,
        description="A secondary intent if the user's message contains multiple requests (e.g., logging and then asking for advice)."
    )
    confidence: float = Field(
        ...,
        description="The confidence of the primary intent classification (0.0 to 1.0)."
    )
    rationale: str = Field(
        ...,
        description="A brief explanation for the chosen primary intent."
    )

Update health_advisor/router/agent.py Instructions:
The router_agent's instructions will be updated to recognize these new intents and the concept of a secondary intent.

code
Python
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# In health_advisor/router/agent.py
# ...
instructions=[
    "You are an intent classification router for a health chatbot.",
    "Your job is to analyze the user's LATEST message in the context of the conversation and the current `workflow_session_state` to determine their primary and secondary intents.",
    "Possible intents: 'log', 'recall', 'coach', 'clarify_response', 'control_action', 'unknown'.",
    "- 'log': User is providing new health information. THIS IS THE DEFAULT.",
    "- 'recall': User is asking about their past data.",
    "- 'coach': User is asking for advice or help.",
    "- 'clarify_response': User is answering a clarifying question you asked.",
    "- 'control_action': The message is a system command like '/resolve'.",
    "If a message contains two actions (e.g., 'I have a migraine, what should I do?'), set `primary_intent` to 'log' and `secondary_intent` to 'coach'.",
    "You must return your decision in the structured RouterDecision JSON format."
]
Step 2: Implement the Stateful MasterAgent in agents.py

The MasterAgent will now be a stateful class that orchestrates the entire user interaction, including handling control messages and multi-intent requests.

Modify agents.py:

code
Python
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# agents.py
# ... (imports) ...

# --- Instantiate all specialist agents ---
logger_workflow = HealthLoggerWorkflowWrapper()
recall_specialist = RecallAgentWrapper()
coach_specialist = CoachAgentWrapper()

# --- THE NEW, STATEFUL MASTER ORCHESTRATOR ---
class MasterAgent:
    name = "Health Companion"

    def run(self, prompt: str, files: Optional[list] = None) -> ChatResult:
        print(f"\n--- MasterAgent: Routing user prompt: '{prompt}' ---")
        
        # In a real app, session_id would be managed per user conversation.
        # We use a fixed one here for simplicity.
        session_id = "user_main_session"

        # 1. HANDLE CONTROL MESSAGES & PENDING ACTIONS (SHORT-CIRCUIT)
        # We need access to the session state to check for pending actions.
        # Let's assume our wrappers can expose this.
        # For simplicity in this plan, we'll imagine a helper.
        # pending_action = get_session_state(session_id).get("pending_action")
        # if prompt.startswith("/resolve") and pending_action:
        #     print("--> Handling resolved action directly.")
        #     # Logic to call the correct commit step (e.g., from the CoachAgent)
        #     # This bypasses the router entirely.
        #     return coach_specialist.commit_action(prompt, files, session_id)

        # 2. GET ROUTING DECISION (STATE-AWARE)
        # We would pass the current state (e.g., open episodes) to the router.
        # router_context = {"open_episode": get_session_state(session_id).get("open_episode_id")}
        router_response = router_agent.run(prompt, session_id=session_id) # Pass session_id for history
        
        if not isinstance(router_response.content, RouterDecision):
            print("⚠️ Router agent failed. Defaulting to logger.")
            return logger_workflow.run(prompt, files, session_id=session_id)

        decision: RouterDecision = router_response.content
        print(f"🧠 Router Decision: Primary='{decision.primary_intent}', Secondary='{decision.secondary_intent}', Confidence={decision.confidence:.2f}")

        # 3. APPLY CONFIDENCE THRESHOLDS & HEURISTICS
        final_intent = decision.primary_intent
        if decision.confidence < 0.7:
            # Simple heuristic fallback
            if any(word in prompt.lower() for word in ["when", "did i", "show me"]):
                final_intent = "recall"
            elif any(word in prompt.lower() for word in ["what should i do", "help"]):
                final_intent = "coach"
            print(f"Confidence low, applying heuristic. Final intent: '{final_intent}'")

        # 4. EXECUTE THE WORKFLOW (potentially multi-step)
        primary_result = None
        if final_intent == "recall":
            print("--> Routing to Recall Specialist")
            primary_result = recall_specialist.run(prompt, files, session_id=session_id)
        
        elif final_intent == "coach":
            print("--> Routing to Coach Specialist")
            primary_result = coach_specialist.run(prompt, files, session_id=session_id)
        
        else: # Default to logger
            print("--> Routing to Logger Workflow")
            primary_result = logger_workflow.run(prompt, files, session_id=session_id)

        # 5. HANDLE SECONDARY INTENT (CHAINING)
        if decision.secondary_intent and primary_result:
            print(f"--- Handling secondary intent: '{decision.secondary_intent}' ---")
            # The context from the first action is now in the session history.
            # The next agent will see it automatically.
            if decision.secondary_intent == "coach":
                print("--> Chaining to Coach Specialist")
                secondary_result = coach_specialist.run(
                    "Given what I just told you, what should I do?", 
                    files=None, 
                    session_id=session_id
                )
                # Combine the results
                combined_text = f"{primary_result.text}\n\n{secondary_result.text}"
                return ChatResult(text=combined_text)
        
        return primary_result

# --- AGENT REGISTRY & UI ---
# The rest of agents.py and app.py remains the same: the UI will have the
# "Health Companion (Auto-Router)" as the default, with specialists available for testing.
How This Plan Addresses the Gaps

Expanded Router Contract: The RouterDecision schema now supports primary_intent and secondary_intent, allowing the Master Agent to handle multi-intent turns like "I have a migraine, what should I do?".

Confidence Thresholds: The MasterAgent now includes a simple confidence check and heuristic fallback, making the routing more robust.

State-Aware Routing: By passing the session_id to the router_agent and enabling add_history_to_messages, the router gains crucial context about the ongoing conversation, preventing it from misclassifying follow-up messages.

Control Message Handling: The plan outlines where to add the logic to short-circuit the router for control messages like /resolve (though the implementation is stubbed for brevity).

Context Chaining: The plan for handling secondary intents ensures that the output of one agent (e.g., the logger's confirmation) becomes context for the next (e.g., the coach), leading to more natural, chained interactions.

Shared Primitives: The recommendation to create a core/ module is excellent and should be followed. All agents and workflows will import from this single source of truth for ontology and policies.

UI for Testing: The plan to keep the specialist agents in the dropdown for debugging while defaulting to the orchestrator for the user is the best of both worlds.

This revised architecture is significantly more intelligent and robust. It directly incorporates the advanced suggestions, creating a system that is not only functional but also maintainable and prepared for future complexity.