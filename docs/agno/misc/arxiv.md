---
title: Arxiv
category: misc
source_lines: 77210-77258
line_count: 48
---

# Arxiv
Source: https://docs.agno.com/tools/toolkits/search/arxiv



**ArxivTools** enable an Agent to search for publications on Arxiv.

## Prerequisites

The following example requires the `arxiv` and `pypdf` libraries.

```shell
pip install -U arxiv pypdf
```

## Example

The following agent will run seach arXiv for "language models" and print the response.

```python cookbook/tools/arxiv_tools.py
from agno.agent import Agent
from agno.tools.arxiv import ArxivTools

agent = Agent(tools=[ArxivTools()], show_tool_calls=True)
agent.print_response("Search arxiv for 'language models'", markdown=True)
```

## Toolkit Params

| Parameter           | Type   | Default | Description                                                        |
| ------------------- | ------ | ------- | ------------------------------------------------------------------ |
| `search_arxiv`      | `bool` | `True`  | Enables the functionality to search the arXiv database.            |
| `read_arxiv_papers` | `bool` | `True`  | Allows reading of arXiv papers directly.                           |
| `download_dir`      | `Path` | -       | Specifies the directory path where downloaded files will be saved. |

## Toolkit Functions

| Function                                 | Description                                                                                        |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `search_arxiv_and_update_knowledge_base` | This function searches arXiv for a topic, adds the results to the knowledge base and returns them. |
| `search_arxiv`                           | Searches arXiv for a query.                                                                        |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/arxiv.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/arxiv_tools.py)


