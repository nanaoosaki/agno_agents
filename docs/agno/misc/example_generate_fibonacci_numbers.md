---
title: Example: Generate Fibonacci numbers
category: misc
source_lines: 75422-75501
line_count: 79
---

# Example: Generate Fibonacci numbers
agent.print_response(
    "Write Python code to generate the first 10 Fibonacci numbers and calculate their sum and average"
)

```

## Toolkit Params

| Parameter            | Type   | Default | Description                                               |
| -------------------- | ------ | ------- | --------------------------------------------------------- |
| `api_key`            | `str`  | `None`  | E2B API key. If not provided, uses E2B\_API\_KEY env var. |
| `run_code`           | `bool` | `True`  | Whether to register the run\_code function                |
| `upload_file`        | `bool` | `True`  | Whether to register the upload\_file function             |
| `download_result`    | `bool` | `True`  | Whether to register the download\_result functions        |
| `filesystem`         | `bool` | `False` | Whether to register filesystem operations                 |
| `internet_access`    | `bool` | `False` | Whether to register internet access functions             |
| `sandbox_management` | `bool` | `False` | Whether to register sandbox management functions          |
| `timeout`            | `int`  | `300`   | Timeout in seconds for the sandbox (default: 5 minutes)   |
| `sandbox_options`    | `dict` | `None`  | Additional options to pass to the Sandbox constructor     |
| `command_execution`  | `bool` | `False` | Whether to register command execution functions           |

## Toolkit Functions

### Code Execution

| Function          | Description                                    |
| ----------------- | ---------------------------------------------- |
| `run_python_code` | Run Python code in the E2B sandbox environment |

### File Operations

| Function                     | Description                                             |
| ---------------------------- | ------------------------------------------------------- |
| `upload_file`                | Upload a file to the sandbox                            |
| `download_png_result`        | Add a PNG image result as an ImageArtifact to the agent |
| `download_chart_data`        | Extract chart data from an interactive chart in results |
| `download_file_from_sandbox` | Download a file from the sandbox to the local system    |

### Filesystem Operations

| Function             | Description                                            |
| -------------------- | ------------------------------------------------------ |
| `list_files`         | List files and directories in a path in the sandbox    |
| `read_file_content`  | Read the content of a file from the sandbox            |
| `write_file_content` | Write text content to a file in the sandbox            |
| `watch_directory`    | Watch a directory for changes for a specified duration |

### Command Execution

| Function                  | Description                                    |
| ------------------------- | ---------------------------------------------- |
| `run_command`             | Run a shell command in the sandbox environment |
| `stream_command`          | Run a shell command and stream its output      |
| `run_background_command`  | Run a shell command in the background          |
| `kill_background_command` | Kill a background command                      |

### Internet Access

| Function         | Description                                             |
| ---------------- | ------------------------------------------------------- |
| `get_public_url` | Get a public URL for a service running in the sandbox   |
| `run_server`     | Start a server in the sandbox and return its public URL |

### Sandbox Management

| Function                 | Description                           |
| ------------------------ | ------------------------------------- |
| `set_sandbox_timeout`    | Update the timeout for the sandbox    |
| `get_sandbox_status`     | Get the current status of the sandbox |
| `shutdown_sandbox`       | Shutdown the sandbox immediately      |
| `list_running_sandboxes` | List all running sandboxes            |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/e2b.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/e2b_tools.py)


