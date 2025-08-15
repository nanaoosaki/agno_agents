---
title: Command line authentication
category: misc
source_lines: 58502-58530
line_count: 28
---

# Command line authentication
Source: https://docs.agno.com/faq/cli-auth



If you run `ag auth` and you get the error: `CLI authentication failed` or your CLI gets stuck on

```
Waiting for a response from browser...
```

It means that your CLI was not able to authenticate with your Agno account on [app.agno.com](https://app.agno.com)

The quickest fix for this is to export your `AGNO_API_KEY` environment variable. You can do this by running the following command:

```bash
export AGNO_API_KEY=<your_api_key>
```

Your API key can be found on [app.agno.com](https://app.agno.com/settings) in the sidebar under `API Key`.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/agno/images/cli-faq.png" alt="agno-api-key" width={600} />

Reason for CLI authentication failure:

* Some browsers like Safari and Brave block connection to the localhost domain. Browsers like Chrome work great with `ag setup`.


