---
title: Capture Reasoning Content
category: misc
source_lines: 21651-21668
line_count: 17
---

# Capture Reasoning Content
Source: https://docs.agno.com/examples/concepts/reasoning/agents/capture-reasoning-content-cot



This example demonstrates how to access and print the `reasoning_content`
when using either `reasoning=True` or setting a specific `reasoning_model`.

## Code

```python cookbook/reasoning/agents/capture_reasoning_content_default_COT.py

from agno.agent import Agent
from agno.models.openai import OpenAIChat

print("\n=== Example 1: Using reasoning=True (default COT) ===\n")

