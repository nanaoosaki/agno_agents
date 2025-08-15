---
title: Agent Extra Metrics
category: metrics
source_lines: 20102-20117
line_count: 15
---

# Agent Extra Metrics
Source: https://docs.agno.com/examples/concepts/others/agent_extra_metrics



This example shows how to get special token metrics like audio, cached and reasoning tokens.

## Code

```python cookbook/agent_concepts/other/agent_extra_metrics.py
import requests
from agno.agent import Agent
from agno.media import Audio
from agno.models.openai import OpenAIChat

