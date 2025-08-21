from agno.agent import Agent
from agno.models.openai import OpenAIChat

# Defrom agno.agent import Agent
from agno.models.openai import OpenAIChat
# load environment variables
from dotenv import load_dotenv
load_dotenv()
import os

# Define a tool that adds an item to the shopping list
def add_item(agent: Agent, item: str) -> str:
    """Add an item to the shopping list."""
    agent.session_state["shopping_list"].append(item)
    return f"The shopping list is now {agent.session_state['shopping_list']}"


# Create an Agent that maintains state
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini-2024-07-18", api_key=os.getenv("OPENAI_API_KEY")),
    # Initialize the session state with a counter starting at 0
    session_state={"shopping_list": []},
    tools=[add_item],
    # You can use variables from the session state in the instructions
    instructions="Current state (shopping list) is: {shopping_list}",
    # Important: Add the state to the messages
    add_state_in_messages=True,
    markdown=True,
)

# Example usage
agent.print_response("Add milk, eggs, and bread to the shopping list", stream=True)
print(f"Final session state: {agent.session_state}")
#define a tool that adds an item to the shopping list
def add_item(agent: Agent, item: str) -> str:
    """Add an item to the shopping list."""
    agent.session_state["shopping_list"].append(item)
    return f"The shopping list is now {agent.session_state['shopping_list']}"


# Create an Agent that maintains state
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini-2024-07-18", api_key=os.getenv("OPENAI_API_KEY")),
    # Initialize the session state with a counter starting at 0
    session_state={"shopping_list": []},
    tools=[add_item],
    # You can use variables from the session state in the instructions
    instructions="Current state (shopping list) is: {shopping_list}",
    # Important: Add the state to the messages
    add_state_in_messages=True,
    markdown=True,
)

# Example usage
agent.print_response("Add milk, eggs, and bread to the shopping list", stream=True)
print(f"Final session state: {agent.session_state}")