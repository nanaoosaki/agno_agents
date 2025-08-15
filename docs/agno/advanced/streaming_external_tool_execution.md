---
title: Streaming External Tool Execution
category: advanced
source_lines: 32397-32412
line_count: 15
---

# Streaming External Tool Execution
Source: https://docs.agno.com/examples/concepts/user-control-flows/10-external-tool-execution-stream

This example demonstrates how to implement streaming external tool execution, allowing for real-time interaction and response streaming while executing tools outside of the agent's control.

## Code

```python cookbook/agent_concepts/user_control_flows/external_tool_execution_stream.py
import subprocess

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool
from agno.utils import pprint

