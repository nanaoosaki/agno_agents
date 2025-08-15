---
title: Initialize OpenLIT instrumentation. The disable_batch flag is set to true to process traces immediately.
category: misc
source_lines: 19828-19878
line_count: 50
---

# Initialize OpenLIT instrumentation. The disable_batch flag is set to true to process traces immediately.
openlit.init(tracer=tracer, disable_batch=True)

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGoTools()],
    markdown=True,
    debug_mode=True,
)

agent.print_response("What is currently trending on Twitter?")
```

## Usage

<Steps>
  <Step title="Install Dependencies">
    ```bash
    pip install agno openai langfuse openlit opentelemetry-sdk opentelemetry-exporter-otlp
    ```
  </Step>

  <Step title="Set Environment Variables">
    ```bash
    export LANGFUSE_PUBLIC_KEY=<your-public-key>
    export LANGFUSE_SECRET_KEY=<your-secret-key>
    ```
  </Step>

  <Step title="Run the Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/observability/langfuse_via_openlit.py
      ```

      ```bash Windows
      python cookbook/observability/langfuse_via_openlit.py
      ```
    </CodeGroup>
  </Step>
</Steps>

## Notes

* **Data Regions**: Adjust the `OTEL_EXPORTER_OTLP_ENDPOINT` for your data region or local deployment as needed:
  * `https://us.cloud.langfuse.com/api/public/otel` for the US region
  * `https://cloud.langfuse.com/api/public/otel` for the EU region
  * `http://localhost:3000/api/public/otel` for local deployment


