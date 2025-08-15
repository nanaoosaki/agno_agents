---
title: Initialize LangWatch and instrument Agno
category: misc
source_lines: 66408-66433
line_count: 25
---

# Initialize LangWatch and instrument Agno
langwatch.setup(
    instrumentors=[AgnoInstrumentor()]
)

agent = Agent(
    name="Stock Price Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[YFinanceTools()],
    instructions="You are a stock price agent. Answer questions in the style of a stock analyst.",
    debug_mode=True,
)

agent.print_response("What is the current price of Tesla?")
```

## Notes

* **No OpenTelemetry Setup Needed**: You do **not** need to set any OpenTelemetry environment variables or configure exporters manually—`langwatch.setup()` handles everything.
* **Troubleshooting**: If you see no traces in LangWatch, ensure your `LANGWATCH_API_KEY` is set and that the instrumentor is included in `langwatch.setup()`.
* For advanced configuration (custom attributes, endpoint, etc.), see the [LangWatch Python integration guide](https://docs.langwatch.ai/integration/python/integrations/agno).

By following these steps, you can effectively integrate Agno with LangWatch,  enabling comprehensive observability and monitoring of your AI agents.


