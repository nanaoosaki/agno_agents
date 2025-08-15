---
title: Example 1: Business Search
category: misc
source_lines: 28996-29004
line_count: 8
---

# Example 1: Business Search
print("\n=== Business Search Example ===")
agent.print_response(
    "Find me highly rated Indian restaurants in Phoenix, AZ with their contact details",
    markdown=True,
    stream=True,
)

