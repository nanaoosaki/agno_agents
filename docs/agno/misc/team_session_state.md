---
title: Team Session State
category: misc
source_lines: 51211-51227
line_count: 16
---

# Team Session State
Source: https://docs.agno.com/examples/teams/shared_state/team_session_state



This example demonstrates how a shared team\_session\_state can propagate and persist across nested agents and subteams, enabling seamless state management for collaborative tasks.

## Code

```python cookbook/teams/team_with_nested_shared_state.py

from agno.agent.agent import Agent
from agno.models.openai.chat import OpenAIChat
from agno.team import Team


