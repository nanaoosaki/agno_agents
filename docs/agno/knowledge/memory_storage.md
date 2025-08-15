---
title: Memory Storage
category: knowledge
source_lines: 63247-63272
line_count: 25
---

# Memory Storage

To persist memories across sessions and execution cycles, store memories in a persistent storage like a database.

If you're using Memory in production, persistent storage is critical as you'd want to retain user memories across application restarts.

Agno's memory system supports multiple persistent storage options.

## Storage Options

The Memory class supports different backend storage options through a pluggable database interface. Currently, Agno provides:

1. [SQLite Storage](/reference/memory/storage/sqlite)
2. [PostgreSQL Storage](/reference/memory/storage/postgres)
3. [MongoDB Storage](/reference/memory/storage/mongo)
4. [Redis Storage](/reference/memory/storage/redis)

## Setting Up Storage

To configure memory storage, you'll need to create a database instance and pass it to the Memory constructor:

```python
from agno.memory.v2.memory import Memory
from agno.memory.v2.db.sqlite import SqliteMemoryDb

