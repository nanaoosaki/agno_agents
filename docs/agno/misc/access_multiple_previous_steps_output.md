---
title: Access Multiple Previous Steps Output
category: misc
source_lines: 56278-56303
line_count: 25
---

# Access Multiple Previous Steps Output
Source: https://docs.agno.com/examples/workflows_2/06-workflows-advanced-concepts/access_multiple_previous_steps_output

This example demonstrates **Workflows 2.0** advanced data flow capabilities

This example demonstrates **Workflows 2.0** shows how to:

1. Access outputs from **specific named steps** (`get_step_content()`)
2. Aggregate **all previous outputs** (`get_all_previous_content()`)
3. Create comprehensive reports by combining multiple research sources

## Key Features:

* **Step Output Access**: Retrieve data from any previous step by name or collectively.
* **Custom Reporting**: Combine and analyze outputs from parallel or sequential steps.
* **Streaming Support**: Real-time updates during execution.

```python access_multiple_previous_steps_output.py
from agno.agent.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.workflow.v2.step import Step
from agno.workflow.v2.types import StepInput, StepOutput
from agno.workflow.v2.workflow import Workflow

