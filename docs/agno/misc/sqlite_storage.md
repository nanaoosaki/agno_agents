---
title: Sqlite Storage
category: misc
source_lines: 69203-69217
line_count: 14
---

# Sqlite Storage
Source: https://docs.agno.com/storage/sqlite



Agno supports using Sqlite as a storage backend for Agents using the `SqliteStorage` class.

## Usage

You need to provide either `db_url`, `db_file` or `db_engine`. The following example uses `db_file`.

```python sqlite_storage_for_agent.py
from agno.storage.sqlite import SqliteStorage

