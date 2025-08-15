---
title: Configure the tracer provider
category: misc
source_lines: 66530-66537
line_count: 7
---

# Configure the tracer provider
tracer_provider = TracerProvider()
tracer_provider.add_span_processor(
    SimpleSpanProcessor(OTLPSpanExporter(endpoint=OTEL_EXPORTER_OTLP_ENDPOINT, headers=headers))
)
trace_api.set_tracer_provider(tracer_provider=tracer_provider)

