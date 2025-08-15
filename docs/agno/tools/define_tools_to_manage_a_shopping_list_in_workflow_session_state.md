---
title: Define tools to manage a shopping list in workflow session state
category: tools
source_lines: 85055-85126
line_count: 71
---

# Define tools to manage a shopping list in workflow session state
def add_item(agent: Agent, item: str) -> str:
    """Add an item to the shopping list in workflow session state.

    Args:
        item (str): The item to add to the shopping list
    """
    if agent.workflow_session_state is None:
        agent.workflow_session_state = {}

    if "shopping_list" not in agent.workflow_session_state:
        agent.workflow_session_state["shopping_list"] = []

    # Check if item already exists (case-insensitive)
    existing_items = [
        existing_item.lower()
        for existing_item in agent.workflow_session_state["shopping_list"]
    ]
    if item.lower() not in existing_items:
        agent.workflow_session_state["shopping_list"].append(item)
        return f"Added '{item}' to the shopping list."
    else:
        return f"'{item}' is already in the shopping list."


def remove_item(agent: Agent, item: str) -> str:
    """Remove an item from the shopping list in workflow session state.

    Args:
        item (str): The item to remove from the shopping list
    """
    if agent.workflow_session_state is None:
        agent.workflow_session_state = {}

    if "shopping_list" not in agent.workflow_session_state:
        agent.workflow_session_state["shopping_list"] = []
        return f"Shopping list is empty. Cannot remove '{item}'."

    # Find and remove item (case-insensitive)
    shopping_list = agent.workflow_session_state["shopping_list"]
    for i, existing_item in enumerate(shopping_list):
        if existing_item.lower() == item.lower():
            removed_item = shopping_list.pop(i)
            return f"Removed '{removed_item}' from the shopping list."

    return f"'{item}' not found in the shopping list."


def remove_all_items(agent: Agent) -> str:
    """Remove all items from the shopping list in workflow session state."""
    if agent.workflow_session_state is None:
        agent.workflow_session_state = {}

    agent.workflow_session_state["shopping_list"] = []
    return "Removed all items from the shopping list."


def list_items(agent: Agent) -> str:
    """List all items in the shopping list from workflow session state."""
    if (
        agent.workflow_session_state is None
        or "shopping_list" not in agent.workflow_session_state
        or not agent.workflow_session_state["shopping_list"]
    ):
        return "Shopping list is empty."

    items = agent.workflow_session_state["shopping_list"]
    items_str = "\n".join([f"- {item}" for item in items])
    return f"Shopping list:\n{items_str}"


