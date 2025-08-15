---
title: Weave
category: misc
source_lines: 66433-66476
line_count: 43
---

# Weave
Source: https://docs.agno.com/observability/weave

Integrate Agno with Weave to send traces and gain insights into your agent's performance.

## Integrating Agno with Weave by WandB

[Weave](https://weave-docs.wandb.ai/) provides a powerful platform for logging and visualizing model calls. By integrating Agno with Weave, you can track and analyze your agent's performance and behavior.

## Prerequisites

1. **Install Dependencies**

Ensure you have the necessary packages installed:

```bash
pip install weave
```

2. **Create a WandB Account**

* Sign up for an account at [WandB](https://wandb.ai).
* Obtain your API key from [WandB Dashboard](https://wandb.ai/authorize).

3. **Set Environment Variables**

Configure your environment with the WandB API key:

```bash
export WANDB_API_KEY=<your-api-key>
```

## Sending Traces to Weave

* ### Example: Using `weave.op` decorator

This method requires installing the [weave package](https://pypi.org/project/weave/) and then utilising `@weave.op` decorator over any function you wish to automatically trace. This works by creating wrappers around the functions.

```python
import weave
from agno.agent import Agent
from agno.models.openai import OpenAIChat

