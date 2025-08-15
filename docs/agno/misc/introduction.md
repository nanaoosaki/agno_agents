---
title: Introduction
category: misc
source_lines: 86181-86525
line_count: 344
---

# Introduction
Source: https://docs.agno.com/workspaces/workspace-management/introduction



**Agno Workspaces** are standardized codebases for running Agentic Systems locally using Docker and in production on AWS. They help us manage our Agentic System as code.

![workspace](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/workspace.png)

## Create a new workspace

Run `ag ws create` to create a new workspace, the command will ask your for a starter template and workspace name.

<CodeGroup>
  ```bash Create Workspace
  ag ws create
  ```

  ```bash Create Agent App
  ag ws create -t agent-app-aws -n agent-app
  ```

  ```bash Create Agent API
  ag ws create -t agent-api-aws -n agent-api
  ```
</CodeGroup>

## Start workspace resources

Run `ag ws up` to start i.e. create workspace resources

<CodeGroup>
  ```bash terminal
  ag ws up
  ```

  ```bash shorthand
  ag ws up dev:docker
  ```

  ```bash full options
  ag ws up --env dev --infra docker
  ```

  ```bash short options
  ag ws up -e dev -i docker
  ```
</CodeGroup>

## Stop workspace resources

Run `ag ws down` to stop i.e. delete workspace resources

<CodeGroup>
  ```bash terminal
  ag ws down
  ```

  ```bash shorthand
  ag ws down dev:docker
  ```

  ```bash full options
  ag ws down --env dev --infra docker
  ```

  ```bash short options
  ag ws down -e dev -i docker
  ```
</CodeGroup>

## Patch workspace resources

Run `ag ws patch` to patch i.e. update workspace resources

<CodeGroup>
  ```bash terminal
  ag ws patch
  ```

  ```bash shorthand
  ag ws patch dev:docker
  ```

  ```bash full options
  ag ws patch --env dev --infra docker
  ```

  ```bash short options
  ag ws patch -e dev -i docker
  ```
</CodeGroup>

<br />

<Note>
  The `patch` command in under development for some resources. Use `restart` if needed
</Note>

## Restart workspace

Run `ag ws restart` to stop resources and start them again

<CodeGroup>
  ```bash terminal
  ag ws restart
  ```

  ```bash shorthand
  ag ws restart dev:docker
  ```

  ```bash full options
  ag ws restart --env dev --infra docker
  ```

  ```bash short options
  ag ws restart -e dev -i docker
  ```
</CodeGroup>

## Setup existing workspace

If you clone the codebase directly (eg: if your coworker created it) - run `ag ws setup` to set it up locally

<CodeGroup>
  ```bash terminal
  ag ws setup
  ```

  ```bash with debug logs
  ag ws setup -d
  ```
</CodeGroup>

## Command Options

<Note>Run `ag ws up --help` to view all options</Note>

### Environment (`--env`)

Use the `--env` or `-e` flag to filter the environment (dev/prd)

<CodeGroup>
  ```bash flag
  ag ws up --env dev
  ```

  ```bash shorthand
  ag ws up dev
  ```

  ```bash short options
  ag ws up -e dev
  ```
</CodeGroup>

### Infra (`--infra`)

Use the `--infra` or `-i` flag to filter the infra (docker/aws/k8s)

<CodeGroup>
  ```bash flag
  ag ws up --infra docker
  ```

  ```bash shorthand
  ag ws up :docker
  ```

  ```bash short options
  ag ws up -i docker
  ```
</CodeGroup>

### Group (`--group`)

Use the `--group` or `-g` flag to filter by resource group.

<CodeGroup>
  ```bash flag
  ag ws up --group app
  ```

  ```bash full options
  ag ws up \
    --env dev \
    --infra docker \
    --group app
  ```

  ```bash shorthand
  ag ws up dev:docker:app
  ```

  ```bash short options
  ag ws up \
    -e dev \
    -i docker \
    -g app
  ```
</CodeGroup>

### Name (`--name`)

Use the `--name` or `-n` flag to filter by resource name

<CodeGroup>
  ```bash flag
  ag ws up --name app
  ```

  ```bash full options
  ag ws up \
    --env dev \
    --infra docker \
    --name app
  ```

  ```bash shorthand
  ag ws up dev:docker::app
  ```

  ```bash short options
  ag ws up \
    -e dev \
    -i docker \
    -n app
  ```
</CodeGroup>

### Type (`--type`)

Use the `--type` or `-t` flag to filter by resource type.

<CodeGroup>
  ```bash flag
  ag ws up --type container
  ```

  ```bash full options
  ag ws up \
    --env dev \
    --infra docker \
    --type container
  ```

  ```bash shorthand
  ag ws up dev:docker:app::container
  ```

  ```bash short options
  ag ws up \
    -e dev \
    -i docker \
    -t container
  ```
</CodeGroup>

### Dry Run (`--dry-run`)

The `--dry-run` or `-dr` flag can be used to **dry-run** the command. `ag ws up -dr` will only print resources, not create them.

<CodeGroup>
  ```bash flag
  ag ws up --dry-run
  ```

  ```bash full options
  ag ws up \
    --env dev \
    --infra docker \
    --dry-run
  ```

  ```bash shorthand
  ag ws up dev:docker -dr
  ```

  ```bash short options
  ag ws up \
    -e dev \
    -i docker \
    -dr
  ```
</CodeGroup>

### Show Debug logs (`--debug`)

Use the `--debug` or `-d` flag to show debug logs.

<CodeGroup>
  ```bash flag
  ag ws up -d
  ```

  ```bash full options
  ag ws up \
    --env dev \
    --infra docker \
    -d
  ```

  ```bash shorthand
  ag ws up dev:docker -d
  ```

  ```bash short options
  ag ws up \
    -e dev \
    -i docker \
    -d
  ```
</CodeGroup>

### Force recreate images & containers (`-f`)

Use the `--force` or `-f` flag to force recreate images & containers

<CodeGroup>
  ```bash flag
  ag ws up -f
  ```

  ```bash full options
  ag ws up \
    --env dev \
    --infra docker \
    -f
  ```

  ```bash shorthand
  ag ws up dev:docker -f
  ```

  ```bash short options
  ag ws up \
    -e dev \
    -i docker \
    -f
  ```
</CodeGroup>


