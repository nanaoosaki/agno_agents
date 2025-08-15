---
title: Create individual steps
category: misc
source_lines: 55753-55759
line_count: 6
---

# Create individual steps
research_hn_step = Step(name="Research HackerNews", agent=researcher)
research_web_step = Step(name="Research Web", agent=researcher)
write_step = Step(name="Write Article", agent=writer)
review_step = Step(name="Review Article", agent=reviewer)

