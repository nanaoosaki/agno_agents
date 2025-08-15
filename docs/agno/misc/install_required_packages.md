---
title: Install required packages
category: misc
source_lines: 64608-64629
line_count: 21
---

# Install required packages
pip install agno litellm
```

Set up your API key:
Regardless of the model used(OpenAI, Hugging Face, or XAI) the API key is referenced as `LITELLM_API_KEY`.

```shell
export LITELLM_API_KEY=your_api_key_here
```

## SDK Integration

The `LiteLLM` class provides direct integration with the LiteLLM Python SDK.

### Basic Usage

```python
from agno.agent import Agent
from agno.models.litellm import LiteLLM

