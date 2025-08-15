---
title: Gemini
category: misc
source_lines: 74037-74147
line_count: 110
---

# Gemini
Source: https://docs.agno.com/tools/toolkits/models/gemini



`GeminiTools` are a set of tools that allow an Agent to interact with Google AI API services for generating images and videos.

## Prerequisites

Before using `GeminiTools`, make sure to have the `google-genai` library installed and the credentials configured.

1. **Install the library:**
   ```bash
   pip install google-genai agno
   ```

2. **Set your credentials:**
   * For Gemini API:
     ```bash
     export GOOGLE_API_KEY="your-google-genai-api-key"
     ```
   * For Vertex AI:
     ```bash
     export GOOGLE_CLOUD_PROJECT="your-google-cloud-project-id"
     export GOOGLE_CLOUD_LOCATION="your-google-cloud-location"
     export GOOGLE_GENAI_USE_VERTEXAI=true
     ```

## Initialization

Import `GeminiTools` and add it to your Agent's tool list.

```python
from agno.agent import Agent
from agno.tools.models.gemini import GeminiTools

agent = Agent(
    tools=[GeminiTools()],
    show_tool_calls=True,
)
```

## Usage Examples

GeminiTools can be used for a variety of tasks. Here are some examples:

### Image Generation

```python image_generation_agent.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.models.gemini import GeminiTools
from agno.utils.media import save_base64_data

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[GeminiTools()],
    show_tool_calls=True,
)

agent.print_response(
    "Create an artistic portrait of a cyberpunk samurai in a rainy city",
)
response = agent.run_response
if response.images:
    save_base64_data(response.images[0].content, "tmp/cyberpunk_samurai.png")
```

### Video Generation

<Note>
  Video generation requires Vertex AI.
</Note>

```python video_generation_agent.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.models.gemini import GeminiTools
from agno.utils.media import save_base64_data

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[GeminiTools(vertexai=True)],
    show_tool_calls=True,
    debug_mode=True,
)

agent.print_response(
    "Generate a 5-second video of a kitten playing a piano",
)
response = agent.run_response
if response.videos:
    for video in response.videos:
        save_base64_data(video.content, f"tmp/kitten_piano_{video.id}.mp4")
```

## Toolkit Functions

| Function         | Description                              |
| ---------------- | ---------------------------------------- |
| `generate_image` | Generate an image based on a text prompt |
| `generate_video` | Generate a video based on a text prompt  |

## Developer Resources

* View [Toolkit](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/models/gemini.py)
* View [Image Generation Guide](https://ai.google.dev/gemini-api/docs/image-generation)
* View [Video Generation Guide](https://ai.google.dev/gemini-api/docs/video)


