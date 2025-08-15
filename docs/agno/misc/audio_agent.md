---
title: Audio Agent
category: misc
source_lines: 34690-34715
line_count: 25
---

# Audio Agent
Source: https://docs.agno.com/examples/getting-started/audio-agent



This example shows how to create an AI agent that can process audio input and generate audio responses. You can use this agent for various voice-based interactions, from analyzing speech content to generating natural-sounding responses.

Example audio interactions to try:

* Upload a recording of a conversation for analysis
* Have the agent respond to questions with voice output
* Process different languages and accents
* Analyze tone and emotion in speech

## Code

```python audio_agent.py
from textwrap import dedent

import requests
from agno.agent import Agent
from agno.media import Audio
from agno.models.openai import OpenAIChat
from agno.utils.audio import write_audio_to_file

