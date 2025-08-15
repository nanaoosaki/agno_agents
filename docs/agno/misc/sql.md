---
title: SQL
category: misc
source_lines: 73486-73580
line_count: 94
---

# SQL
Source: https://docs.agno.com/tools/toolkits/database/sql



**SQLTools** enable an Agent to run SQL queries and interact with databases.

## Prerequisites

The following example requires the `sqlalchemy` library and a database URL.

```shell
pip install -U sqlalchemy
```

You will also need to install the appropriate Python adapter for the specific database you intend to use.

### PostgreSQL

For PostgreSQL, you can install the `psycopg2-binary` adapter:

```shell
pip install -U psycopg2-binary
```

### MySQL

For MySQL, you can install the `mysqlclient` adapter:

```shell
pip install -U mysqlclient
```

The `mysqlclient` adapter may have additional system-level dependencies. Please consult the [official installation guide](https://github.com/PyMySQL/mysqlclient/blob/main/README.md#install) for more details.

You will also need a database. The following example uses a Postgres database running in a Docker container.

```shell
 docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  agno/pgvector:16
```

## Example

The following agent will run a SQL query to list all tables in the database and describe the contents of one of the tables.

```python cookbook/tools/sql_tools.py
from agno.agent import Agent
from agno.tools.sql import SQLTools

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

agent = Agent(tools=[SQLTools(db_url=db_url)])
agent.print_response("List the tables in the database. Tell me about contents of one of the tables", markdown=True)
```

## Toolkit Params

| Parameter        | Type             | Default | Description                                                                 |
| ---------------- | ---------------- | ------- | --------------------------------------------------------------------------- |
| `db_url`         | `str`            | -       | The URL for connecting to the database.                                     |
| `db_engine`      | `Engine`         | -       | The database engine used for connections and operations.                    |
| `user`           | `str`            | -       | The username for database authentication.                                   |
| `password`       | `str`            | -       | The password for database authentication.                                   |
| `host`           | `str`            | -       | The hostname or IP address of the database server.                          |
| `port`           | `int`            | -       | The port number on which the database server is listening.                  |
| `schema`         | `str`            | -       | The specific schema within the database to use.                             |
| `dialect`        | `str`            | -       | The SQL dialect used by the database.                                       |
| `tables`         | `Dict[str, Any]` | -       | A dictionary mapping table names to their respective metadata or structure. |
| `list_tables`    | `bool`           | `True`  | Enables the functionality to list all tables in the database.               |
| `describe_table` | `bool`           | `True`  | Enables the functionality to describe the schema of a specific table.       |
| `run_sql_query`  | `bool`           | `True`  | Enables the functionality to execute SQL queries directly.                  |

## Toolkit Functions

| Function         | Description                               |
| ---------------- | ----------------------------------------- |
| `list_tables`    | Lists all tables in the database.         |
| `describe_table` | Describes the schema of a specific table. |
| `run_sql_query`  | Executes SQL queries directly.            |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/sql.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/sql_tools.py)


