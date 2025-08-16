---
url: https://docs.anthropic.com/en/docs/claude-code/ide-integrations
crawled_at: 2025-08-16T11:48:30.193279
depth: 1
title: Add Claude Code to your IDE
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
Configuration
Add Claude Code to your IDE
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


Configuration
# Add Claude Code to your IDE
Copy page
Learn how to add Claude Code to your favorite IDE
Claude Code works great with any Integrated Development Environment (IDE) that has a terminal. Just run `claude`, and you’re ready to go.
In addition, Claude Code provides dedicated integrations for popular IDEs, which provide features like interactive diff viewing, selection context sharing, and more. These integrations currently exist for:
  * **Visual Studio Code** (including popular forks like Cursor, Windsurf, and VSCodium)
  * **JetBrains IDEs** (including IntelliJ, PyCharm, Android Studio, WebStorm, PhpStorm and GoLand)


## 
[​](https://docs.anthropic.com/en/docs/claude-code/ide-integrations#features)
Features
  * **Quick launch** : Use `Cmd+Esc` (Mac) or `Ctrl+Esc` (Windows/Linux) to open Claude Code directly from your editor, or click the Claude Code button in the UI
  * **Diff viewing** : Code changes can be displayed directly in the IDE diff viewer instead of the terminal. You can configure this in `/config`
  * **Selection context** : The current selection/tab in the IDE is automatically shared with Claude Code
  * **File reference shortcuts** : Use `Cmd+Option+K` (Mac) or `Alt+Ctrl+K` (Linux/Windows) to insert file references (e.g., @File#L1-99)
  * **Diagnostic sharing** : Diagnostic errors (lint, syntax, etc.) from the IDE are automatically shared with Claude as you work


## 
[​](https://docs.anthropic.com/en/docs/claude-code/ide-integrations#installation)
Installation
  * VS Code+
  * JetBrains


To install Claude Code on VS Code and popular forks like Cursor, Windsurf, and VSCodium:
  1. Open VS Code
  2. Open the integrated terminal
  3. Run `claude` - the extension will auto-install


To install Claude Code on VS Code and popular forks like Cursor, Windsurf, and VSCodium:
  1. Open VS Code
  2. Open the integrated terminal
  3. Run `claude` - the extension will auto-install


To install Claude Code on JetBrains IDEs like IntelliJ, PyCharm, Android Studio, WebStorm, PhpStorm and GoLand, find and install the [Claude Code plugin](https://docs.anthropic.com/s/claude-code-jetbrains) from the marketplace and restart your IDE.
The plugin may also be auto-installed when you run `claude` in the integrated terminal. The IDE must be restarted completely to take effect.
**Remote Development Limitations** : When using JetBrains Remote Development, you must install the plugin in the remote host via `Settings > Plugin (Host)`.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/ide-integrations#usage)
Usage
### 
[​](https://docs.anthropic.com/en/docs/claude-code/ide-integrations#from-your-ide)
From your IDE
Run `claude` from your IDE’s integrated terminal, and all features will be active.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/ide-integrations#from-external-terminals)
From external terminals
Use the `/ide` command in any external terminal to connect Claude Code to your IDE and activate all features.
If you want Claude to have access to the same files as your IDE, start Claude Code from the same directory as your IDE project root.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/ide-integrations#configuration)
Configuration
IDE integrations work with Claude Code’s configuration system:
  1. Run `claude`
  2. Enter the `/config` command
  3. Adjust your preferences. Setting the diff tool to `auto` will enable automatic IDE detection


## 
[​](https://docs.anthropic.com/en/docs/claude-code/ide-integrations#troubleshooting)
Troubleshooting
### 
[​](https://docs.anthropic.com/en/docs/claude-code/ide-integrations#vs-code-extension-not-installing)
VS Code extension not installing
  * Ensure you’re running Claude Code from VS Code’s integrated terminal
  * Ensure that the CLI corresponding to your IDE is installed: 
    * For VS Code: `code` command should be available
    * For Cursor: `cursor` command should be available
    * For Windsurf: `windsurf` command should be available
    * For VSCodium: `codium` command should be available
    * If not installed, use `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux) and search for “Shell Command: Install ‘code’ command in PATH” (or the equivalent for your IDE)
  * Check that VS Code has permission to install extensions


### 
[​](https://docs.anthropic.com/en/docs/claude-code/ide-integrations#jetbrains-plugin-not-working)
JetBrains plugin not working
  * Ensure you’re running Claude Code from the project root directory
  * Check that the JetBrains plugin is enabled in the IDE settings
  * Completely restart the IDE. You may need to do this multiple times
  * For JetBrains Remote Development, ensure that the Claude Code plugin is installed in the remote host and not locally on the client


For additional help, refer to our [troubleshooting guide](https://docs.anthropic.com/en/docs/claude-code/troubleshooting).
Was this page helpful?
YesNo
[Settings](https://docs.anthropic.com/en/docs/claude-code/settings)[Terminal configuration](https://docs.anthropic.com/en/docs/claude-code/terminal-config)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Features](https://docs.anthropic.com/en/docs/claude-code/ide-integrations#features)
  * [Installation](https://docs.anthropic.com/en/docs/claude-code/ide-integrations#installation)
  * [Usage](https://docs.anthropic.com/en/docs/claude-code/ide-integrations#usage)
  * [From your IDE](https://docs.anthropic.com/en/docs/claude-code/ide-integrations#from-your-ide)
  * [From external terminals](https://docs.anthropic.com/en/docs/claude-code/ide-integrations#from-external-terminals)
  * [Configuration](https://docs.anthropic.com/en/docs/claude-code/ide-integrations#configuration)
  * [Troubleshooting](https://docs.anthropic.com/en/docs/claude-code/ide-integrations#troubleshooting)
  * [VS Code extension not installing](https://docs.anthropic.com/en/docs/claude-code/ide-integrations#vs-code-extension-not-installing)
  * [JetBrains plugin not working](https://docs.anthropic.com/en/docs/claude-code/ide-integrations#jetbrains-plugin-not-working)


