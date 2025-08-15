---
title: Mongo Storage
category: misc
source_lines: 68947-68963
line_count: 16
---

# Mongo Storage
Source: https://docs.agno.com/storage/mongodb



Agno supports using MongoDB as a storage backend for Agents using the `MongoDbStorage` class.

## Usage

You need to provide either `db_url` or `client`. The following example uses `db_url`.

```python mongodb_storage_for_agent.py
from agno.storage.mongodb import MongoDbStorage

db_url = "mongodb://ai:ai@localhost:27017/agno"

