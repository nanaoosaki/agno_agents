---
title: Development Application
category: misc
source_lines: 85760-85861
line_count: 101
---

# Development Application
Source: https://docs.agno.com/workspaces/workspace-management/development-app



Your development application runs locally on docker and its resources are defined in the `workspace/dev_resources.py` file. This guide shows how to:

1. [Build a development image](#build-your-development-image)
2. [Restart all docker containers](#restart-all-containers)
3. [Recreate development resources](#recreate-development-resources)

## Workspace Settings

The `WorkspaceSettings` object in the `workspace/settings.py` file defines common settings used by your workspace apps and resources.

## Build your development image

Your application uses the `agno` images by default. To use your own image:

* Open `workspace/settings.py` file
* Update the `image_repo` to your image repository
* Set `build_images=True`

```python workspace/settings.py
ws_settings = WorkspaceSettings(
    ...
    # -*- Image Settings
    # Repository for images
    image_repo="local",
    # Build images locally
    build_images=True,
)
```

### Build a new image

Build the development image using:

<CodeGroup>
  ```bash terminal
  ag ws up --env dev --infra docker --type image
  ```

  ```bash short options
  ag ws up -e dev -i docker -t image
  ```
</CodeGroup>

To `force` rebuild images, use the `--force` or `-f` flag

<CodeGroup>
  ```bash terminal
  ag ws up --env dev --infra docker --type image --force
  ```

  ```bash short options
  ag ws up -e dev -i docker -t image -f
  ```
</CodeGroup>

***

## Restart all containers

Restart all docker containers using:

<CodeGroup>
  ```bash terminal
  ag ws restart --env dev --infra docker --type container
  ```

  ```bash short options
  ag ws restart -e dev -c docker -t container
  ```
</CodeGroup>

***

## Recreate development resources

To recreate all dev resources, use the `--force` flag:

<CodeGroup>
  ```bash terminal
  ag ws up -f
  ```

  ```bash full options
  ag ws up --env dev --infra docker --force
  ```

  ```bash shorthand
  ag ws up dev:docker -f
  ```

  ```bash short options
  ag ws up -e dev -i docker -f
  ```
</CodeGroup>


