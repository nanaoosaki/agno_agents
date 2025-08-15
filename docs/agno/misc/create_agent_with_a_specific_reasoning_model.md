---
title: Create agent with a specific reasoning_model
category: misc
source_lines: 21689-21696
line_count: 7
---

# Create agent with a specific reasoning_model
agent_with_reasoning_model = Agent(
    model=OpenAIChat(id="gpt-4o"),
    reasoning_model=OpenAIChat(id="gpt-4o"),  # Should default to manual COT
    markdown=True,
)

