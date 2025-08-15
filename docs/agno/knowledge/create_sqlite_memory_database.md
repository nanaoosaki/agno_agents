---
title: Create SQLite memory database
category: knowledge
source_lines: 18201-18207
line_count: 6
---

# Create SQLite memory database
memory_db = SqliteMemoryDb(
    table_name="agent_memories",  # Table name to use in the database
    db_file="tmp/memory.db",      # Path to SQLite database file
)

