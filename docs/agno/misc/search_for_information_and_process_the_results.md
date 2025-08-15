---
title: Search for information and process the results
category: misc
source_lines: 74575-74594
line_count: 19
---

# Search for information and process the results
agent.print_response("What are the latest developments in large language models?", markdown=True)
```

### 2. Website Content Crawler

This tool uses Apify's [Website Content Crawler](https://apify.com/apify/website-content-crawler) Actor to extract text content from websites, making it perfect for RAG applications.

```python
from agno.agent import Agent
from agno.tools.apify import ApifyTools

agent = Agent(
    tools=[
        ApifyTools(actors=["apify/website-content-crawler"])
    ],
    markdown=True
)

