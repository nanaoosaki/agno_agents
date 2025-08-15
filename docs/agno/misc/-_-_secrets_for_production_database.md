---
title: -*- Secrets for production database
category: misc
source_lines: 86947-86978
line_count: 31
---

# -*- Secrets for production database
prd_db_secret = SecretsManager(
    ...
    # Create secret from workspace/secrets/prd_db_secrets.yml
    secret_files=[ws_settings.ws_root.joinpath("workspace/secrets/prd_db_secrets.yml")],
)
```

Read the secret in production apps using:

<CodeGroup>
  ```python FastApi
  prd_fastapi = FastApi(
      ...
      aws_secrets=[prd_secret],
      ...
  )
  ```

  ```python RDS
  prd_db = DbInstance(
      ...
      aws_secret=prd_db_secret,
      ...
  )
  ```
</CodeGroup>

Production resources can also read secrets using yaml files but we highly recommend using [AWS Secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html).


