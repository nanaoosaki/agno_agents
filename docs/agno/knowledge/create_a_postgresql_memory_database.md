---
title: Create a PostgreSQL memory database
category: knowledge
source_lines: 63329-63335
line_count: 6
---

# Create a PostgreSQL memory database
memory_db = PostgresMemoryDb(
    table_name="user_memories",
    connection_string="postgresql://user:password@localhost:5432/mydb"
)

