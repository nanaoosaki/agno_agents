---
title: Image to Audio Agent
category: misc
source_lines: 19079-19156
line_count: 77
---

# Image to Audio Agent
Source: https://docs.agno.com/examples/concepts/multimodal/image-to-audio



## Code

```python
from pathlib import Path

from agno.agent import Agent, RunResponse
from agno.media import Image
from agno.models.openai import OpenAIChat
from agno.utils.audio import write_audio_to_file
from rich import print
from rich.text import Text

image_agent = Agent(model=OpenAIChat(id="gpt-4o"))

image_path = Path(__file__).parent.joinpath("sample.jpg")
image_story: RunResponse = image_agent.run(
    "Write a 3 sentence fiction story about the image",
    images=[Image(filepath=image_path)],
)
formatted_text = Text.from_markup(
    f":sparkles: [bold magenta]Story:[/bold magenta] {image_story.content} :sparkles:"
)
print(formatted_text)

audio_agent = Agent(
    model=OpenAIChat(
        id="gpt-4o-audio-preview",
        modalities=["text", "audio"],
        audio={"voice": "alloy", "format": "wav"},
    ),
)

audio_story: RunResponse = audio_agent.run(
    f"Narrate the story with flair: {image_story.content}"
)
if audio_story.response_audio is not None:
    write_audio_to_file(
        audio=audio_story.response_audio.content, filename="tmp/sample_story.wav"
    )
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
    pip install -U openai rich agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/multimodal/image_to_audio.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/multimodal/image_to_audio.py
      ```
    </CodeGroup>
  </Step>
</Steps>


