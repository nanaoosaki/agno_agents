---
title: Create a Loop step for deep tech research
category: misc
source_lines: 55988-55997
line_count: 9
---

# Create a Loop step for deep tech research
deep_tech_research_loop = Loop(
    name="Deep Tech Research Loop",
    steps=[research_hackernews],
    end_condition=research_quality_check,
    max_iterations=3,
    description="Perform iterative deep research on tech topics",
)

