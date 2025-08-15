---
title: Coordinated Team
category: misc
source_lines: 66031-66044
line_count: 13
---

# Coordinated Team
reasoning_team = Team(
    name="Finance Reasoning Team",
    mode="coordinate",
    model=LangDB(id="xai/grok-4"),
    members=[web_agent, finance_agent],
    instructions=[
        "Collaborate to provide comprehensive financial insights",
        "Consider both fundamental analysis and market sentiment"
    ],- **Virtual Models**: Automatic model routing based on cost, performance, or capabilities
    success_criteria="Complete financial analysis with recommendations"
)

