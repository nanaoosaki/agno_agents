---
title: Create memory storage
category: knowledge
source_lines: 63363-63370
line_count: 7
---

# Create memory storage
memory_db = SqliteMemoryDb(
    table_name="memories",
    db_file="tmp/memory.db"
)
memory = Memory(db=memory_db)

