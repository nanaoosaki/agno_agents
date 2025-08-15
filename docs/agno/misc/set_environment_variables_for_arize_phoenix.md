---
title: Set environment variables for Arize Phoenix
category: misc
source_lines: 65767-65771
line_count: 4
---

# Set environment variables for Arize Phoenix
os.environ["PHOENIX_CLIENT_HEADERS"] = f"api_key={os.getenv('ARIZE_PHOENIX_API_KEY')}"
os.environ["PHOENIX_COLLECTOR_ENDPOINT"] = "https://app.phoenix.arize.com"

