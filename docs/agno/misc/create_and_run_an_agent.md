---
title: Create and run an agent
category: misc
source_lines: 65703-65707
line_count: 4
---

# Create and run an agent
agent = Agent(model=OpenAIChat(id="gpt-4o"))
response = agent.run("Share a 2 sentence horror story")

