---
title: Create an agent equipped with X toolkit
category: misc
source_lines: 78614-78626
line_count: 12
---

# Create an agent equipped with X toolkit
agent = Agent(
    instructions=[
        "Use X tools to interact as the authorized user",
        "Generate appropriate content when asked to create posts",
        "Only post content when explicitly instructed",
        "Respect X's usage policies and rate limits",
    ],
    tools=[x_tools],
    show_tool_calls=True,
)

