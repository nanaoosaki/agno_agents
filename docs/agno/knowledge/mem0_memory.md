---
title: Mem0 Memory
category: knowledge
source_lines: 18283-18304
line_count: 21
---

# Mem0 Memory
Source: https://docs.agno.com/examples/concepts/memory/mem0-memory



## Code

```python cookbook/agent_concepts/memory/mem0_memory.py
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.utils.pprint import pprint_run_response
from mem0 import MemoryClient

client = MemoryClient()

user_id = "agno"
messages = [
    {"role": "user", "content": "My name is John Billings."},
    {"role": "user", "content": "I live in NYC."},
    {"role": "user", "content": "I'm going to a concert tomorrow."},
]
