---
title: LiteLLM
category: misc
source_lines: 64591-64608
line_count: 17
---

# LiteLLM
Source: https://docs.agno.com/models/litellm

Integrate LiteLLM with Agno for a unified LLM experience.

[LiteLLM](https://docs.litellm.ai/docs/) provides a unified interface for various LLM providers, allowing you to use different models with the same code.

Agno integrates with LiteLLM in two ways:

1. **Direct SDK integration** - Using the LiteLLM Python SDK
2. **Proxy Server integration** - Using LiteLLM as an OpenAI-compatible proxy

## Prerequisites

For both integration methods, you'll need:

```shell
