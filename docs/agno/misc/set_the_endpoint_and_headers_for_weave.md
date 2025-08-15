---
title: Set the endpoint and headers for Weave
category: misc
source_lines: 66516-66521
line_count: 5
---

# Set the endpoint and headers for Weave
WANDB_BASE_URL = "https://trace.wandb.ai"
PROJECT_ID = "<your-entity>/<your-project>"
OTEL_EXPORTER_OTLP_ENDPOINT = f"{WANDB_BASE_URL}/otel/v1/traces"

