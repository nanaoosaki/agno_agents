---
title: Persistant State with Storage
category: misc
source_lines: 23355-23371
line_count: 16
---

# Persistant State with Storage
Source: https://docs.agno.com/examples/concepts/state/03-session-state-storage



This example demonstrates how to persist an agent’s session state using a SQLite storage, allowing continuity across multiple runs.

## Code

```python cookbook/agent_concepts/state/session_state_storage.py

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage


