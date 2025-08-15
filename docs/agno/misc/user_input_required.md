---
title: User Input Required
category: misc
source_lines: 31768-31784
line_count: 16
---

# User Input Required
Source: https://docs.agno.com/examples/concepts/user-control-flows/04-user-input-required

This example demonstrates how to implement user input collection during agent execution, allowing users to provide specific information for tool parameters.

## Code

```python cookbook/agent_concepts/user_control_flows/user_input_required.py
from typing import List

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool
from agno.tools.function import UserInputField
from agno.utils import pprint

