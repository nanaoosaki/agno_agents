---
title: pprint(movie_agent.content)
category: misc
source_lines: 43283-43322
line_count: 39
---

# pprint(movie_agent.content)

movie_agent.print_response("New York")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export IBM_WATSONX_API_KEY=xxx
    export IBM_WATSONX_PROJECT_ID=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U ibm-watsonx-ai pydantic rich agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/models/ibm/watsonx/structured_output.py
      ```

      ```bash Windows
      python cookbook\models\ibm\watsonx\structured_output.py
      ```
    </CodeGroup>
  </Step>
</Steps>

This example shows how to use structured output with IBM WatsonX. It defines a Pydantic model `MovieScript` with various fields and their descriptions, then creates an agent using this model as the `response_model`. The model's output will be parsed into this structured format.


