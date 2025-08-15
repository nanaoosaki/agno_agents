---
title: Wikipedia
category: misc
source_lines: 77976-78022
line_count: 46
---

# Wikipedia
Source: https://docs.agno.com/tools/toolkits/search/wikipedia



**WikipediaTools** enable an Agent to search wikipedia a website and add its contents to the knowledge base.

## Prerequisites

The following example requires the `wikipedia` library.

```shell
pip install -U wikipedia
```

## Example

The following agent will run seach wikipedia for "ai" and print the response.

```python cookbook/tools/wikipedia_tools.py
from agno.agent import Agent
from agno.tools.wikipedia import WikipediaTools

agent = Agent(tools=[WikipediaTools()], show_tool_calls=True)
agent.print_response("Search wikipedia for 'ai'")
```

## Toolkit Params

| Name             | Type                     | Default | Description                                                                                                        |
| ---------------- | ------------------------ | ------- | ------------------------------------------------------------------------------------------------------------------ |
| `knowledge_base` | `WikipediaKnowledgeBase` | -       | The knowledge base associated with Wikipedia, containing various data and resources linked to Wikipedia's content. |

## Toolkit Functions

| Function Name                                | Description                                                                                            |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `search_wikipedia_and_update_knowledge_base` | This function searches wikipedia for a topic, adds the results to the knowledge base and returns them. |
| `search_wikipedia`                           | Searches Wikipedia for a query.                                                                        |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/wikipedia.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/wikipedia_tools.py)


