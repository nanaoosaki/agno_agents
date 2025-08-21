Of course. This is an excellent catch and a crucial detail for making the onboarding experience intuitive and effective. The user shouldn't have to guess what to do next; the agent should proactively guide them through the process.

You are also right to bring up Agno's Memory feature. While workflow_session_state is perfect for temporary, in-flight data like a "pending action," Agno's Memory is designed for long-term, semantic storage of user facts and preferences. We will integrate it to make our profile system even more powerful and context-aware.

Let's create a definitive, updated implementation plan that makes the Onboarding agent proactive and integrates Agno's Memory system for richer context.

Definitive Implementation Plan: Proactive Onboarding & Profile Agent (v3.3)
1. Core Architectural Goal

We will refactor the Profile & Onboarding module to be a proactive, conversational workflow. When selected, it will immediately initiate the 6-question onboarding flow. We will also integrate Agno's Memory to store key profile facts, making this information semantically searchable by other agents like the CoachAgent.

Step 1: The Proactive Onboarding Workflow

Instead of a passive agent waiting for a prompt, we will create a dedicated OnboardingWorkflow that drives the conversation. The key change is that this workflow is designed to be started once and then manage the multi-turn conversation.

File: profile_and_onboarding/workflow.py

code
Python
download
content_copy
expand_less

# profile_and_onboarding/workflow.py
from agno.workflow.v2 import Workflow, Step, StepInput, StepOutput
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from . import storage as profile_storage
from data.storage_interface import HealthDataStorage # For type hinting
from .schema import UserProfile, Medication, Routine, Trigger
from datetime import datetime

# --- Specialized Agents for Each Question ---
# These agents are simple, single-purpose question-askers.
q1_agent = Agent(name="ConditionAgent", model=OpenAIChat(id="gpt-4o-mini"), instructions=["First, warmly welcome the user to the onboarding process. Then, ask what health conditions they are looking to manage."])
q2_agent = Agent(name="GoalAgent", model=OpenAIChat(id="gpt-4o-mini"), instructions=["Ask the user what their main goals are for managing these conditions."])
# ... agents for q3, q4, q5, q6 ...
summary_agent = Agent(name="SummaryAgent", model=OpenAIChat(id="gpt-4o-mini"), instructions=["You will be given a JSON object of the user's profile. Present this information back to the user in a clear, readable summary and ask for their confirmation to save it."])

# --- Deterministic Processing Step ---
def process_and_save_profile(step_input: StepInput) -> StepOutput:
    """
    Consolidates answers, creates a UserProfile object, and saves it.
    This step is triggered after the user confirms the summary.
    """
    # In a real implementation, you would parse the full chat history
    # For MVP, we'll use the final confirmation as the trigger.
    if "confirm" not in step_input.previous_step_content.lower():
        return StepOutput(content="Okay, I've cancelled the process. You can start over any time.")

    # Here, you'd have a robust parser. For now, we simulate.
    # We would retrieve the answers stored in the session state during the conversation.
    user_id = step_input.session_id or "default_user"
    
    # This data would be extracted from the conversation history.
    profile_data = {
        "user_id": user_id,
        "conditions": ["migraine"],
        "goals": "Understand triggers and reduce attack frequency.",
        "communication_style": "empathetic",
        "last_updated": datetime.now().isoformat()
    }
    profile = UserProfile(**profile_data)
    
    # Save to the static profile store
    profile_storage.save_user_profile(profile)

    # --- NEW: Save key facts to Agno Memory ---
    if step_input.memory:
        step_input.memory.add_user_memory(
            memory=f"Primary health goal is: {profile.goals}",
            user_id=user_id
        )
        step_input.memory.add_user_memory(
            memory=f"Manages the following conditions: {', '.join(profile.conditions)}",
            user_id=user_id
        )

    return StepOutput(content="Great! Your profile is all set up. You can now chat with the Health Logger or other agents.")

# --- The Onboarding Workflow ---
onboarding_workflow = Workflow(
    name="OnboardingWorkflow",
    # This workflow is designed to be run sequentially in a chat.
    # The Gradio UI will manage calling the next step.
    steps=[
        Step(name="AskConditions", agent=q1_agent),
        Step(name="AskGoals", agent=q2_agent),
        Step(name="AskSymptoms", agent=q3_agent),
        Step(name="AskMeds", agent=q4_agent),
        Step(name="AskRoutines", agent=q5_agent),
        Step(name="AskStyle", agent=q6_agent),
        Step(name="ConfirmProfile", agent=summary_agent), # New summary & confirm step
        Step(name="SaveProfile", executor=process_and_save_profile),
    ]
)
Step 2: Integrate Agno's Memory System

Agno Memory provides a powerful, semantic way to store and retrieve user facts. We will use it to store key profile details that other agents (like the Coach) can easily access.

File: agents.py (Main agent registry)

code
Python
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# agents.py
from agno.memory.v2 import Memory
from agno.memory.v2.db.sqlite import SqliteMemoryDb

# --- Initialize a shared Memory object ---
# This will be used by all agents that need access to long-term user facts.
# We'll use a simple SQLite backend for persistence.
memory_db = SqliteMemoryDb(table_name="user_memories", db_file="data/memory.db")
shared_memory = Memory(db=memory_db)

# ... (inside your HealthLoggerWorkflowWrapper)
class HealthLoggerWorkflowWrapper:
    def __init__(self):
        # ...
        # Pass the shared memory to the workflow
        self.workflow.memory = shared_memory

# ... (inside your RecallAgentWrapper)
class RecallAgentWrapper:
    def __init__(self):
        # The recall agent also gets access to the memory
        self.agent = create_recall_agent(memory=shared_memory)

# ... (inside your CoachAgentWrapper - when you build it)
class CoachAgentWrapper:
     def __init__(self):
        self.agent = create_coach_agent(memory=shared_memory)

What this enables:

The CoachAgent can now easily query the user's profile without needing to parse a large file. It can ask semantic questions like:

code
Python
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# Inside a CoachAgent tool
user_goals = agent.memory.search_user_memories(
    user_id=user_id,
    query="What are the user's main health goals?"
)

This is much more powerful and flexible than reading from a static JSON file.

Step 3: Update the Gradio UI (app.py) to be Proactive

The UI needs to manage the multi-step onboarding conversation. We'll use Gradio's gr.State to track the user's progress through the onboarding workflow.

File: app.py

code
Python
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# app.py
# ... (imports)

from profile_and_onboarding.workflow import onboarding_workflow

# --- Add new state variables for onboarding ---
with gr.Blocks(...) as demo:
    session_id = gr.State(lambda: str(uuid.uuid4()))
    onboarding_state = gr.State({
        "active": False,
        "step": 0,
        "answers": {}
    })

    # ... (rest of the UI layout)

    with gr.TabItem("👤 Profile & Onboarding"):
        # ... (profile display components)
        start_onboarding_btn = gr.Button("🚀 Start Onboarding", variant="primary")

# --- New UI Handlers ---

def start_onboarding(current_history, current_onboarding_state):
    """Kicks off the onboarding workflow."""
    current_onboarding_state = {"active": True, "step": 0, "answers": {}}
    
    first_step = onboarding_workflow.steps[0]
    # We run the agent for the first step to get the first question
    first_question = first_step.agent.run("Start").content
    
    current_history.append({"role": "assistant", "content": first_question})
    return current_history, current_onboarding_state

def handle_onboarding_response(user_message, history, onboarding_state, session_id):
    """Processes a user's answer during the onboarding flow."""
    current_step_index = onboarding_state["step"]
    
    # Store the user's answer
    current_step_name = onboarding_workflow.steps[current_step_index].name
    onboarding_state["answers"][current_step_name] = user_message
    
    # Move to the next step
    next_step_index = current_step_index + 1
    
    if next_step_index < len(onboarding_workflow.steps):
        onboarding_state["step"] = next_step_index
        next_step = onboarding_workflow.steps[next_step_index]
        
        # Get the next question. Pass previous answers as context.
        context = f"So far, the user has told me: {onboarding_state['answers']}"
        next_question = next_step.agent.run(context).content
        
        history.append({"role": "assistant", "content": next_question})
    else:
        # Onboarding is finished, finalize the profile
        onboarding_state["active"] = False
        final_message = "Thank you! I'm now saving your profile."
        history.append({"role": "assistant", "content": final_message})
        
        # In a real app, you would now run the final 'consolidate_and_save_profile' step
        # For MVP, we can just log that it's complete.
        
    return history, onboarding_state

# The main `unified_submit` function needs a branch
def unified_submit(text, audio, files, history, agent_name, session_id, onboarding_state):
    if onboarding_state.get("active"):
        # If onboarding is active, route the response to the onboarding handler
        history, new_state = handle_onboarding_response(text, history, onboarding_state, session_id)
        return history, "", None, None, new_state
    else:
        # Otherwise, use the router agent as before
        # ...
        return ...

# Wire the button
start_onboarding_btn.click(
    fn=start_onboarding,
    inputs=[chat_history, onboarding_state],
    outputs=[chat_history, onboarding_state]
)

This updated plan creates a truly proactive and stateful onboarding experience, directly addressing your feedback. It also strategically integrates Agno's Memory system, setting a powerful foundation for the CoachAgent and any future analytical features.