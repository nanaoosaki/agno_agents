---
title: Create Git Repo
category: misc
source_lines: 86057-86088
line_count: 31
---

# Create Git Repo
Source: https://docs.agno.com/workspaces/workspace-management/git-repo



Create a git repository to share your application with your team.

<Steps>
  <Step title="Create a git repository">
    Create a new [git repository](https://github.com/new).
  </Step>

  <Step title="Push your code">
    Push your code to the git repository.

    ```bash terminal
    git init
    git add .
    git commit -m "Init LLM App"
    git branch -M main
    git remote add origin https://github.com/[YOUR_GIT_REPO].git
    git push -u origin main
    ```
  </Step>

  <Step title="Ask your team to join">
    Ask your team to follow the [setup steps for new users](/workspaces/workspace-management/new-users) to use this workspace.
  </Step>
</Steps>


