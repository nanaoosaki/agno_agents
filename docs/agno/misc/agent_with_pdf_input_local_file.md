---
title: Agent with PDF Input (Local File)
category: misc
source_lines: 47414-47431
line_count: 17
---

# Agent with PDF Input (Local File)
Source: https://docs.agno.com/examples/models/openai/responses/pdf_input_local



## Code

```python cookbook/models/openai/responses/pdf_input_local.py
from pathlib import Path

from agno.agent import Agent
from agno.media import File
from agno.models.openai.responses import OpenAIResponses
from agno.utils.media import download_file

pdf_path = Path(__file__).parent.joinpath("ThaiRecipes.pdf")

