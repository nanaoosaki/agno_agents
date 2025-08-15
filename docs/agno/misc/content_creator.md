---
title: Content Creator
category: misc
source_lines: 52360-52383
line_count: 23
---

# Content Creator
Source: https://docs.agno.com/examples/workflows/content-creator



**ContentCreator** streamlines the process of planning, creating, and distributing engaging content across LinkedIn and Twitter.

Create a file `config.py` with the following code:

```python config.py
import os
from enum import Enum

from dotenv import load_dotenv

load_dotenv()


TYPEFULLY_API_URL = "https://api.typefully.com/v1/drafts/"
TYPEFULLY_API_KEY = os.getenv("TYPEFULLY_API_KEY")
HEADERS = {"X-API-KEY": f"Bearer {TYPEFULLY_API_KEY}"}


