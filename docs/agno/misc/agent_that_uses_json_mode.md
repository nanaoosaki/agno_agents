---
title: Agent that uses JSON mode
category: misc
source_lines: 48003-48010
line_count: 7
---

# Agent that uses JSON mode
json_mode_agent = Agent(
    model=Together(id="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"),
    description="You write movie scripts.",
    response_model=MovieScript,
)

