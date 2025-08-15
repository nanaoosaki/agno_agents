---
title: Print the memories for the user
category: misc
source_lines: 63010-63015
line_count: 5
---

# Print the memories for the user
memories = memory.get_user_memories(user_id=john_doe_id)
print("Memories about John Doe:")
pprint(memories)

