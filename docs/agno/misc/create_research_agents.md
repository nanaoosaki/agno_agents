---
title: Create research agents
category: misc
source_lines: 70852-70867
line_count: 15
---

# Create research agents
trend_analyst = Agent(
    name="Trend Analyst",
    model=OpenAIChat("gpt-4o"),
    role="Analyzes market trends and sector performance.",
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True)]
)

risk_assessor = Agent(
    name="Risk Assessor", 
    model=OpenAIChat("gpt-4o"),
    role="Identifies and evaluates market risks and opportunities.",
    tools=[YFinanceTools(company_news=True, company_info=True)]
)

