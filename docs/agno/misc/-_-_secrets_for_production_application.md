---
title: -*- Secrets for production application
category: misc
source_lines: 86938-86947
line_count: 9
---

# -*- Secrets for production application
prd_secret = SecretsManager(
    ...
    # Create secret from workspace/secrets/prd_app_secrets.yml
    secret_files=[
        ws_settings.ws_root.joinpath("workspace/secrets/prd_app_secrets.yml")
    ],
)

