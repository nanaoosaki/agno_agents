---
title: Run agent and return the response as a stream
category: misc
source_lines: 1569-1575
line_count: 6
---

# Run agent and return the response as a stream
response_stream: Iterator[RunResponseEvent] = agent.run(
    "Tell me a 5 second short story about a lion",
    stream=True
)

