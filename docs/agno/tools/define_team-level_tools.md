---
title: Define team-level tools
category: tools
source_lines: 70629-70652
line_count: 23
---

# Define team-level tools
def list_items(team: Team) -> str:
    """List all items in the shopping list."""
    # Access shared state (not private state)
    shopping_list = team.team_session_state["shopping_list"]
    
    if not shopping_list:
        return "The shopping list is empty."
    
    items_text = "\n".join([f"- {item}" for item in shopping_list])
    return f"Current shopping list:\n{items_text}"


def add_chore(team: Team, chore: str) -> str:
    """Add a completed chore to the team's private log."""
    # Access team's private state
    if "chores" not in team.session_state:
        team.session_state["chores"] = []
    
    team.session_state["chores"].append(chore)
    return f"Logged chore: {chore}"


