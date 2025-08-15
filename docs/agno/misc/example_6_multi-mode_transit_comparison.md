---
title: Example 6: Multi-mode Transit Comparison
category: misc
source_lines: 29046-29093
line_count: 47
---

# Example 6: Multi-mode Transit Comparison
print("\n=== Transit Options Example ===")
agent.print_response(
    """Compare different travel modes from 'Phoenix Convention Center' to 'Phoenix Art Museum':
    1. Driving
    2. Walking
    3. Transit (if available)
    Include estimated time and distance for each option.""",
    markdown=True,
    stream=True,
)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API keys">
    ```bash
    export GOOGLE_MAPS_API_KEY=xxx
    export OPENAI_API_KEY=xxx
    ```

    Get your API key from the [Google Cloud Console](https://console.cloud.google.com/projectselector2/google/maps-apis/credentials)
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U openai googlemaps agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/google_maps_tools.py
      ```

      ```bash Windows
      python cookbook/tools/google_maps_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


