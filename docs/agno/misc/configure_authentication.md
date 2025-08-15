---
title: Configure authentication
category: misc
source_lines: 66521-66530
line_count: 9
---

# Configure authentication
WANDB_API_KEY = os.getenv("WANDB_API_KEY")
AUTH = base64.b64encode(f"api:{WANDB_API_KEY}".encode()).decode()

headers = {
    "Authorization": f"Basic {AUTH}",
    "project_id": PROJECT_ID,
}

