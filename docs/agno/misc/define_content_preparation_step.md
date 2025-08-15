---
title: Define content preparation step
category: misc
source_lines: 54935-54954
line_count: 19
---

# Define content preparation step
content_prep_step = Step(
    name="ContentPreparation",
    agent=content_agent,
    description="Prepare and organize all research for writing",
)

writing_step = Step(
    name="Writing",
    agent=writer,
    description="Write an article based on the research",
)

editing_step = Step(
    name="Editing",
    agent=editor,
    description="Edit and polish the article",
)

