---
title: Team State
category: misc
source_lines: 70530-70598
line_count: 68
---

# Team State
Source: https://docs.agno.com/teams/shared-state

Learn about the shared state of Agent Teams.

There are multiple ways to share state between team members.

## Shared Team State

Team Session State enables sophisticated state management across teams of agents, with both shared and private state capabilities.

Teams often need to coordinate on shared information (like a shopping list) while maintaining their own private metrics or configuration. Agno provides an elegant three-tier state system for this.

Agno's Team state management provides three distinct levels:

* Team's team\_session\_state - Shared state accessible by all team members.
* Team's session\_state - Private state only accessible by the team leader
* Agent's session\_state - Private state for each agent members

<Check>
  Team state propagates through nested team structures as well
</Check>

### How to use Team Session State

You can set the `team_session_state` parameter on `Team` to share state between team members.
This state is available to all team members and is synchronized between them.

For example:

```python
team = Team(
    members=[agent1, agent2, agent3],
    team_session_state={"shopping_list": []},
)
```

Members can access the shared state using the `team_session_state` attribute in tools.

For example:

```python
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
```

### Example

Here's a simple example of a team managing a shared shopping list:

```python team_session_state.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team import Team


