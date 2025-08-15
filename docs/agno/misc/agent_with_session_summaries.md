---
title: Agent with Session Summaries
category: misc
source_lines: 17130-17157
line_count: 27
---

# Agent with Session Summaries
Source: https://docs.agno.com/examples/concepts/memory/07-agent-with-summaries



This example demonstrates how to create session summaries.

To enable this, set `enable_session_summaries=True` in the Agent config.

## Code

```python cookbook/agent_concepts/memory/08_agent_with_summaries.py

from agno.agent.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.memory.v2.summarizer import SessionSummarizer
from agno.models.anthropic.claude import Claude
from rich.pretty import pprint

memory_db = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db")

memory = Memory(
    db=memory_db,
    summarizer=SessionSummarizer(model=Claude(id="claude-3-5-sonnet-20241022")),
)

