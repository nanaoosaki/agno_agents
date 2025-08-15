---
title: Mem0
category: misc
source_lines: 73225-73260
line_count: 35
---

# Mem0
Source: https://docs.agno.com/tools/toolkits/database/mem0

The toolkit enables an Agent to interact with a Mem0 memory system, providing capabilities to store, retrieve, search, and manage persistent memory data associated with users.

## Prerequisites

The Mem0 toolkit requires the `mem0ai` Python package and either a Mem0 API key for cloud usage or local configuration for self-hosted deployments.

```shell
pip install mem0ai
```

For cloud usage with the [Mem0 app](https://app.mem0.ai/dashboard/get-started):

```shell
export MEM0_API_KEY=your_api_key
export MEM0_ORG_ID=your_org_id          # Optional
export MEM0_PROJECT_ID=your_project_id  # Optional
```

## Example

The following example demonstrates how to create an agent with access to Mem0 memory:

```python cookbook/tools/mem0_tools.py
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mem0 import Mem0Tools

USER_ID = "jane_doe"
SESSION_ID = "agno_session"

