---
url: https://docs.anthropic.com/en/docs/claude-code/output-styles
crawled_at: 2025-08-16T12:07:19.210378
depth: 1
title: Output styles
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
Build with Claude Code
Output styles
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


Build with Claude Code
# Output styles
Copy page
Adapt Claude Code for uses beyond software engineering
Output styles allow you to use Claude Code as any type of agent while keeping its core capabilities, such as running local scripts, reading/writing files, and tracking TODOs.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/output-styles#built-in-output-styles)
Built-in output styles
Claude Code’s **Default** output style is the existing system prompt, designed to help you complete software engineering tasks efficiently.
There are two additional built-in output styles focused on teaching you the codebase and how Claude operates:
  * **Explanatory** : Provides educational “Insights” in between helping you complete software engineering tasks. Helps you understand implementation choices and codebase patterns.
  * **Learning** : Collaborative, learn-by-doing mode where Claude will not only share “Insights” while coding, but also ask you to contribute small, strategic pieces of code yourself. Claude Code will add `TODO(human)` markers in your code for you to implement.


## 
[​](https://docs.anthropic.com/en/docs/claude-code/output-styles#how-output-styles-work)
How output styles work
Output styles directly modify Claude Code’s system prompt.
  * Non-default output styles exclude instructions specific to code generation and efficient output normally built into Claude Code (such as responding concisely and verifying code with tests).
  * Instead, these output styles have their own custom instructions added to the system prompt.


## 
[​](https://docs.anthropic.com/en/docs/claude-code/output-styles#change-your-output-style)
Change your output style
You can either:
  * Run `/output-style` to access the menu and select your output style (this can also be accessed from the `/config` menu)
  * Run `/output-style [style]`, such as `/output-style explanatory`, to directly switch to a style


These changes apply to the [local project level](https://docs.anthropic.com/en/docs/claude-code/settings) and are saved in `.claude/settings.local.json`.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/output-styles#create-a-custom-output-style)
Create a custom output style
To set up a new output style with Claude’s help, run `/output-style:new I want an output style that ...`
By default, output styles created through `/output-style:new` are saved as markdown files at the user level in `~/.claude/output-styles` and can be used across projects. They have the following structure:
Copy
```
---
name: My Custom Style
description:
  A brief description of what this style does, to be displayed to the user
---

# Custom Style Instructions

You are an interactive CLI tool that helps users with software engineering
tasks. [Your custom instructions here...]

## Specific Behaviors

[Define how the assistant should behave in this style...]

```

You can also create your own output style Markdown files and save them either at the user level (`~/.claude/output-styles`) or the project level (`.claude/output-styles`).
## 
[​](https://docs.anthropic.com/en/docs/claude-code/output-styles#comparisons-to-related-features)
Comparisons to related features
### 
[​](https://docs.anthropic.com/en/docs/claude-code/output-styles#output-styles-vs-claude-md-vs-%E2%80%94append-system-prompt)
Output Styles vs. CLAUDE.md vs. —append-system-prompt
Output styles completely “turn off” the parts of Claude Code’s default system prompt specific to software engineering. Neither CLAUDE.md nor `--append-system-prompt` edit Claude Code’s default system prompt. CLAUDE.md adds the contents as a user message _following_ Claude Code’s default system prompt. `--append-system-prompt` appends the content to the system prompt.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/output-styles#output-styles-vs-agents)
Output Styles vs. [Agents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
Output styles directly affect the main agent loop and only affect the system prompt. Agents are invoked to handle specific tasks and can include additional settings like the model to use, the tools they have available, and some context about when to use the agent.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/output-styles#output-styles-vs-custom-slash-commands)
Output Styles vs. [Custom Slash Commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands)
You can think of output styles as “stored system prompts” and custom slash commands as “stored prompts”.
Was this page helpful?
YesNo
[Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)[Claude Code hooks](https://docs.anthropic.com/en/docs/claude-code/hooks-guide)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Built-in output styles](https://docs.anthropic.com/en/docs/claude-code/output-styles#built-in-output-styles)
  * [How output styles work](https://docs.anthropic.com/en/docs/claude-code/output-styles#how-output-styles-work)
  * [Change your output style](https://docs.anthropic.com/en/docs/claude-code/output-styles#change-your-output-style)
  * [Create a custom output style](https://docs.anthropic.com/en/docs/claude-code/output-styles#create-a-custom-output-style)
  * [Comparisons to related features](https://docs.anthropic.com/en/docs/claude-code/output-styles#comparisons-to-related-features)
  * [Output Styles vs. CLAUDE.md vs. —append-system-prompt](https://docs.anthropic.com/en/docs/claude-code/output-styles#output-styles-vs-claude-md-vs-%E2%80%94append-system-prompt)
  * [Output Styles vs. Agents](https://docs.anthropic.com/en/docs/claude-code/output-styles#output-styles-vs-agents)
  * [Output Styles vs. Custom Slash Commands](https://docs.anthropic.com/en/docs/claude-code/output-styles#output-styles-vs-custom-slash-commands)


