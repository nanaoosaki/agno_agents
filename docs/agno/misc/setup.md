---
title: Setup
category: misc
source_lines: 5507-5535
line_count: 28
---

# Setup

## Set your AWS credentials

```bash
export AWS_ACCESS_KEY_ID = xxx
export AWS_SECRET_ACCESS_KEY = xxx
export AWS_REGION = xxx
```

<Note>
  By default, this embedder uses the `cohere.embed-multilingual-v3` model. You must enable access to this model from the AWS Bedrock model catalog before using this embedder.
</Note>

## Run PgVector

```bash
docker run - d \
    - e POSTGRES_DB = ai \
    - e POSTGRES_USER = ai \
    - e POSTGRES_PASSWORD = ai \
    - e PGDATA = /var/lib/postgresql/data/pgdata \
    - v pgvolume: / var/lib/postgresql/data \
    - p 5532: 5432 \
    - -name pgvector \
    agnohq/pgvector: 16
```

