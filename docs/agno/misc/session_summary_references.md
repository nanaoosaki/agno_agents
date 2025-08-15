---
title: Session Summary References
category: misc
source_lines: 17824-17845
line_count: 21
---

# Session Summary References
Source: https://docs.agno.com/examples/concepts/memory/13-session-summary-references



This example shows how to use the `add_session_summary_references` parameter in the Agent config to
add references to the session summaries to the Agent.

## Code

```13_session_summary_references.py
from agno.agent.agent import Agent
from agno.memory.v2.db.postgres import PostgresMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.google.gemini import Gemini
from agno.storage.postgres import PostgresStorage

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

memory_db = PostgresMemoryDb(table_name="memory", db_url=db_url)

