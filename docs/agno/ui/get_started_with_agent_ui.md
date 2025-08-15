---
title: Get Started with Agent UI
category: ui
source_lines: 44-190
line_count: 146
---

# Get Started with Agent UI

To clone the Agent UI, run the following command in your terminal:

```bash
npx create-agent-ui@latest
```

Enter `y` to create a new project, install dependencies, then run the agent-ui using:

```bash
cd agent-ui && npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view the Agent UI, but remember to connect to your local agents.

<Frame>
  <img height="200" src="https://mintlify.s3.us-west-1.amazonaws.com/agno/images/agent-ui-homepage.png" style={{ borderRadius: '8px' }} />
</Frame>

<br />

<Accordion title="Clone the repository manually" icon="github">
  You can also clone the repository manually

  ```bash
  git clone https://github.com/agno-agi/agent-ui.git
  ```

  And run the agent-ui using

  ```bash
  cd agent-ui && pnpm install && pnpm dev
  ```
</Accordion>

## Connect to Local Agents

The Agent UI needs to connect to a playground server, which you can run locally or on any cloud provider.

Let's start with a local playground server. Create a file `playground.py`

```python playground.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.playground import Playground
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

agent_storage: str = "tmp/agents.db"

web_agent = Agent(
    name="Web Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=["Always include sources"],
    # Store the agent sessions in a sqlite database
    storage=SqliteStorage(table_name="web_agent", db_file=agent_storage),
    # Adds the current date and time to the instructions
    add_datetime_to_instructions=True,
    # Adds the history of the conversation to the messages
    add_history_to_messages=True,
    # Number of history responses to add to the messages
    num_history_responses=5,
    # Adds markdown formatting to the messages
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Always use tables to display data"],
    storage=SqliteStorage(table_name="finance_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)

playground = Playground(agents=[web_agent, finance_agent])
app = playground.get_app()

if __name__ == "__main__":
    playground.serve("playground:app", reload=True)
```

In another terminal, run the playground server:

<Steps>
  <Step title="Setup your virtual environment">
    <CodeGroup>
      ```bash Mac
      python3 -m venv .venv
      source .venv/bin/activate
      ```

      ```bash Windows
      python3 -m venv aienv
      aienv/scripts/activate
      ```
    </CodeGroup>
  </Step>

  <Step title="Install dependencies">
    <CodeGroup>
      ```bash Mac
      pip install -U openai duckduckgo-search yfinance sqlalchemy 'fastapi[standard]' agno
      ```

      ```bash Windows
      pip install -U openai duckduckgo-search yfinance sqlalchemy 'fastapi[standard]' agno
      ```
    </CodeGroup>
  </Step>

  <Step title="Export your OpenAI key">
    <CodeGroup>
      ```bash Mac
      export OPENAI_API_KEY=sk-***
      ```

      ```bash Windows
      setx OPENAI_API_KEY sk-***
      ```
    </CodeGroup>
  </Step>

  <Step title="Run the Playground">
    ```shell
    python playground.py
    ```
  </Step>
</Steps>

<Tip>Make sure the `serve_playground_app()` points to the file containing your `Playground` app.</Tip>

## View the playground

* Open [http://localhost:3000](http://localhost:3000) to view the Agent UI
* Select the `localhost:7777` endpoint and start chatting with your agents!

<video autoPlay muted controls className="w-full aspect-video" src="https://mintlify.s3.us-west-1.amazonaws.com/agno/videos/agent-ui-demo.mp4" />


