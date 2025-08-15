---
title: Create a SQLite database for memory
category: knowledge
source_lines: 63272-63278
line_count: 6
---

# Create a SQLite database for memory
memory_db = SqliteMemoryDb(
    table_name="memories",  # The table name to use
    db_file="path/to/memory.db"  # The SQLite database file
)

