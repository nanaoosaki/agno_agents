---
title: Create agent with reasoning=True (default model COT)
category: misc
source_lines: 21668-21675
line_count: 7
---

# Create agent with reasoning=True (default model COT)
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    reasoning=True,
    markdown=True,
)

