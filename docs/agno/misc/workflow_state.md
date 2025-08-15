---
title: Workflow State
category: misc
source_lines: 82262-82274
line_count: 12
---

# Workflow State
Source: https://docs.agno.com/workflows/state



All workflows come with a `session_state` dictionary that you can use to cache intermediate results. The `session_state` is tied to a `session_id` and can be persisted to a database.

Provide your workflows with `storage` to enable persistence of session state in a database.

For example, you can use the `SqliteWorkflowStorage` to cache results in a Sqlite database.

```python
