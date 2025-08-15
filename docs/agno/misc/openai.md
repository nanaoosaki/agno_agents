---
title: OpenAI
category: misc
source_lines: 74277-74431
line_count: 154
---

# OpenAI
Source: https://docs.agno.com/tools/toolkits/models/openai



OpenAITools allow an Agent to interact with OpenAI models for performing audio transcription, image generation, and text-to-speech.

## Prerequisites

Before using `OpenAITools`, ensure you have the `openai` library installed and your OpenAI API key configured.

1. **Install the library:**
   ```bash
   pip install -U openai
   ```

2. **Set your API key:** Obtain your API key from [OpenAI](https://platform.openai.com/account/api-keys) and set it as an environment variable.

   <CodeGroup>
     ```bash Mac
     export OPENAI_API_KEY="your-openai-api-key"
     ```

     ```bash Windows
     setx OPENAI_API_KEY "your-openai-api-key"
     ```
   </CodeGroup>

## Initialization

Import `OpenAITools` and add it to your Agent's tool list.

```python
from agno.agent import Agent
from agno.tools.openai import OpenAITools

agent = Agent(
    name="OpenAI Agent",
    tools=[OpenAITools()],
    show_tool_calls=True,
    markdown=True,
)
```

## Usage Examples

### 1. Transcribing Audio

This example demonstrates an agent that transcribes an audio file.

```python transcription_agent.py
from pathlib import Path
from agno.agent import Agent
from agno.tools.openai import OpenAITools
from agno.utils.media import download_file

audio_url = "https://agno-public.s3.amazonaws.com/demo_data/sample_conversation.wav"

local_audio_path = Path("tmp/sample_conversation.wav")
download_file(audio_url, local_audio_path)

agent = Agent(
    name="OpenAI Transcription Agent",
    tools=[OpenAITools(transcription_model="whisper-1")],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response(f"Transcribe the audio file located at '{local_audio_path}'")
```

### 2. Generating Images

This example demonstrates an agent that generates an image based on a text prompt.

```python image_generation_agent.py
from agno.agent import Agent
from agno.tools.openai import OpenAITools
from agno.utils.media import save_base64_data

agent = Agent(
    name="OpenAI Image Generation Agent",
    tools=[OpenAITools(image_model="dall-e-3")],
    show_tool_calls=True,
    markdown=True,
)

response = agent.run("Generate a photorealistic image of a cozy coffee shop interior")

if response.images:
    save_base64_data(response.images[0].content, "tmp/coffee_shop.png")
```

### 3. Generating Speech

This example demonstrates an agent that generates speech from text.

```python speech_synthesis_agent.py
from agno.agent import Agent
from agno.tools.openai import OpenAITools
from agno.utils.media import save_base64_data

agent = Agent(
    name="OpenAI Speech Agent",
    tools=[OpenAITools(
        text_to_speech_model="tts-1",
        text_to_speech_voice="alloy",
        text_to_speech_format="mp3"
    )],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Generate audio for the text: 'Hello, this is a synthesized voice example.'")

response = agent.run_response
if response and response.audio:
    save_base64_data(response.audio[0].base64_audio, "tmp/hello.mp3")
```

<Note> View more examples [here](/examples/concepts/tools/models/openai). </Note>

## Customization

You can customize the underlying OpenAI models used for transcription, image generation, and TTS:

```python
OpenAITools(
    transcription_model="whisper-1",
    image_model="dall-e-3",
    text_to_speech_model="tts-1-hd",
    text_to_speech_voice="nova",
    text_to_speech_format="wav"
)
```

## Toolkit Functions

The `OpenAITools` toolkit provides the following functions:

| Function           | Description                                              |
| ------------------ | -------------------------------------------------------- |
| `transcribe_audio` | Transcribes audio from a local file path or a public URL |
| `generate_image`   | Generates images based on a text prompt                  |
| `generate_speech`  | Synthesizes speech from text                             |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/openai.py)
* View [OpenAI Transcription Guide](https://platform.openai.com/docs/guides/speech-to-text)
* View [OpenAI Image Generation Guide](https://platform.openai.com/docs/guides/image-generation?image-generation-model=gpt-image-1)
* View [OpenAI Text-to-Speech Guide](https://platform.openai.com/docs/guides/text-to-speech)


