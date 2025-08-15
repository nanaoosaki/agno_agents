---
title: Showing input audio, output audio and total audio tokens metrics
category: metrics
source_lines: 20136-20152
line_count: 16
---

# Showing input audio, output audio and total audio tokens metrics
print(f"Input audio tokens: {agent.run_response.metrics['input_audio_tokens']}")
print(f"Output audio tokens: {agent.run_response.metrics['output_audio_tokens']}")
print(f"Audio tokens: {agent.run_response.metrics['audio_tokens']}")

agent = Agent(
    model=OpenAIChat(id="o3-mini"),
    markdown=True,
    telemetry=False,
    monitoring=False,
    debug_mode=True,
)
agent.print_response(
    "Solve the trolley problem. Evaluate multiple ethical frameworks. Include an ASCII diagram of your solution.",
    stream=False,
)
