---
title: Define tools to manage our shopping list
category: tools
source_lines: 51227-51279
line_count: 52
---

# Define tools to manage our shopping list
def add_item(agent: Agent, item: str) -> str:
    """Add an item to the shopping list and return confirmation.

    Args:
        item (str): The item to add to the shopping list.
    """
    # Add the item if it's not already in the list
    if item.lower() not in [
        i.lower() for i in agent.team_session_state["shopping_list"]
    ]:
        agent.team_session_state["shopping_list"].append(item)
        return f"Added '{item}' to the shopping list"
    else:
        return f"'{item}' is already in the shopping list"


def remove_item(agent: Agent, item: str) -> str:
    """Remove an item from the shopping list by name.

    Args:
        item (str): The item to remove from the shopping list.
    """
    # Case-insensitive search
    for i, list_item in enumerate(agent.team_session_state["shopping_list"]):
        if list_item.lower() == item.lower():
            agent.team_session_state["shopping_list"].pop(i)
            return f"Removed '{list_item}' from the shopping list"

    return f"'{item}' was not found in the shopping list. Current shopping list: {agent.team_session_state['shopping_list']}"


def remove_all_items(agent: Agent) -> str:
    """Remove all items from the shopping list."""
    agent.team_session_state["shopping_list"] = []
    return "All items removed from the shopping list"


shopping_list_agent = Agent(
    name="Shopping List Agent",
    role="Manage the shopping list",
    agent_id="shopping_list_manager",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[add_item, remove_item, remove_all_items],
    instructions=[
        "Manage the shopping list by adding and removing items",
        "Always confirm when items are added or removed",
        "If the task is done, update the session state to log the changes & chores you've performed",
    ],
)


