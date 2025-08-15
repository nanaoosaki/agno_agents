---
title: E2B
category: misc
source_lines: 75363-75422
line_count: 59
---

# E2B
Source: https://docs.agno.com/tools/toolkits/others/e2b

Enable your Agents to run code in a remote, secure sandbox.

**E2BTools** enable an Agent to execute code in a secure sandboxed environment with support for Python, file operations, and web server capabilities.

## Prerequisites

The E2B tools require the `e2b_code_interpreter` Python package and an E2B API key.

```shell
pip install e2b_code_interpreter
```

```shell
export E2B_API_KEY=your_api_key
```

## Example

The following example demonstrates how to create an agent that can run Python code in a secure sandbox:

```python cookbook/tools/e2b_tools.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.e2b import E2BTools

e2b_tools = E2BTools(
    timeout=600,  # 10 minutes timeout (in seconds)
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
        "",
        "You can use these tools:",
        "1. Run Python code (run_python_code)",
        "2. Upload files to the sandbox (upload_file)",
        "3. Download files from the sandbox (download_file_from_sandbox)",
        "4. Generate and add visualizations as image artifacts (download_png_result)",
        "5. List files in the sandbox (list_files)",
        "6. Read and write file content (read_file_content, write_file_content)",
        "7. Start web servers and get public URLs (run_server, get_public_url)",
        "8. Manage the sandbox lifecycle (set_sandbox_timeout, get_sandbox_status, shutdown_sandbox)",
    ],
)

