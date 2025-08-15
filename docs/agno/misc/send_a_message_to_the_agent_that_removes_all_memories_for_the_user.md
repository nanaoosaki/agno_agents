---
title: Send a message to the agent that removes all memories for the user
category: misc
source_lines: 63015-63039
line_count: 24
---

# Send a message to the agent that removes all memories for the user
agent.print_response(
    "Remove all existing memories of me.",
    stream=True,
    user_id=john_doe_id,
)
memories = memory.get_user_memories(user_id=john_doe_id)
print("Memories about John Doe:")
pprint(memories)
```

## Memory Management

The `Memory` class in Agno lets you manage all aspects of user memory. Let's start with some examples of using `Memory` outside of Agents. We will:

* Add, update and delete memories
* Store memories in a database
* Create memories from conversations
* Search over memories

```python
from agno.memory.v2.memory import Memory
from agno.memory.v2.db.sqlite import SqliteMemoryDb

