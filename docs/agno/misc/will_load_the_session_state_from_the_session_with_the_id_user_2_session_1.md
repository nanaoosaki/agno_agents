---
title: Will load the session state from the session with the id "user_2_session_1"
category: misc
source_lines: 2060-2078
line_count: 18
---

# Will load the session state from the session with the id "user_2_session_1"
agent.print_response("How old am I?", session_id="user_2_session_1", user_id="user_2")
```

## Persisting state in database

`session_state` is part of the Agent session and is saved to the database after each run if a `storage` driver is provided.

Here's an example of an Agent that maintains a shopping list and persists the state in a database. Run this script multiple times to see the state being persisted.

```python session_state_storage.py
"""Run `pip install agno openai sqlalchemy` to install dependencies."""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage


