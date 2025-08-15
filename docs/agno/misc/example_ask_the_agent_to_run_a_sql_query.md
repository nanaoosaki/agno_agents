---
title: Example: Ask the agent to run a SQL query
category: misc
source_lines: 73447-73486
line_count: 39
---

# Example: Ask the agent to run a SQL query
agent.print_response("""
Please run a SQL query to get all users from the users table
who signed up in the last 30 days
""")
```

## Toolkit Params

| Name               | Type                             | Default | Description                                      |
| ------------------ | -------------------------------- | ------- | ------------------------------------------------ |
| `connection`       | `psycopg2.extensions.connection` | `None`  | Optional database connection object.             |
| `db_name`          | `str`                            | `None`  | Optional name of the database to connect to.     |
| `user`             | `str`                            | `None`  | Optional username for database authentication.   |
| `password`         | `str`                            | `None`  | Optional password for database authentication.   |
| `host`             | `str`                            | `None`  | Optional host for the database connection.       |
| `port`             | `int`                            | `None`  | Optional port for the database connection.       |
| `run_queries`      | `bool`                           | `True`  | Enables running SQL queries.                     |
| `inspect_queries`  | `bool`                           | `False` | Enables inspecting SQL queries before execution. |
| `summarize_tables` | `bool`                           | `True`  | Enables summarizing table structures.            |
| `export_tables`    | `bool`                           | `False` | Enables exporting tables from the database.      |

## Toolkit Functions

| Function               | Description                                                                                                                                                                                                                                                                                             |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `show_tables`          | Retrieves and displays a list of tables in the database. Returns the list of tables.                                                                                                                                                                                                                    |
| `describe_table`       | Describes the structure of a specified table by returning its columns, data types, and maximum character length. Parameters include 'table' to specify the table name. Returns the table description.                                                                                                   |
| `summarize_table`      | Summarizes a table by computing aggregates such as min, max, average, standard deviation, and non-null counts for numeric columns. Parameters include 'table' to specify the table name, and an optional 'table\_schema' to specify the schema (default is "public"). Returns the summary of the table. |
| `inspect_query`        | Inspects an SQL query by returning the query plan. Parameters include 'query' to specify the SQL query. Returns the query plan.                                                                                                                                                                         |
| `export_table_to_path` | Exports a specified table in CSV format to a given path. Parameters include 'table' to specify the table name and an optional 'path' to specify where to save the file (default is the current directory). Returns the result of the export operation.                                                  |
| `run_query`            | Executes an SQL query and returns the result. Parameters include 'query' to specify the SQL query. Returns the result of the query execution.                                                                                                                                                           |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/postgres.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/postgres_tools.py)


