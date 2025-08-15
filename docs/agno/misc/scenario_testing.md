---
title: Scenario Testing
category: misc
source_lines: 70895-70912
line_count: 17
---

# Scenario Testing
Source: https://docs.agno.com/testing/scenario-testing



This example demonstrates how to use the [Scenario](https://github.com/langwatch/scenario) framework for agentic simulation-based testing. Scenario enables you to simulate conversations between agents, user simulators, and judges, making it easy to test and evaluate agent behaviors in a controlled environment.

> **Tip:** For a more advanced scenario testing example, check out the [customer support scenario](https://github.com/langwatch/create-agent-app/tree/main/agno_example) for a more complex agent, including tool calls and advanced scenario features.

## Basic Scenario Testing

```python cookbook/agent_concepts/other/scenario_testing.py
import pytest
import scenario
from agno.agent import Agent
from agno.models.openai import OpenAIChat

