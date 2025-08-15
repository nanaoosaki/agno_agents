---
title: Newspaper
category: misc
source_lines: 79569-79614
line_count: 45
---

# Newspaper
Source: https://docs.agno.com/tools/toolkits/web_scrape/newspaper



**NewspaperTools** enable an Agent to read news articles using the Newspaper4k library.

## Prerequisites

The following example requires the `newspaper3k` library.

```shell
pip install -U newspaper3k
```

## Example

The following agent will summarize the wikipedia article on language models.

```python cookbook/tools/newspaper_tools.py
from agno.agent import Agent
from agno.tools.newspaper import NewspaperTools

agent = Agent(tools=[NewspaperTools()])
agent.print_response("Please summarize https://en.wikipedia.org/wiki/Language_model")
```

## Toolkit Params

| Parameter          | Type   | Default | Description                                                   |
| ------------------ | ------ | ------- | ------------------------------------------------------------- |
| `get_article_text` | `bool` | `True`  | Enables the functionality to retrieve the text of an article. |

## Toolkit Functions

| Function           | Description                                                                                                                                                                             |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `get_article_text` | Retrieves the text of an article from a specified URL. Parameters include `url` for the URL of the article. Returns the text of the article or an error message if the retrieval fails. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/newspaper.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/newspaper_tools.py)


