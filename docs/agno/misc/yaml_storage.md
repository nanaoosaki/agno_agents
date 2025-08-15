---
title: YAML Storage
category: misc
source_lines: 69238-69271
line_count: 33
---

# YAML Storage
Source: https://docs.agno.com/storage/yaml



Agno supports using local YAML files as a storage backend for Agents using the `YamlStorage` class.

## Usage

```python yaml_storage_for_agent.py
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.storage.yaml import YamlStorage

agent = Agent(
    storage=YamlStorage(path="tmp/agent_sessions_yaml"),
    tools=[DuckDuckGoTools()],
    add_history_to_messages=True,
)

agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")
```

## Params

<Snippet file="storage-yaml-params.mdx" />

## Developer Resources

* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/storage/yaml_storage/yaml_storage_for_agent.py)


