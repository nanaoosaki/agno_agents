---
title: Function instead of steps
category: misc
source_lines: 54282-54305
line_count: 23
---

# Function instead of steps
Source: https://docs.agno.com/examples/workflows_2/01-basic-workflows/function_instead_of_steps

This example demonstrates how to use just a single function instead of steps in a workflow.

This example demonstrates **Workflows 2.0** using a single custom execution function instead of
discrete steps. This pattern gives you complete control over the orchestration logic while still
benefiting from workflow features like storage, streaming, and session management.

**When to use**: When you need maximum flexibility and control over the execution flow, similar
to Workflows 1.0 approach but with a better structured approach.

```python function_instead_of_steps.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.utils.pprint import pprint_run_response
from agno.workflow.v2.types import WorkflowExecutionInput
from agno.workflow.v2.workflow import Workflow

