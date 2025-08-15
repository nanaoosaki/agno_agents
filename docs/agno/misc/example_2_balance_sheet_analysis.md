---
title: Example 2: Balance Sheet Analysis
category: misc
source_lines: 28762-28802
line_count: 40
---

# Example 2: Balance Sheet Analysis
print("\n=== Balance Sheet Analysis Example ===")
agent.print_response(
    "Analyze the balance sheets for MSFT over the last 3 years. Focus on debt-to-equity ratio and cash position.",
    stream=True,
)

```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API credentials">
    ```bash
    export FINANCIAL_DATASETS_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
        python cookbook/tools/financial_datasets_tools.py
      ```

      ```bash Windows
        python cookbook/tools/financial_datasets_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


