---
title: Define steps
category: misc
source_lines: 82947-82958
line_count: 11
---

# Define steps
analysis_step = Step(
    name="Image Analysis Step",
    agent=image_analyzer,
)

research_step = Step(
    name="News Research Step", 
    agent=news_researcher,
)

