---
title: Google Maps Tools
category: tools
source_lines: 28973-28996
line_count: 23
---

# Google Maps Tools
Source: https://docs.agno.com/examples/concepts/tools/others/google_maps



## Code

```python cookbook/tools/google_maps_tools.py
from agno.agent import Agent
from agno.tools.google_maps import GoogleMapTools
from agno.tools.crawl4ai import Crawl4aiTools  # Optional: for enriching place data

agent = Agent(
    name="Maps API Demo Agent",
    tools=[
        GoogleMapTools(),
        Crawl4aiTools(max_length=5000),  # Optional: for scraping business websites
    ],
    description="Location and business information specialist for mapping and location-based queries.",
    markdown=True,
    show_tool_calls=True,
)

