---
title: Get the most recent memory
category: knowledge
source_lines: 63182-63190
line_count: 8
---

# Get the most recent memory
memories = memory.search_user_memories(
    user_id=john_doe_id, limit=1, retrieval_method="last_n"
)
print("John Doe's last_n memories:")
for i, m in enumerate(memories):
    print(f"{i}: {m.memory}")

