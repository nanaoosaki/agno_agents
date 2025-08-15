---
title: Agent With User Memory
category: knowledge
source_lines: 10576-10616
line_count: 40
---

# Agent With User Memory
Source: https://docs.agno.com/examples/applications/whatsapp/agent_with_user_memory



This example shows how to use  memory with whatsapp app.

## Code

```python cookbook/apps/whatsapp/agent_with_user_memory.py
from textwrap import dedent

from agno.agent import Agent
from agno.app.whatsapp.app import WhatsappAPI
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.manager import MemoryManager
from agno.memory.v2.memory import Memory
from agno.models.google import Gemini
from agno.storage.sqlite import SqliteStorage
from agno.tools.googlesearch import GoogleSearchTools

agent_storage = SqliteStorage(
    table_name="agent_sessions", db_file="tmp/persistent_memory.db"
)
memory_db = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db")

memory = Memory(
    db=memory_db,
    memory_manager=MemoryManager(
        memory_capture_instructions="""\
                        Collect User\'s name,
                        Collect Information about user\'s passion and hobbies,
                        Collect Information about the users likes and dislikes,
                        Collect information about what the user is doing with their life right now
                    """,
        model=Gemini(id="gemini-2.0-flash"),
    ),
)


