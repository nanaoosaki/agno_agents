---
title: Pubmed
category: misc
source_lines: 77674-77712
line_count: 38
---

# Pubmed
Source: https://docs.agno.com/tools/toolkits/search/pubmed



**PubmedTools** enable an Agent to search for Pubmed for articles.

## Example

The following agent will search Pubmed for articles related to "ulcerative colitis".

```python cookbook/tools/pubmed.py
from agno.agent import Agent
from agno.tools.pubmed import PubmedTools

agent = Agent(tools=[PubmedTools()], show_tool_calls=True)
agent.print_response("Tell me about ulcerative colitis.")
```

## Toolkit Params

| Parameter     | Type  | Default                    | Description                                                            |
| ------------- | ----- | -------------------------- | ---------------------------------------------------------------------- |
| `email`       | `str` | `"your_email@example.com"` | Specifies the email address to use.                                    |
| `max_results` | `int` | `None`                     | Optional parameter to specify the maximum number of results to return. |

## Toolkit Functions

| Function        | Description                                                                                                                                                                                                                                                                                 |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `search_pubmed` | Searches PubMed for articles based on a specified query. Parameters include `query` for the search term and `max_results` for the maximum number of results to return (default is 10). Returns a JSON string containing the search results, including publication date, title, and summary. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/pubmed.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/pubmed_tools.py)


