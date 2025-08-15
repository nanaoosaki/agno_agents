---
title: Background Execution Poll
category: misc
source_lines: 56407-56427
line_count: 20
---

# Background Execution Poll
Source: https://docs.agno.com/examples/workflows_2/06-workflows-advanced-concepts/background_execution_poll

This example demonstrates how to poll the result of a workflow that is running in the background

This example demonstrates how to poll the result of a workflow that is running in the background.

```python background_execution_poll.py
import asyncio

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.team import Team
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.hackernews import HackerNewsTools
from agno.utils.pprint import pprint_run_response
from agno.workflow.v2.step import Step
from agno.workflow.v2.workflow import Workflow

