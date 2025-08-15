---
title: Mcp Demo
category: misc
source_lines: 9049-9069
line_count: 20
---

# Mcp Demo
Source: https://docs.agno.com/examples/applications/playground/mcp_demo



## Code

```python cookbook/apps/playground/mcp_demo.py
import asyncio
from os import getenv
from textwrap import dedent

import nest_asyncio
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.playground import Playground
from agno.storage.agent.sqlite import SqliteAgentStorage
from agno.tools.mcp import MCPTools
from mcp import StdioServerParameters

