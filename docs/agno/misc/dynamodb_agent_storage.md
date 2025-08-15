---
title: DynamoDB Agent Storage
category: misc
source_lines: 23860-23874
line_count: 14
---

# DynamoDB Agent Storage
Source: https://docs.agno.com/examples/concepts/storage/agent_storage/dynamodb



Agno supports using DynamoDB as a storage backend for Agents using the `DynamoDbStorage` class.

## Usage

You need to provide `aws_access_key_id` and `aws_secret_access_key` parameters to the `DynamoDbStorage` class.

```python dynamodb_storage_for_agent.py
from agno.storage.dynamodb import DynamoDbStorage

