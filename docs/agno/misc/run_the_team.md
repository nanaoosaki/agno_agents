---
title: Run the team
category: misc
source_lines: 69988-69994
line_count: 6
---

# Run the team
run_stream: Iterator[RunResponse] = team.run(
    "What is the stock price of NVDA", stream=True
)
pprint_run_response(run_stream, markdown=True)

