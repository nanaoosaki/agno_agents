---
title: What is Storage?
category: misc
source_lines: 68717-68838
line_count: 121
---

# What is Storage?
Source: https://docs.agno.com/storage/introduction

Storage is a way to persist Agent sessions and state to a database or file.

Use **Session Storage** to persist Agent sessions and state to a database or file.

<Tip>
  **Why do we need Session Storage?**

  Agents are ephemeral and the built-in memory only lasts for the current execution cycle.

  In production environments, we serve (or trigger) Agents via an API and need to continue the same session across multiple requests. Storage persists the session history and state in a database and allows us to pick up where we left off.

  Storage also let's us inspect and evaluate Agent sessions, extract few-shot examples and build internal monitoring tools. It lets us **look at the data** which helps us build better Agents.
</Tip>

Adding storage to an Agent, Team or Workflow is as simple as providing a `Storage` driver and Agno handles the rest. You can use Sqlite, Postgres, Mongo or any other database you want.

Here's a simple example that demostrates persistence across execution cycles:

```python storage.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from rich.pretty import pprint

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    # Fix the session id to continue the same session across execution cycles
    session_id="fixed_id_for_demo",
    storage=SqliteStorage(table_name="agent_sessions", db_file="tmp/data.db"),
    add_history_to_messages=True,
    num_history_runs=3,
)
agent.print_response("What was my last question?")
agent.print_response("What is the capital of France?")
agent.print_response("What was my last question?")
pprint(agent.get_messages_for_session())
```

The first time you run this, the answer to "What was my last question?" will not be available. But run it again and the Agent will able to answer properly. Because we have fixed the session id, the Agent will continue from the same session every time you run the script.

## Benefits of Storage

Storage has typically been an under-discussed part of Agent Engineering -- but we see it as the unsung hero of production agentic applications.

In production, you need storage to:

* Continue sessions: retrieve sessions history and pick up where you left off.
* Get list of sessions: To continue a previous session, you need to maintain a list of sessions available for that agent.
* Save state between runs: save the Agent's state to a database or file so you can inspect it later.

But there is so much more:

* Storage saves our Agent's session data for inspection and evaluations.
* Storage helps us extract few-shot examples, which can be used to improve the Agent.
* Storage enables us to build internal monitoring tools and dashboards.

<Warning>
  Storage is such a critical part of your Agentic infrastructure that it should never be offloaded to a third party. You should almost always use your own storage layer for your Agents.
</Warning>

## Agent Storage

When working with agents, storage allows users to continue conversations where they left off. Every message, along with the agent's responses, is saved to your database of choice.

Here's a simple example of adding storage to an agent:

```python storage.py
"""Run `pip install duckduckgo-search sqlalchemy openai` to install dependencies."""

from agno.agent import Agent
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    storage=SqliteStorage(
        table_name="agent_sessions", db_file="tmp/data.db", auto_upgrade_schema=True
    ),
    tools=[DuckDuckGoTools()],
    add_history_to_messages=True,
    add_datetime_to_instructions=True,
)
agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem?")
agent.print_response("List my messages one by one")
```

## Team Storage

`Storage` drivers also works with teams, providing persistent memory and state management for multi-agent collaborative systems. With team storage, you can maintain conversation history, shared context, and team state across multiple sessions.

<Note>
  Learn more about [teams](/teams/) and their storage capabilities to build powerful multi-agent systems with persistent state.
</Note>

## Workflow Storage

The storage system in Agno also works with workflows, enabling more complex multi-agent systems with state management. This allows for persistent conversations and cached results across workflow sessions.

<Note>
  Learn more about using storage with [workflows](/workflows/) to build powerful multi-agent systems with state management.
</Note>

## Supported Storage Backends

The following databases are supported as a storage backend:

* [PostgreSQL](/storage/postgres)
* [Sqlite](/storage/sqlite)
* [SingleStore](/storage/singlestore)
* [DynamoDB](/storage/dynamodb)
* [MongoDB](/storage/mongodb)
* [YAML](/storage/yaml)
* [JSON](/storage/json)
* [Redis](/storage/redis)

Check detailed [examples](/examples/concepts/storage) for each storage


