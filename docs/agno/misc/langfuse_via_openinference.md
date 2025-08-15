---
title: Langfuse via OpenInference
category: misc
source_lines: 19690-19720
line_count: 30
---

# Langfuse via OpenInference
Source: https://docs.agno.com/examples/concepts/observability/langfuse_via_openinference



## Overview

This example demonstrates how to instrument your Agno agent with OpenInference and send traces to Langfuse.

## Code

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

LANGFUSE_AUTH = base64.b64encode(
    f"{os.getenv('LANGFUSE_PUBLIC_KEY')}:{os.getenv('LANGFUSE_SECRET_KEY')}".encode()
).decode()
os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = (
    "https://us.cloud.langfuse.com/api/public/otel"  # 🇺🇸 US data region
)
