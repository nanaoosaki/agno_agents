---
title: Create agents for research
category: misc
source_lines: 55607-55630
line_count: 23
---

# Create agents for research
research_agent = Agent(
    name="Research Agent",
    role="Research specialist",
    tools=[HackerNewsTools(), DuckDuckGoTools()],
    instructions="You are a research specialist. Research the given topic thoroughly.",
    markdown=True,
)

analysis_agent = Agent(
    name="Analysis Agent",
    role="Data analyst",
    instructions="You are a data analyst. Analyze and summarize research findings.",
    markdown=True,
)

content_agent = Agent(
    name="Content Agent",
    role="Content creator",
    instructions="You are a content creator. Create engaging content based on research.",
    markdown=True,
)

