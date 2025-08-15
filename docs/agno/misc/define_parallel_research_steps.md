---
title: Define parallel research steps
category: misc
source_lines: 54922-54935
line_count: 13
---

# Define parallel research steps
tech_research_step = Step(
    name="TechResearch",
    agent=tech_researcher,
    description="Research tech developments from Hacker News",
)

news_research_step = Step(
    name="NewsResearch",
    agent=news_researcher,
    description="Research current news and trends",
)

