---
title: Sets the global default tracer provider
category: misc
source_lines: 19818-19823
line_count: 5
---

# Sets the global default tracer provider
from opentelemetry import trace

trace.set_tracer_provider(trace_provider)

