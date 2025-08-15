---
title: Delete a memory
category: knowledge
source_lines: 16593-16601
line_count: 8
---

# Delete a memory
print("\nDeleting memory")
memory.delete_user_memory(user_id=jane_doe_id, memory_id=memory_id_2)
print("Memory deleted\n")
memories = memory.get_user_memories(user_id=jane_doe_id)
print("Memories:")
pprint(memories)

