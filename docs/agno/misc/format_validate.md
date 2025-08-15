---
title: Format & Validate
category: misc
source_lines: 86017-86057
line_count: 40
---

# Format & Validate
Source: https://docs.agno.com/workspaces/workspace-management/format-and-validate



## Format

Formatting the codebase using a set standard saves us time and mental energy. Agno templates are pre-configured with [ruff](https://docs.astral.sh/ruff/) that you can run using a helper script or directly.

<CodeGroup>
  ```bash terminal
  ./scripts/format.sh
  ```

  ```bash ruff
  ruff format .
  ```
</CodeGroup>

## Validate

Linting and Type Checking add an extra layer of protection to the codebase. We highly recommending running the validate script before pushing any changes.

Agno templates are pre-configured with [ruff](https://docs.astral.sh/ruff/) and [mypy](https://mypy.readthedocs.io/en/stable/) that you can run using a helper script or directly. Checkout the `pyproject.toml` file for the configuration.

<CodeGroup>
  ```bash terminal
  ./scripts/validate.sh
  ```

  ```bash ruff
  ruff check .
  ```

  ```bash mypy
  mypy .
  ```
</CodeGroup>


