---
title: Step with Function using Additional Data
category: misc
source_lines: 56638-56661
line_count: 23
---

# Step with Function using Additional Data
Source: https://docs.agno.com/examples/workflows_2/06-workflows-advanced-concepts/step_with_function_additional_data

This example demonstrates **Workflows 2.0** support for passing metadata and contextual information to steps via `additional_data`.

This example shows how to pass metadata and contextual information to steps via `additional_data`. This allows separation of workflow logic from configuration, enabling dynamic behavior based on external context.

## Key Features:

* **Context-Aware Steps**: Access `step_input.additional_data` in custom functions
* **Flexible Metadata**: Pass user info, priorities, settings, etc.
* **Clean Separation**: Keep workflow logic focused while enriching steps with context

```python step_with_function_additional_data.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.workflow.v2.step import Step, StepInput, StepOutput
from agno.workflow.v2.workflow import Workfl ow

