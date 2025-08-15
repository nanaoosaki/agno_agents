---
title: Financial Analysis Agent
category: misc
source_lines: 66023-66031
line_count: 8
---

# Financial Analysis Agent
finance_agent = Agent(
    name="Financial Analyst",
    model=LangDB(id="xai/grok-4"),
    tools=[YFinanceTools(stock_price=True, company_info=True)],
    instructions="Perform quantitative financial analysis"
)

