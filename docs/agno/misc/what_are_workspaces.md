---
title: What are Workspaces?
category: misc
source_lines: 85353-85365
line_count: 12
---

# What are Workspaces?

**Workspaces are standardized codebases for production Agentic Systems.** They contain:

* A RestAPI (FastAPI) for serving Agents, Teams and Workflows.
* A streamlit application for testing -- think of this as an admin interface.
* A postgres database for session and vector storage.

Workspaces are setup to run locally using docker and be easily deployed to AWS. They're a fantastic starting point and exactly what we use for our customers. You'll definitely need to customize them to fit your specific needs, but they'll get you started much faster.

They contain years of learnings, available for free for the open-source community.

