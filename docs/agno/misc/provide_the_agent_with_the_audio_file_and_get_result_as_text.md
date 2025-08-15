---
title: Provide the agent with the audio file and get result as text
category: misc
source_lines: 46424-46465
line_count: 41
---

# Provide the agent with the audio file and get result as text
agent = Agent(
    model=OpenAIChat(id="gpt-4o-audio-preview", modalities=["text"]),
    markdown=True,
)
agent.print_response(
    "What is in this audio?", audio=[Audio(content=wav_data, format="wav")]
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
    pip install -U openai requests agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/models/openai/chat/audio_input_agent.py
      ```

      ```bash Windows
      python cookbook/models/openai/chat/audio_input_agent.py
      ```
    </CodeGroup>
  </Step>
</Steps>


