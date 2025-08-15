---
title: Create a user memory manually
category: knowledge
source_lines: 63052-63070
line_count: 18
---

# Create a user memory manually
memory_id = memory.add_user_memory(
    memory=UserMemory(
        memory="The user's name is Jane Doe",
        topics=["personal", "name"]
    ),
    user_id="jane_doe@example.com"
)
```

### Updating a memory

```python
from agno.memory.v2.memory import Memory
from agno.memory.v2.schema import UserMemory

memory = Memory()

