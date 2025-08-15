---
title: Meeting Summary Agent
category: misc
source_lines: 27709-27791
line_count: 82
---

# Meeting Summary Agent
Source: https://docs.agno.com/examples/concepts/tools/models/openai/meeting-summarizer

Multi-modal Agno agent that transcribes meeting recordings, extracts key insights, generates visual summaries, and creates audio summaries using OpenAI tools.

This example demonstrates a multi-modal meeting summarizer and visualizer agent that uses OpenAITools and ReasoningTools to transcribe a meeting recording, extract key insights, generate a visual summary, and synthesize an audio summary.

## Code

```python ref/meeting_summarizer_agent.py
"""Example: Meeting Summarizer & Visualizer Agent

This script uses OpenAITools (transcribe_audio, generate_image, generate_speech)
to process a meeting recording, summarize it, visualize it, and create an audio summary.

Requires: pip install openai agno
"""

from pathlib import Path
from textwrap import dedent

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.openai import OpenAITools
from agno.tools.reasoning import ReasoningTools
from agno.utils.media import download_file, save_base64_data

input_audio_url: str = (
    "https://agno-public.s3.us-east-1.amazonaws.com/demo_data/sample_audio.mp3"
)

local_audio_path = Path("tmp/meeting_recording.mp3")
print(f"Downloading file to local path: {local_audio_path}")
download_file(input_audio_url, local_audio_path)

meeting_agent: Agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    tools=[OpenAITools(), ReasoningTools()],
    description=dedent("""\
        You are an efficient Meeting Assistant AI.
        Your purpose is to process audio recordings of meetings, extract key information,
        create a visual representation, and provide an audio summary.
    """),
    instructions=dedent(f"""\
        Follow these steps precisely:
        1. Receive the path to an audio file.
        2. Use the `transcribe_audio` tool to get the text transcription.
        3. Analyze the transcription and write a concise summary highlighting key discussion points, decisions, and action items.
        4. Based *only* on the summary created in step 3, generate formatted meeting minutes.
        5. Convert the meeting minutes into an audio summary using the `generate_speech` tool.
    """),
    markdown=True,
    show_tool_calls=True,
)

response = meeting_agent.run(
    f"Please process the meeting recording located at '{local_audio_path}'",
)
if response.audio:
    save_base64_data(response.audio[0].base64_audio, Path("tmp/meeting_summary.mp3"))
    print(f"Meeting summary saved to: {Path('tmp/meeting_summary.mp3')}")
```

## Usage

<Steps>
  <Step title="Install dependencies">
    ```bash
    pip install openai agno
    ```
  </Step>

  <Step title="Run the example">
    ```bash
    python ref/meeting_summarizer_agent.py
    ```
  </Step>
</Steps>

By default, the audio summary will be saved to `tmp/meeting_summary.mp3`.


