---
title: Postgres
category: misc
source_lines: 73398-73435
line_count: 37
---

# Postgres
Source: https://docs.agno.com/tools/toolkits/database/postgres



**PostgresTools** enable an Agent to interact with a PostgreSQL database.

## Prerequisites

The following example requires the `psycopg2` library.

```shell
pip install -U psycopg2
```

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

The following agent will list all tables in the database.

```python cookbook/tools/postgres.py
from agno.agent import Agent
from agno.tools.postgres import PostgresTools

