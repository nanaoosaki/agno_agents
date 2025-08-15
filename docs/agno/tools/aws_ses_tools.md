---
title: AWS SES Tools
category: tools
source_lines: 28066-28079
line_count: 13
---

# AWS SES Tools
Source: https://docs.agno.com/examples/concepts/tools/others/aws_ses



## Code

```python cookbook/tools/aws_ses_tools.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.aws_ses import AWSSESTool
from agno.tools.duckduckgo import DuckDuckGoTools

