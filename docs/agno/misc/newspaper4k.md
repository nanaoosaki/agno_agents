---
title: Newspaper4k
category: misc
source_lines: 79614-79662
line_count: 48
---

# Newspaper4k
Source: https://docs.agno.com/tools/toolkits/web_scrape/newspaper4k



**Newspaper4k** enables an Agent to read news articles using the Newspaper4k library.

## Prerequisites

The following example requires the `newspaper4k` and `lxml_html_clean` libraries.

```shell
pip install -U newspaper4k lxml_html_clean
```

## Example

The following agent will summarize the article: [https://www.rockymountaineer.com/blog/experience-icefields-parkway-scenic-drive-lifetime](https://www.rockymountaineer.com/blog/experience-icefields-parkway-scenic-drive-lifetime).

```python cookbook/tools/newspaper4k_tools.py
from agno.agent import Agent
from agno.tools.newspaper4k import Newspaper4kTools

agent = Agent(tools=[Newspaper4kTools()], debug_mode=True, show_tool_calls=True)
agent.print_response("Please summarize https://www.rockymountaineer.com/blog/experience-icefields-parkway-scenic-drive-lifetime")
```

## Toolkit Params

| Parameter         | Type   | Default | Description                                                                        |
| ----------------- | ------ | ------- | ---------------------------------------------------------------------------------- |
| `read_article`    | `bool` | `True`  | Enables the functionality to read the full content of an article.                  |
| `include_summary` | `bool` | `False` | Specifies whether to include a summary of the article along with the full content. |
| `article_length`  | `int`  | -       | The maximum length of the article or its summary to be processed or returned.      |

## Toolkit Functions

| Function           | Description                                                  |
| ------------------ | ------------------------------------------------------------ |
| `get_article_data` | This function reads the full content and data of an article. |
| `read_article`     | This function reads the full content of an article.          |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/newspaper4k.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/newspaper4k_tools.py)


