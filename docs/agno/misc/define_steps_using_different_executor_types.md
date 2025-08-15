---
title: Define steps using different executor types
category: misc
source_lines: 56766-56779
line_count: 13
---

# Define steps using different executor types

research_step = Step(
    name="Research Step",
    team=research_team,
)

content_planning_step = Step(
    name="Content Planning Step",
    executor=custom_content_planning_function,
)


