---
title: Create a storage backend using the MySQL database
category: misc
source_lines: 25379-25400
line_count: 21
---

# Create a storage backend using the MySQL database
storage = MySQLStorage(
    # store sessions in the agno.workflows table
    table_name="workflow_sessions",
    # db_url: MySQL database URL
    db_url=db_url,
)

  # Add storage to the Workflow
workflow = Workflow(storage=storage)
```

## Params

<Snippet file="storage-mysql-params.mdx" />

## Developer Resources

* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/storage/mysql_storage/mysql_storage_for_workflow.py)


