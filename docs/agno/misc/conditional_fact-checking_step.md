---
title: Conditional fact-checking step
category: misc
source_lines: 84351-84364
line_count: 13
---

# Conditional fact-checking step
fact_check_step = Step(
    name="fact_check",
    description="Verify facts and claims",
    agent=fact_checker,
)

write_article = Step(
    name="write_article",
    description="Write final article",
    agent=writer,
)

