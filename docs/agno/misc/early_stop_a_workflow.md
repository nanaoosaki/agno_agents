---
title: Early Stop a Workflow
category: misc
source_lines: 56536-56556
line_count: 20
---

# Early Stop a Workflow
Source: https://docs.agno.com/examples/workflows_2/06-workflows-advanced-concepts/early_stop_workflow

This example demonstrates **Workflows 2.0** early termination of a running workflow.

This example shows how to create workflows that can terminate
gracefully when quality conditions aren't met, preventing downstream processing of
invalid or unsafe data.

**When to use**: When you need safety mechanisms, quality gates, or validation checkpoints
that should prevent downstream processing if conditions aren't met. Ideal for data
validation pipelines, security checks, quality assurance workflows, or any process where
continuing with invalid inputs could cause problems.

```python early_stop_workflow_with_agents.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.workflow.v2 import Workflow
from agno.workflow.v2.types import StepInput, StepOutput

