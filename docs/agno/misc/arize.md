---
title: Arize
category: misc
source_lines: 65720-65767
line_count: 47
---

# Arize
Source: https://docs.agno.com/observability/arize

Integrate Agno with Arize Phoenix to send traces and gain insights into your agent's performance.

## Integrating Agno with Arize Phoenix

[Arize Phoenix](https://phoenix.arize.com/) is a powerful platform for monitoring and analyzing AI models. By integrating Agno with Arize Phoenix, you can leverage OpenInference to send traces and gain insights into your agent's performance.

## Prerequisites

1. **Install Dependencies**

   Ensure you have the necessary packages installed:

   ```bash
   pip install arize-phoenix openai openinference-instrumentation-agno opentelemetry-sdk opentelemetry-exporter-otlp
   ```

2. **Setup Arize Phoenix Account**

   * Create an account at [Arize Phoenix](https://phoenix.arize.com/).
   * Obtain your API key from the Arize Phoenix dashboard.

3. **Set Environment Variables**

   Configure your environment with the Arize Phoenix API key:

   ```bash
   export ARIZE_PHOENIX_API_KEY=<your-key>
   ```

## Sending Traces to Arize Phoenix

* ### Example: Using Arize Phoenix with OpenInference

This example demonstrates how to instrument your Agno agent with OpenInference and send traces to Arize Phoenix.

```python
import asyncio
import os

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools
from phoenix.otel import register

