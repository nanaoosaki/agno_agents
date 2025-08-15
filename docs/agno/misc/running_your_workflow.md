---
title: Running your Workflow
category: misc
source_lines: 84037-84062
line_count: 25
---

# Running your Workflow
Source: https://docs.agno.com/workflows_2/run_workflow

Learn how to run a workflow and get the response.

The `Workflow.run()` function runs the agent and generates a response, either as a `WorkflowRunResponse` object or a stream of `WorkflowRunResponse` objects.

Many of our examples use `workflow.print_response()` which is a helper utility to print the response in the terminal. This uses `workflow.run()` under the hood.

## Running your Workflow

Here's how to run your workflow. The response is captured in the `response`.

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.workflow.v2.step import Step
from agno.workflow.v2.workflow import Workflow
from agno.run.v2.workflow import WorkflowRunResponse
from agno.utils.pprint import pprint_run_response

