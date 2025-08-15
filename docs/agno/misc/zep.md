---
title: Zep
category: misc
source_lines: 73580-73610
line_count: 30
---

# Zep
Source: https://docs.agno.com/tools/toolkits/database/zep



**ZepTools** enable an Agent to interact with a Zep memory system, providing capabilities to store, retrieve, and search memory data associated with user sessions.

## Prerequisites

The ZepTools require the `zep-cloud` Python package and a Zep API key.

```shell
pip install zep-cloud
```

```shell
export ZEP_API_KEY=your_api_key
```

## Example

The following example demonstrates how to create an agent with access to Zep memory:

```python cookbook/tools/zep_tools.py
import time

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.zep import ZepTools

