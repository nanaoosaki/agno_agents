---
title: Blog to Podcast Agent
category: misc
source_lines: 18702-18800
line_count: 98
---

# Blog to Podcast Agent
Source: https://docs.agno.com/examples/concepts/multimodal/blog-to-podcast



## Code

```python
import os
from uuid import uuid4
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.eleven_labs import ElevenLabsTools
from agno.tools.firecrawl import FirecrawlTools
from agno.agent import Agent, RunResponse
from agno.utils.audio import write_audio_to_file
from agno.utils.log import logger


url = "https://www.bcg.com/capabilities/artificial-intelligence/ai-agents"

blog_to_podcast_agent = Agent(
    name="Blog to Podcast Agent",
    agent_id="blog_to_podcast_agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        ElevenLabsTools(
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            target_directory="audio_generations",
        ),
        FirecrawlTools(),
    ],
    description="You are an AI agent that can generate audio using the ElevenLabs API.",
    instructions=[
        "When the user provides a blog URL:",
        "1. Use FirecrawlTools to scrape the blog content",
        "2. Create a concise summary of the blog content that is NO MORE than 2000 characters long", 
        "3. The summary should capture the main points while being engaging and conversational",
        "4. Use the ElevenLabsTools to convert the summary to audio",
        "You don't need to find the appropriate voice first, I already specified the voice to user",
        "Ensure the summary is within the 2000 character limit to avoid ElevenLabs API limits",
    ],
    markdown=True,
    debug_mode=True,
)

podcast: RunResponse = blog_to_podcast_agent.run(
    f"Convert the blog content to a podcast: {url}"
)

save_dir = "audio_generations"

if podcast.audio is not None and len(podcast.audio) > 0:
    try:
        os.makedirs(save_dir, exist_ok=True)
        filename = f"{save_dir}/sample_podcast{uuid4()}.wav"
        write_audio_to_file(
            audio=podcast.audio[0].base64_audio,
            filename=filename
        )
        print(f"Audio saved successfully to: {filename}")
    except Exception as e:
        print(f"Error saving audio file: {e}")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export OPENAI_API_KEY=xxx
    export ELEVEN_LABS_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U openai elevenlabs firecrawl-py agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/multimodal/blog_to_podcast.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/multimodal/blog_to_podcast.py
      ```
    </CodeGroup>
  </Step>
</Steps>


