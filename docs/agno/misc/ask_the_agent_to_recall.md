---
title: Ask the agent to recall
category: misc
source_lines: 48553-48597
line_count: 44
---

# Ask the agent to recall
agent.print_response(
    "What have we been talking about, do you know my name?", stream=True
)
```

<Note>
  Ensure Postgres database is running.
</Note>

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Start Postgres database">
    ```bash
    ./cookbook/scripts/run_pgvector.sh
    ```
  </Step>

  <Step title="Install Libraries">
    ```bash
    pip install -U agno openai vllm sqlalchemy psycopg[binary] pgvector
    ```
  </Step>

  <Step title="Start vLLM server">
    ```bash
    vllm serve microsoft/Phi-3-mini-128k-instruct \
        --dtype float32 \
        --enable-auto-tool-choice \
        --tool-call-parser pythonic
    ```
  </Step>

  <Step title="Run Agent">
    ```bash
    python cookbook/models/vllm/memory.py
    ```
  </Step>
</Steps>


