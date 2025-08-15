---
title: MySQL Agent Storage
category: misc
source_lines: 23972-24001
line_count: 29
---

# MySQL Agent Storage
Source: https://docs.agno.com/examples/concepts/storage/agent_storage/mysql



Agno supports using MySQL as a storage backend for Agents using the `MySQLStorage` class.

## Usage

### Run MySQL

Install [docker desktop](https://docs.docker.com/desktop/install/mac-install/) and run **MySQL** on port **3306** using:

```bash
docker run -d \
  -e MYSQL_ROOT_PASSWORD=root \
  -e MYSQL_DATABASE=agno \
  -e MYSQL_USER=agno \
  -e MYSQL_PASSWORD=agno \
  -p 3306:3306 \
  --name mysql \
  mysql:8.0
```

```python mysql_storage_for_agent.py
from agno.storage.mysql import MySQLStorage

db_url = "mysql+pymysql://agno:agno@localhost:3306/agno"

