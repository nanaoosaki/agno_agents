---
title: User Memories
category: misc
source_lines: 62891-62916
line_count: 25
---

# User Memories
Source: https://docs.agno.com/memory/memory



When we speak about Memory, the commonly agreed upon understanding of Memory is the ability to store insights and facts about the user the Agent is interacting with. In short, build a persona of the user, learn about their preferences and use that to personalize the Agent's response.

## Agentic Memory

Agno Agents natively support Agentic Memory Management and recommends it as the starting point for your memory journey.

With Agentic Memory, The Agent itself creates, updates and deletes memories from user conversations.

Set `enable_agentic_memory=True` to give the Agent a tool to manage memories of the user, this tool passes the task to the `MemoryManager` class.

> You may also set `enable_user_memories=True` which always runs the `MemoryManager` after each user message. [See below for an example.](#create-memories-after-each-run)

```python agentic_memory.py
from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from rich.pretty import pprint

