---
title: Add a user memory that will persist across restarts
category: knowledge
source_lines: 63306-63316
line_count: 10
---

# Add a user memory that will persist across restarts
user_id = "user@example.com"
memory.add_user_memory(
    memory=UserMemory(
        memory="The user prefers dark mode in applications",
        topics=["preferences", "ui"]
    ),
    user_id=user_id
)

