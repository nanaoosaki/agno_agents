---
title: Multi-User Multi-Session Chat Concurrent
category: misc
source_lines: 17592-17622
line_count: 30
---

# Multi-User Multi-Session Chat Concurrent
Source: https://docs.agno.com/examples/concepts/memory/11-multi-user-multi-session-chat-concurrent



This example shows how to run a multi-user, multi-session chat concurrently. In this example, we have 3 users and 4 sessions:

* User 1 has 2 sessions.
* User 2 has 1 session.
* User 3 has 1 session.

## Code

```python cookbook/agent_concepts/memory/12_multi_user_multi_session_chat_concurrent.py
import asyncio

from agno.agent.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.anthropic.claude import Claude
from agno.models.google.gemini import Gemini
from agno.storage.sqlite import SqliteStorage

agent_storage = SqliteStorage(
    table_name="agent_sessions", db_file="tmp/persistent_memory.db"
)
memory_db = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db")

memory = Memory(model=Claude(id="claude-3-5-sonnet-20241022"), db=memory_db)

