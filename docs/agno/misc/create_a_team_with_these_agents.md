---
title: Create a team with these agents
category: misc
source_lines: 69818-69828
line_count: 10
---

# Create a team with these agents
content_team = Team(
    name="Content Team",
    mode="coordinate",
    members=[researcher, writer],
    instructions="You are a team of researchers and writers that work together to create high-quality content.",
    model=OpenAIChat("gpt-4o"),
    markdown=True,
)

