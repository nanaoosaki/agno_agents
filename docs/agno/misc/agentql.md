---
title: AgentQL
category: misc
source_lines: 79135-79196
line_count: 61
---

# AgentQL
Source: https://docs.agno.com/tools/toolkits/web_scrape/agentql



**AgentQLTools** enable an Agent to browse and scrape websites using the AgentQL API.

## Prerequisites

The following example requires the `agentql` library and an API token which can be obtained from [AgentQL](https://agentql.com/).

```shell
pip install -U agentql
```

```shell
export AGENTQL_API_KEY=***
```

## Example

The following agent will open a web browser and scrape all the text from the page.

```python cookbook/tools/agentql_tools.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.agentql import AgentQLTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o"), tools=[AgentQLTools()], show_tool_calls=True
)

agent.print_response("https://docs.agno.com/introduction", markdown=True)
```

<Note>
  AgentQL will open up a browser instance (don't close it) and do scraping on
  the site.
</Note>

## Toolkit Params

| Parameter       | Type   | Default | Description                         |
| --------------- | ------ | ------- | ----------------------------------- |
| `api_key`       | `str`  | `None`  | API key for AgentQL                 |
| `scrape`        | `bool` | `True`  | Whether to use the scrape text tool |
| `agentql_query` | `str`  | `None`  | Custom AgentQL query                |

## Toolkit Functions

| Function                | Description                                          |
| ----------------------- | ---------------------------------------------------- |
| `scrape_website`        | Used to scrape all text from a web page              |
| `custom_scrape_website` | Uses the custom `agentql_query` to scrape a web page |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/agentql.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/agentql_tools.py)


