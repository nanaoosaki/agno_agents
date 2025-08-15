---
title: Create a fresh agent with reasoning_model for streaming
category: advanced
source_lines: 21742-21749
line_count: 7
---

# Create a fresh agent with reasoning_model for streaming
streaming_agent_with_model = Agent(
    model=OpenAIChat(id="gpt-4o"),
    reasoning_model=OpenAIChat(id="gpt-4o"),
    markdown=True,
)

