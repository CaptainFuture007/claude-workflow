---
url: https://docs.anthropic.com/en/docs/claude-code/slash-commands
crawled_at: 2025-08-16T12:07:16.167724
depth: 1
title: Slash commands
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
Reference
Slash commands
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


Reference
# Slash commands
Copy page
Control Claude’s behavior during an interactive session with slash commands.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/slash-commands#built-in-slash-commands)
Built-in slash commands
Command | Purpose  
---|---  
`/add-dir` | Add additional working directories  
`/agents` | Manage custom AI subagents for specialized tasks  
`/bug` | Report bugs (sends conversation to Anthropic)  
`/clear` | Clear conversation history  
`/compact [instructions]` | Compact conversation with optional focus instructions  
`/config` | View/modify configuration  
`/cost` | Show token usage statistics  
`/doctor` | Checks the health of your Claude Code installation  
`/help` | Get usage help  
`/init` | Initialize project with CLAUDE.md guide  
`/login` | Switch Anthropic accounts  
`/logout` | Sign out from your Anthropic account  
`/mcp` | Manage MCP server connections and OAuth authentication  
`/memory` | Edit CLAUDE.md memory files  
`/model` | Select or change the AI model  
`/permissions` | View or update [permissions](https://docs.anthropic.com/en/docs/claude-code/iam#configuring-permissions)  
`/pr_comments` | View pull request comments  
`/review` | Request code review  
`/status` | View account and system statuses  
`/terminal-setup` | Install Shift+Enter key binding for newlines (iTerm2 and VSCode only)  
`/vim` | Enter vim mode for alternating insert and command modes  
## 
[​](https://docs.anthropic.com/en/docs/claude-code/slash-commands#custom-slash-commands)
Custom slash commands
Custom slash commands allow you to define frequently-used prompts as Markdown files that Claude Code can execute. Commands are organized by scope (project-specific or personal) and support namespacing through directory structures.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/slash-commands#syntax)
Syntax
Copy
```
/<command-name> [arguments]

```

#### 
[​](https://docs.anthropic.com/en/docs/claude-code/slash-commands#parameters)
Parameters
Parameter | Description  
---|---  
`<command-name>` | Name derived from the Markdown filename (without `.md` extension)  
`[arguments]` | Optional arguments passed to the command  
### 
[​](https://docs.anthropic.com/en/docs/claude-code/slash-commands#command-types)
Command types
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/slash-commands#project-commands)
Project commands
Commands stored in your repository and shared with your team. When listed in `/help`, these commands show “(project)” after their description.
**Location** : `.claude/commands/`
In the following example, we create the `/optimize` command:
Copy
```
# Create a project command
mkdir -p .claude/commands
echo "Analyze this code for performance issues and suggest optimizations:" > .claude/commands/optimize.md

```

#### 
[​](https://docs.anthropic.com/en/docs/claude-code/slash-commands#personal-commands)
Personal commands
Commands available across all your projects. When listed in `/help`, these commands show “(user)” after their description.
**Location** : `~/.claude/commands/`
In the following example, we create the `/security-review` command:
Copy
```
# Create a personal command
mkdir -p ~/.claude/commands
echo "Review this code for security vulnerabilities:" > ~/.claude/commands/security-review.md

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/slash-commands#features)
Features
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/slash-commands#namespacing)
Namespacing
Organize commands in subdirectories. The subdirectories are used for organization and appear in the command description, but they do not affect the command name itself. The description will show whether the command comes from the project directory (`.claude/commands`) or the user-level directory (`~/.claude/commands`), along with the subdirectory name.
Conflicts between user and project level commands are not supported. Otherwise, multiple commands with the same base file name can coexist.
For example, a file at `.claude/commands/frontend/component.md` creates the command `/component` with description showing “(project:frontend)”. Meanwhile, a file at `~/.claude/commands/component.md` creates the command `/component` with description showing “(user)”.
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/slash-commands#arguments)
Arguments
Pass dynamic values to commands using the `$ARGUMENTS` placeholder.
For example:
Copy
```
# Command definition
echo 'Fix issue #$ARGUMENTS following our coding standards' > .claude/commands/fix-issue.md

# Usage
> /fix-issue 123

```

#### 
[​](https://docs.anthropic.com/en/docs/claude-code/slash-commands#bash-command-execution)
Bash command execution
Execute bash commands before the slash command runs using the `!` prefix. The output is included in the command context. You _must_ include `allowed-tools` with the `Bash` tool, but you can choose the specific bash commands to allow.
For example:
Copy
```
---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
description: Create a git commit
---

## Context

- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`

## Your task

Based on the above changes, create a single git commit.

```

#### 
[​](https://docs.anthropic.com/en/docs/claude-code/slash-commands#file-references)
File references
Include file contents in commands using the `@` prefix to [reference files](https://docs.anthropic.com/en/docs/claude-code/common-workflows#reference-files-and-directories).
For example:
Copy
```
# Reference a specific file

Review the implementation in @src/utils/helpers.js

# Reference multiple files

Compare @src/old-version.js with @src/new-version.js

```

#### 
[​](https://docs.anthropic.com/en/docs/claude-code/slash-commands#thinking-mode)
Thinking mode
Slash commands can trigger extended thinking by including [extended thinking keywords](https://docs.anthropic.com/en/docs/claude-code/common-workflows#use-extended-thinking).
### 
[​](https://docs.anthropic.com/en/docs/claude-code/slash-commands#frontmatter)
Frontmatter
Command files support frontmatter, useful for specifying metadata about the command:
Frontmatter | Purpose | Default  
---|---|---  
`allowed-tools` | List of tools the command can use | Inherits from the conversation  
`argument-hint` | The arguments expected for the slash command. Example: `argument-hint: add [tagId] | remove [tagId] | list`. This hint is shown to the user when auto-completing the slash command. | None  
`description` | Brief description of the command | Uses the first line from the prompt  
`model` | Specific model string (see [Models overview](https://docs.anthropic.com/en/docs/about-claude/models/overview)) | Inherits from the conversation  
For example:
Copy
```
---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
argument-hint: [message]
description: Create a git commit
model: claude-3-5-haiku-20241022
---

An example command

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/slash-commands#mcp-slash-commands)
MCP slash commands
MCP servers can expose prompts as slash commands that become available in Claude Code. These commands are dynamically discovered from connected MCP servers.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/slash-commands#command-format)
Command format
MCP commands follow the pattern:
Copy
```
/mcp__<server-name>__<prompt-name> [arguments]

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/slash-commands#features-2)
Features
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/slash-commands#dynamic-discovery)
Dynamic discovery
MCP commands are automatically available when:
  * An MCP server is connected and active
  * The server exposes prompts through the MCP protocol
  * The prompts are successfully retrieved during connection


#### 
[​](https://docs.anthropic.com/en/docs/claude-code/slash-commands#arguments-2)
Arguments
MCP prompts can accept arguments defined by the server:
Copy
```
# Without arguments
> /mcp__github__list_prs

# With arguments
> /mcp__github__pr_review 456
> /mcp__jira__create_issue "Bug title" high

```

#### 
[​](https://docs.anthropic.com/en/docs/claude-code/slash-commands#naming-conventions)
Naming conventions
  * Server and prompt names are normalized
  * Spaces and special characters become underscores
  * Names are lowercased for consistency


### 
[​](https://docs.anthropic.com/en/docs/claude-code/slash-commands#managing-mcp-connections)
Managing MCP connections
Use the `/mcp` command to:
  * View all configured MCP servers
  * Check connection status
  * Authenticate with OAuth-enabled servers
  * Clear authentication tokens
  * View available tools and prompts from each server


## 
[​](https://docs.anthropic.com/en/docs/claude-code/slash-commands#see-also)
See also
  * [Interactive mode](https://docs.anthropic.com/en/docs/claude-code/interactive-mode) - Shortcuts, input modes, and interactive features
  * [CLI reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference) - Command-line flags and options
  * [Settings](https://docs.anthropic.com/en/docs/claude-code/settings) - Configuration options
  * [Memory management](https://docs.anthropic.com/en/docs/claude-code/memory) - Managing Claude’s memory across sessions


Was this page helpful?
YesNo
[Interactive mode](https://docs.anthropic.com/en/docs/claude-code/interactive-mode)[Hooks reference](https://docs.anthropic.com/en/docs/claude-code/hooks)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Built-in slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands#built-in-slash-commands)
  * [Custom slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands#custom-slash-commands)
  * [Syntax](https://docs.anthropic.com/en/docs/claude-code/slash-commands#syntax)
  * [Parameters](https://docs.anthropic.com/en/docs/claude-code/slash-commands#parameters)
  * [Command types](https://docs.anthropic.com/en/docs/claude-code/slash-commands#command-types)
  * [Project commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands#project-commands)
  * [Personal commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands#personal-commands)
  * [Features](https://docs.anthropic.com/en/docs/claude-code/slash-commands#features)
  * [Namespacing](https://docs.anthropic.com/en/docs/claude-code/slash-commands#namespacing)
  * [Arguments](https://docs.anthropic.com/en/docs/claude-code/slash-commands#arguments)
  * [Bash command execution](https://docs.anthropic.com/en/docs/claude-code/slash-commands#bash-command-execution)
  * [File references](https://docs.anthropic.com/en/docs/claude-code/slash-commands#file-references)
  * [Thinking mode](https://docs.anthropic.com/en/docs/claude-code/slash-commands#thinking-mode)
  * [Frontmatter](https://docs.anthropic.com/en/docs/claude-code/slash-commands#frontmatter)
  * [MCP slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands#mcp-slash-commands)
  * [Command format](https://docs.anthropic.com/en/docs/claude-code/slash-commands#command-format)
  * [Features](https://docs.anthropic.com/en/docs/claude-code/slash-commands#features-2)
  * [Dynamic discovery](https://docs.anthropic.com/en/docs/claude-code/slash-commands#dynamic-discovery)
  * [Arguments](https://docs.anthropic.com/en/docs/claude-code/slash-commands#arguments-2)
  * [Naming conventions](https://docs.anthropic.com/en/docs/claude-code/slash-commands#naming-conventions)
  * [Managing MCP connections](https://docs.anthropic.com/en/docs/claude-code/slash-commands#managing-mcp-connections)
  * [See also](https://docs.anthropic.com/en/docs/claude-code/slash-commands#see-also)


