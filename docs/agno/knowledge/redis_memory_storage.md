---
title: Redis Memory Storage
category: knowledge
source_lines: 18079-18097
line_count: 18
---

# Redis Memory Storage
Source: https://docs.agno.com/examples/concepts/memory/db/mem-redis-memory



## Code

```python cookbook/agent_concepts/memory/redis_memory.py
"""
This example shows how to use the Memory class with Redis storage.
"""

from agno.agent.agent import Agent
from agno.memory.v2.db.redis import RedisMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.openai import OpenAIChat
from agno.storage.redis import RedisStorage

