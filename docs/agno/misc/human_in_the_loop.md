---
title: Human in the loop
category: misc
source_lines: 71333-71380
line_count: 47
---

# Human in the loop
Source: https://docs.agno.com/tools/hitl



Human in the loop (HITL) let's you get input from a user before or after executing a tool call.

The example below shows how to use a tool hook to get user confirmation before executing a tool call.

## Example: Human in the loop using tool hooks

This example shows how to:

* Add hooks to tools for user confirmation
* Handle user input during tool execution
* Gracefully cancel operations based on user choice

```python hitl.py
"""🤝 Human-in-the-Loop: Adding User Confirmation to Tool Calls

This example shows how to implement human-in-the-loop functionality in your Agno tools.
It shows how to:
- Add tool hooks to tools for user confirmation
- Handle user input during tool execution
- Gracefully cancel operations based on user choice

Some practical applications:
- Confirming sensitive operations before execution
- Reviewing API calls before they're made
- Validating data transformations
- Approving automated actions in critical systems

Run `pip install openai httpx rich agno` to install dependencies.
"""

import json
from typing import Any, Callable, Dict, Iterator

import httpx
from agno.agent import Agent
from agno.exceptions import StopAgentRun
from agno.models.openai import OpenAIChat
from agno.tools import FunctionCall, tool
from rich.console import Console
from rich.pretty import pprint
from rich.prompt import Prompt

