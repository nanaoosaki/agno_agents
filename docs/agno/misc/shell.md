---
title: Shell
category: misc
source_lines: 73961-73996
line_count: 35
---

# Shell
Source: https://docs.agno.com/tools/toolkits/local/shell



**ShellTools** enable an Agent to interact with the shell to run commands.

## Example

The following agent will run a shell command and show contents of the current directory.

<Note>
  Mention your OS to the agent to make sure it runs the correct command.
</Note>

```python cookbook/tools/shell_tools.py
from agno.agent import Agent
from agno.tools.shell import ShellTools

agent = Agent(tools=[ShellTools()], show_tool_calls=True)
agent.print_response("Show me the contents of the current directory", markdown=True)
```

## Functions in Toolkit

| Function            | Description                                           |
| ------------------- | ----------------------------------------------------- |
| `run_shell_command` | Runs a shell command and returns the output or error. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/shell.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/shell_tools.py)


