---
title: Agent API: FastAPI and Postgres
category: core
source_lines: 85246-85277
line_count: 31
---

# Agent API: FastAPI and Postgres
Source: https://docs.agno.com/workspaces/agent-api/local



The Agent API workspace provides a simple RestAPI + database for serving agents. It contains:

* A FastAPI server for serving Agents, Teams and Workflows.
* A postgres database for session and vector storage.

<Snippet file="setup.mdx" />

<Snippet file="create-agent-api-codebase.mdx" />

<Snippet file="run-agent-api-local.mdx" />

<Snippet file="stop-local-workspace.mdx" />

## Next

Congratulations on running your Agent API locally. Next Steps:

* [Run your Agent API on AWS](/workspaces/agent-api/aws)
* Read how to [update workspace settings](/workspaces/workspace-management/workspace-settings)
* Read how to [create a git repository for your workspace](/workspaces/workspace-management/git-repo)
* Read how to [manage the development application](/workspaces/workspace-management/development-app)
* Read how to [format and validate your code](/workspaces/workspace-management/format-and-validate)
* Read how to [add python libraries](/workspaces/workspace-management/install)
* Chat with us on [discord](https://agno.link/discord)


