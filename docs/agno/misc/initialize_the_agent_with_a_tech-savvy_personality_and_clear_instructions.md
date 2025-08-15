---
title: Initialize the agent with a tech-savvy personality and clear instructions
category: misc
source_lines: 71448-71461
line_count: 13
---

# Initialize the agent with a tech-savvy personality and clear instructions
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[get_top_hackernews_stories],
    markdown=True,
)

agent.print_response(
    "Fetch the top 2 hackernews stories?", stream=True, console=console
)
```


