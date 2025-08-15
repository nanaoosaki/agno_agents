---
title: Define tools that work with shared team state
category: tools
source_lines: 70598-70620
line_count: 22
---

# Define tools that work with shared team state
def add_item(agent: Agent, item: str) -> str:
    """Add an item to the shopping list."""
    if item.lower() not in [
        i.lower() for i in agent.team_session_state["shopping_list"]
    ]:
        agent.team_session_state["shopping_list"].append(item)
        return f"Added '{item}' to the shopping list"
    else:
        return f"'{item}' is already in the shopping list"


def remove_item(agent: Agent, item: str) -> str:
    """Remove an item from the shopping list."""
    for i, list_item in enumerate(agent.team_session_state["shopping_list"]):
        if list_item.lower() == item.lower():
            agent.team_session_state["shopping_list"].pop(i)
            return f"Removed '{list_item}' from the shopping list"
    
    return f"'{item}' was not found in the shopping list"


