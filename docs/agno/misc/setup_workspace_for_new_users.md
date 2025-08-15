---
title: Setup workspace for new users
category: misc
source_lines: 86525-86641
line_count: 116
---

# Setup workspace for new users
Source: https://docs.agno.com/workspaces/workspace-management/new-users



Follow these steps to setup an existing workspace:

<Steps>
  <Step title="Clone git repository">
    Clone the git repo and `cd` into the workspace directory

    <CodeGroup>
      ```bash Mac
      git clone https://github.com/[YOUR_GIT_REPO].git

      cd your_workspace_directory
      ```

      ```bash Windows
      git clone https://github.com/[YOUR_GIT_REPO].git

      cd your_workspace_directory
      ```
    </CodeGroup>
  </Step>

  <Step title="Create and activate a virtual env">
    <CodeGroup>
      ```bash Mac
      python3 -m venv aienv
      source aienv/bin/activate
      ```

      ```bash Windows
      python3 -m venv aienv
      aienv/scripts/activate
      ```
    </CodeGroup>
  </Step>

  <Step title="Install agno">
    <CodeGroup>
      ```bash Mac
      pip install -U agno
      ```

      ```bash Windows
      pip install -U agno
      ```
    </CodeGroup>
  </Step>

  <Step title="Setup workspace">
    <CodeGroup>
      ```bash Mac
      ag ws setup
      ```

      ```bash Windows
      ag ws setup
      ```
    </CodeGroup>
  </Step>

  <Step title="Copy secrets">
    Copy `workspace/example_secrets` to `workspace/secrets`

    <CodeGroup>
      ```bash Mac
      cp -r workspace/example_secrets workspace/secrets
      ```

      ```bash Windows
      cp -r workspace/example_secrets workspace/secrets
      ```
    </CodeGroup>
  </Step>

  <Step title="Start workspace">
    <Note>
      Install [docker desktop](https://docs.docker.com/desktop/install/mac-install/) if needed.
    </Note>

    <CodeGroup>
      ```bash terminal
      ag ws up
      ```

      ```bash full options
      ag ws up --env dev --infra docker
      ```

      ```bash shorthand
      ag ws up dev:docker
      ```
    </CodeGroup>
  </Step>

  <Step title="Stop workspace">
    <CodeGroup>
      ```bash terminal
      ag ws down
      ```

      ```bash full options
      ag ws down --env dev --infra docker
      ```

      ```bash shorthand
      ag ws down dev:docker
      ```
    </CodeGroup>
  </Step>
</Steps>


