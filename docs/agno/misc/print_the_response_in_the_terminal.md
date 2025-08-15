---
title: Print the response in the terminal
category: misc
source_lines: 63884-63905
line_count: 21
---

# Print the response in the terminal
agent.print_response("write a two sentence horror story")
```

### Configuration Options

The `CerebrasOpenAI` class accepts the following parameters:

| Parameter  | Type | Description                                                     | Default                                              |
| ---------- | ---- | --------------------------------------------------------------- | ---------------------------------------------------- |
| `id`       | str  | Model identifier (e.g., "llama-4-scout-17b-16e-instruct")       | **Required**                                         |
| `name`     | str  | Display name for the model                                      | "Cerebras"                                           |
| `provider` | str  | Provider name                                                   | "Cerebras"                                           |
| `api_key`  | str  | API key (falls back to CEREBRAS\_API\_KEY environment variable) | None                                                 |
| `base_url` | str  | URL of the Cerebras OpenAI-compatible endpoint                  | "[https://api.cerebras.ai](https://api.cerebras.ai)" |

### Examples

* View more examples [here](../examples/models/cerebras_openai).


