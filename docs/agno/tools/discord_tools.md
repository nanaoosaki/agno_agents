---
title: Discord Tools
category: tools
source_lines: 30538-30616
line_count: 78
---

# Discord Tools
Source: https://docs.agno.com/examples/concepts/tools/social/discord



## Code

```python cookbook/tools/discord_tools.py
from agno.agent import Agent
from agno.tools.discord import DiscordTools

discord_tools = DiscordTools(
    bot_token=discord_token,
    enable_messaging=True,
    enable_history=True,
    enable_channel_management=True,
    enable_message_management=True,
)

discord_agent = Agent(
    name="Discord Agent",
    instructions=[
        "You are a Discord bot that can perform various operations.",
        "You can send messages, read message history, manage channels, and delete messages.",
    ],
    tools=[discord_tools],
    show_tool_calls=True,
    markdown=True,
)

channel_id = "YOUR_CHANNEL_ID"
server_id = "YOUR_SERVER_ID"

discord_agent.print_response(
    f"Send a message 'Hello from Agno!' to channel {channel_id}", stream=True
)

discord_agent.print_response(f"Get information about channel {channel_id}", stream=True)

discord_agent.print_response(f"List all channels in server {server_id}", stream=True)

discord_agent.print_response(
    f"Get the last 5 messages from channel {channel_id}", stream=True
)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your Discord token">
    ```bash
    export DISCORD_BOT_TOKEN=xxx
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U discord.py openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/discord_tools.py
      ```

      ```bash Windows
      python cookbook/tools/discord_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


