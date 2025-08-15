---
title: Create a storage backend using the Postgres database
category: misc
source_lines: 69063-69071
line_count: 8
---

# Create a storage backend using the Postgres database
storage = PostgresStorage(
    # store sessions in the ai.sessions table
    table_name="agent_sessions",
    # db_url: Postgres database URL
    db_url=db_url,
)

