---
title: Replace a user memory
category: knowledge
source_lines: 63070-63090
line_count: 20
---

# Replace a user memory
memory_id = memory.replace_user_memory(
    # The id of the memory to replace
    memory_id=previous_memory_id,
    # The new memory to replace it with
    memory=UserMemory(
        memory="The user's name is Verna Doe",
        topics=["personal", "name"]
    ),
    user_id="jane_doe@example.com"
)
```

### Deleting a memory

```python
from agno.memory.v2.memory import Memory

memory = Memory()

