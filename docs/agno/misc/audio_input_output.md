---
title: Audio Input Output
category: misc
source_lines: 18354-18368
line_count: 14
---

# Audio Input Output
Source: https://docs.agno.com/examples/concepts/multimodal/audio-input-output



## Code

```python
import requests
from agno.agent import Agent
from agno.media import Audio
from agno.models.openai import OpenAIChat
from agno.utils.audio import write_audio_to_file

