---
title: Create agent with both memory and storage
category: knowledge
source_lines: 63376-63390
line_count: 14
---

# Create agent with both memory and storage
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    memory=memory,
    storage=agent_storage,
    enable_user_memories=True,
)
```

## Memory Management

When using persistent storage, the Memory system offers several functions to manage stored memories:

```python
