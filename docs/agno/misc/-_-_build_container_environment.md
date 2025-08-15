---
title: -*- Build container environment
category: misc
source_lines: 85675-85750
line_count: 75
---

# -*- Build container environment
container_env = {
    ...
    # Migrate database on startup using alembic
    "MIGRATE_DB": ws_settings.prd_db_enabled,
}
...
```

### Update the ECS Task Definition

Because we updated the Environment Variables, we need to update the Task Definition:

<CodeGroup>
  ```bash terminal
  ag ws patch --env prd --infra aws --name td
  ```

  ```bash shorthand
  ag ws patch -e prd -i aws -n td
  ```
</CodeGroup>

### Update the ECS Service

After updating the task definition, redeploy the production application:

<CodeGroup>
  ```bash terminal
  ag ws patch --env prd --infra aws --name service
  ```

  ```bash shorthand
  ag ws patch -e prd -i aws -n service
  ```
</CodeGroup>

## Manually migrate prodution database

Another approach is to SSH into the production container to run the migration manually. Your ECS tasks are already enabled with SSH access. Run the alembic command to migrate the production database:

```bash
ECS_CLUSTER=ai-app-prd-cluster
TASK_ARN=$(aws ecs list-tasks --cluster ai-app-prd-cluster --query "taskArns[0]" --output text)
CONTAINER_NAME=ai-api-prd

aws ecs execute-command --cluster $ECS_CLUSTER \
    --task $TASK_ARN \
    --container $CONTAINER_NAME \
    --interactive \
    --command "alembic -c db/alembic.ini upgrade head"
```

***

## How the migrations directory was created

<Note>
  These commands have been run and are described for completeness
</Note>

The migrations directory was created using:

```bash
docker exec -it ai-api cd db && alembic init migrations
```

* After running the above command, the `db/migrations` directory should be created.
* Update `alembic.ini`
  * set `script_location = db/migrations`
  * uncomment `black` hook in `[post_write_hooks]`
* Update `db/migrations/env.py` file following [this link](https://alembic.sqlalchemy.org/en/latest/autogenerate.html)
* Add the following function to `configure` to only include tables in the target\_metadata

```python db/migrations/env.py
