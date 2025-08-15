---
title: Create the team
category: misc
source_lines: 69980-69988
line_count: 8
---

# Create the team
team = Team(
    name="Stock Research Team",
    model=OpenAIChat("gpt-4o"),
    members=[stock_searcher],
    markdown=True,
)

