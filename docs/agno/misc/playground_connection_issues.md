---
title: Playground Connection Issues
category: misc
source_lines: 58901-58971
line_count: 70
---

# Playground Connection Issues
Source: https://docs.agno.com/faq/playground-connection



If you're experiencing connection issues in the Agno Playground, particularly when trying to connect to **local endpoints**, this guide will help you resolve them.

## Browser Compatibility

Some browsers have security restrictions that prevent connections to localhost domains due to mixed content security issues. Here's what you need to know about different browsers:

### Recommended Browsers

* **Chrome & Edge**: These browsers work well with local connections by default and are our recommended choices
* **Firefox**: Generally works well with local connections

### Browsers with Known Issues

* **Safari**: May block local connections due to its strict security policies
* **Brave**: Blocks local connections by default due to its shield feature

## Solutions

### For Brave Users

If you're using Brave browser, you can try these steps:

1. Click on the Brave shield icon in the address bar
2. Turn off the shield for the current site
3. Refresh the endpoint and try connecting again

<video autoPlay muted controls className="w-full aspect-video" src="https://mintlify.s3.us-west-1.amazonaws.com/agno/videos/brave-shields.mp4" />

### For Other Browsers

If you're using Safari or experiencing issues with other browsers, you can use one of these solutions:

#### 1. Use Chrome or Edge

The simplest solution is to use Chrome or Edge browsers which have better support for local connections.

#### 2. Use Tunneling Services

You can use tunneling services to expose your local endpoint to the internet:

##### Using ngrok

1. Install ngrok from [ngrok.com](https://ngrok.com)
2. Run your local server
3. Create a tunnel with ngrok:

```bash
ngrok http <your-local-port>
```

4. Use the provided ngrok URL in the playground

##### Using Cloudflare Tunnel

1. Install Cloudflare Tunnel (cloudflared) from [Cloudflare's website](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation/)
2. Authenticate with Cloudflare
3. Create a tunnel:

```bash
cloudflared tunnel --url http://localhost:<your-local-port>
```

4. Use the provided Cloudflare URL in the playground


