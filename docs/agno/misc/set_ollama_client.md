---
title: Set Ollama Client
category: misc
source_lines: 46136-46155
line_count: 19
---

# Set Ollama Client
Source: https://docs.agno.com/examples/models/ollama/set_client



## Code

```python cookbook/models/ollama/set_client.py
from agno.agent import Agent, RunResponse  # noqa
from agno.models.ollama import Ollama
from agno.tools.yfinance import YFinanceTools
from ollama import Client as OllamaClient

agent = Agent(
    model=Ollama(id="llama3.2", client=OllamaClient()),
    tools=[YFinanceTools(stock_price=True)],
    markdown=True,
)

