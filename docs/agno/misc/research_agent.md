---
title: Research Agent
category: misc
source_lines: 66015-66023
line_count: 8
---

# Research Agent
web_agent = Agent(
    name="Market Research Agent",
    model=LangDB(id="openai/gpt-4.1"),
    tools=[DuckDuckGoTools()],
    instructions="Research current market conditions and news"
)

