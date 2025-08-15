---
title: Postgres Storage
category: misc
source_lines: 69033-69063
line_count: 30
---

# Postgres Storage
Source: https://docs.agno.com/storage/postgres



Agno supports using PostgreSQL as a storage backend for Agents using the `PostgresStorage` class.

## Usage

### Run PgVector

Install [docker desktop](https://docs.docker.com/desktop/install/mac-install/) and run **PgVector** on port **5532** using:

```bash
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

```python postgres_storage_for_agent.py
from agno.storage.postgres import PostgresStorage

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

