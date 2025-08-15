---
title: Memory Search
category: knowledge
source_lines: 16827-16847
line_count: 20
---

# Memory Search
Source: https://docs.agno.com/examples/concepts/memory/04-memory-search



This example demonstrates how to search for user memories using different retrieval methods

* last\_n: Retrieves the last n memories
* first\_n: Retrieves the first n memories
* semantic: Retrieves memories using semantic search

## Code

```python cookbook/agent_concepts/memory/05_memory_search.py
from agno.memory.v2 import Memory, UserMemory
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.models.google.gemini import Gemini
from rich.pretty import pprint

memory_db = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db")
