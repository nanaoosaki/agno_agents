---
title: Create streaming team
category: advanced
source_lines: 70867-70878
line_count: 11
---

# Create streaming team
market_research_team = Team(
    name="Market Research Team",
    mode="coordinate", 
    model=OpenAIChat("gpt-4o"),
    members=[trend_analyst, risk_assessor],
    response_model=MarketAnalysis,
    markdown=True,
    show_members_responses=True,
)

