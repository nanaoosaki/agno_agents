---
title: === WORKFLOW STEPS ===
category: misc
source_lines: 84338-84351
line_count: 13
---

# === WORKFLOW STEPS ===
research_step = Step(
    name="research",
    description="Research the topic",
    agent=researcher,
)

summarize_step = Step(
    name="summarize",
    description="Summarize research findings",
    agent=summarizer,
)

