---
title: Tokens-per-minute rate limiting
category: misc
source_lines: 59051-59081
line_count: 30
---

# Tokens-per-minute rate limiting
Source: https://docs.agno.com/faq/tpm-issues



![Chat with pdf](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/tpm_issues.png)

If you face any problems with proprietary models (like OpenAI models) where you are rate limited, we provide the option to set `exponential_backoff=True` and to change `delay_between_retries` to a value in seconds (defaults to 1 second).

For example:

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    markdown=True,
    exponential_backoff=True,
    delay_between_retries=2
)
agent.print_response("Tell me about a breaking news story from New York.", stream=True)
```

See our [models documentation](../models/) for specific information about rate limiting.

In the case of OpenAI, they have tier based rate limits. See the [docs](https://platform.openai.com/docs/guides/rate-limits/usage-tiers) for more information.


