---
title: We have to create a tool with the correct name, arguments and docstring for the agent to know what to call.
category: misc
source_lines: 32412-32502
line_count: 90
---

# We have to create a tool with the correct name, arguments and docstring for the agent to know what to call.
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

for run_response in agent.run(
    "What files do I have in my current directory?", stream=True
):
    if run_response.is_paused:
        for tool in run_response.tools_awaiting_external_execution:
            if tool.tool_name == execute_shell_command.name:
                print(
                    f"Executing {tool.tool_name} with args {tool.tool_args} externally"
                )
                # We execute the tool ourselves. You can also execute something completely external here.
                result = execute_shell_command.entrypoint(**tool.tool_args)
                # We have to set the result on the tool execution object so that the agent can continue
                tool.result = result

        run_response = agent.continue_run(
            run_id=agent.run_response.run_id,
            updated_tools=agent.run_response.tools,
            stream=True,
        )
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
      python cookbook/agent_concepts/user_control_flows/external_tool_execution_stream.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/user_control_flows/external_tool_execution_stream.py
      ```
    </CodeGroup>
  </Step>
</Steps>

## Key Features

* Uses `agent.run(stream=True)` for streaming responses
* Implements streaming continuation with `agent.continue_run(stream=True)`
* Maintains real-time interaction with external tool execution
* Demonstrates how to handle streaming responses with external tools

## Use Cases

* Real-time external tool execution
* Streaming applications with external service calls
* Interactive interfaces with external tool execution
* Progressive response generation with external tools


