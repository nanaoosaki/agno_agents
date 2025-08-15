---
title: First run - this will create the cache
category: misc
source_lines: 37442-37448
line_count: 6
---

# First run - this will create the cache
response = agent.run(
    "Explain the difference between REST and GraphQL APIs with examples"
)
print(f"First run cache write tokens = {response.metrics['cache_write_tokens']}")  # type: ignore

