---
title: Second run - this will use the cached system prompt
category: misc
source_lines: 37448-37456
line_count: 8
---

# Second run - this will use the cached system prompt
response = agent.run(
    "What are the key principles of clean code and how do I apply them in Python?"
)
print(f"Second run cache read tokens = {response.metrics['cached_tokens']}")  # type: ignore
```


