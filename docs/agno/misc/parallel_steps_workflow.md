---
title: Parallel Steps Workflow
category: misc
source_lines: 55728-55748
line_count: 20
---

# Parallel Steps Workflow
Source: https://docs.agno.com/examples/workflows_2/04-workflows-parallel-execution/parallel_steps_workflow

This example demonstrates **Workflows 2.0** parallel execution for independent tasks that can run simultaneously. Shows how to optimize workflow performance by executing non-dependent steps in parallel, significantly reducing total execution time.

This example demonstrates **Workflows 2.0** parallel execution for independent tasks that
can run simultaneously. Shows how to optimize workflow performance by executing
non-dependent steps in parallel, significantly reducing total execution time.

**When to use**: When you have independent tasks that don't depend on each other's output
but can contribute to the same final goal. Ideal for research from multiple sources,
parallel data processing, or any scenario where tasks can run simultaneously.

```python parallel_steps_workflow.py
from agno.agent import Agent
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.hackernews import HackerNewsTools
from agno.workflow.v2 import Step, Workflow
from agno.workflow.v2.parallel import Parallel

