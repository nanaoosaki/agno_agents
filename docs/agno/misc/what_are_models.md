---
title: What are Models?
category: misc
source_lines: 64474-64538
line_count: 64
---

# What are Models?
Source: https://docs.agno.com/models/introduction

Language Models are machine-learning programs that are trained to understand natural language and code.

Models act as the **brain** of the Agent - helping it reason, act, and respond to the user. The better the model, the smarter the Agent.

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="Share 15 minute healthy recipes.",
    markdown=True,
)
agent.print_response("Share a breakfast recipe.", stream=True)
```

## Error handling

You can set `exponential_backoff` to `True` on the `Agent` to automatically retry requests that fail due to third-party model provider errors.

```python
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    exponential_backoff=True,
    retries=2,
    retry_delay=1,
)
```

## Supported Models

Agno supports the following model providers:

* [AI/ML API](/models/aimlapi)
* [Anthropic](/models/anthropic)
* [AWS Bedrock](/models/aws-bedrock)
* [Azure AI Foundry](/models/azure-ai-foundry)
* [Claude via AWS Bedrock](/models/aws-claude)
* [Cohere](/models/cohere)
* [DeepSeek](/models/deepseek)
* [Fireworks](/models/fireworks)
* [Google Gemini](/models/google)
* [Groq](/models/groq)
* [Hugging Face](/models/huggingface)
* [LiteLLM](/models/litellm)
* [Mistral](/models/mistral)
* [NVIDIA](/models/nvidia)
* [Nebius AI Studio](/models/nebius)
* [Ollama](/models/ollama)
* [OpenAI](/models/openai)
* [OpenAI Like](/models/openai-like)
* [OpenAI via Azure](/models/azure-openai)
* [OpenRouter](/models/openrouter)
* [Perplexity](/models/perplexity)
* [Sambanova](/models/sambanova)
* [Together](/models/together)
* [vLLM](/models/vllm)
* [xAI](/models/xai)
* [LangDB](/models/langdb)


