---
title: SSH Access
category: misc
source_lines: 86978-87010
line_count: 32
---

# SSH Access
Source: https://docs.agno.com/workspaces/workspace-management/ssh-access



SSH Access is an important part of the developer workflow.

## Dev SSH Access

SSH into the dev containers using the `docker exec` command

```bash
docker exec -it ai-api zsh
```

## Production SSH Access

Your ECS tasks are already enabled with SSH access. SSH into the production containers using:

```bash
ECS_CLUSTER=ai-app-prd-cluster
TASK_ARN=$(aws ecs list-tasks --cluster ai-app-prd-cluster --query "taskArns[0]" --output text)
CONTAINER_NAME=ai-api-prd

aws ecs execute-command --cluster $ECS_CLUSTER \
    --task $TASK_ARN \
    --container $CONTAINER_NAME \
    --interactive \
    --command "zsh"
```


