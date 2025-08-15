---
title: Multiple Agents Sharing Memory
category: knowledge
source_lines: 17247-17267
line_count: 20
---

# Multiple Agents Sharing Memory
Source: https://docs.agno.com/examples/concepts/memory/08-agents-share-memory



In this example, we have two agents that share the same memory.

## Code

```python cookbook/agent_concepts/memory/09_agents_share_memory.py

from agno.agent.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.google.gemini import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from rich.pretty import pprint

memory_db = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db")

