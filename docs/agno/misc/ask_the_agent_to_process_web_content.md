---
title: Ask the agent to process web content
category: misc
source_lines: 74594-74613
line_count: 19
---

# Ask the agent to process web content
agent.print_response("Summarize the content from https://docs.agno.com/introduction", markdown=True)
```

### 3. Google Places Crawler

The [Google Places Crawler](https://apify.com/compass/crawler-google-places) extracts data about businesses from Google Maps and Google Places.

```python
from agno.agent import Agent
from agno.tools.apify import ApifyTools

agent = Agent(
    tools=[
        ApifyTools(actors=["compass/crawler-google-places"])
    ],
    show_tool_calls=True
)

