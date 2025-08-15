---
title: LanceDB Agent Knowledge
category: knowledge
source_lines: 80574-80597
line_count: 23
---

# LanceDB Agent Knowledge
Source: https://docs.agno.com/vectordb/lancedb



## Setup

```shell
pip install lancedb
```

## Example

```python agent_with_knowledge.py
import typer
from typing import Optional
from rich.prompt import Prompt

from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb
from agno.vectordb.search import SearchType

