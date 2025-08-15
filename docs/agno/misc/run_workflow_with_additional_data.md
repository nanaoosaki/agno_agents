---
title: Run workflow with additional_data
category: misc
source_lines: 82805-82868
line_count: 63
---

# Run workflow with additional_data
workflow.print_response(
    message="AI trends in 2024",
    additional_data={
        "user_email": "kaustubh@agno.com",
        "priority": "high",
        "client_type": "enterprise",
        "budget": "$50000",
        "deadline": "2024-12-15"
    },
    markdown=True,
    stream=True
)
```

**More Examples**:

* [Step with Function and Additional Data](/examples/workflows_2/06-workflows-advanced-concepts/step_with_function_additional_data)

## Structured Inputs

Use Pydantic models for type-safe inputs:

```python
from pydantic import BaseModel, Field

class ResearchRequest(BaseModel):
    topic: str = Field(description="Research topic")
    depth: int = Field(description="Research depth (1-10)")
    sources: List[str] = Field(description="Preferred sources")

workflow.print_response(
    message=ResearchRequest(
        topic="AI trends 2024",
        depth=8,
        sources=["academic", "industry"]
    )
)
```

**More Examples**:

* [Pydantic Model as Input](/examples/workflows_2/06-workflows-advanced-concepts/pydantic_model_as_input)

## Structured IO at Each Step Level

Workflows features a powerful type-safe data flow system where each step in your workflow can:

1. **Receive** structured input (Pydantic models, lists, dicts, or raw strings)
2. **Produce** structured output (validated Pydantic models)
3. **Maintain** type safety throughout the entire workflow execution

### How Data Flows Between Steps

1. **Input Handling**:
   * The first step receives the workflow's input message
   * Subsequent steps receive the previous step's structured output

2. **Output Processing**:
   * Each Agent processes the input using its `response_model`
   * The output is automatically validated against the model

```python
