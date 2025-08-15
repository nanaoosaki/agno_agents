---
title: Singlestore Agent Storage
category: misc
source_lines: 24120-24139
line_count: 19
---

# Singlestore Agent Storage
Source: https://docs.agno.com/examples/concepts/storage/agent_storage/singlestore



Agno supports using Singlestore as a storage backend for Agents using the `SingleStoreStorage` class.

## Usage

Obtain the credentials for Singlestore from [here](https://portal.singlestore.com/)

```python singlestore_storage_for_agent.py
from os import getenv

from sqlalchemy.engine import create_engine

from agno.agent import Agent
from agno.storage.singlestore import SingleStoreStorage

