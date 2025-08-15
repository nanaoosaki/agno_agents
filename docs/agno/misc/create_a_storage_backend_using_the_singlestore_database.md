---
title: Create a storage backend using the Singlestore database
category: misc
source_lines: 69180-69190
line_count: 10
---

# Create a storage backend using the Singlestore database
storage = SingleStoreStorage(
    # store sessions in the ai.sessions table
    table_name="agent_sessions",
    # db_engine: Singlestore database engine
    db_engine=db_engine,
    # schema: Singlestore schema
    schema=DATABASE,
)

