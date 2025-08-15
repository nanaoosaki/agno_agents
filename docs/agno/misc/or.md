---
title: or
category: misc
source_lines: 75074-75123
line_count: 49
---

# or
export CONFLUENCE_API_KEY="your-api-key"
```

## Example

The following agent will retrieve the number of spaces and their names.

```python
from agno.agent import Agent
from agno.tools.confluence import ConfluenceTools

agent = Agent(
    name="Confluence agent",
    tools=[ConfluenceTools()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("How many spaces are there and what are their names?")
```

## Toolkit Functions

| Parameter    | Type   | Default | Description                                                                                                             |
| ------------ | ------ | ------- | ----------------------------------------------------------------------------------------------------------------------- |
| `username`   | `str`  | -       | Confluence username. Can also be set via environment variable CONFLUENCE\_USERNAME.                                     |
| `password`   | `str`  | -       | Confluence password or API key. Can also be set via environment variables CONFLUENCE\_API\_KEY or CONFLUENCE\_PASSWORD. |
| `url`        | `str`  | -       | Confluence instance URL. Can also be set via environment variable CONFLUENCE\_URL.                                      |
| `api_key`    | `str`  | -       | Confluence API key (alternative to password).                                                                           |
| `ssl_verify` | `bool` | `True`  | If True, verify the SSL certificate.                                                                                    |

## Toolkit Functions

| Function                  | Description                                                     |
| ------------------------- | --------------------------------------------------------------- |
| `get_page_content`        | Gets the content of a specific page.                            |
| `get_all_space_detail`    | Gets details about all Confluence spaces.                       |
| `get_space_key`           | Gets the Confluence key for the specified space.                |
| `get_all_page_from_space` | Gets details of all pages from the specified space.             |
| `create_page`             | Creates a new Confluence page with the provided title and body. |
| `update_page`             | Updates an existing Confluence page.                            |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/confluence.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/confluence.py)


