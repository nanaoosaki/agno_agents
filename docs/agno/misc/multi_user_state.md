---
title: Multi User State
category: misc
source_lines: 23435-23451
line_count: 16
---

# Multi User State
Source: https://docs.agno.com/examples/concepts/state/04-session-state-user-id



This example demonstrates how to maintain state for each user in a multi-user environment

## Code

```python cookbook/agent_concepts/state/session_state_user_id.py
import json

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.utils.log import log_info

