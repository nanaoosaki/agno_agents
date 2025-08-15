---
title: Read the image file content as bytes
category: misc
source_lines: 49230-49267
line_count: 37
---

# Read the image file content as bytes
image_bytes = image_path.read_bytes()

agent.print_response(
    "Tell me about this image and give me the latest news about it.",
    images=[
        Image(content=image_bytes),
    ],
    stream=True,
)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export XAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U openai duckduckgo-search agno
    ```
  </Step>

  <Step title="Run Agent">
    ```bash
    python cookbook/models/xai/image_agent_bytes.py
    ```
  </Step>
</Steps>


