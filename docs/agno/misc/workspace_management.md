---
title: Workspace Management
category: misc
source_lines: 59762-59803
line_count: 41
---

# Workspace Management
phi ws create -> ag ws create
phi ws config -> ag ws config
phi ws delete -> ag ws delete
phi ws up <environment> -> ag ws up <environment>
phi ws down <environment> -> ag ws down <environment>
phi ws patch <environment> -> ag ws patch <environment>
phi ws restart <environment> -> ag ws restart <environment>
```

<Note>
  The commands `ag ws up dev` and `ag ws up prod` have to be used instead of `ag ws up` to start the workspace in development and production mode respectively.
</Note>

### New Commands

* `ag ping` -> Check if you are authenticated

### Removed Commands

* `phi ws setup` -> Replaced by `ag setup`

### Infrastructure Path Changes

The infrastructure-related code has been reorganized for better clarity:

* **Docker Infrastructure**: This has been moved to a separate package in `/libs/infra/agno_docker` and has a separate PyPi package [`agno-docker`](https://pypi.org/project/agno-docker/).
* **AWS Infrastructure**: This has been moved to a separate package in `/libs/infra/agno_aws` and has a separate PyPi package [`agno-aws`](https://pypi.org/project/agno-aws/).

We recommend installing these packages in applications that you intend to deploy to AWS using Agno, or if you are migrating from a Phidata application.

The specific path changes are:

* `import phi.aws.resource.xxx` ➔ `import agno.aws.resource.xxx`
* `import phi.docker.xxx` ➔ `import agno.docker.xxx`

***

Follow the steps above to ensure your codebase is compatible with the latest version of Agno AI. If you encounter any issues, don't hesitate to contact us on [Discourse](https://community.phidata.com/) or [Discord](https://discord.gg/4MtYHHrgA8).


