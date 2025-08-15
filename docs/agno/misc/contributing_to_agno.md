---
title: Contributing to Agno
category: misc
source_lines: 59445-59491
line_count: 46
---

# Contributing to Agno
Source: https://docs.agno.com/how-to/contribute

Learn how to contribute to Agno through our fork and pull request workflow.

Agno is an open-source project and we welcome contributions.

## 👩‍💻 How to contribute

Please follow the [fork and pull request](https://docs.github.com/en/get-started/quickstart/contributing-to-projects) workflow:

* Fork the repository.
* Create a new branch for your feature.
* Add your feature or improvement.
* Send a pull request.
* We appreciate your support & input!

## Development setup

1. Clone the repository.
2. Create a virtual environment:
   * For Unix, use `./scripts/dev_setup.sh`.
   * This setup will:
     * Create a `.venv` virtual environment in the current directory.
     * Install the required packages.
     * Install the `agno` package in editable mode.
3. Activate the virtual environment:
   * On Unix: `source .venv/bin/activate`

> From here on you have to use `uv pip install` to install missing packages

## Formatting and validation

Ensure your code meets our quality standards by running the appropriate formatting and validation script before submitting a pull request:

* For Unix:
  * `./scripts/format.sh`
  * `./scripts/validate.sh`

These scripts will perform code formatting with `ruff` and static type checks with `mypy`.

Read more about the guidelines [here](https://github.com/agno-agi/agno/tree/main/cookbook/CONTRIBUTING.md)

Message us on [Discord](https://discord.gg/4MtYHHrgA8) or post on [Discourse](https://community.agno.com/) if you have any questions or need help with credits.


