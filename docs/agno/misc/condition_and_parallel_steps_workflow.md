---
title: Condition and Parallel Steps Workflow
category: misc
source_lines: 54997-55024
line_count: 27
---

# Condition and Parallel Steps Workflow
Source: https://docs.agno.com/examples/workflows_2/02-workflows-conditional-execution/condition_and_parallel_steps_stream

This example demonstrates **Workflows 2.0** advanced pattern combining conditional execution with parallel processing.

This example shows how to create sophisticated workflows where multiple
conditions evaluate simultaneously, each potentially triggering different research strategies
based on comprehensive content analysis.

**When to use**: When you need comprehensive, multi-dimensional content analysis where
different aspects of the input may trigger different specialized research pipelines
simultaneously. Ideal for adaptive research workflows that can leverage multiple sources
based on various content characteristics.

```python condition_and_parallel_steps_stream.py
from typing import List, Union

from agno.agent.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.exa import ExaTools
from agno.tools.hackernews import HackerNewsTools
from agno.workflow.v2.condition import Condition
from agno.workflow.v2.parallel import Parallel
from agno.workflow.v2.step import Step
from agno.workflow.v2.types import StepInput
from agno.workflow.v2.workflow import Workflow

