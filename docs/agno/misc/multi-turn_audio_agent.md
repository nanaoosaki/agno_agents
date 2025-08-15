---
title: Multi-turn Audio Agent
category: misc
source_lines: 18425-18491
line_count: 66
---

# Multi-turn Audio Agent
Source: https://docs.agno.com/examples/concepts/multimodal/audio-multi-turn



## Code

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.utils.audio import write_audio_to_file

agent = Agent(
    model=OpenAIChat(
        id="gpt-4o-audio-preview",
        modalities=["text", "audio"],
        audio={"voice": "alloy", "format": "wav"},
    ),
    debug_mode=True,
    add_history_to_messages=True,
)

agent.run("Is a golden retriever a good family dog?")
if agent.run_response.response_audio is not None:
    write_audio_to_file(
        audio=agent.run_response.response_audio.content, filename="tmp/answer_1.wav"
    )

agent.run("Why do you say they are loyal?")
if agent.run_response.response_audio is not None:
    write_audio_to_file(
        audio=agent.run_response.response_audio.content, filename="tmp/answer_2.wav"
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
    pip install -U openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/multimodal/audio_multi_turn.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/multimodal/audio_multi_turn.py
      ```
    </CodeGroup>
  </Step>
</Steps>


