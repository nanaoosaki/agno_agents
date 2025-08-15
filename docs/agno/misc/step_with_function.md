---
title: Step with function
category: misc
source_lines: 54601-54624
line_count: 23
---

# Step with function
Source: https://docs.agno.com/examples/workflows_2/01-basic-workflows/step_with_function

This example demonstrates how to use named steps with custom function executors.

This example demonstrates **Workflows 2.0** using named Step objects with custom function
executors. This pattern combines the benefits of named steps with the flexibility of
custom functions, allowing for sophisticated data processing within structured workflow steps.

**When to use**: When you need named step organization but want custom logic that goes
beyond what agents/teams provide. Ideal for complex data processing, multi-step operations,
or when you need to orchestrate multiple agents within a single step.

```python step_with_function.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.workflow.v2.step import Step, StepInput, StepOutput
from agno.workflow.v2.workflow import Workflow

