---
title: CSV Tools
category: tools
source_lines: 26024-26089
line_count: 65
---

# CSV Tools
Source: https://docs.agno.com/examples/concepts/tools/database/csv



## Code

```python cookbook/tools/csv_tools.py
from pathlib import Path

import httpx
from agno.agent import Agent
from agno.tools.csv_toolkit import CsvTools

url = "https://agno-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv"
response = httpx.get(url)

imdb_csv = Path(__file__).parent.joinpath("imdb.csv")
imdb_csv.parent.mkdir(parents=True, exist_ok=True)
imdb_csv.write_bytes(response.content)

agent = Agent(
    tools=[CsvTools(csvs=[imdb_csv])],
    markdown=True,
    show_tool_calls=True,
    instructions=[
        "First always get the list of files",
        "Then check the columns in the file",
        "Then run the query to answer the question",
    ],
)
agent.cli_app(stream=False)
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
    pip install -U httpx openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/csv_tools.py
      ```

      ```bash Windows
      python cookbook/tools/csv_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


