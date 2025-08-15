---
title: Print the response stream in markdown format
category: misc
source_lines: 1575-1584
line_count: 9
---

# Print the response stream in markdown format
pprint_run_response(response_stream, markdown=True)
```

### Streaming Intermediate Steps

For even more detailed streaming, you can enable intermediate steps by setting `stream_intermediate_steps=True`. This will provide real-time updates about the agent's internal processes.

```python
