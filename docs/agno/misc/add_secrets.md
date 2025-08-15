---
title: Add Secrets
category: misc
source_lines: 86906-86938
line_count: 32
---

# Add Secrets
Source: https://docs.agno.com/workspaces/workspace-management/secrets



Secret management is a critical part of your application security and should be taken seriously.

Local secrets are defined in the `worspace/secrets` directory which is excluded from version control (see `.gitignore`). Its contents should be handled with the same security as passwords.

Production secrets are managed by [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html).

<Note>
  Incase you're missing the secrets dir, copy `workspace/example_secrets`
</Note>

## Development Secrets

Apps running locally can read secrets using a `yaml` file, for example:

```python dev_resources.py
dev_fastapi = FastApi(
    ...
    # Read secrets from secrets/dev_app_secrets.yml
    secrets_file=ws_settings.ws_root.joinpath("workspace/secrets/dev_app_secrets.yml"),
)
```

## Production Secrets

`AWS Secrets` are used to manage production secrets, which are read by the production apps.

```python prd_resources.py
