---
title: Jira Tools
category: tools
source_lines: 29093-29148
line_count: 55
---

# Jira Tools
Source: https://docs.agno.com/examples/concepts/tools/others/jira



## Code

```python cookbook/tools/jira_tools.py
from agno.agent import Agent
from agno.tools.jira import JiraTools

agent = Agent(
    tools=[JiraTools()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("List all open issues in project 'DEMO'")
agent.print_response("Create a new task in project 'DEMO' with high priority")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your Jira credentials">
    ```bash
    export JIRA_API_TOKEN=xxx
    export JIRA_SERVER_URL=xxx
    export JIRA_EMAIL=xxx
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U jira openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/jira_tools.py
      ```

      ```bash Windows
      python cookbook/tools/jira_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


