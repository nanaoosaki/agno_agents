---
title: LangSmith
category: misc
source_lines: 66214-66265
line_count: 51
---

# LangSmith
Source: https://docs.agno.com/observability/langsmith

Integrate Agno with LangSmith to send traces and gain insights into your agent's performance.

## Integrating Agno with LangSmith

LangSmith offers a comprehensive platform for tracing and monitoring AI model calls. By integrating Agno with LangSmith, you can utilize OpenInference to send traces and gain insights into your agent's performance.

## Prerequisites

1. **Create a LangSmith Account**

   * Sign up for an account at [LangSmith](https://smith.langchain.com).
   * Obtain your API key from the LangSmith dashboard.

2. **Set Environment Variables**

   Configure your environment with the LangSmith API key and other necessary settings:

   ```bash
   export LANGSMITH_API_KEY=<your-key>
   export LANGSMITH_TRACING=true
   export LANGSMITH_ENDPOINT=https://eu.api.smith.langchain.com  # or https://api.smith.langchain.com for US
   export LANGSMITH_PROJECT=<your-project-name>
   ```

3. **Install Dependencies**

   Ensure you have the necessary packages installed:

   ```bash
   pip install openai openinference-instrumentation-agno opentelemetry-sdk opentelemetry-exporter-otlp
   ```

## Sending Traces to LangSmith

This example demonstrates how to instrument your Agno agent with OpenInference and send traces to LangSmith.

```python
import os

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from openinference.instrumentation.agno import AgnoInstrumentor
from opentelemetry import trace as trace_api
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

