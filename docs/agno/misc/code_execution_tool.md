---
title: Code Execution Tool
category: misc
source_lines: 36827-36861
line_count: 34
---

# Code Execution Tool
Source: https://docs.agno.com/examples/models/anthropic/code_execution

Learn how to use Anthropic's code execution tool with Agno.

With Anthropic's [code execution tool](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool), your model can execute Python code in a secure, sandboxed environment.
This is useful for your model to perform tasks as analyzing data, creating visualizations, or performing complex calculations.

## Working example

```python
from agno.agent import Agent
from agno.models.anthropic import Claude

agent = Agent(
    model=Claude(
        id="claude-sonnet-4-20250514",
        default_headers={
            "anthropic-beta": "code-execution-2025-05-22"
        }
    ),
    tools=[
        {
            "type": "code_execution_20250522",
            "name": "code_execution",
        }
    ],
    markdown=True,
)

agent.print_response("Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]", stream=True)
```


