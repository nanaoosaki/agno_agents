---
title: Initialize OpenLIT instrumentation
category: misc
source_lines: 66187-66191
line_count: 4
---

# Initialize OpenLIT instrumentation
import openlit
openlit.init(tracer=trace.get_tracer(__name__), disable_batch=True)

