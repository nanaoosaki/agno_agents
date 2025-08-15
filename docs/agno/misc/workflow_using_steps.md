---
title: Workflow using steps
category: misc
source_lines: 54750-54771
line_count: 21
---

# Workflow using steps
Source: https://docs.agno.com/examples/workflows_2/01-basic-workflows/workflow_using_steps

This example demonstrates how to use the Steps object to organize multiple individual steps into logical sequences.

This example demonstrates **Workflows 2.0** using the Steps object to organize multiple
individual steps into logical sequences. This pattern allows you to define reusable step
sequences and choose which sequences to execute in your workflow.

**When to use**: When you have logical groupings of steps that you want to organize, reuse,
or selectively execute. Ideal for creating modular workflow components that can be mixed
and matched based on different scenarios.

```python workflow_using_steps.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.workflow.v2.step import Step
from agno.workflow.v2.steps import Steps
from agno.workflow.v2.workflow import Workflow

