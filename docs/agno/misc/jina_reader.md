---
title: Jina Reader
category: misc
source_lines: 79520-79569
line_count: 49
---

# Jina Reader
Source: https://docs.agno.com/tools/toolkits/web_scrape/jina_reader



**JinaReaderTools** enable an Agent to perform web search tasks using Jina.

## Prerequisites

The following example requires the `jina` library.

```shell
pip install -U jina
```

## Example

The following agent will use Jina API to summarize the content of [https://github.com/AgnoAgi](https://github.com/AgnoAgi)

```python cookbook/tools/jinareader.py
from agno.agent import Agent
from agno.tools.jina import JinaReaderTools

agent = Agent(tools=[JinaReaderTools()])
agent.print_response("Summarize: https://github.com/AgnoAgi")
```

## Toolkit Params

| Parameter            | Type  | Default | Description                                                                |
| -------------------- | ----- | ------- | -------------------------------------------------------------------------- |
| `api_key`            | `str` | -       | The API key for authentication purposes, retrieved from the configuration. |
| `base_url`           | `str` | -       | The base URL of the API, retrieved from the configuration.                 |
| `search_url`         | `str` | -       | The URL used for search queries, retrieved from the configuration.         |
| `max_content_length` | `int` | -       | The maximum length of content allowed, retrieved from the configuration.   |

## Toolkit Functions

| Function       | Description                                                                                                                                                                                            |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `read_url`     | Reads the content of a specified URL using Jina Reader API. Parameters include `url` for the URL to read. Returns the truncated content or an error message if the request fails.                      |
| `search_query` | Performs a web search using Jina Reader API based on a specified query. Parameters include `query` for the search term. Returns the truncated search results or an error message if the request fails. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/jina_reader.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/jina_reader_tools.py)


