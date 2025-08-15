---
title: Sqlite Agent Storage
category: misc
source_lines: 24178-24192
line_count: 14
---

# Sqlite Agent Storage
Source: https://docs.agno.com/examples/concepts/storage/agent_storage/sqlite



Agno supports using Sqlite as a storage backend for Agents using the `SqliteStorage` class.

## Usage

You need to provide either `db_url`, `db_file` or `db_engine`. The following example uses `db_file`.

```python sqlite_storage_for_agent.py
from agno.storage.sqlite import SqliteStorage

