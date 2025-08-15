---
title: Create agents
category: misc
source_lines: 55748-55753
line_count: 5
---

# Create agents
researcher = Agent(name="Researcher", tools=[HackerNewsTools(), GoogleSearchTools()])
writer = Agent(name="Writer")
reviewer = Agent(name="Reviewer")

