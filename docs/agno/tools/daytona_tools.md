---
title: Daytona Tools
category: tools
source_lines: 28428-28495
line_count: 67
---

# Daytona Tools
Source: https://docs.agno.com/examples/concepts/tools/others/daytona

Learn to use Agno's Daytona integration to run your Agent-generated code in a secure sandbox.

## Code

```python cookbook/tools/daytona_tools.py
from agno.agent import Agent
from agno.tools.daytona import DaytonaTools

agent = Agent(
    name="Coding Agent with Daytona tools",
    tools=[DaytonaTools()],
    markdown=True,
    instructions=[
        "You are an expert at writing and executing code. You have access to a remote, secure Daytona sandbox.",
        "Your primary purpose is to:",
        "1. Write clear, efficient code based on user requests",
        "2. ALWAYS execute the code in the Daytona sandbox using run_code",
        "3. Show the actual execution results to the user",
        "4. Provide explanations of how the code works and what the output means",
        "Guidelines:",
        "- NEVER just provide code without executing it",
        "- Execute all code using the run_code tool to show real results",
        "- Support Python, JavaScript, and TypeScript execution",
        "- Use file operations (create_file, read_file) when working with scripts",
        "- Install missing packages when needed using run_shell_command",
        "- Always show both the code AND the execution output",
        "- Handle errors gracefully and explain any issues encountered",
    ],
    show_tool_calls=True,
)

agent.print_response(
    "Write Python code to generate 10 random numbers between 1 and 100, sort them in ascending order, and print each number"
)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API keys">
    Get your Daytona API key from the [Daytona Dashboard](https://app.daytona.io/dashboard/keys):

    ```bash
    export DAYTONA_API_KEY=<your_api_key>
    export DAYTONA_API_URL=<your_api_url>  # optional
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U agno daytona
    ```
  </Step>

  <Step title="Run Example">
    ```bash
    python cookbook/tools/daytona_tools.py
    ```
  </Step>
</Steps>


