---
title: Standalone Memory Operations
category: knowledge
source_lines: 16556-16571
line_count: 15
---

# Standalone Memory Operations
Source: https://docs.agno.com/examples/concepts/memory/01-standalone-memory



This example shows how to manually add, retrieve, delete, and replace user memories.

## Code

```python cookbook/agent_concepts/memory/01_standalone_memory.py
from agno.memory.v2 import Memory, UserMemory
from rich.pretty import pprint

memory = Memory()

