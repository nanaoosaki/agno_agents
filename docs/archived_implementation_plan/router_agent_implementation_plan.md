The solution is to create a Master Orchestrator Agent. This will be the single, default agent the user interacts with. Internally, this orchestrator will use the lightweight RouterAgent you've conceptualized to classify the user's intent and then delegate the task to the correct specialist (Logger, Recall, or Coach).

This approach gives you the best of both worlds:

For the User: A single, intelligent Health Companion.

For the Developer: We keep the specialist agents (Logger, Recall, Coach) modular and separate, making them easy to test, maintain, and enhance individually. We can still keep the dropdown in our Gradio UI for development/testing purposes, but the default option will be the Master Orchestrator.

Here is the definitive implementation plan to build this orchestration layer.

Implementation Plan: The Master Orchestrator Agent
Step 1: Create the Router Agent and its Schema

This component is the "brain" of the orchestrator. Its only job is to classify intent.

Create health_advisor/router/schema.py:

code
Python
download
content_copy
expand_less

# health_advisor/router/schema.py
from pydantic import BaseModel, Field
from typing import Literal

class RouterDecision(BaseModel):
    """The structured output from the Router Agent."""
    intent: Literal["log", "recall", "coach", "unknown"] = Field(
        ...,
        description="Classified intent. 'log' for new data, 'recall' for history questions, 'coach' for advice."
    )
    confidence: float = Field(
        ...,
        description="Confidence of the classification (0.0 to 1.0)."
    )
    rationale: str = Field(
        ...,
        description="Brief explanation for the chosen intent."
    )

Create health_advisor/router/agent.py:

code
Python
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# health_advisor/router/agent.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from .schema import RouterDecision

router_agent = Agent(
    name="IntentRouterAgent",
    model=OpenAIChat(id="gpt-4o-mini"),
    response_model=RouterDecision,
    add_history_to_messages=True,
    num_history_runs=3,
    instructions=[
        "You are an intent classification router for a health chatbot.",
        "Your job is to analyze the user's LATEST message in the context of the conversation and determine their primary intent: 'log', 'recall', or 'coach'.",
        "- Use 'log' if the user is providing new health information, symptoms, or actions (e.g., 'I have a headache', 'My sleep was bad'). This is the most common intent.",
        "- Use 'recall' if the user is asking a question about their past data (e.g., 'When was my last...', 'Did I ever...', 'Show me...').",
        "- Use 'coach' if the user is asking for advice, help, or suggestions (e.g., 'What should I do?', 'How can I relieve this?').",
        "You must return your decision in the structured RouterDecision JSON format."
    ]
)
Step 2: Create the Master Orchestrator Logic in the Main agents.py

This is where we tie everything together. The MasterAgent is not an LLM agent itself; it's a pure Python class that uses other agents.

Modify agents.py:

code
Python
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# agents.py
# ... (all your existing imports) ...

# --- Import all the necessary components ---
from healthlogger.workflow import HealthLoggerWorkflowWrapper
from health_advisor.recall.agent import RecallAgentWrapper
from health_advisor.coach.agent import CoachAgentWrapper
from health_advisor.router.agent import router_agent
from health_advisor.router.schema import RouterDecision

# --- Instantiate our specialist agents (we'll call them internally) ---
logger_specialist = HealthLoggerWorkflowWrapper()
recall_specialist = RecallAgentWrapper()
coach_specialist = CoachAgentWrapper()

# --- THE NEW MASTER ORCHESTRATOR AGENT ---
class MasterAgent:
    """
    The single entry point for the UI. It routes requests to the correct specialist.
    """
    name = "Health Companion"

    def run(self, prompt: str, files: Optional[list] = None) -> ChatResult:
        print(f"\n--- MasterAgent: Routing user prompt: '{prompt}' ---")
        
        # 1. Get the routing decision from the Router Agent
        router_response = router_agent.run(prompt)
        
        if not isinstance(router_response.content, RouterDecision):
            print("⚠️ Router agent failed. Defaulting to logger.")
            return logger_specialist.run(prompt, files)

        decision: RouterDecision = router_response.content
        print(f"🧠 Router Decision: Intent='{decision.intent}', Confidence={decision.confidence:.2f}")

        # 2. Execute the chosen specialist agent based on the decision
        if decision.intent == "recall":
            print("--> Routing to Recall Specialist")
            return recall_specialist.run(prompt, files)
        elif decision.intent == "coach":
            print("--> Routing to Coach Specialist")
            return coach_specialist.run(prompt, files)
        else: # Default to the logger for 'log' or 'unknown' intents
            print("--> Routing to Logger Specialist")
            return logger_specialist.run(prompt, files)

# --- UPDATE THE AGENT REGISTRY ---
# The UI will now have the MasterAgent as the primary option,
# but we keep the specialists for easy testing.
AGENTS: Dict[str, Any] = {
    "Health Companion (Auto-Router)": MasterAgent(),
    "--- (Testing Only) ---": None, # This acts as a separator in the UI
    "Health Logger (Workflow)": logger_specialist,
    "Recall Agent": recall_specialist,
    "Coach Agent": coach_specialist,
}

# The call_agent function remains the same.
def call_agent(agent_name: str, user_text: str, filepaths: Optional[List[str]]) -> ChatResult:
    agent = AGENTS.get(agent_name)
    if not agent:
        return ChatResult(text=f"Separator selected. Please choose an agent.")
    return agent.run(user_text, files=filepaths)
Step 3: Update the Gradio UI (app.py)

The change is minimal. We just need to ensure the default agent in the dropdown is our new MasterAgent. The user no longer needs to think, but the developer still can for testing.

Modify app.py:

code
Python
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# app.py
# ... (imports and functions)

# --- Gradio UI Layout ---
with gr.Blocks(title="Agno Health Companion") as demo:
    gr.Markdown("## Health Companion")
    
    with gr.Row():
        # The dropdown now defaults to the MasterAgent, but still allows selecting specialists for testing.
        agent_name = gr.Dropdown(
            choices=list(AGENTS.keys()),
            value="Health Companion (Auto-Router)", # <-- Set the default
            label="Select Agent (Default is Auto-Router)"
        )
        clear_btn = gr.Button("Clear Chat")

    # ... (the rest of your UI layout and event handlers remain exactly the same)
The Final User and Developer Experience

For the User: They will launch the app, see "Health Companion (Auto-Router)" pre-selected, and start chatting. They will never need to touch the dropdown. The agent will intelligently log, recall, or coach based on the conversation, providing a seamless experience.

For You (The Developer): When you need to test the CoachAgent's logic in isolation, you can simply select "Coach Agent" from the dropdown and interact with it directly, bypassing the router. This is incredibly powerful for debugging and iterating on individual components.

This plan achieves both of your goals perfectly. It provides the intelligent, unified experience the user needs while preserving the modularity and testability that you, the developer, require.