---
title: E2B Code Execution
category: misc
source_lines: 28560-28597
line_count: 37
---

# E2B Code Execution
Source: https://docs.agno.com/examples/concepts/tools/others/e2b

Learn to use Agno's E2B integration to run your Agent-generated code in a secure sandbox.

## Code

```python cookbook/tools/e2b_tools.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.e2b import E2BTools

e2b_tools = E2BTools(
    timeout=600,  # 10 minutes timeout (in seconds)
    filesystem=True,
    internet_access=True,
    sandbox_management=True,
    command_execution=True,
)

agent = Agent(
    name="Code Execution Sandbox",
    agent_id="e2b-sandbox",
    model=OpenAIChat(id="gpt-4o"),
    tools=[e2b_tools],
    markdown=True,
    show_tool_calls=True,
    instructions=[
        "You are an expert at writing and validating Python code using a secure E2B sandbox environment.",
        "Your primary purpose is to:",
        "1. Write clear, efficient Python code based on user requests",
        "2. Execute and verify the code in the E2B sandbox",
        "3. Share the complete code with the user, as this is the main use case",
        "4. Provide thorough explanations of how the code works",
    ],
)

