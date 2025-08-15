---
title: Create an agent that manages the shopping list
category: misc
source_lines: 70620-70629
line_count: 9
---

# Create an agent that manages the shopping list
shopping_agent = Agent(
    name="Shopping List Agent",
    role="Manage the shopping list",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[add_item, remove_item],
)


