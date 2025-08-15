---
title: Create an Agent with the AWSLambdaTool
category: misc
source_lines: 74692-74699
line_count: 7
---

# Create an Agent with the AWSLambdaTool
agent = Agent(
    tools=[AWSLambdaTools(region_name="us-east-1")],
    name="AWS Lambda Agent",
    show_tool_calls=True,
)

