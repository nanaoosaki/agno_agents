---
title: Monitoring
category: misc
source_lines: 60197-60281
line_count: 84
---

# Monitoring

You can track your Agent in real-time on [app.agno.com](https://app.agno.com).

## Authenticate

Authenticate with [agno.com](https://app.agno.com) to start monitoring your sessions.
Check out [Authentication guide](/how-to/authentication) for instructions on how to Authenticate with Agno.

## Enable Monitoring

Enable monitoring for a single agent or globally for all agents by setting `AGNO_MONITOR=true`.

### For a Specific Agent

```python
agent = Agent(markdown=True, monitoring=True)
```

### Globally for all Agents

```bash
export AGNO_MONITOR=true
```

## Monitor Your Agents

Run your agent and view the sessions on the [sessions page](https://app.agno.com/sessions).

<Steps>
  <Step title="Create a file with sample code">
    ```python monitoring.py
    from agno.agent import Agent

    agent = Agent(markdown=True, monitoring=True)
    agent.print_response("Share a 2 sentence horror story")
    ```
  </Step>

  <Step title="Run your Agent">
    ```shell
    python monitoring.py
    ```
  </Step>

  <Step title="View your sessions">
    View your sessions at [app.agno.com/sessions](https://app.agno.com/sessions)

    <img height="200" src="https://mintlify.s3.us-west-1.amazonaws.com/agno/images/monitoring.png" style={{ borderRadius: "8px" }} />
  </Step>
</Steps>

<Info>Facing issues? Check out our [troubleshooting guide](/faq/cli-auth)</Info>

## Debug Logs

Want to see the system prompt, user messages and tool calls?

Agno includes a built-in debugger that will print debug logs in the terminal. Set `debug_mode=True` on any agent or set `AGNO_DEBUG=true` in your environment.

```python debug_logs.py
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=Claude(id="claude-sonnet-4-20250514"),
    tools=[YFinanceTools(stock_price=True)],
    instructions="Use tables to display data. Don't include any other text.",
    markdown=True,
    debug_mode=True,
)
agent.print_response("What is the stock price of Apple?", stream=True)
```

Run the agent to view debug logs in the terminal:

```shell
python debug_logs.py
```

<video autoPlay muted controls className="w-full aspect-video" style={{ borderRadius: '8px' }} src="https://mintlify.s3.us-west-1.amazonaws.com/agno/videos/debug_logs.mp4" />


