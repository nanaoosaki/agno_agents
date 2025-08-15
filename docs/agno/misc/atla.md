---
title: Atla
category: misc
source_lines: 65842-65877
line_count: 35
---

# Atla
Source: https://docs.agno.com/observability/atla

Integrate `Atla` with Agno for real-time monitoring, automated evaluation, and performance analytics of your AI agents.

[Atla](https://www.atla-ai.com/) is an advanced observability platform designed specifically for AI agent monitoring and evaluation.
This integration provides comprehensive insights into agent performance, automated quality assessment, and detailed analytics for production AI systems.

## Prerequisites

* **API Key**: Obtain your API key from the [Atla dashboard](https://app.atla-ai.com)

Install the Atla Insights SDK with Agno support:

```bash
pip install "atla-insights"
```

## Configuration

Configure your API key as an environment variable:

```bash
export ATLA_API_KEY="your_api_key_from_atla_dashboard"
```

## Example

```python
from os import getenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from atla_insights import configure, instrument_agno

