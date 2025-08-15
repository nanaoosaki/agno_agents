---
title: Loop with Parallel Steps Workflow
category: misc
source_lines: 55585-55607
line_count: 22
---

# Loop with Parallel Steps Workflow
Source: https://docs.agno.com/examples/workflows_2/03-workflows-loop-execution/loop_with_parallel_steps_stream

This example demonstrates **Workflows 2.0** most sophisticated pattern combining loop execution with parallel processing and real-time streaming.

This example shows how to create iterative
workflows that execute multiple independent tasks simultaneously within each iteration,
optimizing both quality and performance.

**When to use**: When you need iterative quality improvement with parallel task execution
in each iteration. Ideal for comprehensive research workflows where multiple independent
tasks contribute to overall quality, and you need to repeat until quality thresholds are met.

```python loop_with_parallel_steps_stream.py
from typing import List

from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.workflow.v2 import Loop, Parallel, Step, Workflow
from agno.workflow.v2.types import StepOutput

