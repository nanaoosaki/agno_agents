---
title: Use the function to log a model call
category: misc
source_lines: 66487-66516
line_count: 29
---

# Use the function to log a model call
run("Share a 2 sentence horror story")
```

* ### Example: Using OpenTelemetry

In this method, we utilize weave's support for OpenTelemetry based trace logging. This method does not require installing `weave` Python SDK as a dependency.

First, install the required OpenTelemetry dependencies:

```bash
pip install openai openinference-instrumentation-agno opentelemetry-sdk opentelemetry-exporter-otlp-proto-http
```

This example demonstrates how to instrument your Agno agent with OpenInference and send traces to Weave:

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

