---
title: Create a reusable content creation sequence
category: misc
source_lines: 84838-84849
line_count: 11
---

# Create a reusable content creation sequence
article_creation_sequence = Steps(
    name="ArticleCreation",
    description="Complete article creation workflow from research to final edit",
    steps=[
        Step(name="research", agent=researcher),
        Step(name="writing", agent=writer), 
        Step(name="editing", agent=editor),
    ],
)

