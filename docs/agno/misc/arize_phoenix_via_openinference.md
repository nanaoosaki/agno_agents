---
title: Arize Phoenix via OpenInference
category: misc
source_lines: 19546-19566
line_count: 20
---

# Arize Phoenix via OpenInference
Source: https://docs.agno.com/examples/concepts/observability/arize-phoenix-via-openinference



## Overview

This example demonstrates how to instrument your Agno agent with OpenInference and send traces to Arize Phoenix.

## Code

```python
import asyncio
import os

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools
from phoenix.otel import register

