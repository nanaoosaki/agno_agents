---
title: Image Generation Model
category: misc
source_lines: 10749-10816
line_count: 67
---

# Image Generation Model
Source: https://docs.agno.com/examples/applications/whatsapp/image_generation_model



This example shows how to use the image generation model to generate images with whatsapp app.

## Code

```python cookbook/apps/whatsapp/image_generation_model.py
from agno.agent import Agent
from agno.app.whatsapp.app import WhatsappAPI
from agno.models.google import Gemini

image_agentg = Agent(
    model=Gemini(
        id="gemini-2.0-flash-exp-image-generation",
        response_modalities=["Text", "Image"],
    ),
    debug_mode=True,
)

whatsapp_app = WhatsappAPI(
    agent=image_agent,
    name="Image Generation Model",
    app_id="image_generation_model",
    description="A model that generates images using the Gemini API.",
)

app = whatsapp_app.get_app()

if __name__ == "__main__":
    whatsapp_app.serve(app="image_generation_model:app", port=8000, reload=True)

```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export GOOGLE_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U agno google-generativeai "uvicorn[standard]"
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/apps/whatsapp/image_generation_model.py
      ```

      ```bash Windows
      python cookbook/apps/whatsapp/image_generation_model.py
      ```
    </CodeGroup>
  </Step>
</Steps>


