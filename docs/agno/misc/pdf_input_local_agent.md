---
title: PDF Input Local Agent
category: misc
source_lines: 37240-37256
line_count: 16
---

# PDF Input Local Agent
Source: https://docs.agno.com/examples/models/anthropic/pdf_input_local



## Code

```python cookbook/models/anthropic/pdf_input_local.py
from pathlib import Path
from agno.agent import Agent
from agno.media import File
from agno.models.anthropic import Claude
from agno.utils.media import download_file

pdf_path = Path(__file__).parent.joinpath("ThaiRecipes.pdf")

