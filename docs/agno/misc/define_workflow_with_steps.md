---
title: Define workflow with steps
category: misc
source_lines: 82796-82805
line_count: 9
---

# Define workflow with steps
workflow = Workflow(
    name="Content Creation Workflow",
    steps=[
        Step(name="Research Step", team=research_team),
        Step(name="Content Planning Step", executor=custom_content_planning_function),
    ]
)

