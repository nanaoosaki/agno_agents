---
title: Agent with Storage
category: misc
source_lines: 48597-48663
line_count: 66
---

# Agent with Storage
Source: https://docs.agno.com/examples/models/vllm/storage



## Code

```python cookbook/models/vllm/storage.py
from agno.agent import Agent
from agno.models.vllm import vLLM
from agno.storage.postgres import PostgresStorage
from agno.tools.duckduckgo import DuckDuckGoTools

DB_URL = "postgresql+psycopg://ai:ai@localhost:5532/ai"

agent = Agent(
    model=vLLM(id="Qwen/Qwen2.5-7B-Instruct"),
    storage=PostgresStorage(table_name="agent_sessions", db_url=DB_URL),
    tools=[DuckDuckGoTools()],
    add_history_to_messages=True,
)

agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")
```

<Note>
  Ensure Postgres database is running.
</Note>

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install Libraries">
    ```bash
    pip install -U agno openai vllm sqlalchemy psycopg[binary] duckduckgo-search
    ```
  </Step>

  <Step title="Start Postgres database">
    ```bash
    ./cookbook/scripts/run_pgvector.sh
    ```
  </Step>

  <Step title="Start vLLM server">
    ```bash
    vllm serve Qwen/Qwen2.5-7B-Instruct \
        --enable-auto-tool-choice \
        --tool-call-parser hermes \
        --dtype float16 \
        --max-model-len 8192 \
        --gpu-memory-utilization 0.9
    ```
  </Step>

  <Step title="Run Agent">
    ```bash
    python cookbook/models/vllm/storage.py
    ```
  </Step>
</Steps>


