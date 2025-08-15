---
title: Asynchronous streaming
category: advanced
source_lines: 70372-70384
line_count: 12
---

# Asynchronous streaming
async for chunk in await team.arun("What is the weather in Tokyo?", stream=True):
    print(chunk.content, end="", flush=True)
```

## Streaming Intermediate Steps

Throughout the execution of a team, multiple events take place, and we provide these events in real-time for enhanced team transparency.

You can enable streaming of intermediate steps by setting `stream_intermediate_steps=True`.

```python
