---
title: Web Browser Tools
category: tools
source_lines: 77005-77038
line_count: 33
---

# Web Browser Tools
Source: https://docs.agno.com/tools/toolkits/others/web-browser

WebBrowser Tools enable an Agent to open a URL in a web browser.

## Example

```python cookbook/tools/webbrowser_tools.py
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.webbrowser import WebBrowserTools

agent = Agent(
    model=Gemini("gemini-2.0-flash"),
    tools=[WebBrowserTools(), DuckDuckGoTools()],
    instructions=[
        "Find related websites and pages using DuckDuckGo"
        "Use web browser to open the site"
    ],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Find an article explaining MCP and open it in the web browser.")
```

## Toolkit Functions

| Function    | Description                  |
| ----------- | ---------------------------- |
| `open_page` | Opens a URL in a web browser |


