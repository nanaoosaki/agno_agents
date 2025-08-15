---
title: Create agent with LangDB model (uses environment variables automatically)
category: misc
source_lines: 65988-65996
line_count: 8
---

# Create agent with LangDB model (uses environment variables automatically)
agent = Agent(
    name="Web Research Agent",
    model=LangDB(id="openai/gpt-4.1"),
    tools=[DuckDuckGoTools()],
    instructions="Answer questions using web search and provide comprehensive information"
)

