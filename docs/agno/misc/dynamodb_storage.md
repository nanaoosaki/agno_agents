---
title: DynamoDB Storage
category: misc
source_lines: 68675-68689
line_count: 14
---

# DynamoDB Storage
Source: https://docs.agno.com/storage/dynamodb



Agno supports using DynamoDB as a storage backend for Agents, Teams and Workflows using the `DynamoDbStorage` class.

## Usage

You need to provide `aws_access_key_id` and `aws_secret_access_key` parameters to the `DynamoDbStorage` class.

```python dynamodb_storage_for_agent.py
from agno.storage.dynamodb import DynamoDbStorage

