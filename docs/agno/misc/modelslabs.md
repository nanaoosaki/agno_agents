---
title: ModelsLabs
category: misc
source_lines: 76428-76455
line_count: 27
---

# ModelsLabs
Source: https://docs.agno.com/tools/toolkits/others/models_labs



## Prerequisites

You need to install the `requests` library.

```bash
pip install requests
```

Set the `MODELS_LAB_API_KEY` environment variable.

```bash
export MODELS_LAB_API_KEY=****
```

## Example

The following agent will use ModelsLabs to generate a video based on a text prompt.

```python cookbook/tools/models_labs_tools.py
from agno.agent import Agent
from agno.tools.models_labs import ModelsLabsTools

