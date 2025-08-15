---
title: Configure the Phoenix tracer
category: misc
source_lines: 65815-65821
line_count: 6
---

# Configure the Phoenix tracer
tracer_provider = register(
    project_name="agno-stock-price-agent",  # Default is 'default'
    auto_instrument=True,  # Automatically use the installed OpenInference instrumentation
)

