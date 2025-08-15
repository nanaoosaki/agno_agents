---
title: Step 3: Instrument and execute
category: misc
source_lines: 65889-65902
line_count: 13
---

# Step 3: Instrument and execute
with instrument_agno("openai"):
    response = agent.run("Retrieve the latest news about the stock market.")
    print(response.content)
```

Now go to the [Atla dashboard](https://app.atla-ai.com/app/) and view the traces created by your agent. You can visualize the execution flow, monitor performance, and debug issues directly from the Atla dashboard.

<Frame caption="Atla Agent run trace">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/agno/images/atla-trace-summary.png" style={{ borderRadius: '10px', width: '100%', maxWidth: '800px' }} alt="atla-trace" />
</Frame>


