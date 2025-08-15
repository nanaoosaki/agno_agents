---
title: Zendesk
category: misc
source_lines: 77157-77210
line_count: 53
---

# Zendesk
Source: https://docs.agno.com/tools/toolkits/others/zendesk



**ZendeskTools** enable an Agent to access Zendesk API to search for articles.

## Prerequisites

The following example requires the `requests` library and auth credentials.

```shell
pip install -U requests
```

```shell
export ZENDESK_USERNAME=***
export ZENDESK_PW=***
export ZENDESK_COMPANY_NAME=***
```

## Example

The following agent will run seach Zendesk for "How do I login?" and print the response.

```python cookbook/tools/zendesk_tools.py
from agno.agent import Agent
from agno.tools.zendesk import ZendeskTools

agent = Agent(tools=[ZendeskTools()], show_tool_calls=True)
agent.print_response("How do I login?", markdown=True)
```

## Toolkit Params

| Parameter      | Type  | Default | Description                                                             |
| -------------- | ----- | ------- | ----------------------------------------------------------------------- |
| `username`     | `str` | -       | The username used for authentication or identification purposes.        |
| `password`     | `str` | -       | The password associated with the username for authentication purposes.  |
| `company_name` | `str` | -       | The name of the company related to the user or the data being accessed. |

## Toolkit Functions

| Function         | Description                                                                                    |
| ---------------- | ---------------------------------------------------------------------------------------------- |
| `search_zendesk` | This function searches for articles in Zendesk Help Center that match the given search string. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/zendesk.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/zendesk_tools.py)


