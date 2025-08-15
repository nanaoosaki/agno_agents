---
title: Add Python Libraries
category: misc
source_lines: 86791-86906
line_count: 115
---

# Add Python Libraries
Source: https://docs.agno.com/workspaces/workspace-management/python-packages



Agno templates are setup to manage dependencies using a [pyproject.toml](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#declaring-project-metadata) file, **which is used to generate the `requirements.txt` file using [uv](https://github.com/astral-sh/uv) or [pip-tools](https://pip-tools.readthedocs.io/en/latest/).**

Adding or Updating a python library is a 2 step process:

1. Add library to the `pyproject.toml` file
2. Auto-Generate the `requirements.txt` file

<Warning>
  We highly recommend auto-generating the `requirements.txt` file using this process.
</Warning>

## Update pyproject.toml

* Open the `pyproject.toml` file
* Add new libraries to the dependencies section.

## Generate requirements

After updating the `dependencies` in the `pyproject.toml` file, auto-generate the `requirements.txt` file using a helper script or running `pip-compile` directly.

<CodeGroup>
  ```bash terminal
  ./scripts/generate_requirements.sh
  ```

  ```bash pip compile
  pip-compile \
      --no-annotate \
      --pip-args "--no-cache-dir" \
      -o requirements.txt pyproject.toml
  ```
</CodeGroup>

If you'd like to upgrade all python libraries to their latest version, run:

<CodeGroup>
  ```bash terminal
  ./scripts/generate_requirements.sh upgrade
  ```

  ```bash pip compile
  pip-compile \
      --upgrade \
      --no-annotate \
      --pip-args "--no-cache-dir" \
      -o requirements.txt pyproject.toml
  ```
</CodeGroup>

## Rebuild Images

After updating the `requirements.txt` file, rebuild your images.

### Rebuild dev images

<CodeGroup>
  ```bash terminal
  ag ws up --env dev --infra docker --type image
  ```

  ```bash short options
  ag ws up -e dev -i docker -t image
  ```
</CodeGroup>

### Rebuild production images

<Note>
  Remember to [authenticate with ECR](workspaces/workspace-management/production-app#ecr-images) if needed.
</Note>

<CodeGroup>
  ```bash terminal
  ag ws up --env prd --infra aws --type image
  ```

  ```bash short options
  ag ws up -e prd -i aws -t image
  ```
</CodeGroup>

## Recreate Resources

After rebuilding images, recreate the resources.

### Recreate dev containers

<CodeGroup>
  ```bash terminal
  ag ws restart --env dev --infra docker --type container
  ```

  ```bash short options
  ag ws restart -e dev -c docker -t container
  ```
</CodeGroup>

### Update ECS services

<CodeGroup>
  ```bash terminal
  ag ws patch --env prd --infra aws --name service
  ```

  ```bash short options
  ag ws patch -e prd -i aws -n service
  ```
</CodeGroup>


