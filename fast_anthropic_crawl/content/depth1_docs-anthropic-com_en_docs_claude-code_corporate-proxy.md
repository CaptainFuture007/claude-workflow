---
url: https://docs.anthropic.com/en/docs/claude-code/corporate-proxy
crawled_at: 2025-08-16T11:48:36.149649
depth: 1
title: Corporate proxy configuration
description: [Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](https://docs.a...
---

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](https://docs.anthropic.com/)
English
Search...
⌘K
  * [Research](https://www.anthropic.com/research)
  * [Login](https://console.anthropic.com/login)
  * [Support](https://support.anthropic.com/)
  * [Discord](https://www.anthropic.com/discord)
  * [Sign up](https://console.anthropic.com/login)
  * [Sign up](https://console.anthropic.com/login)


Search...
Navigation
Deployment
Corporate proxy configuration
[Welcome](https://docs.anthropic.com/en/home)[Developer Platform](https://docs.anthropic.com/en/docs/intro)[Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)[Model Context Protocol (MCP)](https://docs.anthropic.com/en/docs/mcp)[API Reference](https://docs.anthropic.com/en/api/messages)[Resources](https://docs.anthropic.com/en/resources/overview)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)
##### Getting started
  * [Overview](https://docs.anthropic.com/en/docs/claude-code/overview)
  * [Quickstart](https://docs.anthropic.com/en/docs/claude-code/quickstart)
  * [Common workflows](https://docs.anthropic.com/en/docs/claude-code/common-workflows)


##### Build with Claude Code
  * [Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code/sdk)
  * [Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
  * [Output styles](https://docs.anthropic.com/en/docs/claude-code/output-styles)
  * [Claude Code hooks](https://docs.anthropic.com/en/docs/claude-code/hooks-guide)
  * [GitHub Actions](https://docs.anthropic.com/en/docs/claude-code/github-actions)
  * [Model Context Protocol (MCP)](https://docs.anthropic.com/en/docs/claude-code/mcp)
  * [Troubleshooting](https://docs.anthropic.com/en/docs/claude-code/troubleshooting)


##### Deployment
  * [Overview](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations)
  * [Amazon Bedrock](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock)
  * [Google Vertex AI](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai)
  * [Corporate proxy](https://docs.anthropic.com/en/docs/claude-code/corporate-proxy)
  * [LLM gateway](https://docs.anthropic.com/en/docs/claude-code/llm-gateway)
  * [Development containers](https://docs.anthropic.com/en/docs/claude-code/devcontainer)


##### Administration
  * [Advanced installation](https://docs.anthropic.com/en/docs/claude-code/setup)
  * [Identity and Access Management](https://docs.anthropic.com/en/docs/claude-code/iam)
  * [Security](https://docs.anthropic.com/en/docs/claude-code/security)
  * [Data usage](https://docs.anthropic.com/en/docs/claude-code/data-usage)
  * [Monitoring](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage)
  * [Costs](https://docs.anthropic.com/en/docs/claude-code/costs)
  * [Analytics](https://docs.anthropic.com/en/docs/claude-code/analytics)


##### Configuration
  * [Settings](https://docs.anthropic.com/en/docs/claude-code/settings)
  * [Add Claude Code to your IDE](https://docs.anthropic.com/en/docs/claude-code/ide-integrations)
  * [Terminal configuration](https://docs.anthropic.com/en/docs/claude-code/terminal-config)
  * [Memory management](https://docs.anthropic.com/en/docs/claude-code/memory)
  * [Status line configuration](https://docs.anthropic.com/en/docs/claude-code/statusline)


##### Reference
  * [CLI reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference)
  * [Interactive mode](https://docs.anthropic.com/en/docs/claude-code/interactive-mode)
  * [Slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands)
  * [Hooks reference](https://docs.anthropic.com/en/docs/claude-code/hooks)


##### Resources
  * [Legal and compliance](https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance)


Deployment
# Corporate proxy configuration
Copy page
Learn how to configure Claude Code to work with corporate proxy servers, including environment variable configuration, authentication, and SSL/TLS certificate handling.
Claude Code supports standard HTTP/HTTPS proxy configurations through environment variables. This allows you to route all Claude Code traffic through your organization’s proxy servers for security, compliance, and monitoring purposes.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/corporate-proxy#basic-proxy-configuration)
Basic proxy configuration
### 
[​](https://docs.anthropic.com/en/docs/claude-code/corporate-proxy#environment-variables)
Environment variables
Claude Code respects standard proxy environment variables:
Copy
```
# HTTPS proxy (recommended)
export HTTPS_PROXY=https://proxy.example.com:8080

# HTTP proxy (if HTTPS not available)
export HTTP_PROXY=http://proxy.example.com:8080

```

Claude Code currently does not support the `NO_PROXY` environment variable. All traffic will be routed through the configured proxy.
Claude Code does not support SOCKS proxies.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/corporate-proxy#authentication)
Authentication
### 
[​](https://docs.anthropic.com/en/docs/claude-code/corporate-proxy#basic-authentication)
Basic authentication
If your proxy requires basic authentication, include credentials in the proxy URL:
Copy
```
export HTTPS_PROXY=http://username:password@proxy.example.com:8080

```

Avoid hardcoding passwords in scripts. Use environment variables or secure credential storage instead.
For proxies requiring advanced authentication (NTLM, Kerberos, etc.), consider using an LLM Gateway service that supports your authentication method.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/corporate-proxy#ssl-certificate-issues)
SSL certificate issues
If your proxy uses custom SSL certificates, you may encounter certificate errors.
Ensure that you set the correct certificate bundle path:
Copy
```
export SSL_CERT_FILE=/path/to/certificate-bundle.crt
export NODE_EXTRA_CA_CERTS=/path/to/certificate-bundle.crt

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/corporate-proxy#network-access-requirements)
Network access requirements
Claude Code requires access to the following URLs:
  * `api.anthropic.com` - Claude API endpoints
  * `statsig.anthropic.com` - Telemetry and metrics
  * `sentry.io` - Error reporting


Ensure these URLs are allowlisted in your proxy configuration and firewall rules. This is especially important when using Claude Code in containerized or restricted network environments.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/corporate-proxy#additional-resources)
Additional resources
  * [Claude Code settings](https://docs.anthropic.com/en/docs/claude-code/settings)
  * [Environment variables reference](https://docs.anthropic.com/en/docs/claude-code/settings#environment-variables)
  * [Troubleshooting guide](https://docs.anthropic.com/en/docs/claude-code/troubleshooting)


Was this page helpful?
YesNo
[Google Vertex AI](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai)[LLM gateway](https://docs.anthropic.com/en/docs/claude-code/llm-gateway)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Basic proxy configuration](https://docs.anthropic.com/en/docs/claude-code/corporate-proxy#basic-proxy-configuration)
  * [Environment variables](https://docs.anthropic.com/en/docs/claude-code/corporate-proxy#environment-variables)
  * [Authentication](https://docs.anthropic.com/en/docs/claude-code/corporate-proxy#authentication)
  * [Basic authentication](https://docs.anthropic.com/en/docs/claude-code/corporate-proxy#basic-authentication)
  * [SSL certificate issues](https://docs.anthropic.com/en/docs/claude-code/corporate-proxy#ssl-certificate-issues)
  * [Network access requirements](https://docs.anthropic.com/en/docs/claude-code/corporate-proxy#network-access-requirements)
  * [Additional resources](https://docs.anthropic.com/en/docs/claude-code/corporate-proxy#additional-resources)


