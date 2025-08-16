---
url: https://docs.anthropic.com/en/docs/claude-code/devcontainer
crawled_at: 2025-08-16T11:48:34.935052
depth: 1
title: Development containers
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
Development containers
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
# Development containers
Copy page
Learn about the Claude Code development container for teams that need consistent, secure environments.
The reference [devcontainer setup](https://github.com/anthropics/claude-code/tree/main/.devcontainer) and associated [Dockerfile](https://github.com/anthropics/claude-code/blob/main/.devcontainer/Dockerfile) offer a preconfigured development container that you can use as is, or customize for your needs. This devcontainer works with the Visual Studio Code [Dev Containers extension](https://code.visualstudio.com/docs/devcontainers/containers) and similar tools.
The container’s enhanced security measures (isolation and firewall rules) allow you to run `claude --dangerously-skip-permissions` to bypass permission prompts for unattended operation.
While the devcontainer provides substantial protections, no system is completely immune to all attacks. When executed with `--dangerously-skip-permissions`, devcontainers do not prevent a malicious project from exfiltrating anything accessible in the devcontainer including Claude Code credentials. We recommend only using devcontainers when developing with trusted repositories. Always maintain good security practices and monitor Claude’s activities.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/devcontainer#key-features)
Key features
  * **Production-ready Node.js** : Built on Node.js 20 with essential development dependencies
  * **Security by design** : Custom firewall restricting network access to only necessary services
  * **Developer-friendly tools** : Includes git, ZSH with productivity enhancements, fzf, and more
  * **Seamless VS Code integration** : Pre-configured extensions and optimized settings
  * **Session persistence** : Preserves command history and configurations between container restarts
  * **Works everywhere** : Compatible with macOS, Windows, and Linux development environments


## 
[​](https://docs.anthropic.com/en/docs/claude-code/devcontainer#getting-started-in-4-steps)
Getting started in 4 steps
  1. Install VS Code and the Remote - Containers extension
  2. Clone the [Claude Code reference implementation](https://github.com/anthropics/claude-code/tree/main/.devcontainer) repository
  3. Open the repository in VS Code
  4. When prompted, click “Reopen in Container” (or use Command Palette: Cmd+Shift+P → “Remote-Containers: Reopen in Container”)


## 
[​](https://docs.anthropic.com/en/docs/claude-code/devcontainer#configuration-breakdown)
Configuration breakdown
The devcontainer setup consists of three primary components:
  * [**devcontainer.json**](https://github.com/anthropics/claude-code/blob/main/.devcontainer/devcontainer.json): Controls container settings, extensions, and volume mounts
  * [**Dockerfile**](https://github.com/anthropics/claude-code/blob/main/.devcontainer/Dockerfile): Defines the container image and installed tools
  * [**init-firewall.sh**](https://github.com/anthropics/claude-code/blob/main/.devcontainer/init-firewall.sh): Establishes network security rules


## 
[​](https://docs.anthropic.com/en/docs/claude-code/devcontainer#security-features)
Security features
The container implements a multi-layered security approach with its firewall configuration:
  * **Precise access control** : Restricts outbound connections to whitelisted domains only (npm registry, GitHub, Anthropic API, etc.)
  * **Allowed outbound connections** : The firewall permits outbound DNS and SSH connections
  * **Default-deny policy** : Blocks all other external network access
  * **Startup verification** : Validates firewall rules when the container initializes
  * **Isolation** : Creates a secure development environment separated from your main system


## 
[​](https://docs.anthropic.com/en/docs/claude-code/devcontainer#customization-options)
Customization options
The devcontainer configuration is designed to be adaptable to your needs:
  * Add or remove VS Code extensions based on your workflow
  * Modify resource allocations for different hardware environments
  * Adjust network access permissions
  * Customize shell configurations and developer tooling


## 
[​](https://docs.anthropic.com/en/docs/claude-code/devcontainer#example-use-cases)
Example use cases
### 
[​](https://docs.anthropic.com/en/docs/claude-code/devcontainer#secure-client-work)
Secure client work
Use devcontainers to isolate different client projects, ensuring code and credentials never mix between environments.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/devcontainer#team-onboarding)
Team onboarding
New team members can get a fully configured development environment in minutes, with all necessary tools and settings pre-installed.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/devcontainer#consistent-ci%2Fcd-environments)
Consistent CI/CD environments
Mirror your devcontainer configuration in CI/CD pipelines to ensure development and production environments match.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/devcontainer#related-resources)
Related resources
  * [VS Code devcontainers documentation](https://code.visualstudio.com/docs/devcontainers/containers)
  * [Claude Code security best practices](https://docs.anthropic.com/en/docs/claude-code/security)
  * [Corporate proxy configuration](https://docs.anthropic.com/en/docs/claude-code/corporate-proxy)


Was this page helpful?
YesNo
[LLM gateway](https://docs.anthropic.com/en/docs/claude-code/llm-gateway)[Advanced installation](https://docs.anthropic.com/en/docs/claude-code/setup)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Key features](https://docs.anthropic.com/en/docs/claude-code/devcontainer#key-features)
  * [Getting started in 4 steps](https://docs.anthropic.com/en/docs/claude-code/devcontainer#getting-started-in-4-steps)
  * [Configuration breakdown](https://docs.anthropic.com/en/docs/claude-code/devcontainer#configuration-breakdown)
  * [Security features](https://docs.anthropic.com/en/docs/claude-code/devcontainer#security-features)
  * [Customization options](https://docs.anthropic.com/en/docs/claude-code/devcontainer#customization-options)
  * [Example use cases](https://docs.anthropic.com/en/docs/claude-code/devcontainer#example-use-cases)
  * [Secure client work](https://docs.anthropic.com/en/docs/claude-code/devcontainer#secure-client-work)
  * [Team onboarding](https://docs.anthropic.com/en/docs/claude-code/devcontainer#team-onboarding)
  * [Consistent CI/CD environments](https://docs.anthropic.com/en/docs/claude-code/devcontainer#consistent-ci%2Fcd-environments)
  * [Related resources](https://docs.anthropic.com/en/docs/claude-code/devcontainer#related-resources)


