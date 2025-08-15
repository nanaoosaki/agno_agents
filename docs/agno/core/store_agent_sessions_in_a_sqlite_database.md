---
title: Store agent sessions in a SQLite database
category: core
source_lines: 60051-60168
line_count: 117
---

# Store agent sessions in a SQLite database
storage = SqliteStorage(table_name="agent_sessions", db_file="tmp/agent.db")

agent = Agent(
    name="Agno Assist",
    model=Claude(id="claude-sonnet-4-20250514"),
    instructions=[
        "Search your knowledge before answering the question.",
        "Only include the output in your response. No other text.",
    ],
    knowledge=knowledge,
    storage=storage,
    add_datetime_to_instructions=True,
    # Add the chat history to the messages
    add_history_to_messages=True,
    # Number of history runs
    num_history_runs=3,
    markdown=True,
)

if __name__ == "__main__":
    # Load the knowledge base, comment out after first run
    # Set recreate to True to recreate the knowledge base if needed
    agent.knowledge.load(recreate=False)
    agent.print_response("What is Agno?", stream=True)
```

Install dependencies, export your `OPENAI_API_KEY` and run the Agent

<Steps>
  <Step title="Install new dependencies">
    <CodeGroup>
      ```bash Mac
      uv pip install -U lancedb tantivy openai sqlalchemy
      ```

      ```bash Windows
      uv pip install -U lancedb tantivy openai sqlalchemy
      ```
    </CodeGroup>
  </Step>

  <Step title="Run the agent">
    ```shell
    python level_2_agent.py
    ```
  </Step>
</Steps>

## Level 3: Agents with memory and reasoning

* **Reasoning:** enables Agents to **"think" & "analyze"**, improving reliability and quality. `ReasoningTools` is one of the best approaches to improve an Agent's response quality.
* **Memory:** enables Agents to classify, store and recall user preferences, personalizing their responses. Memory helps the Agent build personas and learn from previous interactions.

```python level_3_agent.py
from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.anthropic import Claude
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools

memory = Memory(
    # Use any model for creating and managing memories
    model=Claude(id="claude-sonnet-4-20250514"),
    # Store memories in a SQLite database
    db=SqliteMemoryDb(table_name="user_memories", db_file="tmp/agent.db"),
    # We disable deletion by default, enable it if needed
    delete_memories=True,
    clear_memories=True,
)

agent = Agent(
    model=Claude(id="claude-sonnet-4-20250514"),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True),
    ],
    # User ID for storing memories, `default` if not provided
    user_id="ava",
    instructions=[
        "Use tables to display data.",
        "Include sources in your response.",
        "Only include the report in your response. No other text.",
    ],
    memory=memory,
    # Let the Agent manage its memories
    enable_agentic_memory=True,
    markdown=True,
)

if __name__ == "__main__":
    # This will create a memory that "ava's" favorite stocks are NVIDIA and TSLA
    agent.print_response(
        "My favorite stocks are NVIDIA and TSLA",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )
    # This will use the memory to answer the question
    agent.print_response(
        "Can you compare my favorite stocks?",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )
```

Run the Agent

```shell
python level_3_agent.py
```

<Tip>You can use the `Memory` and `Reasoning` separately, you don't need to use them together.</Tip>


