---
title: Multi-User Multi-Session Chat
category: misc
source_lines: 17441-17473
line_count: 32
---

# Multi-User Multi-Session Chat
Source: https://docs.agno.com/examples/concepts/memory/10-multi-user-multi-session-chat



This example demonstrates how to run a multi-user, multi-session chat.

In this example, we have 3 users and 4 sessions.

* User 1 has 2 sessions.
* User 2 has 1 session.
* User 3 has 1 session.

## Code

```python cookbook/agent_concepts/memory/11_multi_user_multi_session_chat.py

import asyncio

from agno.agent.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.google.gemini import Gemini
from agno.storage.sqlite import SqliteStorage

agent_storage = SqliteStorage(
    table_name="agent_sessions", db_file="tmp/persistent_memory.db"
)
memory_db = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db")

memory = Memory(db=memory_db)

