---
title: -*- FastAPI running on ECS
category: misc
source_lines: 85920-85963
line_count: 43
---

# -*- FastAPI running on ECS
prd_fastapi = FastApi(
    ...
    # To enable HTTPS, create an ACM certificate and add the ARN below:
    load_balancer_enable_https=True,
    load_balancer_certificate_arn="arn:aws:acm:us-east-1:497891874516:certificate/6598c24a-d4fc-4f17-8ee0-0d3906eb705f",
    ...
)
```

4. Create new Loadbalancer Listeners

Create new listeners for the loadbalancer to pickup the HTTPs configuration.

<CodeGroup>
  ```bash terminal
  ag ws up --env prd --infra aws --name listener
  ```

  ```bash shorthand
  ag ws up -e prd -i aws -n listener
  ```
</CodeGroup>

<Note>The certificate should be `Issued` before applying it.</Note>

After this, `https` should be working on your custom domain.

5. Update existing listeners to redirect HTTP to HTTPS

<CodeGroup>
  ```bash terminal
  ag ws patch --env prd --infra aws --name listener
  ```

  ```bash shorthand
  ag ws patch -e prd -i aws -n listener
  ```
</CodeGroup>

After this, all HTTP requests should redirect to HTTPS automatically.


