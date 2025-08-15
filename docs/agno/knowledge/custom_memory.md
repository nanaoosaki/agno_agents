---
title: Custom Memory
category: knowledge
source_lines: 17341-17365
line_count: 24
---

# Custom Memory
Source: https://docs.agno.com/examples/concepts/memory/09-custom-memory



This example shows how you can configure the Memory Manager and Summarizer models individually.

In this example, we use OpenRouter and LLama 3.3-70b-instruct for the memory manager and Claude 3.5 Sonnet for the summarizer, while using Gemini for the Agent.

We also set custom system prompts for the memory manager and summarizer.

## Code

```python cookbook/agent_concepts/memory/10_custom_memory.py
from agno.agent.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory, MemoryManager, SessionSummarizer
from agno.models.anthropic.claude import Claude
from agno.models.google.gemini import Gemini
from agno.models.openrouter.openrouter import OpenRouter
from rich.pretty import pprint

memory_db = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db")

