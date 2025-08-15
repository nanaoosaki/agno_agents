---
title: Daytona
category: misc
source_lines: 75252-75363
line_count: 111
---

# Daytona
Source: https://docs.agno.com/tools/toolkits/others/daytona

The toolkit enables an Agent to execute code in a secure, remote Daytona sandbox environment.

## Prerequisites

The Daytona tools require the `daytona` Python package

```shell
pip install daytona
```

The API credentials can be obtained from the [Daytona Dashboard](https://app.daytona.io/dashboard/keys):

```shell
export DAYTONA_API_KEY=<your_api_key>
export DAYTONA_API_URL=<your_api_url>  # optional
```

## Example

```python cookbook/tools/daytona_tools.py
from textwrap import dedent

from agno.agent import Agent
from agno.tools.daytona import DaytonaTools

agent = Agent(
    name="Coding Agent with Daytona tools",
    tools=[DaytonaTools()],
    markdown=True,
    instructions=dedent("""
    You are an expert at writing and executing code. You have access to a remote, secure Daytona sandbox.
    Your primary purpose is to:
        1. Write clear, efficient code based on user requests
        2. ALWAYS execute the code in the Daytona sandbox using run_code
        3. Show the actual execution results to the user
        4. Provide explanations of how the code works and what the output means
    Guidelines:
        - NEVER just provide code without executing it
        - Execute all code using the run_code tool to show real results
        - Support Python, JavaScript, and TypeScript execution
        - Use file operations (create_file, read_file) when working with scripts
        - Install missing packages when needed using run_shell_command
        - Always show both the code AND the execution output
        - Handle errors gracefully and explain any issues encountered
    """),
    show_tool_calls=True,
)

agent.print_response(
    "Write JavaScript code to generate 10 random numbers between 1 and 100, sort them in ascending order, and print each number"
)
```

## Toolkit Params

| Parameter             | Type             | Default            | Description                                                             |
| --------------------- | ---------------- | ------------------ | ----------------------------------------------------------------------- |
| `api_key`             | `str`            | `DAYTONA_API_KEY`  | Daytona API key. Defaults to environment variable                       |
| `api_url`             | `str`            | `DAYTONA_API_URL`  | Daytona API URL. Defaults to environment variable                       |
| `sandbox_id`          | `str`            | `None`             | Specific sandbox ID to use. If None, creates or uses persistent sandbox |
| `sandbox_language`    | `CodeLanguage`   | `PYTHON`           | Primary language for the sandbox (PYTHON, JAVASCRIPT, TYPESCRIPT)       |
| `sandbox_target`      | `str`            | `None`             | Target configuration for the sandbox                                    |
| `sandbox_os`          | `str`            | `None`             | Operating system for the sandbox                                        |
| `auto_stop_interval`  | `int`            | `60`               | Auto-stop interval in minutes (0 to disable)                            |
| `sandbox_os_user`     | `str`            | `None`             | OS user for the sandbox                                                 |
| `sandbox_env_vars`    | `Dict[str, str]` | `None`             | Environment variables for the sandbox                                   |
| `sandbox_labels`      | `Dict[str, str]` | `{}`               | Labels for the sandbox                                                  |
| `sandbox_public`      | `bool`           | `None`             | Whether the sandbox should be public                                    |
| `organization_id`     | `str`            | `None`             | Organization ID for the sandbox                                         |
| `timeout`             | `int`            | `300`              | Timeout for sandbox operations in seconds                               |
| `auto_create_sandbox` | `bool`           | `True`             | Automatically create sandbox if none exists                             |
| `verify_ssl`          | `bool`           | `False`            | Whether to verify SSL certificates                                      |
| `persistent`          | `bool`           | `True`             | Whether to reuse the same sandbox across agent sessions                 |
| `instructions`        | `str`            | Default guidelines | Custom instructions for the toolkit                                     |
| `add_instructions`    | `bool`           | `False`            | Whether to add instructions to the agent                                |

## Toolkit Functions

### Code Execution

| Function   | Description                                                   |
| ---------- | ------------------------------------------------------------- |
| `run_code` | Execute Python, JavaScript, or TypeScript code in the sandbox |

### File Operations

| Function      | Description                                  |
| ------------- | -------------------------------------------- |
| `create_file` | Create or update files in the sandbox        |
| `read_file`   | Read file contents from the sandbox          |
| `list_files`  | List directory contents in the sandbox       |
| `delete_file` | Delete files or directories from the sandbox |

### Shell & Environment

| Function            | Description                                         |
| ------------------- | --------------------------------------------------- |
| `run_shell_command` | Execute shell commands (bash) in the sandbox        |
| `change_directory`  | Change the current working directory in the sandbox |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/daytona.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/daytona_tools.py)
* [Daytona Documentation](https://daytona.io/docs)
* [Daytona Console](https://app.daytona.io/dashboard/keys)


