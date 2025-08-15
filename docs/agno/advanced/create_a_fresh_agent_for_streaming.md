---
title: Create a fresh agent for streaming
category: advanced
source_lines: 21712-21719
line_count: 7
---

# Create a fresh agent for streaming
streaming_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    reasoning=True,
    markdown=True,
)

