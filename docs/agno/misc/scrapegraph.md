---
title: ScrapeGraph
category: misc
source_lines: 79741-79809
line_count: 68
---

# ScrapeGraph
Source: https://docs.agno.com/tools/toolkits/web_scrape/scrapegraph

Agno ScrapeGraphTools enable an Agent to extract structured data from webpages for LLMs in markdown format.

## Prerequisites

The following examples require the `scrapegraph-py` library.

```shell
pip install -U scrapegraph-py
```

Optionally, if your ScrapeGraph configuration or specific models require an API key, set the `SGAI_API_KEY` environment variable:

```shell
export SGAI_API_KEY="YOUR_SGAI_API_KEY"
```

## Example

The following agent uses `ScrapeGraphTools` to extract specific information from a webpage using the `smartscraper` functionality.

```python
from agno.agent import Agent
from agno.tools.scrapegraph import ScrapeGraphTools

agent = Agent(
    tools=[ScrapeGraphTools(smartscraper=True)],
    show_tool_calls=True,
)

agent.print_response("""
    "Use smartscraper to extract the following from https://www.wired.com/category/science/:
- News articles
- Headlines
- Images
- Links
- Author
""",
)
```

<Note>View the [Startup Analyst example](/examples/agents/startup-analyst-agent) & [Agentic Deep Researcher Workflow](/examples/workflows/agentic-deep-researcher) </Note>

## Toolkit Functions

| Function       | Description                                                                                                                          |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `smartscraper` | Extracts structured data from a webpage using an LLM and a natural language prompt. Returns a JSON string of the result or an error. |
| `markdownify`  | Converts a webpage to markdown format. Returns the markdown string or an error.                                                      |

## Toolkit Parameters

These parameters are passed to the `ScrapeGraphTools` constructor.

| Parameter      | Type            | Default | Description                                                                                                |
| -------------- | --------------- | ------- | ---------------------------------------------------------------------------------------------------------- |
| `api_key`      | `Optional[str]` | `None`  | API key for ScrapeGraph services. If not provided, it defaults to the `SGAI_API_KEY` environment variable. |
| `smartscraper` | `bool`          | `True`  | Enable the `smartscraper` tool.                                                                            |
| `markdownify`  | `bool`          | `False` | Enable the `markdownify` tool.                                                                             |

## Developer Resources

* View [Tools Source](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/scrapegraph.py)
* View [Cookbook Example](https://github.com/agno-agi/agno/blob/main/cookbook/tools/scrapegraph_tools.py)


