---
title: JSON Agent Storage
category: misc
source_lines: 23902-23936
line_count: 34
---

# JSON Agent Storage
Source: https://docs.agno.com/examples/concepts/storage/agent_storage/json



Agno supports using local JSON files as a storage backend for Agents using the `JsonStorage` class.

## Usage

```python json_storage_for_agent.py
"""Run `pip install duckduckgo-search openai` to install dependencies."""

from agno.agent import Agent
from agno.storage.json import JsonStorage
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    storage=JsonStorage(dir_path="tmp/agent_sessions_json"),
    tools=[DuckDuckGoTools()],
    add_history_to_messages=True,
)
agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")
```

## Params

<Snippet file="storage-json-params.mdx" />

## Developer Resources

* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/storage/json_storage/json_storage_for_agent.py)


