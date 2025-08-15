---
title: Create and configure the playground app
category: misc
source_lines: 8833-8882
line_count: 49
---

# Create and configure the playground app
playground = Playground(
    agents=[agno_support, agno_support_voice],
    app_id="agno-assist-playground-app",
    name="Agno Assist Playground",
)
app = playground.get_app()

if __name__ == "__main__":
    load_kb = False
    if load_kb:
        agent_knowledge.load(recreate=True)
    playground.serve(app="agno_assist:app", reload=True)


````

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API keys">
    ```bash
    export OPENAI_API_KEY=xxx
    export ELEVEN_LABS_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U agno "uvicorn[standard]" openai lancedb elevenlabs
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/apps/playground/agno_assist.py
      ```

      ```bash Windows
      python cookbook/apps/playground/agno_assist.py
      ```
    </CodeGroup>
  </Step>
</Steps>


