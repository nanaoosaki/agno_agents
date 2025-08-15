---
title: OR set environment variables manually
category: misc
source_lines: 74744-74766
line_count: 22
---

# OR set environment variables manually
export AWS_ACCESS_KEY_ID=****
export AWS_SECRET_ACCESS_KEY=****
export AWS_DEFAULT_REGION=us-east-1
```

<Note>
  Make sure to add the domain or email address you want to send FROM (and, if
  still in sandbox mode, the TO address) to the verified emails in the [SES
  Console](https://console.aws.amazon.com/ses/home).
</Note>

## Example

The following agent researches the latest AI news and then emails a summary via AWS SES:

```python aws_ses_tools.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.aws_ses import AWSSESTool
from agno.tools.duckduckgo import DuckDuckGoTools

