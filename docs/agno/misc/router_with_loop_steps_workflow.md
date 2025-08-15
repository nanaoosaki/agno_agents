---
title: Router with Loop Steps Workflow
category: misc
source_lines: 55904-55928
line_count: 24
---

# Router with Loop Steps Workflow
Source: https://docs.agno.com/examples/workflows_2/05-workflows-conditional-branching/router_with_loop_steps

This example demonstrates **Workflows 2.0** advanced pattern combining Router-based intelligent path selection with Loop execution for iterative quality improvement.

This example shows how to create adaptive workflows that select optimal research strategies and execution patterns based on topic complexity.

**When to use**: When different topic types require fundamentally different research
methodologies - some needing simple single-pass research, others requiring iterative
deep-dive analysis. Ideal for content-adaptive workflows where processing complexity
should match content complexity.

```python router_with_loop_steps.py
from typing import List

from agno.agent.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.workflow.v2.loop import Loop
from agno.workflow.v2.router import Router
from agno.workflow.v2.step import Step
from agno.workflow.v2.types import StepInput, StepOutput
from agno.workflow.v2.workflow import Workflow

