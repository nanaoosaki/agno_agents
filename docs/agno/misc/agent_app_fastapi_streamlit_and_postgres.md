---
title: Agent App: FastAPI, Streamlit and Postgres
category: misc
source_lines: 85312-85346
line_count: 34
---

# Agent App: FastAPI, Streamlit and Postgres
Source: https://docs.agno.com/workspaces/agent-app/local



The Agent App is our go-to workspace for building agentic systems. It contains:

* A FastAPI server for serving Agents, Teams and Workflows.
* A streamlit application for debugging and testing. This streamlit app is very versatile and can be used as an admin interface for the agentic system and shows all sorts of data.
* A postgres database for session and vector storage.

It's designed to run locally using docker and in production on AWS.

<Snippet file="setup.mdx" />

<Snippet file="create-agent-app-codebase.mdx" />

<Snippet file="run-agent-app-local.mdx" />

<Snippet file="stop-local-workspace.mdx" />

## Next

Congratulations on running your AI App locally. Next Steps:

* [Run your Agent App on AWS](/workspaces/agent-app/aws)
* Read how to [update workspace settings](/workspaces/workspace-management/workspace-settings)
* Read how to [create a git repository for your workspace](/workspaces/workspace-management/git-repo)
* Read how to [manage the development application](/workspaces/workspace-management/development-app)
* Read how to [format and validate your code](/workspaces/workspace-management/format-and-validate)
* Read how to [add python libraries](/workspaces/workspace-management/install)
* Chat with us on [discord](https://agno.link/discord)


