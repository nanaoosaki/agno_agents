---
title: Showing reasoning tokens metrics
category: metrics
source_lines: 20152-20161
line_count: 9
---

# Showing reasoning tokens metrics
print(f"Reasoning tokens: {agent.run_response.metrics['reasoning_tokens']}")


agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"), markdown=True, telemetry=False, monitoring=False
)
agent.run("Share a 2 sentence horror story" * 150)
agent.print_response("Share a 2 sentence horror story" * 150)
