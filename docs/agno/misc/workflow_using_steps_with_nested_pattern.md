---
title: Workflow using Steps with Nested Pattern
category: misc
source_lines: 54836-54857
line_count: 21
---

# Workflow using Steps with Nested Pattern
Source: https://docs.agno.com/examples/workflows_2/01-basic-workflows/workflow_using_steps_nested

This example demonstrates **Workflows 2.0** nested patterns using `Steps` to encapsulate a complex workflow with conditional parallel execution.

This example demonstrates **Workflows 2.0** nested patterns using `Steps` to encapsulate
a complex workflow with conditional parallel execution. It combines `Condition`, `Parallel`,
and `Steps` for modular and adaptive content creation.

```python workflow_using_steps_nested.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.exa import ExaTools
from agno.tools.hackernews import HackerNewsTools
from agno.workflow.v2.condition import Condition
from agno.workflow.v2.parallel import Parallel
from agno.workflow.v2.step import Step
from agno.workflow.v2.steps import Steps
from agno.workflow.v2.workflow import Workflow

