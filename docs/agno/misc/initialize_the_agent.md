---
title: Initialize the Agent
category: misc
source_lines: 73613-73621
line_count: 8
---

# Initialize the Agent
agent = Agent(
    model=OpenAIChat(),
    tools=[zep_tools],
    context={"memory": zep_tools.get_zep_memory(memory_type="context")},
    add_context=True,
)

