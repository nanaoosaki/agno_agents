---
title: Langfuse via OpenLIT
category: misc
source_lines: 19780-19806
line_count: 26
---

# Langfuse via OpenLIT
Source: https://docs.agno.com/examples/concepts/observability/langfuse_via_openlit



## Overview

This example demonstrates how to use Langfuse via OpenLIT to trace model calls.

## Code

```python
import base64
import os

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

LANGFUSE_AUTH = base64.b64encode(
    f"{os.getenv('LANGFUSE_PUBLIC_KEY')}:{os.getenv('LANGFUSE_SECRET_KEY')}".encode()
).decode()

os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = (
    "https://us.cloud.langfuse.com/api/public/otel"  # 🇺🇸 US data region
)
