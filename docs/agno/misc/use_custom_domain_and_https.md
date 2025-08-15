---
title: Use Custom Domain and HTTPS
category: misc
source_lines: 85861-85911
line_count: 50
---

# Use Custom Domain and HTTPS
Source: https://docs.agno.com/workspaces/workspace-management/domain-https



## Use a custom domain

1. Register your domain with [Route 53](https://us-east-1.console.aws.amazon.com/route53/).
2. Point the domain to the loadbalancer DNS.

### Custom domain for your Streamlit App

Create a record in the Route53 console to point `app.[YOUR_DOMAIN]` to the Streamlit App.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/agno/images/llm-app-aidev-run.png" alt="llm-app-aidev-run" />

You can visit the app at [http://app.aidev.run](http://app.aidev.run)

<Note>Note the `http` in the domain name.</Note>

### Custom domain for your FastAPI App

Create a record in the Route53 console to point `api.[YOUR_DOMAIN]` to the FastAPI App.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/agno/images/llm-api-aidev-run.png" alt="llm-api-aidev-run" />

You can access the api at [http://api.aidev.run](http://api.aidev.run)

<Note>Note the `http` in the domain name.</Note>

## Add HTTPS

To add HTTPS:

1. Create a certificate using [AWS ACM](https://us-east-1.console.aws.amazon.com/acm). Request a certificat for `*.[YOUR_DOMAIN]`

<img src="https://mintlify.s3.us-west-1.amazonaws.com/agno/images/llm-app-request-cert.png" alt="llm-app-request-cert" />

2. Creating records in Route 53.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/agno/images/llm-app-validate-cert.png" alt="llm-app-validate-cert" />

3. Add the certificate ARN to Apps

<Note>Make sure the certificate is `Issued` before adding it to your Apps</Note>

Update the `llm-app/workspace/prd_resources.py` file and add the `load_balancer_certificate_arn` to the `FastAPI` and `Streamlit` Apps.

```python workspace/prd_resources.py

