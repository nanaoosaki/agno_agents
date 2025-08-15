---
title: SQLite Memory Storage
category: knowledge
source_lines: 18183-18201
line_count: 18
---

# SQLite Memory Storage
Source: https://docs.agno.com/examples/concepts/memory/db/mem-sqlite-memory



## Code

```python cookbook/agent_concepts/memory/sqlite_memory.py
"""
This example shows how to use the Memory class with SQLite storage.
"""

from agno.agent.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage

