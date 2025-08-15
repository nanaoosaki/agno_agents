---
title: Memory operations work the same regardless of the backend
category: knowledge
source_lines: 63348-63363
line_count: 15
---

# Memory operations work the same regardless of the backend
print(f"User has {len(memory.get_user_memories(user_id=user_id))} memories stored")
```

## Integrating with Agent Storage

When building agents with memory, you'll often want to store both agent sessions and memories. Agno makes this easy by allowing you to configure both storage systems:

```python
from agno.agent import Agent
from agno.memory.v2.memory import Memory
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage

