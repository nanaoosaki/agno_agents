---
title: Use the agent
category: misc
source_lines: 66549-66563
line_count: 14
---

# Use the agent
agent.print_response("What is the stock price of Apple?", stream=True)
```

## Notes

* **Environment Variables**: Ensure your environment variables are correctly set for the WandB API key.
* **Project Configuration**: Replace `<your-entity>/<your-project>` with your actual WandB entity and project name for OpenTelemetry setup.
* **Entity Name**: You can find your entity name by visiting your [WandB dashboard](https://wandb.ai/home) and checking the **Teams** field in the left sidebar.
* **Method Selection**: Use `weave.op` decorator for simpler setup, or OpenTelemetry for richer logging and better dashboard reporting.

By following these steps, you can effectively integrate Agno with Weave, enabling comprehensive logging and visualization of your AI agents' model calls.


