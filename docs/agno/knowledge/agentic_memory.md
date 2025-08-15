---
title: Agentic Memory
category: knowledge
source_lines: 17021-17043
line_count: 22
---

# Agentic Memory
Source: https://docs.agno.com/examples/concepts/memory/06-agentic-memory



This example shows you how to use persistent memory with an Agent.

During each run the Agent can create/update/delete user memories.

To enable this, set `enable_agentic_memory=True` in the Agent config.

## Code

```python cookbook/agent_concepts/memory/07_agentic_memory.py
from agno.agent.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.openai import OpenAIChat
from rich.pretty import pprint

memory_db = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db")

