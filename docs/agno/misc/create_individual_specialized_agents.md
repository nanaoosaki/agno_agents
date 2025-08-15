---
title: Create individual specialized agents
category: misc
source_lines: 69804-69818
line_count: 14
---

# Create individual specialized agents
researcher = Agent(
    name="Researcher",
    role="Expert at finding information",
    tools=[DuckDuckGoTools()],
    model=OpenAIChat("gpt-4o"),
)

writer = Agent(
    name="Writer",
    role="Expert at writing clear, engaging content",
    model=OpenAIChat("gpt-4o"),
)

