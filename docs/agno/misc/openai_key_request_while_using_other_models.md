---
title: OpenAI Key Request While Using Other Models
category: misc
source_lines: 58838-58863
line_count: 25
---

# OpenAI Key Request While Using Other Models
Source: https://docs.agno.com/faq/openai-key-request-for-other-models



If you see a request for an OpenAI API key but haven't explicitly configured OpenAI, it's because Agno uses OpenAI models by default in several places, including:

* The default model when unspecified in `Agent`
* The default embedder is OpenAIEmbedder with VectorDBs, unless specified

## Quick fix: Configure a Different Model

It is best to specify the model for the agent explicitly, otherwise it would default to `OpenAIChat`.

For example, to use Google's Gemini instead of OpenAI:

```python
from agno.agent import Agent, RunResponse
from agno.models.google import Gemini

agent = Agent(
    model=Gemini(id="gemini-1.5-flash"),
    markdown=True,
)

