---
title: MongoDB Memory Storage
category: knowledge
source_lines: 17904-17924
line_count: 20
---

# MongoDB Memory Storage
Source: https://docs.agno.com/examples/concepts/memory/db/mem-mongodb-memory



## Code

```python cookbook/agent_concepts/memory/mongodb_memory.py
"""
This example shows how to use the Memory class with MongoDB storage.
"""

import asyncio
import os

from agno.agent.agent import Agent
from agno.memory.v2.db.mongodb import MongoMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.openai.chat import OpenAIChat

