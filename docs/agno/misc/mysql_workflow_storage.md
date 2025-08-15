---
title: MySQL Workflow Storage
category: misc
source_lines: 25350-25379
line_count: 29
---

# MySQL Workflow Storage
Source: https://docs.agno.com/examples/concepts/storage/workflow_storage/mysql



Agno supports using MySQL as a storage backend for Workflows using the `MySQLStorage` class.

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

```python mysql_storage_for_workflow.py
from agno.storage.mysql import MySQLStorage

db_url = "mysql+pymysql://agno:agno@localhost:3306/agno"

