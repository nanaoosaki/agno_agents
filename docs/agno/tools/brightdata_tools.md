---
title: BrightData Tools
category: tools
source_lines: 30997-31021
line_count: 24
---

# BrightData Tools
Source: https://docs.agno.com/examples/concepts/tools/web_scrape/brightdata



## Code

```python cookbook/tools/brightdata_tools.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.brightdata import BrightDataTools
from agno.utils.media import save_base64_data

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        BrightDataTools(
            get_screenshot=True,
        )
    ],
    markdown=True,
    show_tool_calls=True,
)

