---
title: AgentOps
category: misc
source_lines: 65666-65700
line_count: 34
---

# AgentOps
Source: https://docs.agno.com/observability/agentops

Integrate Agno with AgentOps to send traces and logs to a centralized observability platform.

## Integrating Agno with AgentOps

[AgentOps](https://app.agentops.ai/) provides automatic instrumentation for your Agno agents to track all operations including agent interactions, team coordination, tool usage, and workflow execution.

## Prerequisites

1. **Install AgentOps**

   Ensure you have the AgentOps package installed:

   ```bash
   pip install agentops
   ```

2. **Authentication**
   Go to [AgentOps](https://app.agentops.ai/) and copy your API key
   ```bash
   export AGENTOPS_API_KEY=<your-api-key>
   ```

## Logging Model Calls with AgentOps

This example demonstrates how to use AgentOps to log model calls.

```python
import agentops
from agno.agent import Agent
from agno.models.openai import OpenAIChat

