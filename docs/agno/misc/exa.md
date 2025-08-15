---
title: Exa
category: misc
source_lines: 77421-77514
line_count: 93
---

# Exa
Source: https://docs.agno.com/tools/toolkits/search/exa



**ExaTools** enable an Agent to search the web using Exa, retrieve content from URLs, find similar content, and get AI-powered answers.

## Prerequisites

The following examples require the `exa-py` library and an API key which can be obtained from [Exa](https://exa.ai).

```shell
pip install -U exa-py
```

```shell
export EXA_API_KEY=***
```

## Example

The following agent will search Exa for AAPL news and print the response.

```python cookbook/tools/exa_tools.py
from agno.agent import Agent
from agno.tools.exa import ExaTools

agent = Agent(
    tools=[ExaTools(
        include_domains=["cnbc.com", "reuters.com", "bloomberg.com"],
        category="news",
        text_length_limit=1000,
    )],
    show_tool_calls=True,
)
agent.print_response("Search for AAPL news", markdown=True)
```

## Toolkit Functions

| Function       | Description                                                      |
| -------------- | ---------------------------------------------------------------- |
| `search_exa`   | Searches Exa for a query with optional category filtering        |
| `get_contents` | Retrieves detailed content from specific URLs                    |
| `find_similar` | Finds similar content to a given URL                             |
| `exa_answer`   | Gets an AI-powered answer to a question using Exa search results |

## Toolkit Parameters

| Parameter              | Type                  | Default    | Description                                        |
| ---------------------- | --------------------- | ---------- | -------------------------------------------------- |
| `search`               | `bool`                | `True`     | Enable search functionality                        |
| `get_contents`         | `bool`                | `True`     | Enable content retrieval                           |
| `find_similar`         | `bool`                | `True`     | Enable finding similar content                     |
| `answer`               | `bool`                | `True`     | Enable AI-powered answers                          |
| `text`                 | `bool`                | `True`     | Include text content in results                    |
| `text_length_limit`    | `int`                 | `1000`     | Maximum length of text content per result          |
| `highlights`           | `bool`                | `True`     | Include highlighted snippets                       |
| `summary`              | `bool`                | `False`    | Include result summaries                           |
| `num_results`          | `Optional[int]`       | `None`     | Default number of results                          |
| `livecrawl`            | `str`                 | `"always"` | Livecrawl behavior                                 |
| `start_crawl_date`     | `Optional[str]`       | `None`     | Include results crawled after date (YYYY-MM-DD)    |
| `end_crawl_date`       | `Optional[str]`       | `None`     | Include results crawled before date (YYYY-MM-DD)   |
| `start_published_date` | `Optional[str]`       | `None`     | Include results published after date (YYYY-MM-DD)  |
| `end_published_date`   | `Optional[str]`       | `None`     | Include results published before date (YYYY-MM-DD) |
| `use_autoprompt`       | `Optional[bool]`      | `None`     | Enable autoprompt features                         |
| `type`                 | `Optional[str]`       | `None`     | Content type filter (e.g., article, blog, video)   |
| `category`             | `Optional[str]`       | `None`     | Category filter (e.g., news, research paper)       |
| `include_domains`      | `Optional[List[str]]` | `None`     | Restrict results to these domains                  |
| `exclude_domains`      | `Optional[List[str]]` | `None`     | Exclude results from these domains                 |
| `show_results`         | `bool`                | `False`    | Log search results for debugging                   |
| `model`                | `Optional[str]`       | `None`     | Search model to use ('exa' or 'exa-pro')           |

### Categories

Available categories for filtering:

* company
* research paper
* news
* pdf
* github
* tweet
* personal site
* linkedin profile
* financial report

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/exa.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/exa_tools.py)


