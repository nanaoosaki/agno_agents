---
title: Agent that uses structured outputs
category: misc
source_lines: 47652-47660
line_count: 8
---

# Agent that uses structured outputs
structured_output_agent = Agent(
    model=OpenAIResponses(id="gpt-4o"),  
    description="You write movie scripts.",
    response_model=MovieScript,
)


