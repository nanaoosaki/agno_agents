---
title: Singlestore Storage
category: misc
source_lines: 69145-69164
line_count: 19
---

# Singlestore Storage
Source: https://docs.agno.com/storage/singlestore



Agno supports using Singlestore as a storage backend for Agents using the `SingleStoreStorage` class.

## Usage

Obtain the credentials for Singlestore from [here](https://portal.singlestore.com/)

```python singlestore_storage_for_agent.py
from os import getenv

from sqlalchemy.engine import create_engine

from agno.agent import Agent
from agno.storage.singlestore import SingleStoreStorage

