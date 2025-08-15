---
title: Agent with Memory
category: knowledge
source_lines: 48505-48534
line_count: 29
---

# Agent with Memory
Source: https://docs.agno.com/examples/models/vllm/memory



## Code

```python cookbook/models/vllm/memory.py
from agno.agent import Agent
from agno.memory.v2.db.postgres import PostgresMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.vllm import vLLM
from agno.storage.postgres import PostgresStorage

DB_URL = "postgresql+psycopg://ai:ai@localhost:5532/ai"

agent = Agent(
    model=vLLM(id="microsoft/Phi-3-mini-128k-instruct"),
    memory=Memory(
        db=PostgresMemoryDb(table_name="agent_memory", db_url=DB_URL),
    ),
    enable_user_memories=True,
    enable_session_summaries=True,
    storage=PostgresStorage(
        table_name="personalized_agent_sessions",
        db_url=DB_URL,
    ),
)

