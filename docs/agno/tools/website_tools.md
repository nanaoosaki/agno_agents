---
title: Website Tools
category: tools
source_lines: 79857-79903
line_count: 46
---

# Website Tools
Source: https://docs.agno.com/tools/toolkits/web_scrape/website



**WebsiteTools** enable an Agent to parse a website and add its contents to the knowledge base.

## Prerequisites

The following example requires the `beautifulsoup4` library.

```shell
pip install -U beautifulsoup4
```

## Example

The following agent will read the contents of a website and add it to the knowledge base.

```python cookbook/tools/website_tools.py
from agno.agent import Agent
from agno.tools.website import WebsiteTools

agent = Agent(tools=[WebsiteTools()], show_tool_calls=True)
agent.print_response("Search web page: 'https://docs.agno.com/introduction'", markdown=True)
```

## Toolkit Params

| Parameter        | Type                   | Default | Description                                                                                                            |
| ---------------- | ---------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------- |
| `knowledge_base` | `WebsiteKnowledgeBase` | -       | The knowledge base associated with the website, containing various data and resources linked to the website's content. |

## Toolkit Functions

| Function                        | Description                                                                                                                                                                                                          |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `add_website_to_knowledge_base` | This function adds a website's content to the knowledge base. **NOTE:** The website must start with `https://` and should be a valid website. Use this function to get information about products from the internet. |
| `read_url`                      | This function reads a URL and returns the contents.                                                                                                                                                                  |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/website.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/website_tools.py)


