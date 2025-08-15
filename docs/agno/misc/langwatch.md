---
title: LangWatch
category: misc
source_lines: 66370-66408
line_count: 38
---

# LangWatch
Source: https://docs.agno.com/observability/langwatch

Integrate Agno with LangWatch to send traces and gain insights into your agent's performance.

## Prerequisites

1. **Install Dependencies**

   ```bash
   pip install agno openai langwatch openinference-instrumentation-agno
   ```

2. **Create a Langwatch Account**

   * Sign up or log in to your [LangWatch dashboard](https://app.langwatch.ai/).
   * Obtain your API key from your project settings.

3. **Set Environment Variables**

   ```bash
   export LANGWATCH_API_KEY=your-langwatch-api-key
   export OPENAI_API_KEY=your-openai-key
   ```

## Sending Traces to LangWatch

This example demonstrates how to instrument your Agno agent and send traces to LangWatch

```python
import langwatch
import os

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools
from openinference.instrumentation.agno import AgnoInstrumentor

