---
title: Get a response
category: misc
source_lines: 64638-64682
line_count: 44
---

# Get a response
agent.print_response("Share a 2 sentence horror story")
```

### Using Hugging Face Models

LiteLLM can also work with Hugging Face models:

```python
from agno.agent import Agent
from agno.models.litellm import LiteLLM

agent = Agent(
    model=LiteLLM(
        id="huggingface/mistralai/Mistral-7B-Instruct-v0.2",
        top_p=0.95,
    ),
    markdown=True,
)

agent.print_response("What's happening in France?")
```

### Configuration Options

The `LiteLLM` class accepts the following parameters:

| Parameter        | Type                       | Description                                                                           | Default   |
| ---------------- | -------------------------- | ------------------------------------------------------------------------------------- | --------- |
| `id`             | str                        | Model identifier (e.g., "gpt-4o" or "huggingface/mistralai/Mistral-7B-Instruct-v0.2") | "gpt-4o"  |
| `name`           | str                        | Display name for the model                                                            | "LiteLLM" |
| `provider`       | str                        | Provider name                                                                         | "LiteLLM" |
| `api_key`        | Optional\[str]             | API key (falls back to LITELLM\_API\_KEY environment variable)                        | None      |
| `api_base`       | Optional\[str]             | Base URL for API requests                                                             | None      |
| `max_tokens`     | Optional\[int]             | Maximum tokens in the response                                                        | None      |
| `temperature`    | float                      | Sampling temperature                                                                  | 0.7       |
| `top_p`          | float                      | Top-p sampling value                                                                  | 1.0       |
| `request_params` | Optional\[Dict\[str, Any]] | Additional request parameters                                                         | None      |

### SDK Examples

<Note> View more examples [here](../examples/models/litellm). </Note>


