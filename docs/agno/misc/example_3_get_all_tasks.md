---
title: Example 3: Get all tasks
category: misc
source_lines: 76879-76908
line_count: 29
---

# Example 3: Get all tasks
print("\n=== Get all tasks ===")
todoist_agent.print_response("Get all the todoist tasks")
```

## Toolkit Params

| Parameter   | Type  | Default | Description                                             |
| ----------- | ----- | ------- | ------------------------------------------------------- |
| `api_token` | `str` | `None`  | If you want to manually supply the TODOIST\_API\_TOKEN. |

## Toolkit Functions

| Function           | Description                                                                                     |
| ------------------ | ----------------------------------------------------------------------------------------------- |
| `create_task`      | Creates a new task in Todoist with optional project assignment, due date, priority, and labels. |
| `get_task`         | Fetches a specific task.                                                                        |
| `update_task`      | Updates an existing task with new properties such as content, due date, priority, etc.          |
| `close_task`       | Marks a task as completed.                                                                      |
| `delete_task`      | Deletes a specific task from Todoist.                                                           |
| `get_active_tasks` | Retrieves all active (non-completed) tasks.                                                     |
| `get_projects`     | Retrieves all projects in Todoist.                                                              |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/todoist.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/todoist_tool.py)


