---
title: Add memories for Jane Doe
category: misc
source_lines: 16578-16593
line_count: 15
---

# Add memories for Jane Doe
jane_doe_id = "jane_doe@example.com"
print(f"\nUser: {jane_doe_id}")
memory_id_1 = memory.add_user_memory(
    memory=UserMemory(memory="The user's name is Jane Doe", topics=["name"]),
    user_id=jane_doe_id,
)
memory_id_2 = memory.add_user_memory(
    memory=UserMemory(memory="She likes to play tennis", topics=["hobbies"]),
    user_id=jane_doe_id,
)
memories = memory.get_user_memories(user_id=jane_doe_id)
print("Memories:")
pprint(memories)

