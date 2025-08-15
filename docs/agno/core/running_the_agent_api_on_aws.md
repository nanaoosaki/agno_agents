---
title: Running the Agent API on AWS
category: core
source_lines: 85213-85246
line_count: 33
---

# Running the Agent API on AWS
Source: https://docs.agno.com/workspaces/agent-api/aws



Let's run the **Agent API** in production on AWS.

<Snippet file="aws-setup.mdx" />

<Snippet file="update-agent-api-prd-secrets.mdx" />

<Snippet file="create-aws-resources.mdx" />

<Snippet file="agent-app-production-fastapi.mdx" />

<Snippet file="agent-app-update-production.mdx" />

<Snippet file="agent-app-delete-aws-resources.mdx" />

## Next

Congratulations on running your Agent API on AWS. Next Steps:

* Read how to [update workspace settings](/workspaces/workspace-management/workspace-settings)
* Read how to [create a git repository for your workspace](/workspaces/workspace-management/git-repo)
* Read how to [manage the production application](/workspaces/workspace-management/production-app)
* Read how to [format and validate your code](/workspaces/workspace-management/format-and-validate)
* Read how to [add python libraries](/workspaces/workspace-management/install)
* Read how to [add a custom domain and HTTPS](/workspaces/workspace-management/domain-https)
* Read how to [implement CI/CD](/workspaces/workspace-management/ci-cd)
* Chat with us on [discord](https://agno.link/discord)


