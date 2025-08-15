---
title: Audio Conversation Agent
category: misc
source_lines: 8882-8957
line_count: 75
---

# Audio Conversation Agent
Source: https://docs.agno.com/examples/applications/playground/audio_conversation_agent



This example shows how to use the audio conversation agent with playground.

## Code

```python cookbook/apps/playground/audio_conversation_agent.py 
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.playground import Playground
from agno.storage.sqlite import SqliteStorage

audio_and_text_agent = Agent(
    agent_id="audio-text-agent",
    name="Audio and Text Chat Agent",
    model=OpenAIChat(
        id="gpt-4o-audio-preview",
        modalities=["text", "audio"],
        audio={"voice": "alloy", "format": "pcm16"},
    ),
    debug_mode=True,
    add_history_to_messages=True,
    add_datetime_to_instructions=True,
    storage=SqliteStorage(
        table_name="audio_agent", db_file="tmp/audio_agent.db", auto_upgrade_schema=True
    ),
)

playground = Playground(
    agents=[audio_and_text_agent],
    name="Audio Conversation Agent",
    description="A playground for audio conversation agent",
    app_id="audio-conversation-agent",
)
app = playground.get_app()

if __name__ == "__main__":
    playground.serve(app="audio_conversation_agent:app", reload=True)

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
    pip install -U agno "uvicorn[standard]" openai
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/apps/playground/audio_conversation_agent.py
      ```

      ```bash Windows
      python cookbook/apps/playground/audio_conversation_agent.py
      ```
    </CodeGroup>
  </Step>
</Steps>


