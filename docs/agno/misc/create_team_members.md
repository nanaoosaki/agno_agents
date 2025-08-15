---
title: Create team members
category: misc
source_lines: 69972-69980
line_count: 8
---

# Create team members
stock_searcher = Agent(
    name="Stock Searcher",
    model=OpenAIChat("gpt-4o"),
    role="Searches the web for information on a stock.",
    tools=[YFinanceTools()],
)

