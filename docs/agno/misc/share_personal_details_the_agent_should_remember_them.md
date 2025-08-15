---
title: Share personal details; the agent should remember them.
category: misc
source_lines: 48534-48553
line_count: 19
---

# Share personal details; the agent should remember them.
agent.print_response("My name is John Billings.", stream=True)
print("Current memories →")
pprint(agent.memory.memories)
print("Current summary →")
pprint(agent.memory.summaries)

agent.print_response("I live in NYC.", stream=True)
print("Memories →")
pprint(agent.memory.memories)
print("Summary →")
pprint(agent.memory.summaries)

agent.print_response("I'm going to a concert tomorrow.", stream=True)
print("Memories →")
pprint(agent.memory.memories)
print("Summary →")
pprint(agent.memory.summaries)

