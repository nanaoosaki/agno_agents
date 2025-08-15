---
title: Groq
category: misc
source_lines: 74147-74277
line_count: 130
---

# Groq
Source: https://docs.agno.com/tools/toolkits/models/groq



`GroqTools` allows an Agent to interact with the Groq API for performing fast audio transcription, translation, and text-to-speech (TTS).

## Prerequisites

Before using `GroqTools`, ensure you have the `groq` library installed and your Groq API key configured.

1. **Install the library:**
   ```bash
   pip install -U groq
   ```

2. **Set your API key:** Obtain your API key from the [Groq Console](https://console.groq.com/keys) and set it as an environment variable.

   <CodeGroup>
     ```bash Mac
     export GROQ_API_KEY="your-groq-api-key"
     ```

     ```bash Windows
     setx GROQ_API_KEY "your-groq-api-key"
     ```
   </CodeGroup>

## Initialization

Import `GroqTools` and add it to your Agent's tool list.

```python
from agno.agent import Agent
from agno.tools.models.groq import GroqTools

agent = Agent(
    instructions=[
        "You are a helpful assistant that can transcribe audio, translate text and generate speech."
    ],
    tools=[GroqTools()],
    show_tool_calls=True,
)
```

## Usage Examples

### 1. Transcribing Audio

This example demonstrates how to transcribe an audio file hosted at a URL.

```python transcription_agent.py
import os
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.models.groq import GroqTools

audio_url = "https://agno-public.s3.amazonaws.com/demo_data/sample_conversation.wav"

agent = Agent(
    name="Groq Transcription Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[GroqTools()],
    show_tool_calls=True,
)

agent.print_response(f"Please transcribe the audio file located at '{audio_url}'")
```

### 2. Translating Audio and Generating Speech

This example shows how to translate an audio file (e.g., French) to English and then generate a new audio file from the translated text.

```python translation_agent.py
from pathlib import Path
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.models.groq import GroqTools
from agno.utils.media import save_base64_data

local_audio_path = "tmp/sample-fr.mp3"
output_path = Path("tmp/sample-en.mp3")
output_path.parent.mkdir(parents=True, exist_ok=True)

agent = Agent(
    name="Groq Translation Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[GroqTools()],
    show_tool_calls=True,
)

instruction = (
    f"Translate the audio file at '{local_audio_path}' to English. "
    f"Then, generate a new audio file using the translated English text."
)
agent.print_response(instruction)

response = agent.run_response
if response and response.audio:
    save_base64_data(response.audio[0].base64_audio, output_path)
```

You can customize the underlying Groq models used for transcription, translation, and TTS during initialization:

```python
groq_tools = GroqTools(
    transcription_model="whisper-large-v3",
    translation_model="whisper-large-v3",
    tts_model="playai-tts",
    tts_voice="Chip-PlayAI"
)
```

## Toolkit Functions

The `GroqTools` toolkit provides the following functions:

| Function           | Description                                                                  |
| ------------------ | ---------------------------------------------------------------------------- |
| `transcribe_audio` | Transcribes audio from a local file path or a public URL using Groq Whisper. |
| `translate_audio`  | Translates audio from a local file path or public URL to English using Groq. |
| `generate_speech`  | Generates speech from text using Groq TTS.                                   |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/models/groq.py)
* View [Transcription Example](https://github.com/agno-agi/agno/blob/main/cookbook/models/groq/transcription_agent.py)
* View [Translation Example](https://github.com/agno-agi/agno/blob/main/cookbook/models/groq/translation_agent.py)


