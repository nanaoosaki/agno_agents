---
title: Loop Steps Workflow
category: misc
source_lines: 55476-55498
line_count: 22
---

# Loop Steps Workflow
Source: https://docs.agno.com/examples/workflows_2/03-workflows-loop-execution/loop_steps_workflow

This example demonstrates **Workflows 2.0** loop execution for quality-driven iterative processes.

This example demonstrates **Workflows 2.0** to repeatedly execute steps until specific conditions are met,
ensuring adequate research depth before proceeding to content creation.

**When to use**: When you need iterative refinement, quality assurance, or when the
required output quality can't be guaranteed in a single execution. Ideal for research
gathering, data collection, or any process where "good enough" is determined by content
analysis rather than a fixed number of iterations.

```python loop_steps_workflow.py
from typing import List

from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.workflow.v2 import Loop, Step, Workflow
from agno.workflow.v2.types import StepOutput

