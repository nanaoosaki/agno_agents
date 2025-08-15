---
title: Add a memory for the default user
category: knowledge
source_lines: 16571-16578
line_count: 7
---

# Add a memory for the default user
memory.add_user_memory(
    memory=UserMemory(memory="The user's name is John Doe", topics=["name"]),
)
print("Memories:")
pprint(memory.memories)

