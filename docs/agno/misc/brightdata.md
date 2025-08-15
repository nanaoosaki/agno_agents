---
title: BrightData
category: misc
source_lines: 79196-79247
line_count: 51
---

# BrightData
Source: https://docs.agno.com/tools/toolkits/web_scrape/brightdata

BrightDataTools enable an Agent to perform web scraping, search engine queries, screenshots, and structured data extraction using BrightData's API.

**BrightDataTools** provide comprehensive web scraping capabilities including markdown conversion, screenshots, search engine results, and structured data feeds from various platforms like LinkedIn, Amazon, Instagram, and more.

## Prerequisites

The following examples require the `requests` library.

```shell
pip install -U requests
```

You'll also need a BrightData API key. Set the `BRIGHT_DATA_API_KEY` environment variable:

```shell
export BRIGHT_DATA_API_KEY="YOUR_BRIGHTDATA_API_KEY"
```

Optionally, you can configure zone settings:

```shell
export BRIGHT_DATA_WEB_UNLOCKER_ZONE="your_web_unlocker_zone"
export BRIGHT_DATA_SERP_ZONE="your_serp_zone"
```

## Examples

### Basic Web Scraping

Extract structured data from platforms like LinkedIn, Amazon, etc.:

```python
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

