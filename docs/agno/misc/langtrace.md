---
title: Langtrace
category: misc
source_lines: 66303-66346
line_count: 43
---

# Langtrace
Source: https://docs.agno.com/observability/langtrace

Integrate Agno with Langtrace to send traces and gain insights into your agent's performance.

## Integrating Agno with Langtrace

Langtrace provides a powerful platform for tracing and monitoring AI model calls. By integrating Agno with Langtrace, you can gain insights into your agent's performance and behavior.

## Prerequisites

1. **Install Dependencies**

   Ensure you have the necessary package installed:

   ```bash
   pip install langtrace-python-sdk
   ```

2. **Create a Langtrace Account**

   * Sign up for an account at [Langtrace](https://app.langtrace.ai/).
   * Obtain your API key from the Langtrace dashboard.

3. **Set Environment Variables**

   Configure your environment with the Langtrace API key:

   ```bash
   export LANGTRACE_API_KEY=<your-key>
   ```

## Sending Traces to Langtrace

This example demonstrates how to instrument your Agno agent with Langtrace.

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools
from langtrace_python_sdk import langtrace
from langtrace_python_sdk.utils.with_root_span import with_langtrace_root_span

