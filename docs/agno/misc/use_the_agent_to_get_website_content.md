---
title: Use the agent to get website content
category: misc
source_lines: 74551-74575
line_count: 24
---

# Use the agent to get website content
agent.print_response("What information can you find on https://docs.agno.com/introduction ?", markdown=True)
```

## Available Apify Tools

You can easily integrate any Apify Actor as a tool. Here are some examples:

### 1. RAG Web Browser

The [RAG Web Browser](https://apify.com/apify/rag-web-browser) Actor is specifically designed for AI and LLM applications. It searches the web for a query or processes a URL, then cleans and formats the content for your agent. This tool is enabled by default.

```python
from agno.agent import Agent
from agno.tools.apify import ApifyTools

agent = Agent(
    tools=[
        ApifyTools(actors=["apify/rag-web-browser"])
    ],
    show_tool_calls=True,
    markdown=True
)

