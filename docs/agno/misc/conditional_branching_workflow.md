---
title: Conditional Branching Workflow
category: misc
source_lines: 55779-55803
line_count: 24
---

# Conditional Branching Workflow
Source: https://docs.agno.com/examples/workflows_2/05-workflows-conditional-branching/router_steps_workflow

This example demonstrates **Workflows 2.0** router pattern for intelligent, content-based workflow routing.

This example demonstrates **Workflows 2.0** to dynamically select the best execution path based on input
analysis, enabling adaptive workflows that choose optimal strategies per topic.

**When to use**: When you need mutually exclusive execution paths based on business logic.
Ideal for topic-specific workflows, expertise routing, or when different subjects require
completely different processing strategies. Unlike Conditions which can trigger multiple
parallel paths, Router selects exactly one path.

```python router_steps_workflow.py
from typing import List

from agno.agent.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.workflow.v2.router import Router
from agno.workflow.v2.step import Step
from agno.workflow.v2.types import StepInput
from agno.workflow.v2.workflow import Workflow

