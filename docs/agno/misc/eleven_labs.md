---
title: Eleven Labs
category: misc
source_lines: 75501-75530
line_count: 29
---

# Eleven Labs
Source: https://docs.agno.com/tools/toolkits/others/eleven_labs



**ElevenLabsTools** enable an Agent to perform audio generation tasks using [ElevenLabs](https://elevenlabs.io/docs/product/introduction)

## Prerequisites

You need to install the `elevenlabs` library and an API key which can be obtained from [Eleven Labs](https://elevenlabs.io/)

```bash
pip install elevenlabs
```

Set the `ELEVEN_LABS_API_KEY` environment variable.

```bash
export ELEVEN_LABS_API_KEY=****
```

## Example

The following agent will use Eleven Labs to generate audio based on a user prompt.

```python cookbook/tools/eleven_labs_tools.py
from agno.agent import Agent
from agno.tools.eleven_labs import ElevenLabsTools

