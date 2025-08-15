---
title: Condition steps workflow
category: misc
source_lines: 55174-55194
line_count: 20
---

# Condition steps workflow
Source: https://docs.agno.com/examples/workflows_2/02-workflows-conditional-execution/condition_steps_workflow_stream

This example demonstrates how to use conditional steps in a workflow.

This example demonstrates **Workflows 2.0** conditional execution pattern. Shows how to conditionally execute steps based on content analysis,
providing intelligent selection of steps based on the actual data being processed.

**When to use**: When you need intelligent selection of steps based on content analysis rather than
simple input parameters or some other business logic. Ideal for quality gates, content-specific processing, or
adaptive workflows that respond to intermediate results.

```python condition_steps_workflow_stream.py
from agno.agent.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.workflow.v2.condition import Condition
from agno.workflow.v2.step import Step
from agno.workflow.v2.types import StepInput
from agno.workflow.v2.workflow import Workflow

