---
title: Send a history of messages and add memories
category: misc
source_lines: 63139-63182
line_count: 43
---

# Send a history of messages and add memories
memory.create_user_memories(
    messages=[
        Message(role="user", content="My name is Jane Doe"),
        Message(role="assistant", content="That is great!"),
        Message(role="user", content="I like to play chess"),
        Message(role="assistant", content="That is great!"),
    ],
    user_id=jane_doe_id,
)

memories = memory.get_user_memories(user_id=jane_doe_id)
print("Jane Doe's memories:")
for i, m in enumerate(memories):
    print(f"{i}: {m.memory} - {m.topics}")
```

## Memory Search

Agno provides several retrieval methods to search and retrieve user memories:

### Basic Retrieval Methods

You can retrieve memories using chronological methods such as `last_n` (most recent) or `first_n` (oldest first):

```python
from agno.memory.v2 import Memory, UserMemory

memory = Memory()

john_doe_id = "john_doe@example.com"

memory.add_user_memory(
    memory=UserMemory(memory="The user enjoys hiking in the mountains on weekends"),
    user_id=john_doe_id,
)
memory.add_user_memory(
    memory=UserMemory(
        memory="The user enjoys reading science fiction novels before bed"
    ),
    user_id=john_doe_id,
)

