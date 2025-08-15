---
title: -*- Streamlit running on ECS
category: misc
source_lines: 85911-85920
line_count: 9
---

# -*- Streamlit running on ECS
prd_streamlit = Streamlit(
    ...
    # To enable HTTPS, create an ACM certificate and add the ARN below:
    load_balancer_enable_https=True,
    load_balancer_certificate_arn="arn:aws:acm:us-east-1:497891874516:certificate/6598c24a-d4fc-4f17-8ee0-0d3906eb705f",
    ...
)

