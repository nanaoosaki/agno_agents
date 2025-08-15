---
title: Serper
category: misc
source_lines: 77829-77920
line_count: 91
---

# Serper
Source: https://docs.agno.com/tools/toolkits/search/serper



**SerperTools** enable an Agent to search Google, search news, search academic papers, search reviews, and scrape webpages using Serper.

## Prerequisites

The following example requires an API key from [Serper](https://serper.dev/).

```shell
export SERPER_API_KEY=***
```

## Example

The following agent will search for the latest news about artificial intelligence developments:

```python cookbook/tools/serper_tools.py
from agno.agent import Agent
from agno.tools.serper import SerperTools

agent = Agent(
    tools=[SerperTools()],
    show_tool_calls=True,
)

agent.print_response(
    "Search for the latest news about artificial intelligence developments",
    markdown=True,
)
```

## Additional Examples

### Google Scholar Search

```python
agent.print_response(
    "Find 2 recent academic papers about large language model safety and alignment",
    markdown=True,
)
```

### Reviews Search

```python
agent.print_response(
    "Use this Google Place ID: ChIJ_Yjh6Za1j4AR8IgGUZGDDTs and analyze the reviews",
    markdown=True
)
```

### Web Scraping

```python
agent.print_response(
    "Scrape and summarize the main content from this OpenAI blog post: https://openai.com/index/gpt-4/",
    markdown=True
)
```

## Toolkit Params

| Parameter         | Type            | Default          | Description                                                     |
| ----------------- | --------------- | ---------------- | --------------------------------------------------------------- |
| `api_key`         | `Optional[str]` | `None`           | API key for authentication.                                     |
| `country`         | `str`           | `"us"`           | Country code for search results (e.g., "us", "uk").             |
| `location`        | `Optional[str]` | `None`           | Google location code for search results.                        |
| `language`        | `str`           | `"en"`           | Language code for search results (e.g., "en", "es").            |
| `num_results`     | `int`           | `10`             | Default number of search results to retrieve.                   |
| `date_range`      | `Optional[str]` | `None`           | Default date range filter for searches.                         |
| `sort_reviews_by` | `Optional[str]` | `"mostRelevant"` | Sort order for reviews search ("mostRelevant", "newest", etc.). |

## Toolkit Functions

| Function         | Description                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------------------- |
| `search`         | Searches Google for a query. Parameters: `query` (str), optional `num_results` (int).                             |
| `search_news`    | Searches for news articles. Parameters: `query` (str), optional `num_results` (int).                              |
| `search_scholar` | Searches Google Scholar for academic papers. Parameters: `query` (str), optional `num_results` (int).             |
| `search_reviews` | Searches for reviews using place identifiers. Parameters: optional `place_id`, `cid`, `fid`, or `topic_id` (str). |
| `scrape_webpage` | Scrapes content from a webpage. Parameters: `url` (str), optional `markdown` (bool).                              |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/serper.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/serper_tools.py)


