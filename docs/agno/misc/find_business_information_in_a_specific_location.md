---
title: Find business information in a specific location
category: misc
source_lines: 74613-74638
line_count: 25
---

# Find business information in a specific location
agent.print_response("What are the top-rated restaurants in San Francisco?", markdown=True)
agent.print_response("Find coffee shops in Prague", markdown=True)
```

## Example Scenarios

### RAG Web Browser + Google Places Crawler

This example combines web search with local business data to provide comprehensive information about a topic:

```python
from agno.agent import Agent
from agno.tools.apify import ApifyTools

agent = Agent(
    tools=[
        ApifyTools(actors=[
            "apify/rag-web-browser",
            "compass/crawler-google-places"
        ])
    ],
    show_tool_calls=True
)

