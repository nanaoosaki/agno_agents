---
title: Comment out after the knowledge base is loaded
category: knowledge
source_lines: 34405-34435
line_count: 30
---

# Comment out after the knowledge base is loaded
if agent.knowledge is not None:
    agent.knowledge.load()

agent.print_response(
    "How do I make chicken and galangal in coconut milk soup", stream=True
)
agent.print_response("What is the history of Thai curry?", stream=True)
agent.print_response("What ingredients do I need for Pad Thai?", stream=True)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install libraries">
    ```bash
    pip install openai lancedb tantivy pypdf duckduckgo-search agno
    ```
  </Step>

  <Step title="Run the agent">
    ```bash
    python agent_with_knowledge.py
    ```
  </Step>
</Steps>


