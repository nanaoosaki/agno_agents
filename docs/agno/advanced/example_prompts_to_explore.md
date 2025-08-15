---
title: Example prompts to explore:
category: advanced
source_lines: 9125-9183
line_count: 58
---

# Example prompts to explore:
"""
Issue queries:
1. "Find issues needing attention"
2. "Show me issues by label"
3. "What issues are being actively discussed?"
4. "Find related issues"
5. "Analyze issue resolution patterns"

Pull request queries:
1. "What PRs need review?"
2. "Show me recent merged PRs"
3. "Find PRs with conflicts"
4. "What features are being developed?"
5. "Analyze PR review patterns"

Repository queries:
1. "Show repository health metrics"
2. "What are the contribution guidelines?"
3. "Find documentation gaps"
4. "Analyze code quality trends"
5. "Show repository activity patterns"
"""

```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API keys">
    ```bash
    export OPENAI_API_KEY=xxx
    export GITHUB_TOKEN=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U agno "uvicorn[standard]" openai nest-asyncio mcp
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/apps/playground/mcp_demo.py
      ```

      ```bash Windows
      python cookbook/apps/playground/mcp_demo.py
      ```
    </CodeGroup>
  </Step>
</Steps>


