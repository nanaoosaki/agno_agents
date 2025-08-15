---
title: Persistent Memory with SQLite
category: knowledge
source_lines: 16639-16663
line_count: 24
---

# Persistent Memory with SQLite
Source: https://docs.agno.com/examples/concepts/memory/02-persistent-memory



This example shows how to use the Memory class to create a persistent memory.

Every time you run this, the `Memory` object will be re-initialized from the DB.

## Code

```python cookbook/agent_concepts/memory/02_persistent_memory.py
from typing import List

from agno.memory.v2.db.schema import MemoryRow
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.memory.v2.schema import UserMemory

memory_db = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db")
memory = Memory(db=memory_db)

john_doe_id = "john_doe@example.com"

