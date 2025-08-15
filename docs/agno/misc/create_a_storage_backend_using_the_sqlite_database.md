---
title: Create a storage backend using the Sqlite database
category: misc
source_lines: 69217-69225
line_count: 8
---

# Create a storage backend using the Sqlite database
storage = SqliteStorage(
    # store sessions in the ai.sessions table
    table_name="agent_sessions",
    # db_file: Sqlite database file
    db_file="tmp/data.db",
)

