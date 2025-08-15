---
title: Add user memories
category: misc
source_lines: 63338-63348
line_count: 10
---

# Add user memories
user_id = "user@example.com"
memory.add_user_memory(
    memory=UserMemory(
        memory="The user has a premium subscription",
        topics=["subscription", "account"]
    ),
    user_id=user_id
)

