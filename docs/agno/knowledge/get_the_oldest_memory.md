---
title: Get the oldest memory
category: knowledge
source_lines: 63190-63207
line_count: 17
---

# Get the oldest memory
memories = memory.search_user_memories(
    user_id=john_doe_id, limit=1, retrieval_method="first_n"
)
print("John Doe's first_n memories:")
for i, m in enumerate(memories):
    print(f"{i}: {m.memory}")
```

### Agentic Memory Search

Agentic search allows you to find memories based on meaning rather than exact keyword matches. This is particularly useful for retrieving contextually relevant information:

```python
from agno.memory.v2.memory import Memory, UserMemory
from agno.models.google.gemini import Gemini

