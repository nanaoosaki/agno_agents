---
title: Create agent storage
category: misc
source_lines: 63370-63376
line_count: 6
---

# Create agent storage
agent_storage = SqliteStorage(
    table_name="agent_sessions",
    db_file="tmp/agent_storage.db"
)

