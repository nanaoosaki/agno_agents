---
title: Team with Shared State
category: misc
source_lines: 23711-23726
line_count: 15
---

# Team with Shared State
Source: https://docs.agno.com/examples/concepts/state/06-team-session-state



This example demonstrates how a team of agents can collaboratively manage and update a shared session state.

## Code

```python cookbook/teams/team_with_shared_state.py
from agno.agent.agent import Agent
from agno.models.openai.chat import OpenAIChat
from agno.team import Team


