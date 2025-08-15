---
title: Async External Tool Execution
category: misc
source_lines: 32301-32397
line_count: 96
---

# Async External Tool Execution
Source: https://docs.agno.com/examples/concepts/user-control-flows/09-external-tool-execution-async

This example demonstrates how to implement asynchronous external tool execution, allowing for non-blocking execution of tools outside of the agent's control.

## Code

```python cookbook/agent_concepts/user_control_flows/external_tool_execution_async.py
import asyncio
import subprocess

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool
from agno.utils import pprint

@tool(external_execution=True)
def execute_shell_command(command: str) -> str:
    """Execute a shell command.

    Args:
        command (str): The shell command to execute

    Returns:
        str: The output of the shell command
    """
    if command.startswith("ls"):
        return subprocess.check_output(command, shell=True).decode("utf-8")
    else:
        raise Exception(f"Unsupported command: {command}")

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[execute_shell_command],
    markdown=True,
)

run_response = asyncio.run(agent.arun("What files do I have in my current directory?"))
if run_response.is_paused:
    for tool in run_response.tools_awaiting_external_execution:
        if tool.tool_name == execute_shell_command.name:
            print(f"Executing {tool.tool_name} with args {tool.tool_args} externally")
            # We execute the tool ourselves. You can also execute something completely external here.
            result = execute_shell_command.entrypoint(**tool.tool_args)
            # We have to set the result on the tool execution object so that the agent can continue
            tool.result = result

    run_response = asyncio.run(agent.acontinue_run(run_response=run_response))
    pprint.pprint_run_response(run_response)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U agno openai
    ```
  </Step>

  <Step title="Run Example">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/user_control_flows/external_tool_execution_async.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/user_control_flows/external_tool_execution_async.py
      ```
    </CodeGroup>
  </Step>
</Steps>

## Key Features

* Uses `agent.arun()` for asynchronous agent execution
* Implements `agent.acontinue_run()` for async continuation
* Maintains the same external tool execution flow as synchronous version
* Demonstrates how to handle async execution with external tools

## Use Cases

* Non-blocking external tool execution
* High-performance applications requiring async execution
* Web applications with external service calls
* Long-running operations with external tools


