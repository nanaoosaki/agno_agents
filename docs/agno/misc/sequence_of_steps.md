---
title: Sequence of steps
category: misc
source_lines: 54510-54534
line_count: 24
---

# Sequence of steps
Source: https://docs.agno.com/examples/workflows_2/01-basic-workflows/sequence_of_steps

This example demonstrates how to use named steps in a workflow.

This example demonstrates **Workflows 2.0** using named Step objects for better tracking
and organization. This pattern provides clear step identification and enhanced logging
while maintaining simple sequential execution.

## Pattern: Sequential Named Steps

**When to use**: Linear processes where you want clear step identification, better logging,
and future platform support. Ideal when you have distinct phases that benefit from naming.

```python sequence_of_steps.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.workflow.v2.step import Step
from agno.workflow.v2.workflow import Workflow

