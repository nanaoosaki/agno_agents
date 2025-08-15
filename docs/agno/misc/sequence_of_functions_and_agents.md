---
title: Sequence of functions and agents
category: misc
source_lines: 54393-54417
line_count: 24
---

# Sequence of functions and agents
Source: https://docs.agno.com/examples/workflows_2/01-basic-workflows/sequence_of_functions_and_agents

This example demonstrates how to use a sequence of functions and agents in a workflow.

This example demonstrates **Workflows 2.0** combining custom functions with agents and teams
in a sequential execution pattern. This shows how to mix different component types for
maximum flexibility in your workflow design.

**When to use**: Linear processes where you need custom data preprocessing between AI agents,
or when combining multiple component types (functions, agents, teams) in sequence.

```python sequence_of_functions_and_agents.py
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.workflow.v2.types import StepInput, StepOutput
from agno.workflow.v2.workflow import Workflow

