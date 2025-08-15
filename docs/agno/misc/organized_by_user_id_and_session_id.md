---
title: Organized by user ID and session ID
category: misc
source_lines: 23452-23491
line_count: 39
---

# Organized by user ID and session ID
shopping_list = {}


def add_item(agent: Agent, item: str) -> str:
    """Add an item to the current user's shopping list."""
    current_user_id = agent.session_state["current_user_id"]
    current_session_id = agent.session_state["current_session_id"]
    shopping_list.setdefault(current_user_id, {}).setdefault(
        current_session_id, []
    ).append(item)
    return f"Item {item} added to the shopping list"


def remove_item(agent: Agent, item: str) -> str:
    """Remove an item from the current user's shopping list."""
    current_user_id = agent.session_state["current_user_id"]
    current_session_id = agent.session_state["current_session_id"]

    if (
        current_user_id not in shopping_list
        or current_session_id not in shopping_list[current_user_id]
    ):
        return f"No shopping list found for user {current_user_id} and session {current_session_id}"

    if item not in shopping_list[current_user_id][current_session_id]:
        return f"Item '{item}' not found in the shopping list for user {current_user_id} and session {current_session_id}"

    shopping_list[current_user_id][current_session_id].remove(item)
    return f"Item {item} removed from the shopping list"


def get_shopping_list(agent: Agent) -> str:
    """Get the current user's shopping list."""
    current_user_id = agent.session_state["current_user_id"]
    current_session_id = agent.session_state["current_session_id"]
    return f"Shopping list for user {current_user_id} and session {current_session_id}: \n{json.dumps(shopping_list[current_user_id][current_session_id], indent=2)}"


