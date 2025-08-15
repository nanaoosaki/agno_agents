---
title: Langfuse
category: misc
source_lines: 66079-66131
line_count: 52
---

# Langfuse
Source: https://docs.agno.com/observability/langfuse

Integrate Agno with Langfuse to send traces and gain insights into your agent's performance.

## Integrating Agno with Langfuse

Langfuse provides a robust platform for tracing and monitoring AI model calls. By integrating Agno with Langfuse, you can utilize OpenInference and OpenLIT to send traces and gain insights into your agent's performance.

## Prerequisites

1. **Install Dependencies**

   Ensure you have the necessary packages installed:

   ```bash
   pip install agno openai langfuse opentelemetry-sdk opentelemetry-exporter-otlp openinference-instrumentation-agno
   ```

2. **Setup Langfuse Account**

   * Either self-host or sign up for an account at [Langfuse](https://us.cloud.langfuse.com).
   * Obtain your public and secret API keys from the Langfuse dashboard.

3. **Set Environment Variables**

   Configure your environment with the Langfuse API keys:

   ```bash
   export LANGFUSE_PUBLIC_KEY=<your-public-key>
   export LANGFUSE_SECRET_KEY=<your-secret-key>
   ```

## Sending Traces to Langfuse

* ### Example: Using Langfuse with OpenInference

This example demonstrates how to instrument your Agno agent with OpenInference and send traces to Langfuse.

```python
import base64
import os

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools
from openinference.instrumentation.agno import AgnoInstrumentor
from opentelemetry import trace as trace_api
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

