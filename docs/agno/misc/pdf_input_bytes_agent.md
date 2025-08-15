---
title: PDF Input Bytes Agent
category: misc
source_lines: 37170-37186
line_count: 16
---

# PDF Input Bytes Agent
Source: https://docs.agno.com/examples/models/anthropic/pdf_input_bytes



## Code

```python cookbook/models/anthropic/pdf_input_bytes.py
from pathlib import Path
from agno.agent import Agent
from agno.media import File
from agno.models.anthropic import Claude
from agno.utils.media import download_file

pdf_path = Path(__file__).parent.joinpath("ThaiRecipes.pdf")

