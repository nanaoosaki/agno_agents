---
title: Custom Memory Creation
category: knowledge
source_lines: 16707-16726
line_count: 19
---

# Custom Memory Creation
Source: https://docs.agno.com/examples/concepts/memory/03-custom-memory-creation



This example demonstrates how to create user memories with an Agent by providing either text or a list of messages. The Agent uses a custom memory manager to capture and store relevant details.

## Code

```python cookbook/agent_concepts/memory/04_custom_memory_creation.py
from agno.memory.v2 import Memory
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.manager import MemoryManager
from agno.models.anthropic.claude import Claude
from agno.models.google import Gemini
from agno.models.message import Message
from rich.pretty import pprint

memory_db = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db")
