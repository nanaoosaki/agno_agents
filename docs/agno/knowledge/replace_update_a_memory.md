---
title: Replace/update a memory
category: knowledge
source_lines: 63393-63400
line_count: 7
---

# Replace/update a memory
memory.replace_user_memory(
    memory_id="memory_123",
    memory=UserMemory(memory="Updated information about the user"),
    user_id="user@example.com"
)

