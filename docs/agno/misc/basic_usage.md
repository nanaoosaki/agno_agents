---
title: Basic Usage
category: misc
source_lines: 43375-43394
line_count: 19
---

# Basic Usage
Source: https://docs.agno.com/examples/models/langdb/basic



This example demonstrates how to use [LangDB AI Gateway](https://langdb.ai/) with Agno for basic text generation.

For detailed integration instructions, see the [LangDB Agno documentation](https://docs.langdb.ai/getting-started/working-with-agent-frameworks/working-with-agno).

## Code

```python cookbook/models/langdb/basic.py
from agno.agent import Agent, RunResponse  # noqa
from agno.models.langdb import LangDB

agent = Agent(
    model=LangDB(id="deepseek-chat", project_id="langdb-project-id"), markdown=True
)

