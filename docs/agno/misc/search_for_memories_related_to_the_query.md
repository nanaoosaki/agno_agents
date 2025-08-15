---
title: Search for memories related to the query
category: misc
source_lines: 63223-63242
line_count: 19
---

# Search for memories related to the query
memories = memory.search_user_memories(
    user_id=john_doe_id,
    query="What does the user like to do on weekends?",
    retrieval_method="agentic",
)
print("John Doe's found memories:")
for i, m in enumerate(memories):
    print(f"{i}: {m.memory}")
```

With agentic search, the model understands the intent behind your query and returns the most relevant memories, even if they don't contain the exact keywords from your search.

## Developer Resources

* Find full examples in the [Cookbook](https://github.com/agno-agi/agno/tree/main/cookbook/agent_concepts/memory)
* View the class reference for the `Memory` class [here](/reference/memory/memory)


