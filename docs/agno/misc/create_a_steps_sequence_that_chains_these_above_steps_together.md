---
title: Create a Steps sequence that chains these above steps together
category: misc
source_lines: 54810-54817
line_count: 7
---

# Create a Steps sequence that chains these above steps together
article_creation_sequence = Steps(
    name="article_creation",
    description="Complete article creation workflow from research to final edit",
    steps=[research_step, writing_step, editing_step],
)

