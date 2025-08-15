---
title: Create and configure the agent
category: misc
source_lines: 66540-66549
line_count: 9
---

# Create and configure the agent
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[YFinanceTools(stock_price=True)],
    instructions="Use tables to display data. Don't include any other text.",
    markdown=True,
    debug_mode=True
)

