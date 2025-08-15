---
title: How we build Agentic Systems
category: misc
source_lines: 85383-85405
line_count: 22
---

# How we build Agentic Systems

When building Agents, we experiment locally till we achieve 6/10 quality.
This helps us see quick results and get a rough idea of how our solution should look like in production.

Then, we start moving to a production environment and iterate from there. Here's how ***we*** build production systems:

* Serve Agents, Teams and Workflows via a REST API (FastAPI).
* Use a streamlit application for debugging and testing. This streamlit app is generally used as an admin interface for the agentic system and shows all sorts of data.
* Monitor, evaluate and improve the implementation until we reach 9/10 quality.
* In parallel, we start integrating our front-end with the REST API above.

Having built 100s of such systems, we have a standard set of codebases we use and we call them **Workspaces**. They help us manage our Agentic System as code.

![workspace](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/workspace.png)

<Note>
  We strongly believe that your AI applications should run securely inside your VPC.
  We fully support BYOC (Bring Your Own Cloud) and encourage you to use your own cloud account.
</Note>


