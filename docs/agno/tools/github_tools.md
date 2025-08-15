---
title: GitHub Tools
category: tools
source_lines: 28861-28915
line_count: 54
---

# GitHub Tools
Source: https://docs.agno.com/examples/concepts/tools/others/github



## Code

```python cookbook/tools/github_tools.py
from agno.agent import Agent
from agno.tools.github import GithubTools

agent = Agent(
    instructions=[
        "Use your tools to answer questions about the repo: agno-agi/agno",
        "Do not create any issues or pull requests unless explicitly asked to do so",
    ],
    tools=[GithubTools()],
    show_tool_calls=True,
)
agent.print_response("List open pull requests", markdown=True)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your GitHub token">
    ```bash
    export GITHUB_TOKEN=xxx
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U PyGithub openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/github_tools.py
      ```

      ```bash Windows
      python cookbook/tools/github_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


