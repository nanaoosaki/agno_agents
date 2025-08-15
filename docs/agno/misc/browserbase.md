---
title: Browserbase
category: misc
source_lines: 79343-79415
line_count: 72
---

# Browserbase
Source: https://docs.agno.com/tools/toolkits/web_scrape/browserbase



**BrowserbaseTools** enable an Agent to automate browser interactions using Browserbase, a headless browser service.

## Prerequisites

The following example requires Browserbase API credentials after you signup [here](https://www.browserbase.com/), and the Playwright library.

```shell
pip install browserbase playwright
export BROWSERBASE_API_KEY=xxx
export BROWSERBASE_PROJECT_ID=xxx
```

## Example

The following agent will use Browserbase to visit `https://quotes.toscrape.com` and extract content. Then navigate to page two of the website and get quotes from there as well.

```python cookbook/tools/browserbase_tools.py
from agno.agent import Agent
from agno.tools.browserbase import BrowserbaseTools

agent = Agent(
    name="Web Automation Assistant",
    tools=[BrowserbaseTools()],
    instructions=[
        "You are a web automation assistant that can help with:",
        "1. Capturing screenshots of websites",
        "2. Extracting content from web pages",
        "3. Monitoring website changes",
        "4. Taking visual snapshots of responsive layouts",
        "5. Automated web testing and verification",
    ],
    markdown=True,
)

agent.print_response("""
    Visit https://quotes.toscrape.com and:
    1. Extract the first 5 quotes and their authors
    2. Navigate to page 2
    3. Extract the first 5 quotes from page 2
""")
```

<Tip>View the [Startup Analyst MCP agent](/examples/concepts/tools/mcp/stagehand)</Tip>

## Toolkit Params

| Parameter    | Type  | Default | Description                                                                                                                                                                                           |
| ------------ | ----- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_key`    | `str` | `None`  | Browserbase API key. If not provided, uses BROWSERBASE\_API\_KEY env var.                                                                                                                             |
| `project_id` | `str` | `None`  | Browserbase project ID. If not provided, uses BROWSERBASE\_PROJECT\_ID env var.                                                                                                                       |
| `base_url`   | `str` | `None`  | Custom Browserbase API endpoint URL. Only use this if you're using a self-hosted Browserbase instance or need to connect to a different region. If not provided, uses BROWSERBASE\_BASE\_URL env var. |

## Toolkit Functions

| Function           | Description                                                                                                                                           |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `navigate_to`      | Navigates to a URL. Takes a URL and an optional connect\_url parameter.                                                                               |
| `screenshot`       | Takes a screenshot of the current page. Takes a path to save the screenshot, a boolean for full-page capture, and an optional connect\_url parameter. |
| `get_page_content` | Gets the HTML content of the current page. Takes an optional connect\_url parameter.                                                                  |
| `close_session`    | Closes a browser session.                                                                                                                             |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/browserbase.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/browserbase_tools.py)


