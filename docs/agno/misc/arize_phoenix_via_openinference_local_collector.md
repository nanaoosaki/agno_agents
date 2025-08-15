---
title: Arize Phoenix via OpenInference (Local Collector)
category: misc
source_lines: 19618-19637
line_count: 19
---

# Arize Phoenix via OpenInference (Local Collector)
Source: https://docs.agno.com/examples/concepts/observability/arize-phoenix-via-openinference-local



## Overview

This example demonstrates how to instrument your Agno agent with OpenInference and send traces to a local Arize Phoenix collector.

## Code

```python
import os

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools
from phoenix.otel import register

