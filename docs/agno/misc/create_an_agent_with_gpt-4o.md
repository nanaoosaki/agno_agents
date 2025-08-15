---
title: Create an agent with GPT-4o
category: misc
source_lines: 64629-64638
line_count: 9
---

# Create an agent with GPT-4o
agent = Agent(
    model=LiteLLM(
        id="gpt-4o",  # Model ID to use
        name="LiteLLM",  # Optional display name
    ),
    markdown=True,
)

