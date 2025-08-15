---
title: Delete a user memory
category: knowledge
source_lines: 63090-63139
line_count: 49
---

# Delete a user memory
memory.delete_user_memory(user_id="jane_doe@example.com", memory_id=memory_id)
```

### Creating memories from user information

```python
from agno.memory.v2 import Memory
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.models.google import Gemini

memory_db = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db")
memory = Memory(model=Gemini(id="gemini-2.0-flash-exp"), db=memory_db)

john_doe_id = "john_doe@example.com"

memory.create_user_memories(
    message="""
    I enjoy hiking in the mountains on weekends,
    reading science fiction novels before bed,
    cooking new recipes from different cultures,
    playing chess with friends,
    and attending live music concerts whenever possible.
    Photography has become a recent passion of mine, especially capturing landscapes and street scenes.
    I also like to meditate in the mornings and practice yoga to stay centered.
    """,
    user_id=john_doe_id,
)


memories = memory.get_user_memories(user_id=john_doe_id)
print("John Doe's memories:")
for i, m in enumerate(memories):
    print(f"{i}: {m.memory} - {m.topics}")
```

### Creating memories from a conversation

```python
from agno.memory.v2 import Memory
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.models.google import Gemini
from agno.models.message import Message

memory_db = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db")
memory = Memory(model=Gemini(id="gemini-2.0-flash-exp"), db=memory_db)


jane_doe_id = "jane_doe@example.com"
