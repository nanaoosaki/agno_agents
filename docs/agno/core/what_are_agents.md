---
title: What are Agents?
category: core
source_lines: 59929-60038
line_count: 109
---

# What are Agents?
Source: https://docs.agno.com/introduction/agents

**Agents are AI programs that operate autonomously.**

Traditional software follows a pre-programmed sequence of steps. Agents dynamically determine their course of action using a machine learning **model**, its core components are:

* **Model:** controls the flow of execution. It decides whether to reason, act or respond.
* **Tools:** enable an Agent to take actions and interact with external systems.
* **Instructions:** are how we program the Agent, teaching it how to use tools and respond.

Agents also have **memory**, **knowledge**, **storage** and the ability to **reason**:

* **Reasoning:** enables Agents to "think" before responding and "analyze" the results of their actions (i.e. tool calls), this improves reliability and quality of responses.
* **Knowledge:** is domain-specific information that the Agent can **search at runtime** to make better decisions and provide accurate responses (RAG). Knowledge is stored in a vector database and this **search at runtime** pattern is known as Agentic RAG/Agentic Search.
* **Storage:** is used by Agents to save session history and state in a database. Model APIs are stateless and storage enables us to continue conversations from where they left off. This makes Agents stateful, enabling multi-turn, long-term conversations.
* **Memory:** gives Agents the ability to store and recall information from previous interactions, allowing them to learn user preferences and personalize their responses.

<Check>Let's build a few Agents to see how they work.</Check>

## Level 1: Agents with tools and instructions

The simplest Agent has a model, a tool and instructions. Let's build an Agent that can fetch data using the `yfinance` library, along with instructions to display the results in a table.

```python level_1_agent.py
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=Claude(id="claude-sonnet-4-20250514"),
    tools=[YFinanceTools(stock_price=True)],
    instructions="Use tables to display data. Don't include any other text.",
    markdown=True,
)
agent.print_response("What is the stock price of Apple?", stream=True)
```

Create a virtual environment, install dependencies, export your API key and run the Agent.

<Steps>
  <Step title="Setup your virtual environment">
    <CodeGroup>
      ```bash Mac
      uv venv --python 3.12
      source .venv/bin/activate
      ```

      ```bash Windows
      uv venv --python 3.12
      .venv/Scripts/activate
      ```
    </CodeGroup>
  </Step>

  <Step title="Install dependencies">
    <CodeGroup>
      ```bash Mac
      uv pip install -U agno anthropic yfinance
      ```

      ```bash Windows
      uv pip install -U agno anthropic yfinance
      ```
    </CodeGroup>
  </Step>

  <Step title="Export your Anthropic key">
    <CodeGroup>
      ```bash Mac
      export ANTHROPIC_API_KEY=sk-***
      ```

      ```bash Windows
      setx ANTHROPIC_API_KEY sk-***
      ```
    </CodeGroup>
  </Step>

  <Step title="Run the agent">
    ```shell
    python level_1_agent.py
    ```
  </Step>
</Steps>

<Note>
  Set `debug_mode=True` or `export AGNO_DEBUG=true` to see the system prompt and user messages.
</Note>

## Level 2: Agents with knowledge and storage

**Knowledge:** While models have a large amount of training data, we almost always need to give them domain-specific information to make better decisions and provide accurate responses (RAG). We store this information in a vector database and let the Agent **search** it at runtime.

**Storage:** Model APIs are stateless and `Storage` drivers save chat history and state to a database. When the Agent runs, it reads the chat history and state from the database and add it to the messages list, resuming the conversation and making the Agent stateful.

In this example, we'll use:

* `UrlKnowledge` to load Agno documentation to LanceDB, using OpenAI for embeddings.
* `SqliteStorage` to save the Agent's session history and state in a database.

```python level_2_agent.py
from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.url import UrlKnowledge
from agno.models.anthropic import Claude
from agno.storage.sqlite import SqliteStorage
from agno.vectordb.lancedb import LanceDb, SearchType

