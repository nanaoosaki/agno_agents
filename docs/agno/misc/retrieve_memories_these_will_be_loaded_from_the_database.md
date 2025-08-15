---
title: Retrieve memories (these will be loaded from the database)
category: misc
source_lines: 63316-63329
line_count: 13
---

# Retrieve memories (these will be loaded from the database)
user_memories = memory.get_user_memories(user_id=user_id)
for m in user_memories:
    print(f"Memory: {m.memory}")
    print(f"Topics: {m.topics}")
    print(f"Last Updated: {m.last_updated}")
```

```python postgres_memory.py
from agno.memory.v2.memory import Memory
from agno.memory.v2.db.postgres import PostgresMemoryDb
from agno.memory.v2.schema import UserMemory

