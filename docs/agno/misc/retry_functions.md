---
title: Retry Functions
category: misc
source_lines: 36028-36092
line_count: 64
---

# Retry Functions
Source: https://docs.agno.com/examples/getting-started/retry-functions



This example shows how to retry a function call if it fails or you do not like the output. This is useful for:

* Handling temporary failures
* Improving output quality through retries
* Implementing human-in-the-loop validation

## Code

```python retry_functions.py
from typing import Iterator

from agno.agent import Agent
from agno.exceptions import RetryAgentRun
from agno.tools import FunctionCall, tool

num_calls = 0


def pre_hook(fc: FunctionCall):
    global num_calls

    print(f"Pre-hook: {fc.function.name}")
    print(f"Arguments: {fc.arguments}")
    num_calls += 1
    if num_calls < 2:
        raise RetryAgentRun(
            "This wasn't interesting enough, please retry with a different argument"
        )


@tool(pre_hook=pre_hook)
def print_something(something: str) -> Iterator[str]:
    print(something)
    yield f"I have printed {something}"


agent = Agent(tools=[print_something], markdown=True)
agent.print_response("Print something interesting", stream=True)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install libraries">
    ```bash
    pip install openai agno
    ```
  </Step>

  <Step title="Run the agent">
    ```bash
    python retry_functions.py
    ```
  </Step>
</Steps>


