---
title: Structured outputs
category: misc
source_lines: 58971-59051
line_count: 80
---

# Structured outputs
Source: https://docs.agno.com/faq/structured-outputs



## Structured Outputs vs. JSON Mode

When working with language models, generating responses that match a specific structure is crucial for building reliable applications. Agno Agents support two methods to achieve this: **Structured Outputs** and **JSON mode**.

***

### Structured Outputs (Default if supported)

"Structured Outputs" is the **preferred** and most **reliable** way to extract well-formed, schema-compliant responses from a Model. If a model class supports it, Agno Agents use Structured Outputs by default.

With structured outputs, we provide a schema to the model (using Pydantic or JSON Schema), and the model’s response is guaranteed to **strictly follow** that schema. This eliminates many common issues like missing fields, invalid enum values, or inconsistent formatting. Structured Outputs are ideal when you need high-confidence, well-structured responses—like entity extraction, content generation for UI rendering, and more.

In this case, the response model is passed as a keyword argument to the model.

## Example

```python
from pydantic import BaseModel
from agno.agent import Agent
from agno.models.openai import OpenAIChat

class User(BaseModel):
    name: str
    age: int
    email: str

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a helpful assistant that can extract information from a user's profile.",
    response_model=User,
)
```

In the example above, the model will generate a response that matches the `User` schema using structured outputs via OpenAI's `gpt-4o` model. The agent will then return the `User` object as-is.

***

### JSON Mode

Some model classes **do not support Structured Outputs**, or you may want to fall back to JSON mode even when the model supports both options. In such cases, you can enable **JSON mode** by setting `use_json_mode=True`.

JSON mode works by injecting a detailed description of the expected JSON structure into the system prompt. The model is then instructed to return a valid JSON object that follows this structure. Unlike Structured Outputs, the response is **not automatically validated** against the schema at the API level.

## Example

```python
from pydantic import BaseModel
from agno.agent import Agent
from agno.models.openai import OpenAIChat

class User(BaseModel):
    name: str
    age: int
    email: str

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a helpful assistant that can extract information from a user's profile.",
    response_model=User,
    use_json_mode=True,
)

```

### When to use

Use **Structured Outputs** if the model supports it — it’s reliable, clean, and validated automatically.

Use **JSON mode**:

* When the model doesn't support structured outputs. Agno agents do this by default on your behalf.
* When you need broader compatibility, but are okay validating manually.
* When the model does not support tools with structured outputs.


