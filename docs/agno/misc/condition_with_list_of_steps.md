---
title: Condition with list of steps
category: misc
source_lines: 55309-55332
line_count: 23
---

# Condition with list of steps
Source: https://docs.agno.com/examples/workflows_2/02-workflows-conditional-execution/condition_with_list_of_steps

This example demonstrates how to use conditional step to execute multiple steps in parallel.

This example demonstrates **Workflows 2.0** advanced conditional execution where conditions
can trigger multiple steps and run in parallel. Shows how to create sophisticated branching
logic with complex multi-step sequences based on content analysis.

**When to use**: When different topics or content types require completely different
processing pipelines. Ideal for adaptive workflows where the research methodology
should change based on the subject matter or complexity requirements.

```python condition_with_list_of_steps.py
from agno.agent.agent import Agent
from agno.tools.exa import ExaTools
from agno.tools.hackernews import HackerNewsTools
from agno.workflow.v2.condition import Condition
from agno.workflow.v2.parallel import Parallel
from agno.workflow.v2.step import Step
from agno.workflow.v2.types import StepInput
from agno.workflow.v2.workflow import Workflow

