---
title: Step 2: Create your Agno agent
category: misc
source_lines: 65880-65889
line_count: 9
---

# Step 2: Create your Agno agent
agent = Agent(
    name="Market Analysis Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGoTools()],
    instructions="Provide professional market analysis with data-driven insights.",
    debug_mode=True,
)

