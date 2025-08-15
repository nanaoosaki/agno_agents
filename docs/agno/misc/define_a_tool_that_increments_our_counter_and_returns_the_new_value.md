---
title: Define a tool that increments our counter and returns the new value
category: misc
source_lines: 34085-34092
line_count: 7
---

# Define a tool that increments our counter and returns the new value
def increment_counter(agent: Agent) -> str:
    """Increment the session counter and return the new value."""
    agent.session_state["count"] += 1
    return f"The count is now {agent.session_state['count']}"


