---
title: Create an agent with OpenWeatherTools
category: tools
source_lines: 76647-76657
line_count: 10
---

# Create an agent with OpenWeatherTools
agent = Agent(
    tools=[
        OpenWeatherTools(
            units="imperial",  # Options: 'standard', 'metric', 'imperial'
        )
    ],
    markdown=True,
)

