---
title: Linear
category: misc
source_lines: 76198-76261
line_count: 63
---

# Linear
Source: https://docs.agno.com/tools/toolkits/others/linear



**LinearTool** enable an Agent to perform [Linear](https://linear.app/) tasks.

## Prerequisites

The following examples require Linear API key, which can be obtained from [here](https://linear.app/settings/account/security).

```shell
export LINEAR_API_KEY="LINEAR_API_KEY"
```

## Example

The following agent will use Linear API to search for issues in a project for a specific user.

```python cookbook/tools/linear_tools.py
from agno.agent import Agent
from agno.tools.linear import LinearTools

agent = Agent(
    name="Linear Tool Agent",
    tools=[LinearTools()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Show all the issues assigned to user id: 12021")
```

## Toolkit Params

| Parameter                  | Type   | Default | Description                             |
| -------------------------- | ------ | ------- | --------------------------------------- |
| `get_user_details`         | `bool` | `True`  | Enable `get_user_details` tool.         |
| `get_issue_details`        | `bool` | `True`  | Enable `get_issue_details` tool.        |
| `create_issue`             | `bool` | `True`  | Enable `create_issue` tool.             |
| `update_issue`             | `bool` | `True`  | Enable `update_issue` tool.             |
| `get_user_assigned_issues` | `bool` | `True`  | Enable `get_user_assigned_issues` tool. |
| `get_workflow_issues`      | `bool` | `True`  | Enable `get_workflow_issues` tool.      |
| `get_high_priority_issues` | `bool` | `True`  | Enable `get_high_priority_issues` tool. |

## Toolkit Functions

| Function                   | Description                                                      |
| -------------------------- | ---------------------------------------------------------------- |
| `get_user_details`         | Fetch authenticated user details.                                |
| `get_issue_details`        | Retrieve details of a specific issue by issue ID.                |
| `create_issue`             | Create a new issue within a specific project and team.           |
| `update_issue`             | Update the title or state of a specific issue by issue ID.       |
| `get_user_assigned_issues` | Retrieve issues assigned to a specific user by user ID.          |
| `get_workflow_issues`      | Retrieve issues within a specific workflow state by workflow ID. |
| `get_high_priority_issues` | Retrieve issues with a high priority (priority `<=` 2).          |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/linear.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/linear_tools.py)


