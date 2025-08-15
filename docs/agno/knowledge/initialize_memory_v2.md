---
title: Initialize memory.v2
category: knowledge
source_lines: 62921-62927
line_count: 6
---

# Initialize memory.v2
memory = Memory(
    # Use any model for creating memories
    model=OpenAIChat(id="gpt-4.1"),
    db=SqliteMemoryDb(table_name="user_memories", db_file=db_file),
)
