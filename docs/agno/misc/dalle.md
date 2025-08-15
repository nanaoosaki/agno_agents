---
title: Dalle
category: misc
source_lines: 75184-75211
line_count: 27
---

# Dalle
Source: https://docs.agno.com/tools/toolkits/others/dalle



## Prerequisites

You need to install the `openai` library.

```bash
pip install openai
```

Set the `OPENAI_API_KEY` environment variable.

```bash
export OPENAI_API_KEY=****
```

## Example

The following agent will use DALL-E to generate an image based on a text prompt.

```python cookbook/tools/dalle_tools.py
from agno.agent import Agent
from agno.tools.dalle import DalleTools

