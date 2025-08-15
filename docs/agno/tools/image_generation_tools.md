---
title: Image Generation Tools
category: tools
source_lines: 10816-10886
line_count: 70
---

# Image Generation Tools
Source: https://docs.agno.com/examples/applications/whatsapp/image_generation_tools



this example shows how to use the openai tools to generate images with whatsapp app.

## Code

```python cookbook/apps/whatsapp/image_generation_tools.py
from agno.agent import Agent
from agno.app.whatsapp.app import WhatsappAPI
from agno.models.openai import OpenAIChat
from agno.tools.openai import OpenAITools

image_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[OpenAITools(image_model="gpt-image-1")],
    markdown=True,
    show_tool_calls=True,
    debug_mode=True,
    add_history_to_messages=True,
)


whatsapp_app = WhatsappAPI(
    agent=image_agent,
    name="Image Generation Tools",
    app_id="image_generation_tools",
    description="A tool that generates images using the OpenAI API.",
)

app = whatsapp_app.get_app()

if __name__ == "__main__":
    whatsapp_app.serve(app="image_generation_tools:app", port=8000, reload=True)

```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U agno openai "uvicorn[standard]"
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/apps/whatsapp/image_generation_tools.py
      ```

      ```bash Windows
      python cookbook/apps/whatsapp/image_generation_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


