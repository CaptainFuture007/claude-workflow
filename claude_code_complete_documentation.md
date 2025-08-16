# Claude Code Documentation - Complete Guide

**Generated**: August 16, 2025 at 12:08 PM
**Source**: https://docs.anthropic.com/en/docs/claude-code/
**Total Pages**: 34

This document contains the complete Claude Code documentation concatenated from all individual pages for easy reading and searching.

---


## Table of Contents

1. [Claude Code overview](#claude-code-overview)
   - Source: https://docs.anthropic.com/en/docs/claude-code/

2. [Claude Code on Amazon Bedrock](#claude-code-on-amazon-bedrock)
   - Source: https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock

3. [Analytics](#analytics)
   - Source: https://docs.anthropic.com/en/docs/claude-code/analytics

4. [CLI reference](#cli-reference)
   - Source: https://docs.anthropic.com/en/docs/claude-code/cli-reference

5. [Common workflows](#common-workflows)
   - Source: https://docs.anthropic.com/en/docs/claude-code/common-workflows

6. [Corporate proxy configuration](#corporate-proxy-configuration)
   - Source: https://docs.anthropic.com/en/docs/claude-code/corporate-proxy

7. [Manage costs effectively](#manage-costs-effectively)
   - Source: https://docs.anthropic.com/en/docs/claude-code/costs

8. [Data usage](#data-usage)
   - Source: https://docs.anthropic.com/en/docs/claude-code/data-usage

9. [Development containers](#development-containers)
   - Source: https://docs.anthropic.com/en/docs/claude-code/devcontainer

10. [Claude Code GitHub Actions](#claude-code-github-actions)
   - Source: https://docs.anthropic.com/en/docs/claude-code/github-actions

11. [Claude Code on Google Vertex AI](#claude-code-on-google-vertex-ai)
   - Source: https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai

12. [Get started with Claude Code hooks](#get-started-with-claude-code-hooks)
   - Source: https://docs.anthropic.com/en/docs/claude-code/hooks-guide

13. [Hooks reference](#hooks-reference)
   - Source: https://docs.anthropic.com/en/docs/claude-code/hooks

14. [Identity and Access Management](#identity-and-access-management)
   - Source: https://docs.anthropic.com/en/docs/claude-code/iam

15. [Add Claude Code to your IDE](#add-claude-code-to-your-ide)
   - Source: https://docs.anthropic.com/en/docs/claude-code/ide-integrations

16. [Interactive mode](#interactive-mode)
   - Source: https://docs.anthropic.com/en/docs/claude-code/interactive-mode

17. [Legal and compliance](#legal-and-compliance)
   - Source: https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance

18. [LLM gateway configuration](#llm-gateway-configuration)
   - Source: https://docs.anthropic.com/en/docs/claude-code/llm-gateway

19. [Connect Claude Code to tools via MCP](#connect-claude-code-to-tools-via-mcp)
   - Source: https://docs.anthropic.com/en/docs/claude-code/mcp

20. [Manage Claude's memory](#manage-claudes-memory)
   - Source: https://docs.anthropic.com/en/docs/claude-code/memory

21. [Monitoring](#monitoring)
   - Source: https://docs.anthropic.com/en/docs/claude-code/monitoring-usage

22. [Output styles](#output-styles)
   - Source: https://docs.anthropic.com/en/docs/claude-code/output-styles

23. [Claude Code overview](#claude-code-overview)
   - Source: https://docs.anthropic.com/en/docs/claude-code/overview

24. [Quickstart](#quickstart)
   - Source: https://docs.anthropic.com/en/docs/claude-code/quickstart

25. [Claude Code SDK](#claude-code-sdk)
   - Source: https://docs.anthropic.com/en/docs/claude-code/sdk

26. [Security](#security)
   - Source: https://docs.anthropic.com/en/docs/claude-code/security

27. [Claude Code settings](#claude-code-settings)
   - Source: https://docs.anthropic.com/en/docs/claude-code/settings

28. [Set up Claude Code](#set-up-claude-code)
   - Source: https://docs.anthropic.com/en/docs/claude-code/setup

29. [Slash commands](#slash-commands)
   - Source: https://docs.anthropic.com/en/docs/claude-code/slash-commands

30. [Status line configuration](#status-line-configuration)
   - Source: https://docs.anthropic.com/en/docs/claude-code/statusline

31. [Subagents](#subagents)
   - Source: https://docs.anthropic.com/en/docs/claude-code/sub-agents

32. [Optimize your terminal setup](#optimize-your-terminal-setup)
   - Source: https://docs.anthropic.com/en/docs/claude-code/terminal-config

33. [Enterprise deployment overview](#enterprise-deployment-overview)
   - Source: https://docs.anthropic.com/en/docs/claude-code/third-party-integrations

34. [Troubleshooting](#troubleshooting)
   - Source: https://docs.anthropic.com/en/docs/claude-code/troubleshooting


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/ -->

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
Getting started
Claude Code overview
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


Getting started
# Claude Code overview
Copy page
Learn about Claude Code, Anthropic’s agentic coding tool that lives in your terminal and helps you turn ideas into code faster than ever before.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#get-started-in-30-seconds)
Get started in 30 seconds
Prerequisites: [Node.js 18 or newer](https://nodejs.org/en/download/)
Copy
```
# Install Claude Code
npm install -g @anthropic-ai/claude-code

# Navigate to your project
cd your-awesome-project

# Start coding with Claude
claude

```

That’s it! You’re ready to start coding with Claude. [Continue with Quickstart (5 mins) →](https://docs.anthropic.com/en/docs/claude-code/quickstart)
(Got specific setup needs or hit issues? See [advanced setup](https://docs.anthropic.com/en/docs/claude-code/setup) or [troubleshooting](https://docs.anthropic.com/en/docs/claude-code/troubleshooting).)
## 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#what-claude-code-does-for-you)
What Claude Code does for you
  * **Build features from descriptions** : Tell Claude what you want to build in plain English. It will make a plan, write the code, and ensure it works.
  * **Debug and fix issues** : Describe a bug or paste an error message. Claude Code will analyze your codebase, identify the problem, and implement a fix.
  * **Navigate any codebase** : Ask anything about your team’s codebase, and get a thoughtful answer back. Claude Code maintains awareness of your entire project structure, can find up-to-date information from the web, and with [MCP](https://docs.anthropic.com/en/docs/claude-code/mcp) can pull from external datasources like Google Drive, Figma, and Slack.
  * **Automate tedious tasks** : Fix fiddly lint issues, resolve merge conflicts, and write release notes. Do all this in a single command from your developer machines, or automatically in CI.


## 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#why-developers-love-claude-code)
Why developers love Claude Code
  * **Works in your terminal** : Not another chat window. Not another IDE. Claude Code meets you where you already work, with the tools you already love.
  * **Takes action** : Claude Code can directly edit files, run commands, and create commits. Need more? [MCP](https://docs.anthropic.com/en/docs/claude-code/mcp) lets Claude read your design docs in Google Drive, update your tickets in Jira, or use _your_ custom developer tooling.
  * **Unix philosophy** : Claude Code is composable and scriptable. `tail -f app.log | claude -p "Slack me if you see any anomalies appear in this log stream"` _works_. Your CI can run `claude -p "If there are new text strings, translate them into French and raise a PR for @lang-fr-team to review"`.
  * **Enterprise-ready** : Use Anthropic’s API, or host on AWS or GCP. Enterprise-grade [security](https://docs.anthropic.com/en/docs/claude-code/security), [privacy](https://docs.anthropic.com/en/docs/claude-code/data-usage), and [compliance](https://trust.anthropic.com/) is built-in.


## 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#next-steps)
Next steps
## [Quickstart See Claude Code in action with practical examples ](https://docs.anthropic.com/en/docs/claude-code/quickstart)## [Common workflows Step-by-step guides for common workflows ](https://docs.anthropic.com/en/docs/claude-code/common-workflows)## [Troubleshooting Solutions for common issues with Claude Code ](https://docs.anthropic.com/en/docs/claude-code/troubleshooting)## [IDE setup Add Claude Code to your IDE ](https://docs.anthropic.com/en/docs/claude-code/ide-integrations)
## 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#additional-resources)
Additional resources
## [Host on AWS or GCP Configure Claude Code with Amazon Bedrock or Google Vertex AI ](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations)## [Settings Customize Claude Code for your workflow ](https://docs.anthropic.com/en/docs/claude-code/settings)## [Commands Learn about CLI commands and controls ](https://docs.anthropic.com/en/docs/claude-code/cli-reference)## [Reference implementation Clone our development container reference implementation ](https://github.com/anthropics/claude-code/tree/main/.devcontainer)## [Security Discover Claude Code’s safeguards and best practices for safe usage ](https://docs.anthropic.com/en/docs/claude-code/security)## [Privacy and data usage Understand how Claude Code handles your data ](https://docs.anthropic.com/en/docs/claude-code/data-usage)
Was this page helpful?
YesNo
[Quickstart](https://docs.anthropic.com/en/docs/claude-code/quickstart)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Get started in 30 seconds](https://docs.anthropic.com/en/docs/claude-code/overview#get-started-in-30-seconds)
  * [What Claude Code does for you](https://docs.anthropic.com/en/docs/claude-code/overview#what-claude-code-does-for-you)
  * [Why developers love Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview#why-developers-love-claude-code)
  * [Next steps](https://docs.anthropic.com/en/docs/claude-code/overview#next-steps)
  * [Additional resources](https://docs.anthropic.com/en/docs/claude-code/overview#additional-resources)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock -->

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
Claude Code on Amazon Bedrock
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
# Claude Code on Amazon Bedrock
Copy page
Learn about configuring Claude Code through Amazon Bedrock, including setup, IAM configuration, and troubleshooting.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#prerequisites)
Prerequisites
Before configuring Claude Code with Bedrock, ensure you have:
  * An AWS account with Bedrock access enabled
  * Access to desired Claude models (e.g., Claude Sonnet 4) in Bedrock
  * AWS CLI installed and configured (optional - only needed if you don’t have another mechanism for getting credentials)
  * Appropriate IAM permissions


## 
[​](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#setup)
Setup
### 
[​](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#1-enable-model-access)
1. Enable model access
First, ensure you have access to the required Claude models in your AWS account:
  1. Navigate to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/)
  2. Go to **Model access** in the left navigation
  3. Request access to desired Claude models (e.g., Claude Sonnet 4)
  4. Wait for approval (usually instant for most regions)


### 
[​](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#2-configure-aws-credentials)
2. Configure AWS credentials
Claude Code uses the default AWS SDK credential chain. Set up your credentials using one of these methods:
**Option A: AWS CLI configuration**
Copy
```
aws configure

```

**Option B: Environment variables (access key)**
Copy
```
export AWS_ACCESS_KEY_ID=your-access-key-id
export AWS_SECRET_ACCESS_KEY=your-secret-access-key
export AWS_SESSION_TOKEN=your-session-token

```

**Option C: Environment variables (SSO profile)**
Copy
```
aws sso login --profile=<your-profile-name>

export AWS_PROFILE=your-profile-name

```

**Option D: Bedrock API keys**
Copy
```
export AWS_BEARER_TOKEN_BEDROCK=your-bedrock-api-key

```

Bedrock API keys provide a simpler authentication method without needing full AWS credentials. [Learn more about Bedrock API keys](https://aws.amazon.com/blogs/machine-learning/accelerate-ai-development-with-amazon-bedrock-api-keys/).
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#advanced-credential-configuration)
Advanced credential configuration
Claude Code supports automatic credential refresh for AWS SSO and corporate identity providers. Add these settings to your Claude Code settings file (see [Settings](https://docs.anthropic.com/en/docs/claude-code/settings) for file locations).
When Claude Code detects that your AWS credentials are expired (either locally based on their timestamp or when Bedrock returns a credential error), it will automatically run your configured `awsAuthRefresh` and/or `awsCredentialExport` commands to obtain new credentials before retrying the request.
##### Example configuration
Copy
```
{
  "awsAuthRefresh": "aws sso login --profile myprofile",
  "env": {
    "AWS_PROFILE": "myprofile"
  }
}

```

##### Configuration settings explained
**`awsAuthRefresh`**: Use this for commands that modify the`.aws` directory (e.g., updating credentials, SSO cache, or config files). Output is shown to the user (but user input is not supported), making it suitable for browser-based authentication flows where the CLI displays a code to enter in the browser.
**`awsCredentialExport`**: Only use this if you cannot modify`.aws` and must directly return credentials. Output is captured silently (not shown to the user). The command must output JSON in this format:
Copy
```
{
  "Credentials": {
    "AccessKeyId": "value",
    "SecretAccessKey": "value",
    "SessionToken": "value"
  }
}

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#3-configure-claude-code)
3. Configure Claude Code
Set the following environment variables to enable Bedrock:
Copy
```
# Enable Bedrock integration
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=us-east-1  # or your preferred region

# Optional: Override the region for the small/fast model (Haiku)
export ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION=us-west-2

```

When enabling Bedrock for Claude Code, keep the following in mind:
  * `AWS_REGION` is a required environment variable. Claude Code does not read from the `.aws` config file for this setting.
  * When using Bedrock, the `/login` and `/logout` commands are disabled since authentication is handled through AWS credentials.
  * You can use settings files for environment variables like `AWS_PROFILE` that you don’t want to leak to other processes. See [Settings](https://docs.anthropic.com/en/docs/claude-code/settings) for more information.


### 
[​](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#4-model-configuration)
4. Model configuration
Claude Code uses these default models for Bedrock:
Model type | Default value  
---|---  
Primary model | `us.anthropic.claude-3-7-sonnet-20250219-v1:0`  
Small/fast model | `us.anthropic.claude-3-5-haiku-20241022-v1:0`  
To customize models, use one of these methods:
Copy
```
# Using inference profile ID
export ANTHROPIC_MODEL='us.anthropic.claude-opus-4-1-20250805-v1:0'
export ANTHROPIC_SMALL_FAST_MODEL='us.anthropic.claude-3-5-haiku-20241022-v1:0'

# Using application inference profile ARN
export ANTHROPIC_MODEL='arn:aws:bedrock:us-east-2:your-account-id:application-inference-profile/your-model-id'

# Optional: Disable prompt caching if needed
export DISABLE_PROMPT_CACHING=1

```

[Prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) may not be available in all regions
### 
[​](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#5-output-token-configuration)
5. Output token configuration
When using Claude Code with Amazon Bedrock, we recommend the following token settings:
Copy
```
# Recommended output token settings for Bedrock
export CLAUDE_CODE_MAX_OUTPUT_TOKENS=4096
export MAX_THINKING_TOKENS=1024

```

**Why these values:**
  * **`CLAUDE_CODE_MAX_OUTPUT_TOKENS=4096`**: Bedrock’s burndown throttling logic sets a minimum of 4096 tokens as the max_token penalty. Setting this lower won’t reduce costs but may cut off long tool uses, causing the Claude Code agent loop to fail persistently. Claude Code typically uses less than 4096 output tokens without extended thinking, but may need this headroom for tasks involving significant file creation or Write tool usage.
  * **`MAX_THINKING_TOKENS=1024`**: This provides space for extended thinking without cutting off tool use responses, while still maintaining focused reasoning chains. This balance helps prevent trajectory changes that aren’t always helpful for coding tasks specifically.


## 
[​](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#iam-configuration)
IAM configuration
Create an IAM policy with the required permissions for Claude Code:
Copy
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream",
        "bedrock:ListInferenceProfiles"
      ],
      "Resource": [
        "arn:aws:bedrock:*:*:inference-profile/*",
        "arn:aws:bedrock:*:*:application-inference-profile/*"
      ]
    }
  ]
}

```

For more restrictive permissions, you can limit the Resource to specific inference profile ARNs.
For details, see [Bedrock IAM documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html).
We recommend creating a dedicated AWS account for Claude Code to simplify cost tracking and access control.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#troubleshooting)
Troubleshooting
If you encounter region issues:
  * Check model availability: `aws bedrock list-inference-profiles --region your-region`
  * Switch to a supported region: `export AWS_REGION=us-east-1`
  * Consider using inference profiles for cross-region access


If you receive an error “on-demand throughput isn’t supported”:
  * Specify the model as an [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html) ID


## 
[​](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#additional-resources)
Additional resources
  * [Bedrock documentation](https://docs.aws.amazon.com/bedrock/)
  * [Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)
  * [Bedrock inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html)
  * [Claude Code on Amazon Bedrock: Quick Setup Guide](https://community.aws/content/2tXkZKrZzlrlu0KfH8gST5Dkppq/claude-code-on-amazon-bedrock-quick-setup-guide)


Was this page helpful?
YesNo
[Overview](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations)[Google Vertex AI](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Prerequisites](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#prerequisites)
  * [Setup](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#setup)
  * [1. Enable model access](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#1-enable-model-access)
  * [2. Configure AWS credentials](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#2-configure-aws-credentials)
  * [Advanced credential configuration](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#advanced-credential-configuration)
  * [3. Configure Claude Code](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#3-configure-claude-code)
  * [4. Model configuration](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#4-model-configuration)
  * [5. Output token configuration](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#5-output-token-configuration)
  * [IAM configuration](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#iam-configuration)
  * [Troubleshooting](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#troubleshooting)
  * [Additional resources](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#additional-resources)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/analytics -->

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
Administration
Analytics
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


Administration
# Analytics
Copy page
View detailed usage insights and productivity metrics for your organization’s Claude Code deployment.
Claude Code provides an analytics dashboard that helps organizations understand developer usage patterns, track productivity metrics, and optimize their Claude Code adoption.
Analytics are currently available only for organizations using Claude Code with the Anthropic API through the Anthropic Console.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/analytics#access-analytics)
Access analytics
Navigate to the analytics dashboard at [console.anthropic.com/claude_code](https://console.anthropic.com/claude_code).
### 
[​](https://docs.anthropic.com/en/docs/claude-code/analytics#required-roles)
Required roles
  * **Primary Owner**
  * **Owner**
  * **Billing**
  * **Admin**
  * **Developer**


Users with **User** , **Claude Code User** or **Membership Admin** roles cannot access analytics.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/analytics#available-metrics)
Available metrics
### 
[​](https://docs.anthropic.com/en/docs/claude-code/analytics#lines-of-code-accepted)
Lines of code accepted
Total lines of code written by Claude Code that users have accepted in their sessions.
  * Excludes rejected code suggestions
  * Doesn’t track subsequent deletions


### 
[​](https://docs.anthropic.com/en/docs/claude-code/analytics#suggestion-accept-rate)
Suggestion accept rate
Percentage of times users accept code editing tool usage, including:
  * Edit
  * MultiEdit
  * Write
  * NotebookEdit


### 
[​](https://docs.anthropic.com/en/docs/claude-code/analytics#activity)
Activity
**users** : Number of active users in a given day (number on left Y-axis)
**sessions** : Number of active sessions in a given day (number on right Y-axis)
### 
[​](https://docs.anthropic.com/en/docs/claude-code/analytics#spend)
Spend
**users** : Number of active users in a given day (number on left Y-axis)
**spend** : Total dollars spent in a given day (number on right Y-axis)
### 
[​](https://docs.anthropic.com/en/docs/claude-code/analytics#team-insights)
Team insights
**Members** : All users who have authenticated to Claude Code
  * API key users are displayed by **API key identifier**
  * OAuth users are displayed by **email address**


**Spend this month:** Per-user total spend for the current month.
**Lines this month:** Per-user total of accepted code lines for the current month.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/analytics#using-analytics-effectively)
Using analytics effectively
### 
[​](https://docs.anthropic.com/en/docs/claude-code/analytics#monitor-adoption)
Monitor adoption
Track team member status to identify:
  * Active users who can share best practices
  * Overall adoption trends across your organization


### 
[​](https://docs.anthropic.com/en/docs/claude-code/analytics#measure-productivity)
Measure productivity
Tool acceptance rates and code metrics help you:
  * Understand developer satisfaction with Claude Code suggestions
  * Track code generation effectiveness
  * Identify opportunities for training or process improvements


## 
[​](https://docs.anthropic.com/en/docs/claude-code/analytics#related-resources)
Related resources
  * [Monitoring usage with OpenTelemetry](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage) for custom metrics and alerting
  * [Identity and access management](https://docs.anthropic.com/en/docs/claude-code/iam) for role configuration


Was this page helpful?
YesNo
[Costs](https://docs.anthropic.com/en/docs/claude-code/costs)[Settings](https://docs.anthropic.com/en/docs/claude-code/settings)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Access analytics](https://docs.anthropic.com/en/docs/claude-code/analytics#access-analytics)
  * [Required roles](https://docs.anthropic.com/en/docs/claude-code/analytics#required-roles)
  * [Available metrics](https://docs.anthropic.com/en/docs/claude-code/analytics#available-metrics)
  * [Lines of code accepted](https://docs.anthropic.com/en/docs/claude-code/analytics#lines-of-code-accepted)
  * [Suggestion accept rate](https://docs.anthropic.com/en/docs/claude-code/analytics#suggestion-accept-rate)
  * [Activity](https://docs.anthropic.com/en/docs/claude-code/analytics#activity)
  * [Spend](https://docs.anthropic.com/en/docs/claude-code/analytics#spend)
  * [Team insights](https://docs.anthropic.com/en/docs/claude-code/analytics#team-insights)
  * [Using analytics effectively](https://docs.anthropic.com/en/docs/claude-code/analytics#using-analytics-effectively)
  * [Monitor adoption](https://docs.anthropic.com/en/docs/claude-code/analytics#monitor-adoption)
  * [Measure productivity](https://docs.anthropic.com/en/docs/claude-code/analytics#measure-productivity)
  * [Related resources](https://docs.anthropic.com/en/docs/claude-code/analytics#related-resources)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/cli-reference -->

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
CLI reference
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
# CLI reference
Copy page
Complete reference for Claude Code command-line interface, including commands and flags.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/cli-reference#cli-commands)
CLI commands
Command | Description | Example  
---|---|---  
`claude` | Start interactive REPL | `claude`  
`claude "query"` | Start REPL with initial prompt | `claude "explain this project"`  
`claude -p "query"` | Query via SDK, then exit | `claude -p "explain this function"`  
`cat file | claude -p "query"` | Process piped content | `cat logs.txt | claude -p "explain"`  
`claude -c` | Continue most recent conversation | `claude -c`  
`claude -c -p "query"` | Continue via SDK | `claude -c -p "Check for type errors"`  
`claude -r "<session-id>" "query"` | Resume session by ID | `claude -r "abc123" "Finish this PR"`  
`claude update` | Update to latest version | `claude update`  
`claude mcp` | Configure Model Context Protocol (MCP) servers | See the [Claude Code MCP documentation](https://docs.anthropic.com/en/docs/claude-code/mcp).  
## 
[​](https://docs.anthropic.com/en/docs/claude-code/cli-reference#cli-flags)
CLI flags
Customize Claude Code’s behavior with these command-line flags:
Flag | Description | Example  
---|---|---  
`--add-dir` | Add additional working directories for Claude to access (validates each path exists as a directory) | `claude --add-dir ../apps ../lib`  
`--allowedTools` | A list of tools that should be allowed without prompting the user for permission, in addition to [settings.json files](https://docs.anthropic.com/en/docs/claude-code/settings) | `"Bash(git log:*)" "Bash(git diff:*)" "Read"`  
`--disallowedTools` | A list of tools that should be disallowed without prompting the user for permission, in addition to [settings.json files](https://docs.anthropic.com/en/docs/claude-code/settings) | `"Bash(git log:*)" "Bash(git diff:*)" "Edit"`  
`--print`, `-p` | Print response without interactive mode (see [SDK documentation](https://docs.anthropic.com/en/docs/claude-code/sdk) for programmatic usage details) | `claude -p "query"`  
`--append-system-prompt` | Append to system prompt (only with `--print`) | `claude --append-system-prompt "Custom instruction"`  
`--output-format` | Specify output format for print mode (options: `text`, `json`, `stream-json`) | `claude -p "query" --output-format json`  
`--input-format` | Specify input format for print mode (options: `text`, `stream-json`) | `claude -p --output-format json --input-format stream-json`  
`--verbose` | Enable verbose logging, shows full turn-by-turn output (helpful for debugging in both print and interactive modes) | `claude --verbose`  
`--max-turns` | Limit the number of agentic turns in non-interactive mode | `claude -p --max-turns 3 "query"`  
`--model` | Sets the model for the current session with an alias for the latest model (`sonnet` or `opus`) or a model’s full name | `claude --model claude-sonnet-4-20250514`  
`--permission-mode` | Begin in a specified [permission mode](https://docs.anthropic.com/en/docs/claude-code/iam#permission-modes) | `claude --permission-mode plan`  
`--permission-prompt-tool` | Specify an MCP tool to handle permission prompts in non-interactive mode | `claude -p --permission-prompt-tool mcp_auth_tool "query"`  
`--resume` | Resume a specific session by ID, or by choosing in interactive mode | `claude --resume abc123 "query"`  
`--continue` | Load the most recent conversation in the current directory | `claude --continue`  
`--dangerously-skip-permissions` | Skip permission prompts (use with caution) | `claude --dangerously-skip-permissions`  
The `--output-format json` flag is particularly useful for scripting and automation, allowing you to parse Claude’s responses programmatically.
For detailed information about print mode (`-p`) including output formats, streaming, verbose logging, and programmatic usage, see the [SDK documentation](https://docs.anthropic.com/en/docs/claude-code/sdk).
## 
[​](https://docs.anthropic.com/en/docs/claude-code/cli-reference#see-also)
See also
  * [Interactive mode](https://docs.anthropic.com/en/docs/claude-code/interactive-mode) - Shortcuts, input modes, and interactive features
  * [Slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands) - Interactive session commands
  * [Quickstart guide](https://docs.anthropic.com/en/docs/claude-code/quickstart) - Getting started with Claude Code
  * [Common workflows](https://docs.anthropic.com/en/docs/claude-code/common-workflows) - Advanced workflows and patterns
  * [Settings](https://docs.anthropic.com/en/docs/claude-code/settings) - Configuration options
  * [SDK documentation](https://docs.anthropic.com/en/docs/claude-code/sdk) - Programmatic usage and integrations


Was this page helpful?
YesNo
[Status line configuration](https://docs.anthropic.com/en/docs/claude-code/statusline)[Interactive mode](https://docs.anthropic.com/en/docs/claude-code/interactive-mode)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [CLI commands](https://docs.anthropic.com/en/docs/claude-code/cli-reference#cli-commands)
  * [CLI flags](https://docs.anthropic.com/en/docs/claude-code/cli-reference#cli-flags)
  * [See also](https://docs.anthropic.com/en/docs/claude-code/cli-reference#see-also)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/common-workflows -->

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
Getting started
Common workflows
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


Getting started
# Common workflows
Copy page
Learn about common workflows with Claude Code.
Each task in this document includes clear instructions, example commands, and best practices to help you get the most from Claude Code.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#understand-new-codebases)
Understand new codebases
### 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#get-a-quick-codebase-overview)
Get a quick codebase overview
Suppose you’ve just joined a new project and need to understand its structure quickly.
1
Navigate to the project root directory
Copy
```
cd /path/to/project 

```

2
Start Claude Code
Copy
```
claude 

```

3
Ask for a high-level overview
Copy
```
> give me an overview of this codebase 

```

4
Dive deeper into specific components
Copy
```
> explain the main architecture patterns used here 

```

Copy
```
> what are the key data models?

```

Copy
```
> how is authentication handled?

```

Tips:
  * Start with broad questions, then narrow down to specific areas
  * Ask about coding conventions and patterns used in the project
  * Request a glossary of project-specific terms


### 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#find-relevant-code)
Find relevant code
Suppose you need to locate code related to a specific feature or functionality.
1
Ask Claude to find relevant files
Copy
```
> find the files that handle user authentication 

```

2
Get context on how components interact
Copy
```
> how do these authentication files work together? 

```

3
Understand the execution flow
Copy
```
> trace the login process from front-end to database 

```

Tips:
  * Be specific about what you’re looking for
  * Use domain language from the project


* * *
## 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#fix-bugs-efficiently)
Fix bugs efficiently
Suppose you’ve encountered an error message and need to find and fix its source.
1
Share the error with Claude
Copy
```
> I'm seeing an error when I run npm test 

```

2
Ask for fix recommendations
Copy
```
> suggest a few ways to fix the @ts-ignore in user.ts 

```

3
Apply the fix
Copy
```
> update user.ts to add the null check you suggested 

```

Tips:
  * Tell Claude the command to reproduce the issue and get a stack trace
  * Mention any steps to reproduce the error
  * Let Claude know if the error is intermittent or consistent


* * *
## 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#refactor-code)
Refactor code
Suppose you need to update old code to use modern patterns and practices.
1
Identify legacy code for refactoring
Copy
```
> find deprecated API usage in our codebase 

```

2
Get refactoring recommendations
Copy
```
> suggest how to refactor utils.js to use modern JavaScript features 

```

3
Apply the changes safely
Copy
```
> refactor utils.js to use ES2024 features while maintaining the same behavior 

```

4
Verify the refactoring
Copy
```
> run tests for the refactored code 

```

Tips:
  * Ask Claude to explain the benefits of the modern approach
  * Request that changes maintain backward compatibility when needed
  * Do refactoring in small, testable increments


* * *
## 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#use-specialized-subagents)
Use specialized subagents
Suppose you want to use specialized AI subagents to handle specific tasks more effectively.
1
View available subagents
Copy
```
> /agents

```

This shows all available subagents and lets you create new ones.
2
Use subagents automatically
Claude Code will automatically delegate appropriate tasks to specialized subagents:
Copy
```
> review my recent code changes for security issues

```

Copy
```
> run all tests and fix any failures

```

3
Explicitly request specific subagents
Copy
```
> use the code-reviewer subagent to check the auth module

```

Copy
```
> have the debugger subagent investigate why users can't log in

```

4
Create custom subagents for your workflow
Copy
```
> /agents

```

Then select “Create New subagent” and follow the prompts to define:
  * Subagent type (e.g., `api-designer`, `performance-optimizer`)
  * When to use it
  * Which tools it can access
  * Its specialized system prompt


Tips:
  * Create project-specific subagents in `.claude/agents/` for team sharing
  * Use descriptive `description` fields to enable automatic delegation
  * Limit tool access to what each subagent actually needs
  * Check the [subagents documentation](https://docs.anthropic.com/en/docs/claude-code/sub-agents) for detailed examples


* * *
## 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#work-with-tests)
Work with tests
Suppose you need to add tests for uncovered code.
1
Identify untested code
Copy
```
> find functions in NotificationsService.swift that are not covered by tests 

```

2
Generate test scaffolding
Copy
```
> add tests for the notification service 

```

3
Add meaningful test cases
Copy
```
> add test cases for edge conditions in the notification service 

```

4
Run and verify tests
Copy
```
> run the new tests and fix any failures 

```

Tips:
  * Ask for tests that cover edge cases and error conditions
  * Request both unit and integration tests when appropriate
  * Have Claude explain the testing strategy


* * *
## 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#create-pull-requests)
Create pull requests
Suppose you need to create a well-documented pull request for your changes.
1
Summarize your changes
Copy
```
> summarize the changes I've made to the authentication module 

```

2
Generate a PR with Claude
Copy
```
> create a pr 

```

3
Review and refine
Copy
```
> enhance the PR description with more context about the security improvements 

```

4
Add testing details
Copy
```
> add information about how these changes were tested 

```

Tips:
  * Ask Claude directly to make a PR for you
  * Review Claude’s generated PR before submitting
  * Ask Claude to highlight potential risks or considerations


## 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#handle-documentation)
Handle documentation
Suppose you need to add or update documentation for your code.
1
Identify undocumented code
Copy
```
> find functions without proper JSDoc comments in the auth module 

```

2
Generate documentation
Copy
```
> add JSDoc comments to the undocumented functions in auth.js 

```

3
Review and enhance
Copy
```
> improve the generated documentation with more context and examples 

```

4
Verify documentation
Copy
```
> check if the documentation follows our project standards 

```

Tips:
  * Specify the documentation style you want (JSDoc, docstrings, etc.)
  * Ask for examples in the documentation
  * Request documentation for public APIs, interfaces, and complex logic


* * *
## 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#work-with-images)
Work with images
Suppose you need to work with images in your codebase, and you want Claude’s help analyzing image content.
1
Add an image to the conversation
You can use any of these methods:
  1. Drag and drop an image into the Claude Code window
  2. Copy an image and paste it into the CLI with ctrl+v (Do not use cmd+v)
  3. Provide an image path to Claude. E.g., “Analyze this image: /path/to/your/image.png”


2
Ask Claude to analyze the image
Copy
```
> What does this image show?

```

Copy
```
> Describe the UI elements in this screenshot

```

Copy
```
> Are there any problematic elements in this diagram?

```

3
Use images for context
Copy
```
> Here's a screenshot of the error. What's causing it?

```

Copy
```
> This is our current database schema. How should we modify it for the new feature?

```

4
Get code suggestions from visual content
Copy
```
> Generate CSS to match this design mockup

```

Copy
```
> What HTML structure would recreate this component?

```

Tips:
  * Use images when text descriptions would be unclear or cumbersome
  * Include screenshots of errors, UI designs, or diagrams for better context
  * You can work with multiple images in a conversation
  * Image analysis works with diagrams, screenshots, mockups, and more


* * *
## 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#reference-files-and-directories)
Reference files and directories
Use @ to quickly include files or directories without waiting for Claude to read them.
1
Reference a single file
Copy
```
> Explain the logic in @src/utils/auth.js

```

This includes the full content of the file in the conversation.
2
Reference a directory
Copy
```
> What's the structure of @src/components?

```

This provides a directory listing with file information.
3
Reference MCP resources
Copy
```
> Show me the data from @github:repos/owner/repo/issues

```

This fetches data from connected MCP servers using the format @server:resource. See [MCP resources](https://docs.anthropic.com/en/docs/claude-code/mcp#use-mcp-resources) for details.
Tips:
  * File paths can be relative or absolute
  * @ file references add CLAUDE.md in the file’s directory and parent directories to context
  * Directory references show file listings, not contents
  * You can reference multiple files in a single message (e.g., “@file1.js and @file2.js”)


* * *
## 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#use-extended-thinking)
Use extended thinking
Suppose you’re working on complex architectural decisions, challenging bugs, or planning multi-step implementations that require deep reasoning.
1
Provide context and ask Claude to think
Copy
```
> I need to implement a new authentication system using OAuth2 for our API. Think deeply about the best approach for implementing this in our codebase. 

```

Claude will gather relevant information from your codebase and use extended thinking, which will be visible in the interface.
2
Refine the thinking with follow-up prompts
Copy
```
> think about potential security vulnerabilities in this approach 

```

Copy
```
> think harder about edge cases we should handle 

```

Tips to get the most value out of extended thinking:
Extended thinking is most valuable for complex tasks such as:
  * Planning complex architectural changes
  * Debugging intricate issues
  * Creating implementation plans for new features
  * Understanding complex codebases
  * Evaluating tradeoffs between different approaches


The way you prompt for thinking results in varying levels of thinking depth:
  * “think” triggers basic extended thinking
  * intensifying phrases such as “think more”, “think a lot”, “think harder”, or “think longer” triggers deeper thinking


For more extended thinking prompting tips, see [Extended thinking tips](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips).
Claude will display its thinking process as italic gray text above the response.
* * *
## 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#resume-previous-conversations)
Resume previous conversations
Suppose you’ve been working on a task with Claude Code and need to continue where you left off in a later session.
Claude Code provides two options for resuming previous conversations:
  * `--continue` to automatically continue the most recent conversation
  * `--resume` to display a conversation picker


1
Continue the most recent conversation
Copy
```
claude --continue

```

This immediately resumes your most recent conversation without any prompts.
2
Continue in non-interactive mode
Copy
```
claude --continue --print "Continue with my task"

```

Use `--print` with `--continue` to resume the most recent conversation in non-interactive mode, perfect for scripts or automation.
3
Show conversation picker
Copy
```
claude --resume

```

This displays an interactive conversation selector showing:
  * Conversation start time
  * Initial prompt or conversation summary
  * Message count


Use arrow keys to navigate and press Enter to select a conversation.
Tips:
  * Conversation history is stored locally on your machine
  * Use `--continue` for quick access to your most recent conversation
  * Use `--resume` when you need to select a specific past conversation
  * When resuming, you’ll see the entire conversation history before continuing
  * The resumed conversation starts with the same model and configuration as the original


How it works:
  1. **Conversation Storage** : All conversations are automatically saved locally with their full message history
  2. **Message Deserialization** : When resuming, the entire message history is restored to maintain context
  3. **Tool State** : Tool usage and results from the previous conversation are preserved
  4. **Context Restoration** : The conversation resumes with all previous context intact


Examples:
Copy
```
# Continue most recent conversation
claude --continue

# Continue most recent conversation with a specific prompt
claude --continue --print "Show me our progress"

# Show conversation picker
claude --resume

# Continue most recent conversation in non-interactive mode
claude --continue --print "Run the tests again"

```

* * *
## 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees)
Run parallel Claude Code sessions with Git worktrees
Suppose you need to work on multiple tasks simultaneously with complete code isolation between Claude Code instances.
1
Understand Git worktrees
Git worktrees allow you to check out multiple branches from the same repository into separate directories. Each worktree has its own working directory with isolated files, while sharing the same Git history. Learn more in the [official Git worktree documentation](https://git-scm.com/docs/git-worktree).
2
Create a new worktree
Copy
```
# Create a new worktree with a new branch 
git worktree add ../project-feature-a -b feature-a

# Or create a worktree with an existing branch
git worktree add ../project-bugfix bugfix-123

```

This creates a new directory with a separate working copy of your repository.
3
Run Claude Code in each worktree
Copy
```
# Navigate to your worktree 
cd ../project-feature-a

# Run Claude Code in this isolated environment
claude

```

4
Run Claude in another worktree
Copy
```
cd ../project-bugfix
claude

```

5
Manage your worktrees
Copy
```
# List all worktrees
git worktree list

# Remove a worktree when done
git worktree remove ../project-feature-a

```

Tips:
  * Each worktree has its own independent file state, making it perfect for parallel Claude Code sessions
  * Changes made in one worktree won’t affect others, preventing Claude instances from interfering with each other
  * All worktrees share the same Git history and remote connections
  * For long-running tasks, you can have Claude working in one worktree while you continue development in another
  * Use descriptive directory names to easily identify which task each worktree is for
  * Remember to initialize your development environment in each new worktree according to your project’s setup. Depending on your stack, this might include: 
    * JavaScript projects: Running dependency installation (`npm install`, `yarn`)
    * Python projects: Setting up virtual environments or installing with package managers
    * Other languages: Following your project’s standard setup process


* * *
## 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#use-claude-as-a-unix-style-utility)
Use Claude as a unix-style utility
### 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#add-claude-to-your-verification-process)
Add Claude to your verification process
Suppose you want to use Claude Code as a linter or code reviewer.
**Add Claude to your build script:**
Copy
```
// package.json
{
    ...
    "scripts": {
        ...
        "lint:claude": "claude -p 'you are a linter. please look at the changes vs. main and report any issues related to typos. report the filename and line number on one line, and a description of the issue on the second line. do not return any other text.'"
    }
}

```

Tips:
  * Use Claude for automated code review in your CI/CD pipeline
  * Customize the prompt to check for specific issues relevant to your project
  * Consider creating multiple scripts for different types of verification


### 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#pipe-in%2C-pipe-out)
Pipe in, pipe out
Suppose you want to pipe data into Claude, and get back data in a structured format.
**Pipe data through Claude:**
Copy
```
cat build-error.txt | claude -p 'concisely explain the root cause of this build error' > output.txt

```

Tips:
  * Use pipes to integrate Claude into existing shell scripts
  * Combine with other Unix tools for powerful workflows
  * Consider using —output-format for structured output


### 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#control-output-format)
Control output format
Suppose you need Claude’s output in a specific format, especially when integrating Claude Code into scripts or other tools.
1
Use text format (default)
Copy
```
cat data.txt | claude -p 'summarize this data' --output-format text > summary.txt

```

This outputs just Claude’s plain text response (default behavior).
2
Use JSON format
Copy
```
cat code.py | claude -p 'analyze this code for bugs' --output-format json > analysis.json

```

This outputs a JSON array of messages with metadata including cost and duration.
3
Use streaming JSON format
Copy
```
cat log.txt | claude -p 'parse this log file for errors' --output-format stream-json

```

This outputs a series of JSON objects in real-time as Claude processes the request. Each message is a valid JSON object, but the entire output is not valid JSON if concatenated.
Tips:
  * Use `--output-format text` for simple integrations where you just need Claude’s response
  * Use `--output-format json` when you need the full conversation log
  * Use `--output-format stream-json` for real-time output of each conversation turn


* * *
## 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#create-custom-slash-commands)
Create custom slash commands
Claude Code supports custom slash commands that you can create to quickly execute specific prompts or tasks.
For more details, see the [Slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands) reference page.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#create-project-specific-commands)
Create project-specific commands
Suppose you want to create reusable slash commands for your project that all team members can use.
1
Create a commands directory in your project
Copy
```
mkdir -p .claude/commands

```

2
Create a Markdown file for each command
Copy
```
echo "Analyze the performance of this code and suggest three specific optimizations:" > .claude/commands/optimize.md 

```

3
Use your custom command in Claude Code
Copy
```
> /optimize 

```

Tips:
  * Command names are derived from the filename (e.g., `optimize.md` becomes `/optimize`)
  * You can organize commands in subdirectories (e.g., `.claude/commands/frontend/component.md` creates `/component` with “(project:frontend)” shown in the description)
  * Project commands are available to everyone who clones the repository
  * The Markdown file content becomes the prompt sent to Claude when the command is invoked


### 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#add-command-arguments-with-%24arguments)
Add command arguments with $ARGUMENTS
Suppose you want to create flexible slash commands that can accept additional input from users.
1
Create a command file with the $ARGUMENTS placeholder
Copy
```
echo 'Find and fix issue #$ARGUMENTS. Follow these steps: 1.
Understand the issue described in the ticket 2. Locate the relevant code in
our codebase 3. Implement a solution that addresses the root cause 4. Add
appropriate tests 5. Prepare a concise PR description' >
.claude/commands/fix-issue.md 

```

2
Use the command with an issue number
In your Claude session, use the command with arguments.
Copy
```
> /fix-issue 123 

```

This will replace $ARGUMENTS with “123” in the prompt.
Tips:
  * The $ARGUMENTS placeholder is replaced with any text that follows the command
  * You can position $ARGUMENTS anywhere in your command template
  * Other useful applications: generating test cases for specific functions, creating documentation for components, reviewing code in particular files, or translating content to specified languages


### 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#create-personal-slash-commands)
Create personal slash commands
Suppose you want to create personal slash commands that work across all your projects.
1
Create a commands directory in your home folder
Copy
```
mkdir -p ~/.claude/commands 

```

2
Create a Markdown file for each command
Copy
```
echo "Review this code for security vulnerabilities, focusing on:" >
~/.claude/commands/security-review.md 

```

3
Use your personal custom command
Copy
```
> /security-review 

```

Tips:
  * Personal commands show “(user)” in their description when listed with `/help`
  * Personal commands are only available to you and not shared with your team
  * Personal commands work across all your projects
  * You can use these for consistent workflows across different codebases


* * *
## 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#ask-claude-about-its-capabilities)
Ask Claude about its capabilities
Claude has built-in access to its documentation and can answer questions about its own features and limitations.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#example-questions)
Example questions
Copy
```
> can Claude Code create pull requests?

```

Copy
```
> how does Claude Code handle permissions?

```

Copy
```
> what slash commands are available?

```

Copy
```
> how do I use MCP with Claude Code?

```

Copy
```
> how do I configure Claude Code for Amazon Bedrock?

```

Copy
```
> what are the limitations of Claude Code?

```

Claude provides documentation-based answers to these questions. For executable examples and hands-on demonstrations, refer to the specific workflow sections above.
Tips:
  * Claude always has access to the latest Claude Code documentation, regardless of the version you’re using
  * Ask specific questions to get detailed answers
  * Claude can explain complex features like MCP integration, enterprise configurations, and advanced workflows


* * *
## 
[​](https://docs.anthropic.com/en/docs/claude-code/common-workflows#next-steps)
Next steps
## [Claude Code reference implementation Clone our development container reference implementation. ](https://github.com/anthropics/claude-code/tree/main/.devcontainer)
Was this page helpful?
YesNo
[Quickstart](https://docs.anthropic.com/en/docs/claude-code/quickstart)[Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code/sdk)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Understand new codebases](https://docs.anthropic.com/en/docs/claude-code/common-workflows#understand-new-codebases)
  * [Get a quick codebase overview](https://docs.anthropic.com/en/docs/claude-code/common-workflows#get-a-quick-codebase-overview)
  * [Find relevant code](https://docs.anthropic.com/en/docs/claude-code/common-workflows#find-relevant-code)
  * [Fix bugs efficiently](https://docs.anthropic.com/en/docs/claude-code/common-workflows#fix-bugs-efficiently)
  * [Refactor code](https://docs.anthropic.com/en/docs/claude-code/common-workflows#refactor-code)
  * [Use specialized subagents](https://docs.anthropic.com/en/docs/claude-code/common-workflows#use-specialized-subagents)
  * [Work with tests](https://docs.anthropic.com/en/docs/claude-code/common-workflows#work-with-tests)
  * [Create pull requests](https://docs.anthropic.com/en/docs/claude-code/common-workflows#create-pull-requests)
  * [Handle documentation](https://docs.anthropic.com/en/docs/claude-code/common-workflows#handle-documentation)
  * [Work with images](https://docs.anthropic.com/en/docs/claude-code/common-workflows#work-with-images)
  * [Reference files and directories](https://docs.anthropic.com/en/docs/claude-code/common-workflows#reference-files-and-directories)
  * [Use extended thinking](https://docs.anthropic.com/en/docs/claude-code/common-workflows#use-extended-thinking)
  * [Resume previous conversations](https://docs.anthropic.com/en/docs/claude-code/common-workflows#resume-previous-conversations)
  * [Run parallel Claude Code sessions with Git worktrees](https://docs.anthropic.com/en/docs/claude-code/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees)
  * [Use Claude as a unix-style utility](https://docs.anthropic.com/en/docs/claude-code/common-workflows#use-claude-as-a-unix-style-utility)
  * [Add Claude to your verification process](https://docs.anthropic.com/en/docs/claude-code/common-workflows#add-claude-to-your-verification-process)
  * [Pipe in, pipe out](https://docs.anthropic.com/en/docs/claude-code/common-workflows#pipe-in%2C-pipe-out)
  * [Control output format](https://docs.anthropic.com/en/docs/claude-code/common-workflows#control-output-format)
  * [Create custom slash commands](https://docs.anthropic.com/en/docs/claude-code/common-workflows#create-custom-slash-commands)
  * [Create project-specific commands](https://docs.anthropic.com/en/docs/claude-code/common-workflows#create-project-specific-commands)
  * [Add command arguments with $ARGUMENTS](https://docs.anthropic.com/en/docs/claude-code/common-workflows#add-command-arguments-with-%24arguments)
  * [Create personal slash commands](https://docs.anthropic.com/en/docs/claude-code/common-workflows#create-personal-slash-commands)
  * [Ask Claude about its capabilities](https://docs.anthropic.com/en/docs/claude-code/common-workflows#ask-claude-about-its-capabilities)
  * [Example questions](https://docs.anthropic.com/en/docs/claude-code/common-workflows#example-questions)
  * [Next steps](https://docs.anthropic.com/en/docs/claude-code/common-workflows#next-steps)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/corporate-proxy -->

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


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/costs -->

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
Administration
Manage costs effectively
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


Administration
# Manage costs effectively
Copy page
Learn how to track and optimize token usage and costs when using Claude Code.
Claude Code consumes tokens for each interaction. The average cost is $6 per developer per day, with daily costs remaining below $12 for 90% of users.
For team usage, Claude Code charges by API token consumption. On average, Claude Code costs ~$100-200/developer per month with Sonnet 4 though there is large variance depending on how many instances users are running and whether they’re using it in automation.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/costs#track-your-costs)
Track your costs
  * Use `/cost` to see current session usage
  * **Anthropic Console users** : 
    * Check [historical usage](https://support.anthropic.com/en/articles/9534590-cost-and-usage-reporting-in-console) in the Anthropic Console (requires Admin or Billing role)
    * Set [workspace spend limits](https://support.anthropic.com/en/articles/9796807-creating-and-managing-workspaces) for the Claude Code workspace (requires Admin role)
  * **Pro and Max plan users** : Usage is included in your subscription


## 
[​](https://docs.anthropic.com/en/docs/claude-code/costs#managing-costs-for-teams)
Managing costs for teams
When using Anthropic API, you can limit the total Claude Code workspace spend. To configure, [follow these instructions](https://support.anthropic.com/en/articles/9796807-creating-and-managing-workspaces). Admins can view cost and usage reporting by [following these instructions](https://support.anthropic.com/en/articles/9534590-cost-and-usage-reporting-in-console).
On Bedrock and Vertex, Claude Code does not send metrics from your cloud. In order to get cost metrics, several large enterprises reported using [LiteLLM](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#litellm), which is an open-source tool that helps companies [track spend by key](https://docs.litellm.ai/docs/proxy/virtual_keys#tracking-spend). This project is unaffiliated with Anthropic and we have not audited its security.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/costs#rate-limit-recommendations)
Rate limit recommendations
When setting up Claude Code for teams, consider these Token Per Minute (TPM) and Request Per Minute (RPM) per-user recommendations based on your organization size:
Team size | TPM per user | RPM per user  
---|---|---  
1-5 users | 200k-300k | 5-7  
5-20 users | 100k-150k | 2.5-3.5  
20-50 users | 50k-75k | 1.25-1.75  
50-100 users | 25k-35k | 0.62-0.87  
100-500 users | 15k-20k | 0.37-0.47  
500+ users | 10k-15k | 0.25-0.35  
For example, if you have 200 users, you might request 20k TPM for each user, or 4 million total TPM (200*20,000 = 4 million).
The TPM per user decreases as team size grows because we expect fewer users to use Claude Code concurrently in larger organizations. These rate limits apply at the organization level, not per individual user, which means individual users can temporarily consume more than their calculated share when others aren’t actively using the service.
If you anticipate scenarios with unusually high concurrent usage (such as live training sessions with large groups), you may need higher TPM allocations per user.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/costs#reduce-token-usage)
Reduce token usage
  * **Compact conversations:**
    * Claude uses auto-compact by default when context exceeds 95% capacity
    * Toggle auto-compact: Run `/config` and navigate to “Auto-compact enabled”
    * Use `/compact` manually when context gets large
    * Add custom instructions: `/compact Focus on code samples and API usage`
    * Customize compaction by adding to CLAUDE.md:
Copy
```
# Summary instructions

When you are using compact, please focus on test output and code changes

```

  * **Write specific queries:** Avoid vague requests that trigger unnecessary scanning
  * **Break down complex tasks:** Split large tasks into focused interactions
  * **Clear history between tasks:** Use `/clear` to reset context


Costs can vary significantly based on:
  * Size of codebase being analyzed
  * Complexity of queries
  * Number of files being searched or modified
  * Length of conversation history
  * Frequency of compacting conversations
  * Background processes (haiku generation, conversation summarization)


## 
[​](https://docs.anthropic.com/en/docs/claude-code/costs#background-token-usage)
Background token usage
Claude Code uses tokens for some background functionality even when idle:
  * **Haiku generation** : Small creative messages that appear while you type (approximately 1 cent per day)
  * **Conversation summarization** : Background jobs that summarize previous conversations for the `claude --resume` feature
  * **Command processing** : Some commands like `/cost` may generate requests to check status


These background processes consume a small amount of tokens (typically under $0.04 per session) even without active interaction.
For team deployments, we recommend starting with a small pilot group to establish usage patterns before wider rollout.
Was this page helpful?
YesNo
[Monitoring](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage)[Analytics](https://docs.anthropic.com/en/docs/claude-code/analytics)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Track your costs](https://docs.anthropic.com/en/docs/claude-code/costs#track-your-costs)
  * [Managing costs for teams](https://docs.anthropic.com/en/docs/claude-code/costs#managing-costs-for-teams)
  * [Rate limit recommendations](https://docs.anthropic.com/en/docs/claude-code/costs#rate-limit-recommendations)
  * [Reduce token usage](https://docs.anthropic.com/en/docs/claude-code/costs#reduce-token-usage)
  * [Background token usage](https://docs.anthropic.com/en/docs/claude-code/costs#background-token-usage)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/data-usage -->

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
Administration
Data usage
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


Administration
# Data usage
Copy page
Learn about Anthropic’s data usage policies for Claude
## 
[​](https://docs.anthropic.com/en/docs/claude-code/data-usage#data-policies)
Data policies
### 
[​](https://docs.anthropic.com/en/docs/claude-code/data-usage#data-training-policy)
Data training policy
By default, Anthropic does not train generative models using code or prompts that are sent to Claude Code.
We aim to be fully transparent about how we use your data. We may use feedback to improve our products and services, but we will not train generative models using your feedback from Claude Code.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/data-usage#development-partner-program)
Development Partner Program
If you explicitly opt in to methods to provide us with materials to train on, such as via the [Development Partner Program](https://support.anthropic.com/en/articles/11174108-about-the-development-partner-program), we may use those materials provided to train our models. An organization admin can expressly opt-in to the Development Partner Program for their organization. Note that this program is available only for Anthropic first-party API, and not for Bedrock or Vertex users.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/data-usage#feedback-transcripts)
Feedback transcripts
If you choose to send us feedback about Claude Code, such as transcripts of your usage, Anthropic may use that feedback to debug related issues and improve Claude Code’s functionality (e.g., to reduce the risk of similar bugs occurring in the future). We will not train generative models using this feedback. Given their potentially sensitive nature, we store user feedback transcripts for only 30 days.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/data-usage#data-retention)
Data retention
You can use an API key from a zero data retention organization. When doing so, Claude Code will not retain your chat transcripts on our servers. Users’ local Claude Code clients may store sessions locally for up to 30 days so that users can resume them. This behavior is configurable.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/data-usage#privacy-safeguards)
Privacy safeguards
We have implemented several safeguards to protect your data, including:
  * Limited retention periods for sensitive information
  * Restricted access to user session data
  * Clear policies against using feedback for model training


For full details, please review our [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and [Privacy Policy](https://www.anthropic.com/legal/privacy).
## 
[​](https://docs.anthropic.com/en/docs/claude-code/data-usage#data-flow-and-dependencies)
Data flow and dependencies
![Claude Code data flow diagram](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/images/claude-code-data-flow.png)
Claude Code is installed from [NPM](https://www.npmjs.com/package/@anthropic-ai/claude-code). Claude Code runs locally. In order to interact with the LLM, Claude Code sends data over the network. This data includes all user prompts and model outputs. The data is encrypted in transit via TLS and is not encrypted at rest. Claude Code is compatible with most popular VPNs and LLM proxies.
Claude Code is built on Anthropic’s APIs. For details regarding our API’s security controls, including our API logging procedures, please refer to compliance artifacts offered in the [Anthropic Trust Center](https://trust.anthropic.com).
## 
[​](https://docs.anthropic.com/en/docs/claude-code/data-usage#telemetry-services)
Telemetry services
Claude Code connects from users’ machines to the Statsig service to log operational metrics such as latency, reliability, and usage patterns. This logging does not include any code or file paths. Data is encrypted in transit using TLS and at rest using 256-bit AES encryption. Read more in the [Statsig security documentation](https://www.statsig.com/trust/security). To opt out of Statsig telemetry, set the `DISABLE_TELEMETRY` environment variable.
Claude Code connects from users’ machines to Sentry for operational error logging. The data is encrypted in transit using TLS and at rest using 256-bit AES encryption. Read more in the [Sentry security documentation](https://sentry.io/security/). To opt out of error logging, set the `DISABLE_ERROR_REPORTING` environment variable.
When users run the `/bug` command, a copy of their full conversation history including code is sent to Anthropic. The data is encrypted in transit and at rest. Optionally, a Github issue is created in our public repository. To opt out of bug reporting, set the `DISABLE_BUG_COMMAND` environment variable.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/data-usage#default-behaviors-by-api-provider)
Default behaviors by API provider
By default, we disable all non-essential traffic (including error reporting, telemetry, and bug reporting functionality) when using Bedrock or Vertex. You can also opt out of all of these at once by setting the `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` environment variable. Here are the full default behaviors:
Service | Anthropic API | Vertex API | Bedrock API  
---|---|---|---  
**Statsig (Metrics)** | Default on.  
`DISABLE_TELEMETRY=1` to disable. | Default off.  
`CLAUDE_CODE_USE_VERTEX` must be 1. | Default off.  
`CLAUDE_CODE_USE_BEDROCK` must be 1.  
**Sentry (Errors)** | Default on.  
`DISABLE_ERROR_REPORTING=1` to disable. | Default off.  
`CLAUDE_CODE_USE_VERTEX` must be 1. | Default off.  
`CLAUDE_CODE_USE_BEDROCK` must be 1.  
**Anthropic API (`/bug` reports)** | Default on.  
`DISABLE_BUG_COMMAND=1` to disable. | Default off.  
`CLAUDE_CODE_USE_VERTEX` must be 1. | Default off.  
`CLAUDE_CODE_USE_BEDROCK` must be 1.  
All environment variables can be checked into `settings.json` ([read more](https://docs.anthropic.com/en/docs/claude-code/settings)).
Was this page helpful?
YesNo
[Security](https://docs.anthropic.com/en/docs/claude-code/security)[Monitoring](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Data policies](https://docs.anthropic.com/en/docs/claude-code/data-usage#data-policies)
  * [Data training policy](https://docs.anthropic.com/en/docs/claude-code/data-usage#data-training-policy)
  * [Development Partner Program](https://docs.anthropic.com/en/docs/claude-code/data-usage#development-partner-program)
  * [Feedback transcripts](https://docs.anthropic.com/en/docs/claude-code/data-usage#feedback-transcripts)
  * [Data retention](https://docs.anthropic.com/en/docs/claude-code/data-usage#data-retention)
  * [Privacy safeguards](https://docs.anthropic.com/en/docs/claude-code/data-usage#privacy-safeguards)
  * [Data flow and dependencies](https://docs.anthropic.com/en/docs/claude-code/data-usage#data-flow-and-dependencies)
  * [Telemetry services](https://docs.anthropic.com/en/docs/claude-code/data-usage#telemetry-services)
  * [Default behaviors by API provider](https://docs.anthropic.com/en/docs/claude-code/data-usage#default-behaviors-by-api-provider)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/devcontainer -->

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


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/github-actions -->

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
Claude Code GitHub Actions
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
# Claude Code GitHub Actions
Copy page
Learn about integrating Claude Code into your development workflow with Claude Code GitHub Actions
Claude Code GitHub Actions brings AI-powered automation to your GitHub workflow. With a simple `@claude` mention in any PR or issue, Claude can analyze your code, create pull requests, implement features, and fix bugs - all while following your project’s standards.
Claude Code GitHub Actions is currently in beta. Features and functionality may evolve as we refine the experience.
Claude Code GitHub Actions is built on top of the [Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code/sdk), which enables programmatic integration of Claude Code into your applications. You can use the SDK to build custom automation workflows beyond GitHub Actions.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#why-use-claude-code-github-actions%3F)
Why use Claude Code GitHub Actions?
  * **Instant PR creation** : Describe what you need, and Claude creates a complete PR with all necessary changes
  * **Automated code implementation** : Turn issues into working code with a single command
  * **Follows your standards** : Claude respects your `CLAUDE.md` guidelines and existing code patterns
  * **Simple setup** : Get started in minutes with our installer and API key
  * **Secure by default** : Your code stays on Github’s runners


## 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#what-can-claude-do%3F)
What can Claude do?
Claude Code provides powerful GitHub Actions that transform how you work with code:
### 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#claude-code-action)
Claude Code Action
This GitHub Action allows you to run Claude Code within your GitHub Actions workflows. You can use this to build any custom workflow on top of Claude Code.
[View repository →](https://github.com/anthropics/claude-code-action)
### 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#claude-code-action-base)
Claude Code Action (Base)
The foundation for building custom GitHub workflows with Claude. This extensible framework gives you full access to Claude’s capabilities for creating tailored automation.
[View repository →](https://github.com/anthropics/claude-code-base-action)
## 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#setup)
Setup
## 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#quick-setup)
Quick setup
The easiest way to set up this action is through Claude Code in the terminal. Just open claude and run `/install-github-app`.
This command will guide you through setting up the GitHub app and required secrets.
  * You must be a repository admin to install the GitHub app and add secrets
  * This quickstart method is only available for direct Anthropic API users. If you’re using AWS Bedrock or Google Vertex AI, please see the [Using with AWS Bedrock & Google Vertex AI](https://docs.anthropic.com/en/docs/claude-code/github-actions#using-with-aws-bedrock-%26-google-vertex-ai) section.


## 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#manual-setup)
Manual setup
If the `/install-github-app` command fails or you prefer manual setup, please follow these manual setup instructions:
  1. **Install the Claude GitHub app** to your repository: <https://github.com/apps/claude>
  2. **Add ANTHROPIC_API_KEY** to your repository secrets ([Learn how to use secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions))
  3. **Copy the workflow file** from [examples/claude.yml](https://github.com/anthropics/claude-code-action/blob/main/examples/claude.yml) into your repository’s `.github/workflows/`


After completing either the quickstart or manual setup, test the action by tagging `@claude` in an issue or PR comment!
## 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#example-use-cases)
Example use cases
Claude Code GitHub Actions can help you with a variety of tasks. For complete working examples, see the [examples directory](https://github.com/anthropics/claude-code-action/tree/main/examples).
### 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#turn-issues-into-prs)
Turn issues into PRs
In an issue comment:
Copy
```
@claude implement this feature based on the issue description

```

Claude will analyze the issue, write the code, and create a PR for review.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#get-implementation-help)
Get implementation help
In a PR comment:
Copy
```
@claude how should I implement user authentication for this endpoint?

```

Claude will analyze your code and provide specific implementation guidance.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#fix-bugs-quickly)
Fix bugs quickly
In an issue:
Copy
```
@claude fix the TypeError in the user dashboard component

```

Claude will locate the bug, implement a fix, and create a PR.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#best-practices)
Best practices
### 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#claude-md-configuration)
CLAUDE.md configuration
Create a `CLAUDE.md` file in your repository root to define code style guidelines, review criteria, project-specific rules, and preferred patterns. This file guides Claude’s understanding of your project standards.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#security-considerations)
Security considerations
Never commit API keys directly to your repository!
Always use GitHub Secrets for API keys:
  * Add your API key as a repository secret named `ANTHROPIC_API_KEY`
  * Reference it in workflows: `anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}`
  * Limit action permissions to only what’s necessary
  * Review Claude’s suggestions before merging


Always use GitHub Secrets (e.g., `${{ secrets.ANTHROPIC_API_KEY }}`) rather than hardcoding API keys directly in your workflow files.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#optimizing-performance)
Optimizing performance
Use issue templates to provide context, keep your `CLAUDE.md` concise and focused, and configure appropriate timeouts for your workflows.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#ci-costs)
CI costs
When using Claude Code GitHub Actions, be aware of the associated costs:
**GitHub Actions costs:**
  * Claude Code runs on GitHub-hosted runners, which consume your GitHub Actions minutes
  * See [GitHub’s billing documentation](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions) for detailed pricing and minute limits


**API costs:**
  * Each Claude interaction consumes API tokens based on the length of prompts and responses
  * Token usage varies by task complexity and codebase size
  * See [Claude’s pricing page](https://www.anthropic.com/api) for current token rates


**Cost optimization tips:**
  * Use specific `@claude` commands to reduce unnecessary API calls
  * Configure appropriate `max_turns` limits to prevent excessive iterations
  * Set reasonable `timeout_minutes` to avoid runaway workflows
  * Consider using GitHub’s concurrency controls to limit parallel runs


## 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#configuration-examples)
Configuration examples
For ready-to-use workflow configurations for different use cases, including:
  * Basic workflow setup for issue and PR comments
  * Automated code reviews on pull requests
  * Custom implementations for specific needs


Visit the [examples directory](https://github.com/anthropics/claude-code-action/tree/main/examples) in the Claude Code Action repository.
The examples repository includes complete, tested workflows that you can copy directly into your `.github/workflows/` directory.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#using-with-aws-bedrock-%26-google-vertex-ai)
Using with AWS Bedrock & Google Vertex AI
For enterprise environments, you can use Claude Code GitHub Actions with your own cloud infrastructure. This approach gives you control over data residency and billing while maintaining the same functionality.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#prerequisites)
Prerequisites
Before setting up Claude Code GitHub Actions with cloud providers, you need:
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#for-google-cloud-vertex-ai%3A)
For Google Cloud Vertex AI:
  1. A Google Cloud Project with Vertex AI enabled
  2. Workload Identity Federation configured for GitHub Actions
  3. A service account with the required permissions
  4. A GitHub App (recommended) or use the default GITHUB_TOKEN


#### 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#for-aws-bedrock%3A)
For AWS Bedrock:
  1. An AWS account with Amazon Bedrock enabled
  2. GitHub OIDC Identity Provider configured in AWS
  3. An IAM role with Bedrock permissions
  4. A GitHub App (recommended) or use the default GITHUB_TOKEN


1
Create a custom GitHub App (Recommended for 3P Providers)
For best control and security when using 3P providers like Vertex AI or Bedrock, we recommend creating your own GitHub App:
  1. Go to <https://github.com/settings/apps/new>
  2. Fill in the basic information: 
     * **GitHub App name** : Choose a unique name (e.g., “YourOrg Claude Assistant”)
     * **Homepage URL** : Your organization’s website or the repository URL
  3. Configure the app settings: 
     * **Webhooks** : Uncheck “Active” (not needed for this integration)
  4. Set the required permissions: 
     * **Repository permissions** : 
       * Contents: Read & Write
       * Issues: Read & Write
       * Pull requests: Read & Write
  5. Click “Create GitHub App”
  6. After creation, click “Generate a private key” and save the downloaded `.pem` file
  7. Note your App ID from the app settings page
  8. Install the app to your repository: 
     * From your app’s settings page, click “Install App” in the left sidebar
     * Select your account or organization
     * Choose “Only select repositories” and select the specific repository
     * Click “Install”
  9. Add the private key as a secret to your repository: 
     * Go to your repository’s Settings → Secrets and variables → Actions
     * Create a new secret named `APP_PRIVATE_KEY` with the contents of the `.pem` file
  10. Add the App ID as a secret:


  * Create a new secret named `APP_ID` with your GitHub App’s ID


This app will be used with the [actions/create-github-app-token](https://github.com/actions/create-github-app-token) action to generate authentication tokens in your workflows.
**Alternative for Anthropic API or if you don’t want to setup your own Github app** : Use the official Anthropic app:
  1. Install from: <https://github.com/apps/claude>
  2. No additional configuration needed for authentication


2
Configure cloud provider authentication
Choose your cloud provider and set up secure authentication:
AWS Bedrock
**Configure AWS to allow GitHub Actions to authenticate securely without storing credentials.**
> **Security Note** : Use repository-specific configurations and grant only the minimum required permissions.
**Required Setup** :
  1. **Enable Amazon Bedrock** :
     * Request access to Claude models in Amazon Bedrock
     * For cross-region models, request access in all required regions
  2. **Set up GitHub OIDC Identity Provider** :
     * Provider URL: `https://token.actions.githubusercontent.com`
     * Audience: `sts.amazonaws.com`
  3. **Create IAM Role for GitHub Actions** :
     * Trusted entity type: Web identity
     * Identity provider: `token.actions.githubusercontent.com`
     * Permissions: `AmazonBedrockFullAccess` policy
     * Configure trust policy for your specific repository


**Required Values** :
After setup, you’ll need:
  * **AWS_ROLE_TO_ASSUME** : The ARN of the IAM role you created


OIDC is more secure than using static AWS access keys because credentials are temporary and automatically rotated.
See [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html) for detailed OIDC setup instructions.
Google Vertex AI
**Configure Google Cloud to allow GitHub Actions to authenticate securely without storing credentials.**
> **Security Note** : Use repository-specific configurations and grant only the minimum required permissions.
**Required Setup** :
  1. **Enable APIs** in your Google Cloud project:
     * IAM Credentials API
     * Security Token Service (STS) API
     * Vertex AI API
  2. **Create Workload Identity Federation resources** :
     * Create a Workload Identity Pool
     * Add a GitHub OIDC provider with: 
       * Issuer: `https://token.actions.githubusercontent.com`
       * Attribute mappings for repository and owner
       * **Security recommendation** : Use repository-specific attribute conditions
  3. **Create a Service Account** :
     * Grant only `Vertex AI User` role
     * **Security recommendation** : Create a dedicated service account per repository
  4. **Configure IAM bindings** :
     * Allow the Workload Identity Pool to impersonate the service account
     * **Security recommendation** : Use repository-specific principal sets


**Required Values** :
After setup, you’ll need:
  * **GCP_WORKLOAD_IDENTITY_PROVIDER** : The full provider resource name
  * **GCP_SERVICE_ACCOUNT** : The service account email address


Workload Identity Federation eliminates the need for downloadable service account keys, improving security.
For detailed setup instructions, consult the [Google Cloud Workload Identity Federation documentation](https://cloud.google.com/iam/docs/workload-identity-federation).
3
Add Required Secrets
Add the following secrets to your repository (Settings → Secrets and variables → Actions):
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#for-anthropic-api-direct-%3A)
For Anthropic API (Direct):
  1. **For API Authentication** :
     * `ANTHROPIC_API_KEY`: Your Anthropic API key from [console.anthropic.com](https://console.anthropic.com)
  2. **For GitHub App (if using your own app)** :
     * `APP_ID`: Your GitHub App’s ID
     * `APP_PRIVATE_KEY`: The private key (.pem) content


#### 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#for-google-cloud-vertex-ai)
For Google Cloud Vertex AI
  1. **For GCP Authentication** :
     * `GCP_WORKLOAD_IDENTITY_PROVIDER`
     * `GCP_SERVICE_ACCOUNT`
  2. **For GitHub App (if using your own app)** :
     * `APP_ID`: Your GitHub App’s ID
     * `APP_PRIVATE_KEY`: The private key (.pem) content


#### 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#for-aws-bedrock)
For AWS Bedrock
  1. **For AWS Authentication** :
     * `AWS_ROLE_TO_ASSUME`
  2. **For GitHub App (if using your own app)** :
     * `APP_ID`: Your GitHub App’s ID
     * `APP_PRIVATE_KEY`: The private key (.pem) content


4
Create workflow files
Create GitHub Actions workflow files that integrate with your cloud provider. The examples below show complete configurations for both AWS Bedrock and Google Vertex AI:
AWS Bedrock workflow
**Prerequisites:**
  * AWS Bedrock access enabled with Claude model permissions
  * GitHub configured as an OIDC identity provider in AWS
  * IAM role with Bedrock permissions that trusts GitHub Actions


**Required GitHub secrets:**
Secret Name | Description  
---|---  
`AWS_ROLE_TO_ASSUME` | ARN of the IAM role for Bedrock access  
`APP_ID` | Your GitHub App ID (from app settings)  
`APP_PRIVATE_KEY` | The private key you generated for your GitHub App  
Copy
```
name: Claude PR Action 

permissions:
  contents: write
  pull-requests: write
  issues: write
  id-token: write 

on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]
  issues:
    types: [opened, assigned]

jobs:
  claude-pr:
    if: |
      (github.event_name == 'issue_comment' && contains(github.event.comment.body, '@claude')) ||
      (github.event_name == 'pull_request_review_comment' && contains(github.event.comment.body, '@claude')) ||
      (github.event_name == 'issues' && contains(github.event.issue.body, '@claude'))
    runs-on: ubuntu-latest
    env:
      AWS_REGION: us-west-2
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Generate GitHub App token
        id: app-token
        uses: actions/create-github-app-token@v2
        with:
          app-id: ${{ secrets.APP_ID }}
          private-key: ${{ secrets.APP_PRIVATE_KEY }}

      - name: Configure AWS Credentials (OIDC)
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: ${{ secrets.AWS_ROLE_TO_ASSUME }}
          aws-region: us-west-2

      - uses: ./.github/actions/claude-pr-action
        with:
          trigger_phrase: "@claude"
          timeout_minutes: "60"
          github_token: ${{ steps.app-token.outputs.token }}
          use_bedrock: "true"
          model: "us.anthropic.claude-3-7-sonnet-20250219-v1:0"

```

The model ID format for Bedrock includes the region prefix (e.g., `us.anthropic.claude...`) and version suffix.
Google Vertex AI workflow
**Prerequisites:**
  * Vertex AI API enabled in your GCP project
  * Workload Identity Federation configured for GitHub
  * Service account with Vertex AI permissions


**Required GitHub secrets:**
Secret Name | Description  
---|---  
`GCP_WORKLOAD_IDENTITY_PROVIDER` | Workload identity provider resource name  
`GCP_SERVICE_ACCOUNT` | Service account email with Vertex AI access  
`APP_ID` | Your GitHub App ID (from app settings)  
`APP_PRIVATE_KEY` | The private key you generated for your GitHub App  
Copy
```
name: Claude PR Action

permissions:
  contents: write
  pull-requests: write
  issues: write
  id-token: write  

on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]
  issues:
    types: [opened, assigned]

jobs:
  claude-pr:
    if: |
      (github.event_name == 'issue_comment' && contains(github.event.comment.body, '@claude')) ||
      (github.event_name == 'pull_request_review_comment' && contains(github.event.comment.body, '@claude')) ||
      (github.event_name == 'issues' && contains(github.event.issue.body, '@claude'))
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Generate GitHub App token
        id: app-token
        uses: actions/create-github-app-token@v2
        with:
          app-id: ${{ secrets.APP_ID }}
          private-key: ${{ secrets.APP_PRIVATE_KEY }}

      - name: Authenticate to Google Cloud
        id: auth
        uses: google-github-actions/auth@v2
        with:
          workload_identity_provider: ${{ secrets.GCP_WORKLOAD_IDENTITY_PROVIDER }}
          service_account: ${{ secrets.GCP_SERVICE_ACCOUNT }}
      
      - uses: ./.github/actions/claude-pr-action
        with:
          trigger_phrase: "@claude"
          timeout_minutes: "60"
          github_token: ${{ steps.app-token.outputs.token }}
          use_vertex: "true"
          model: "claude-3-7-sonnet@20250219"
        env:
          ANTHROPIC_VERTEX_PROJECT_ID: ${{ steps.auth.outputs.project_id }}
          CLOUD_ML_REGION: us-east5
          VERTEX_REGION_CLAUDE_3_7_SONNET: us-east5

```

The project ID is automatically retrieved from the Google Cloud authentication step, so you don’t need to hardcode it.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#troubleshooting)
Troubleshooting
### 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#claude-not-responding-to-%40claude-commands)
Claude not responding to @claude commands
Verify the GitHub App is installed correctly, check that workflows are enabled, ensure API key is set in repository secrets, and confirm the comment contains `@claude` (not `/claude`).
### 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#ci-not-running-on-claude%E2%80%99s-commits)
CI not running on Claude’s commits
Ensure you’re using the GitHub App or custom app (not Actions user), check workflow triggers include the necessary events, and verify app permissions include CI triggers.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#authentication-errors)
Authentication errors
Confirm API key is valid and has sufficient permissions. For Bedrock/Vertex, check credentials configuration and ensure secrets are named correctly in workflows.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#advanced-configuration)
Advanced configuration
### 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#action-parameters)
Action parameters
The Claude Code Action supports these key parameters:
Parameter | Description | Required  
---|---|---  
`prompt` | The prompt to send to Claude | Yes*  
`prompt_file` | Path to file containing prompt | Yes*  
`anthropic_api_key` | Anthropic API key | Yes**  
`max_turns` | Maximum conversation turns | No  
`timeout_minutes` | Execution timeout | No  
*Either `prompt` or `prompt_file` required  
**Required for direct Anthropic API, not for Bedrock/Vertex
### 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#alternative-integration-methods)
Alternative integration methods
While the `/install-github-app` command is the recommended approach, you can also:
  * **Custom GitHub App** : For organizations needing branded usernames or custom authentication flows. Create your own GitHub App with required permissions (contents, issues, pull requests) and use the actions/create-github-app-token action to generate tokens in your workflows.
  * **Manual GitHub Actions** : Direct workflow configuration for maximum flexibility
  * **MCP Configuration** : Dynamic loading of Model Context Protocol servers


See the [Claude Code Action repository](https://github.com/anthropics/claude-code-action) for detailed documentation.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/github-actions#customizing-claude%E2%80%99s-behavior)
Customizing Claude’s behavior
You can configure Claude’s behavior in two ways:
  1. **CLAUDE.md** : Define coding standards, review criteria, and project-specific rules in a `CLAUDE.md` file at the root of your repository. Claude will follow these guidelines when creating PRs and responding to requests. Check out our [Memory documentation](https://docs.anthropic.com/en/docs/claude-code/memory) for more details.
  2. **Custom prompts** : Use the `prompt` parameter in the workflow file to provide workflow-specific instructions. This allows you to customize Claude’s behavior for different workflows or tasks.


Claude will follow these guidelines when creating PRs and responding to requests.
Was this page helpful?
YesNo
[Claude Code hooks](https://docs.anthropic.com/en/docs/claude-code/hooks-guide)[Model Context Protocol (MCP)](https://docs.anthropic.com/en/docs/claude-code/mcp)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Why use Claude Code GitHub Actions?](https://docs.anthropic.com/en/docs/claude-code/github-actions#why-use-claude-code-github-actions%3F)
  * [What can Claude do?](https://docs.anthropic.com/en/docs/claude-code/github-actions#what-can-claude-do%3F)
  * [Claude Code Action](https://docs.anthropic.com/en/docs/claude-code/github-actions#claude-code-action)
  * [Claude Code Action (Base)](https://docs.anthropic.com/en/docs/claude-code/github-actions#claude-code-action-base)
  * [Setup](https://docs.anthropic.com/en/docs/claude-code/github-actions#setup)
  * [Quick setup](https://docs.anthropic.com/en/docs/claude-code/github-actions#quick-setup)
  * [Manual setup](https://docs.anthropic.com/en/docs/claude-code/github-actions#manual-setup)
  * [Example use cases](https://docs.anthropic.com/en/docs/claude-code/github-actions#example-use-cases)
  * [Turn issues into PRs](https://docs.anthropic.com/en/docs/claude-code/github-actions#turn-issues-into-prs)
  * [Get implementation help](https://docs.anthropic.com/en/docs/claude-code/github-actions#get-implementation-help)
  * [Fix bugs quickly](https://docs.anthropic.com/en/docs/claude-code/github-actions#fix-bugs-quickly)
  * [Best practices](https://docs.anthropic.com/en/docs/claude-code/github-actions#best-practices)
  * [CLAUDE.md configuration](https://docs.anthropic.com/en/docs/claude-code/github-actions#claude-md-configuration)
  * [Security considerations](https://docs.anthropic.com/en/docs/claude-code/github-actions#security-considerations)
  * [Optimizing performance](https://docs.anthropic.com/en/docs/claude-code/github-actions#optimizing-performance)
  * [CI costs](https://docs.anthropic.com/en/docs/claude-code/github-actions#ci-costs)
  * [Configuration examples](https://docs.anthropic.com/en/docs/claude-code/github-actions#configuration-examples)
  * [Using with AWS Bedrock & Google Vertex AI](https://docs.anthropic.com/en/docs/claude-code/github-actions#using-with-aws-bedrock-%26-google-vertex-ai)
  * [Prerequisites](https://docs.anthropic.com/en/docs/claude-code/github-actions#prerequisites)
  * [For Google Cloud Vertex AI:](https://docs.anthropic.com/en/docs/claude-code/github-actions#for-google-cloud-vertex-ai%3A)
  * [For AWS Bedrock:](https://docs.anthropic.com/en/docs/claude-code/github-actions#for-aws-bedrock%3A)
  * [Troubleshooting](https://docs.anthropic.com/en/docs/claude-code/github-actions#troubleshooting)
  * [Claude not responding to @claude commands](https://docs.anthropic.com/en/docs/claude-code/github-actions#claude-not-responding-to-%40claude-commands)
  * [CI not running on Claude’s commits](https://docs.anthropic.com/en/docs/claude-code/github-actions#ci-not-running-on-claude%E2%80%99s-commits)
  * [Authentication errors](https://docs.anthropic.com/en/docs/claude-code/github-actions#authentication-errors)
  * [Advanced configuration](https://docs.anthropic.com/en/docs/claude-code/github-actions#advanced-configuration)
  * [Action parameters](https://docs.anthropic.com/en/docs/claude-code/github-actions#action-parameters)
  * [Alternative integration methods](https://docs.anthropic.com/en/docs/claude-code/github-actions#alternative-integration-methods)
  * [Customizing Claude’s behavior](https://docs.anthropic.com/en/docs/claude-code/github-actions#customizing-claude%E2%80%99s-behavior)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai -->

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
Claude Code on Google Vertex AI
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
# Claude Code on Google Vertex AI
Copy page
Learn about configuring Claude Code through Google Vertex AI, including setup, IAM configuration, and troubleshooting.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai#prerequisites)
Prerequisites
Before configuring Claude Code with Vertex AI, ensure you have:
  * A Google Cloud Platform (GCP) account with billing enabled
  * A GCP project with Vertex AI API enabled
  * Access to desired Claude models (e.g., Claude Sonnet 4)
  * Google Cloud SDK (`gcloud`) installed and configured
  * Quota allocated in desired GCP region


Vertex AI may not support the Claude Code default models on non-`us-east5` regions. Ensure you are using `us-east5` and have quota allocated, or switch to supported models.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai#setup)
Setup
### 
[​](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai#1-enable-vertex-ai-api)
1. Enable Vertex AI API
Enable the Vertex AI API in your GCP project:
Copy
```
# Set your project ID
gcloud config set project YOUR-PROJECT-ID

# Enable Vertex AI API
gcloud services enable aiplatform.googleapis.com

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai#2-request-model-access)
2. Request model access
Request access to Claude models in Vertex AI:
  1. Navigate to the [Vertex AI Model Garden](https://console.cloud.google.com/vertex-ai/model-garden)
  2. Search for “Claude” models
  3. Request access to desired Claude models (e.g., Claude Sonnet 4)
  4. Wait for approval (may take 24-48 hours)


### 
[​](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai#3-configure-gcp-credentials)
3. Configure GCP credentials
Claude Code uses standard Google Cloud authentication.
For more information, see [Google Cloud authentication documentation](https://cloud.google.com/docs/authentication).
### 
[​](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai#4-configure-claude-code)
4. Configure Claude Code
Set the following environment variables:
Copy
```
# Enable Vertex AI integration
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5
export ANTHROPIC_VERTEX_PROJECT_ID=YOUR-PROJECT-ID

# Optional: Disable prompt caching if needed
export DISABLE_PROMPT_CACHING=1

# Optional: Override regions for specific models
export VERTEX_REGION_CLAUDE_3_5_HAIKU=us-central1
export VERTEX_REGION_CLAUDE_3_5_SONNET=us-east5
export VERTEX_REGION_CLAUDE_3_7_SONNET=us-east5
export VERTEX_REGION_CLAUDE_4_0_OPUS=europe-west4
export VERTEX_REGION_CLAUDE_4_0_SONNET=us-east5
export VERTEX_REGION_CLAUDE_4_1_OPUS=europe-west4

```

[Prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) is automatically supported when you specify the `cache_control` ephemeral flag. To disable it, set `DISABLE_PROMPT_CACHING=1`. For heightened rate limits, contact Google Cloud support.
When using Vertex AI, the `/login` and `/logout` commands are disabled since authentication is handled through Google Cloud credentials.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai#5-model-configuration)
5. Model configuration
Claude Code uses these default models for Vertex AI:
Model type | Default value  
---|---  
Primary model | `claude-sonnet-4@20250514`  
Small/fast model | `claude-3-5-haiku@20241022`  
To customize models:
Copy
```
export ANTHROPIC_MODEL='claude-opus-4-1@20250805'
export ANTHROPIC_SMALL_FAST_MODEL='claude-3-5-haiku@20241022'

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai#iam-configuration)
IAM configuration
Assign the required IAM permissions:
The `roles/aiplatform.user` role includes the required permissions:
  * `aiplatform.endpoints.predict` - Required for model invocation
  * `aiplatform.endpoints.computeTokens` - Required for token counting


For more restrictive permissions, create a custom role with only the permissions above.
For details, see [Vertex IAM documentation](https://cloud.google.com/vertex-ai/docs/general/access-control).
We recommend creating a dedicated GCP project for Claude Code to simplify cost tracking and access control.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai#troubleshooting)
Troubleshooting
If you encounter quota issues:
  * Check current quotas or request quota increase through [Cloud Console](https://cloud.google.com/docs/quotas/view-manage)


If you encounter “model not found” 404 errors:
  * Verify you have access to the specified region
  * Confirm model is Enabled in [Model Garden](https://console.cloud.google.com/vertex-ai/model-garden)


If you encounter 429 errors:
  * Ensure the primary model and small/fast model are supported in your selected region


## 
[​](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai#additional-resources)
Additional resources
  * [Vertex AI documentation](https://cloud.google.com/vertex-ai/docs)
  * [Vertex AI pricing](https://cloud.google.com/vertex-ai/pricing)
  * [Vertex AI quotas and limits](https://cloud.google.com/vertex-ai/docs/quotas)


Was this page helpful?
YesNo
[Amazon Bedrock](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock)[Corporate proxy](https://docs.anthropic.com/en/docs/claude-code/corporate-proxy)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Prerequisites](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai#prerequisites)
  * [Setup](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai#setup)
  * [1. Enable Vertex AI API](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai#1-enable-vertex-ai-api)
  * [2. Request model access](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai#2-request-model-access)
  * [3. Configure GCP credentials](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai#3-configure-gcp-credentials)
  * [4. Configure Claude Code](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai#4-configure-claude-code)
  * [5. Model configuration](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai#5-model-configuration)
  * [IAM configuration](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai#iam-configuration)
  * [Troubleshooting](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai#troubleshooting)
  * [Additional resources](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai#additional-resources)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/hooks-guide -->

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
Get started with Claude Code hooks
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
# Get started with Claude Code hooks
Copy page
Learn how to customize and extend Claude Code’s behavior by registering shell commands
Claude Code hooks are user-defined shell commands that execute at various points in Claude Code’s lifecycle. Hooks provide deterministic control over Claude Code’s behavior, ensuring certain actions always happen rather than relying on the LLM to choose to run them.
For reference documentation on hooks, see [Hooks reference](https://docs.anthropic.com/en/docs/claude-code/hooks).
Example use cases for hooks include:
  * **Notifications** : Customize how you get notified when Claude Code is awaiting your input or permission to run something.
  * **Automatic formatting** : Run `prettier` on .ts files, `gofmt` on .go files, etc. after every file edit.
  * **Logging** : Track and count all executed commands for compliance or debugging.
  * **Feedback** : Provide automated feedback when Claude Code produces code that does not follow your codebase conventions.
  * **Custom permissions** : Block modifications to production files or sensitive directories.


By encoding these rules as hooks rather than prompting instructions, you turn suggestions into app-level code that executes every time it is expected to run.
You must consider the security implication of hooks as you add them, because hooks run automatically during the agent loop with your current environment’s credentials. For example, malicious hooks code can exfiltrate your data. Always review your hooks implementation before registering them.
For full security best practices, see [Security Considerations](https://docs.anthropic.com/en/docs/claude-code/hooks#security-considerations) in the hooks reference documentation.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#hook-events-overview)
Hook Events Overview
Claude Code provides several hook events that run at different points in the workflow:
  * **PreToolUse** : Runs before tool calls (can block them)
  * **PostToolUse** : Runs after tool calls complete
  * **UserPromptSubmit** : Runs when the user submits a prompt, before Claude processes it
  * **Notification** : Runs when Claude Code sends notifications
  * **Stop** : Runs when Claude Code finishes responding
  * **Subagent Stop** : Runs when subagent tasks complete
  * **PreCompact** : Runs before Claude Code is about to run a compact operation
  * **SessionStart** : Runs when Claude Code starts a new session or resumes an existing session


Each event receives different data and can control Claude’s behavior in different ways.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#quickstart)
Quickstart
In this quickstart, you’ll add a hook that logs the shell commands that Claude Code runs.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#prerequisites)
Prerequisites
Install `jq` for JSON processing in the command line.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#step-1%3A-open-hooks-configuration)
Step 1: Open hooks configuration
Run the `/hooks` [slash command](https://docs.anthropic.com/en/docs/claude-code/slash-commands) and select the `PreToolUse` hook event.
`PreToolUse` hooks run before tool calls and can block them while providing Claude feedback on what to do differently.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#step-2%3A-add-a-matcher)
Step 2: Add a matcher
Select `+ Add new matcher…` to run your hook only on Bash tool calls.
Type `Bash` for the matcher.
You can use `*` to match all tools.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#step-3%3A-add-the-hook)
Step 3: Add the hook
Select `+ Add new hook…` and enter this command:
Copy
```
jq -r '"\(.tool_input.command) - \(.tool_input.description // "No description")"' >> ~/.claude/bash-command-log.txt

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#step-4%3A-save-your-configuration)
Step 4: Save your configuration
For storage location, select `User settings` since you’re logging to your home directory. This hook will then apply to all projects, not just your current project.
Then press Esc until you return to the REPL. Your hook is now registered!
### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#step-5%3A-verify-your-hook)
Step 5: Verify your hook
Run `/hooks` again or check `~/.claude/settings.json` to see your configuration:
Copy
```
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '\"\\(.tool_input.command) - \\(.tool_input.description // \"No description\")\"' >> ~/.claude/bash-command-log.txt"
          }
        ]
      }
    ]
  }
}

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#step-6%3A-test-your-hook)
Step 6: Test your hook
Ask Claude to run a simple command like `ls` and check your log file:
Copy
```
cat ~/.claude/bash-command-log.txt

```

You should see entries like:
Copy
```
ls - Lists files and directories

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#more-examples)
More Examples
For a complete example implementation, see the [bash command validator example](https://github.com/anthropics/claude-code/blob/main/examples/hooks/bash_command_validator_example.py) in our public codebase.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#code-formatting-hook)
Code Formatting Hook
Automatically format TypeScript files after editing:
Copy
```
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|MultiEdit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | { read file_path; if echo \"$file_path\" | grep -q '\\.ts$'; then npx prettier --write \"$file_path\"; fi; }"
          }
        ]
      }
    ]
  }
}

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#markdown-formatting-hook)
Markdown Formatting Hook
Automatically fix missing language tags and formatting issues in markdown files:
Copy
```
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|MultiEdit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/markdown_formatter.py"
          }
        ]
      }
    ]
  }
}

```

Create `.claude/hooks/markdown_formatter.py` with this content:
Copy
```
#!/usr/bin/env python3
"""
Markdown formatter for Claude Code output.
Fixes missing language tags and spacing issues while preserving code content.
"""
import json
import sys
import re
import os

def detect_language(code):
    """Best-effort language detection from code content."""
    s = code.strip()
    
    # JSON detection
    if re.search(r'^\s*[{\[]', s):
        try:
            json.loads(s)
            return 'json'
        except:
            pass
    
    # Python detection
    if re.search(r'^\s*def\s+\w+\s*\(', s, re.M) or \
       re.search(r'^\s*(import|from)\s+\w+', s, re.M):
        return 'python'
    
    # JavaScript detection  
    if re.search(r'\b(function\s+\w+\s*\(|const\s+\w+\s*=)', s) or \
       re.search(r'=>|console\.(log|error)', s):
        return 'javascript'
    
    # Bash detection
    if re.search(r'^#!.*\b(bash|sh)\b', s, re.M) or \
       re.search(r'\b(if|then|fi|for|in|do|done)\b', s):
        return 'bash'
    
    # SQL detection
    if re.search(r'\b(SELECT|INSERT|UPDATE|DELETE|CREATE)\s+', s, re.I):
        return 'sql'
        
    return 'text'

def format_markdown(content):
    """Format markdown content with language detection."""
    # Fix unlabeled code fences
    def add_lang_to_fence(match):
        indent, info, body, closing = match.groups()
        if not info.strip():
            lang = detect_language(body)
            return f"{indent}```{lang}\n{body}{closing}\n"
        return match.group(0)
    
    fence_pattern = r'(?ms)^([ \t]{0,3})```([^\n]*)\n(.*?)(\n\1```)\s*$'
    content = re.sub(fence_pattern, add_lang_to_fence, content)
    
    # Fix excessive blank lines (only outside code fences)
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content.rstrip() + '\n'

# Main execution
try:
    input_data = json.load(sys.stdin)
    file_path = input_data.get('tool_input', {}).get('file_path', '')
    
    if not file_path.endswith(('.md', '.mdx')):
        sys.exit(0)  # Not a markdown file
    
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        formatted = format_markdown(content)
        
        if formatted != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(formatted)
            print(f"✓ Fixed markdown formatting in {file_path}")
    
except Exception as e:
    print(f"Error formatting markdown: {e}", file=sys.stderr)
    sys.exit(1)

```

Make the script executable:
Copy
```
chmod +x .claude/hooks/markdown_formatter.py

```

This hook automatically:
  * Detects programming languages in unlabeled code blocks
  * Adds appropriate language tags for syntax highlighting
  * Fixes excessive blank lines while preserving code content
  * Only processes markdown files (`.md`, `.mdx`)


### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#custom-notification-hook)
Custom Notification Hook
Get desktop notifications when Claude needs input:
Copy
```
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "notify-send 'Claude Code' 'Awaiting your input'"
          }
        ]
      }
    ]
  }
}

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#file-protection-hook)
File Protection Hook
Block edits to sensitive files:
Copy
```
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|MultiEdit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3 -c \"import json, sys; data=json.load(sys.stdin); path=data.get('tool_input',{}).get('file_path',''); sys.exit(2 if any(p in path for p in ['.env', 'package-lock.json', '.git/']) else 0)\""
          }
        ]
      }
    ]
  }
}

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#learn-more)
Learn more
  * For reference documentation on hooks, see [Hooks reference](https://docs.anthropic.com/en/docs/claude-code/hooks).
  * For comprehensive security best practices and safety guidelines, see [Security Considerations](https://docs.anthropic.com/en/docs/claude-code/hooks#security-considerations) in the hooks reference documentation.
  * For troubleshooting steps and debugging techniques, see [Debugging](https://docs.anthropic.com/en/docs/claude-code/hooks#debugging) in the hooks reference documentation.


Was this page helpful?
YesNo
[Output styles](https://docs.anthropic.com/en/docs/claude-code/output-styles)[GitHub Actions](https://docs.anthropic.com/en/docs/claude-code/github-actions)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Hook Events Overview](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#hook-events-overview)
  * [Quickstart](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#quickstart)
  * [Prerequisites](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#prerequisites)
  * [Step 1: Open hooks configuration](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#step-1%3A-open-hooks-configuration)
  * [Step 2: Add a matcher](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#step-2%3A-add-a-matcher)
  * [Step 3: Add the hook](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#step-3%3A-add-the-hook)
  * [Step 4: Save your configuration](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#step-4%3A-save-your-configuration)
  * [Step 5: Verify your hook](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#step-5%3A-verify-your-hook)
  * [Step 6: Test your hook](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#step-6%3A-test-your-hook)
  * [More Examples](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#more-examples)
  * [Code Formatting Hook](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#code-formatting-hook)
  * [Markdown Formatting Hook](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#markdown-formatting-hook)
  * [Custom Notification Hook](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#custom-notification-hook)
  * [File Protection Hook](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#file-protection-hook)
  * [Learn more](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#learn-more)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/hooks -->

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
Hooks reference
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
# Hooks reference
Copy page
This page provides reference documentation for implementing hooks in Claude Code.
For a quickstart guide with examples, see [Get started with Claude Code hooks](https://docs.anthropic.com/en/docs/claude-code/hooks-guide).
## 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#configuration)
Configuration
Claude Code hooks are configured in your [settings files](https://docs.anthropic.com/en/docs/claude-code/settings):
  * `~/.claude/settings.json` - User settings
  * `.claude/settings.json` - Project settings
  * `.claude/settings.local.json` - Local project settings (not committed)
  * Enterprise managed policy settings


### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#structure)
Structure
Hooks are organized by matchers, where each matcher can have multiple hooks:
Copy
```
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "your-command-here"
          }
        ]
      }
    ]
  }
}

```

  * **matcher** : Pattern to match tool names, case-sensitive (only applicable for `PreToolUse` and `PostToolUse`) 
    * Simple strings match exactly: `Write` matches only the Write tool
    * Supports regex: `Edit|Write` or `Notebook.*`
    * Use `*` to match all tools. You can also use empty string (`""`) or leave `matcher` blank.
  * **hooks** : Array of commands to execute when the pattern matches 
    * `type`: Currently only `"command"` is supported
    * `command`: The bash command to execute (can use `$CLAUDE_PROJECT_DIR` environment variable)
    * `timeout`: (Optional) How long a command should run, in seconds, before canceling that specific command.


For events like `UserPromptSubmit`, `Notification`, `Stop`, and `SubagentStop` that don’t use matchers, you can omit the matcher field:
Copy
```
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/prompt-validator.py"
          }
        ]
      }
    ]
  }
}

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#project-specific-hook-scripts)
Project-Specific Hook Scripts
You can use the environment variable `CLAUDE_PROJECT_DIR` (only available when Claude Code spawns the hook command) to reference scripts stored in your project, ensuring they work regardless of Claude’s current directory:
Copy
```
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/check-style.sh"
          }
        ]
      }
    ]
  }
}

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#hook-events)
Hook Events
### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#pretooluse)
PreToolUse
Runs after Claude creates tool parameters and before processing the tool call.
**Common matchers:**
  * `Task` - Subagent tasks (see [subagents documentation](https://docs.anthropic.com/en/docs/claude-code/sub-agents))
  * `Bash` - Shell commands
  * `Glob` - File pattern matching
  * `Grep` - Content search
  * `Read` - File reading
  * `Edit`, `MultiEdit` - File editing
  * `Write` - File writing
  * `WebFetch`, `WebSearch` - Web operations


### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#posttooluse)
PostToolUse
Runs immediately after a tool completes successfully.
Recognizes the same matcher values as PreToolUse.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#notification)
Notification
Runs when Claude Code sends notifications. Notifications are sent when:
  1. Claude needs your permission to use a tool. Example: “Claude needs your permission to use Bash”
  2. The prompt input has been idle for at least 60 seconds. “Claude is waiting for your input”


### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#userpromptsubmit)
UserPromptSubmit
Runs when the user submits a prompt, before Claude processes it. This allows you to add additional context based on the prompt/conversation, validate prompts, or block certain types of prompts.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#stop)
Stop
Runs when the main Claude Code agent has finished responding. Does not run if the stoppage occurred due to a user interrupt.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#subagentstop)
SubagentStop
Runs when a Claude Code subagent (Task tool call) has finished responding.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#precompact)
PreCompact
Runs before Claude Code is about to run a compact operation.
**Matchers:**
  * `manual` - Invoked from `/compact`
  * `auto` - Invoked from auto-compact (due to full context window)


### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#sessionstart)
SessionStart
Runs when Claude Code starts a new session or resumes an existing session (which currently does start a new session under the hood). Useful for loading in development context like existing issues or recent changes to your codebase.
**Matchers:**
  * `startup` - Invoked from startup
  * `resume` - Invoked from `--resume`, `--continue`, or `/resume`
  * `clear` - Invoked from `/clear`


## 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#hook-input)
Hook Input
Hooks receive JSON data via stdin containing session information and event-specific data:
Copy
```
{
  // Common fields
  session_id: string
  transcript_path: string  // Path to conversation JSON
  cwd: string              // The current working directory when the hook is invoked

  // Event-specific fields
  hook_event_name: string
  ...
}

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#pretooluse-input)
PreToolUse Input
The exact schema for `tool_input` depends on the tool.
Copy
```
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "hook_event_name": "PreToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/path/to/file.txt",
    "content": "file content"
  }
}

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#posttooluse-input)
PostToolUse Input
The exact schema for `tool_input` and `tool_response` depends on the tool.
Copy
```
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "hook_event_name": "PostToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/path/to/file.txt",
    "content": "file content"
  },
  "tool_response": {
    "filePath": "/path/to/file.txt",
    "success": true
  }
}

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#notification-input)
Notification Input
Copy
```
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "hook_event_name": "Notification",
  "message": "Task completed successfully"
}

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#userpromptsubmit-input)
UserPromptSubmit Input
Copy
```
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "hook_event_name": "UserPromptSubmit",
  "prompt": "Write a function to calculate the factorial of a number"
}

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#stop-and-subagentstop-input)
Stop and SubagentStop Input
`stop_hook_active` is true when Claude Code is already continuing as a result of a stop hook. Check this value or process the transcript to prevent Claude Code from running indefinitely.
Copy
```
{
  "session_id": "abc123",
  "transcript_path": "~/.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "hook_event_name": "Stop",
  "stop_hook_active": true
}

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#precompact-input)
PreCompact Input
For `manual`, `custom_instructions` comes from what the user passes into `/compact`. For `auto`, `custom_instructions` is empty.
Copy
```
{
  "session_id": "abc123",
  "transcript_path": "~/.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "hook_event_name": "PreCompact",
  "trigger": "manual",
  "custom_instructions": ""
}

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#sessionstart-input)
SessionStart Input
Copy
```
{
  "session_id": "abc123",
  "transcript_path": "~/.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "hook_event_name": "SessionStart",
  "source": "startup"
}

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#hook-output)
Hook Output
There are two ways for hooks to return output back to Claude Code. The output communicates whether to block and any feedback that should be shown to Claude and the user.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#simple%3A-exit-code)
Simple: Exit Code
Hooks communicate status through exit codes, stdout, and stderr:
  * **Exit code 0** : Success. `stdout` is shown to the user in transcript mode (CTRL-R), except for `UserPromptSubmit` and `SessionStart`, where stdout is added to the context.
  * **Exit code 2** : Blocking error. `stderr` is fed back to Claude to process automatically. See per-hook-event behavior below.
  * **Other exit codes** : Non-blocking error. `stderr` is shown to the user and execution continues.


Reminder: Claude Code does not see stdout if the exit code is 0, except for the `UserPromptSubmit` hook where stdout is injected as context.
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#exit-code-2-behavior)
Exit Code 2 Behavior
Hook Event | Behavior  
---|---  
`PreToolUse` | Blocks the tool call, shows stderr to Claude  
`PostToolUse` | Shows stderr to Claude (tool already ran)  
`Notification` | N/A, shows stderr to user only  
`UserPromptSubmit` | Blocks prompt processing, erases prompt, shows stderr to user only  
`Stop` | Blocks stoppage, shows stderr to Claude  
`SubagentStop` | Blocks stoppage, shows stderr to Claude subagent  
`PreCompact` | N/A, shows stderr to user only  
`SessionStart` | N/A, shows stderr to user only  
### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#advanced%3A-json-output)
Advanced: JSON Output
Hooks can return structured JSON in `stdout` for more sophisticated control:
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#common-json-fields)
Common JSON Fields
All hook types can include these optional fields:
Copy
```
{
  "continue": true, // Whether Claude should continue after hook execution (default: true)
  "stopReason": "string" // Message shown when continue is false
  "suppressOutput": true, // Hide stdout from transcript mode (default: false)
}

```

If `continue` is false, Claude stops processing after the hooks run.
  * For `PreToolUse`, this is different from `"permissionDecision": "deny"`, which only blocks a specific tool call and provides automatic feedback to Claude.
  * For `PostToolUse`, this is different from `"decision": "block"`, which provides automated feedback to Claude.
  * For `UserPromptSubmit`, this prevents the prompt from being processed.
  * For `Stop` and `SubagentStop`, this takes precedence over any `"decision": "block"` output.
  * In all cases, `"continue" = false` takes precedence over any `"decision": "block"` output.


`stopReason` accompanies `continue` with a reason shown to the user, not shown to Claude.
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#pretooluse-decision-control)
`PreToolUse` Decision Control
`PreToolUse` hooks can control whether a tool call proceeds.
  * `"allow"` bypasses the permission system. `permissionDecisionReason` is shown to the user but not to Claude. (_Deprecated`"approve"` value + `reason` has the same behavior._)
  * `"deny"` prevents the tool call from executing. `permissionDecisionReason` is shown to Claude. (_`"block"`value +`reason` has the same behavior._)
  * `"ask"` asks the user to confirm the tool call in the UI. `permissionDecisionReason` is shown to the user but not to Claude.


Copy
```
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow" | "deny" | "ask",
    "permissionDecisionReason": "My reason here (shown to user)"
  },
  "decision": "approve" | "block" | undefined, // Deprecated for PreToolUse but still supported
  "reason": "Explanation for decision" // Deprecated for PreToolUse but still supported
}

```

#### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#posttooluse-decision-control)
`PostToolUse` Decision Control
`PostToolUse` hooks can control whether a tool call proceeds.
  * `"block"` automatically prompts Claude with `reason`.
  * `undefined` does nothing. `reason` is ignored.


Copy
```
{
  "decision": "block" | undefined,
  "reason": "Explanation for decision"
}

```

#### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#userpromptsubmit-decision-control)
`UserPromptSubmit` Decision Control
`UserPromptSubmit` hooks can control whether a user prompt is processed.
  * `"block"` prevents the prompt from being processed. The submitted prompt is erased from context. `"reason"` is shown to the user but not added to context.
  * `undefined` allows the prompt to proceed normally. `"reason"` is ignored.
  * `"hookSpecificOutput.additionalContext"` adds the string to the context if not blocked.


Copy
```
{
  "decision": "block" | undefined,
  "reason": "Explanation for decision",
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "My additional context here"
  }
}

```

#### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#stop%2Fsubagentstop-decision-control)
`Stop`/`SubagentStop` Decision Control
`Stop` and `SubagentStop` hooks can control whether Claude must continue.
  * `"block"` prevents Claude from stopping. You must populate `reason` for Claude to know how to proceed.
  * `undefined` allows Claude to stop. `reason` is ignored.


Copy
```
{
  "decision": "block" | undefined,
  "reason": "Must be provided when Claude is blocked from stopping"
}

```

#### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#sessionstart-decision-control)
`SessionStart` Decision Control
`SessionStart` hooks allow you to load in context at the start of a session.
  * `"hookSpecificOutput.additionalContext"` adds the string to the context.


Copy
```
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "My additional context here"
  }
}

```

#### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#exit-code-example%3A-bash-command-validation)
Exit Code Example: Bash Command Validation
Copy
```
#!/usr/bin/env python3
import json
import re
import sys

# Define validation rules as a list of (regex pattern, message) tuples
VALIDATION_RULES = [
    (
        r"\bgrep\b(?!.*\|)",
        "Use 'rg' (ripgrep) instead of 'grep' for better performance and features",
    ),
    (
        r"\bfind\s+\S+\s+-name\b",
        "Use 'rg --files | rg pattern' or 'rg --files -g pattern' instead of 'find -name' for better performance",
    ),
]


def validate_command(command: str) -> list[str]:
    issues = []
    for pattern, message in VALIDATION_RULES:
        if re.search(pattern, command):
            issues.append(message)
    return issues


try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
    sys.exit(1)

tool_name = input_data.get("tool_name", "")
tool_input = input_data.get("tool_input", {})
command = tool_input.get("command", "")

if tool_name != "Bash" or not command:
    sys.exit(1)

# Validate the command
issues = validate_command(command)

if issues:
    for message in issues:
        print(f"• {message}", file=sys.stderr)
    # Exit code 2 blocks tool call and shows stderr to Claude
    sys.exit(2)

```

#### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#json-output-example%3A-userpromptsubmit-to-add-context-and-validation)
JSON Output Example: UserPromptSubmit to Add Context and Validation
For `UserPromptSubmit` hooks, you can inject context using either method:
  * Exit code 0 with stdout: Claude sees the context (special case for `UserPromptSubmit`)
  * JSON output: Provides more control over the behavior


Copy
```
#!/usr/bin/env python3
import json
import sys
import re
import datetime

# Load input from stdin
try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
    sys.exit(1)

prompt = input_data.get("prompt", "")

# Check for sensitive patterns
sensitive_patterns = [
    (r"(?i)\b(password|secret|key|token)\s*[:=]", "Prompt contains potential secrets"),
]

for pattern, message in sensitive_patterns:
    if re.search(pattern, prompt):
        # Use JSON output to block with a specific reason
        output = {
            "decision": "block",
            "reason": f"Security policy violation: {message}. Please rephrase your request without sensitive information."
        }
        print(json.dumps(output))
        sys.exit(0)

# Add current time to context
context = f"Current time: {datetime.datetime.now()}"
print(context)

"""
The following is also equivalent:
print(json.dumps({
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": context,
  },
}))
"""

# Allow the prompt to proceed with the additional context
sys.exit(0)

```

#### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#json-output-example%3A-pretooluse-with-approval)
JSON Output Example: PreToolUse with Approval
Copy
```
#!/usr/bin/env python3
import json
import sys

# Load input from stdin
try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
    sys.exit(1)

tool_name = input_data.get("tool_name", "")
tool_input = input_data.get("tool_input", {})

# Example: Auto-approve file reads for documentation files
if tool_name == "Read":
    file_path = tool_input.get("file_path", "")
    if file_path.endswith((".md", ".mdx", ".txt", ".json")):
        # Use JSON output to auto-approve the tool call
        output = {
            "decision": "approve",
            "reason": "Documentation file auto-approved",
            "suppressOutput": True  # Don't show in transcript mode
        }
        print(json.dumps(output))
        sys.exit(0)

# For other cases, let the normal permission flow proceed
sys.exit(0)

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#working-with-mcp-tools)
Working with MCP Tools
Claude Code hooks work seamlessly with [Model Context Protocol (MCP) tools](https://docs.anthropic.com/en/docs/claude-code/mcp). When MCP servers provide tools, they appear with a special naming pattern that you can match in your hooks.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#mcp-tool-naming)
MCP Tool Naming
MCP tools follow the pattern `mcp__<server>__<tool>`, for example:
  * `mcp__memory__create_entities` - Memory server’s create entities tool
  * `mcp__filesystem__read_file` - Filesystem server’s read file tool
  * `mcp__github__search_repositories` - GitHub server’s search tool


### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#configuring-hooks-for-mcp-tools)
Configuring Hooks for MCP Tools
You can target specific MCP tools or entire MCP servers:
Copy
```
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__memory__.*",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Memory operation initiated' >> ~/mcp-operations.log"
          }
        ]
      },
      {
        "matcher": "mcp__.*__write.*",
        "hooks": [
          {
            "type": "command",
            "command": "/home/user/scripts/validate-mcp-write.py"
          }
        ]
      }
    ]
  }
}

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#examples)
Examples
For practical examples including code formatting, notifications, and file protection, see [More Examples](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#more-examples) in the get started guide.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#security-considerations)
Security Considerations
### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#disclaimer)
Disclaimer
**USE AT YOUR OWN RISK** : Claude Code hooks execute arbitrary shell commands on your system automatically. By using hooks, you acknowledge that:
  * You are solely responsible for the commands you configure
  * Hooks can modify, delete, or access any files your user account can access
  * Malicious or poorly written hooks can cause data loss or system damage
  * Anthropic provides no warranty and assumes no liability for any damages resulting from hook usage
  * You should thoroughly test hooks in a safe environment before production use


Always review and understand any hook commands before adding them to your configuration.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#security-best-practices)
Security Best Practices
Here are some key practices for writing more secure hooks:
  1. **Validate and sanitize inputs** - Never trust input data blindly
  2. **Always quote shell variables** - Use `"$VAR"` not `$VAR`
  3. **Block path traversal** - Check for `..` in file paths
  4. **Use absolute paths** - Specify full paths for scripts (use `$CLAUDE_PROJECT_DIR` for the project path)
  5. **Skip sensitive files** - Avoid `.env`, `.git/`, keys, etc.


### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#configuration-safety)
Configuration Safety
Direct edits to hooks in settings files don’t take effect immediately. Claude Code:
  1. Captures a snapshot of hooks at startup
  2. Uses this snapshot throughout the session
  3. Warns if hooks are modified externally
  4. Requires review in `/hooks` menu for changes to apply


This prevents malicious hook modifications from affecting your current session.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#hook-execution-details)
Hook Execution Details
  * **Timeout** : 60-second execution limit by default, configurable per command. 
    * A timeout for an individual command does not affect the other commands.
  * **Parallelization** : All matching hooks run in parallel
  * **Environment** : Runs in current directory with Claude Code’s environment 
    * The `CLAUDE_PROJECT_DIR` environment variable is available and contains the absolute path to the project root directory
  * **Input** : JSON via stdin
  * **Output** : 
    * PreToolUse/PostToolUse/Stop: Progress shown in transcript (Ctrl-R)
    * Notification: Logged to debug only (`--debug`)


## 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#debugging)
Debugging
### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#basic-troubleshooting)
Basic Troubleshooting
If your hooks aren’t working:
  1. **Check configuration** - Run `/hooks` to see if your hook is registered
  2. **Verify syntax** - Ensure your JSON settings are valid
  3. **Test commands** - Run hook commands manually first
  4. **Check permissions** - Make sure scripts are executable
  5. **Review logs** - Use `claude --debug` to see hook execution details


Common issues:
  * **Quotes not escaped** - Use `\"` inside JSON strings
  * **Wrong matcher** - Check tool names match exactly (case-sensitive)
  * **Command not found** - Use full paths for scripts


### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#advanced-debugging)
Advanced Debugging
For complex hook issues:
  1. **Inspect hook execution** - Use `claude --debug` to see detailed hook execution
  2. **Validate JSON schemas** - Test hook input/output with external tools
  3. **Check environment variables** - Verify Claude Code’s environment is correct
  4. **Test edge cases** - Try hooks with unusual file paths or inputs
  5. **Monitor system resources** - Check for resource exhaustion during hook execution
  6. **Use structured logging** - Implement logging in your hook scripts


### 
[​](https://docs.anthropic.com/en/docs/claude-code/hooks#debug-output-example)
Debug Output Example
Use `claude --debug` to see hook execution details:
Copy
```
[DEBUG] Executing hooks for PostToolUse:Write
[DEBUG] Getting matching hook commands for PostToolUse with query: Write
[DEBUG] Found 1 hook matchers in settings
[DEBUG] Matched 1 hooks for query "Write"
[DEBUG] Found 1 hook commands to execute
[DEBUG] Executing hook command: <Your command> with timeout 60000ms
[DEBUG] Hook command completed with status 0: <Your stdout>

```

Progress messages appear in transcript mode (Ctrl-R) showing:
  * Which hook is running
  * Command being executed
  * Success/failure status
  * Output or error messages


Was this page helpful?
YesNo
[Slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands)[Legal and compliance](https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Configuration](https://docs.anthropic.com/en/docs/claude-code/hooks#configuration)
  * [Structure](https://docs.anthropic.com/en/docs/claude-code/hooks#structure)
  * [Project-Specific Hook Scripts](https://docs.anthropic.com/en/docs/claude-code/hooks#project-specific-hook-scripts)
  * [Hook Events](https://docs.anthropic.com/en/docs/claude-code/hooks#hook-events)
  * [PreToolUse](https://docs.anthropic.com/en/docs/claude-code/hooks#pretooluse)
  * [PostToolUse](https://docs.anthropic.com/en/docs/claude-code/hooks#posttooluse)
  * [Notification](https://docs.anthropic.com/en/docs/claude-code/hooks#notification)
  * [UserPromptSubmit](https://docs.anthropic.com/en/docs/claude-code/hooks#userpromptsubmit)
  * [Stop](https://docs.anthropic.com/en/docs/claude-code/hooks#stop)
  * [SubagentStop](https://docs.anthropic.com/en/docs/claude-code/hooks#subagentstop)
  * [PreCompact](https://docs.anthropic.com/en/docs/claude-code/hooks#precompact)
  * [SessionStart](https://docs.anthropic.com/en/docs/claude-code/hooks#sessionstart)
  * [Hook Input](https://docs.anthropic.com/en/docs/claude-code/hooks#hook-input)
  * [PreToolUse Input](https://docs.anthropic.com/en/docs/claude-code/hooks#pretooluse-input)
  * [PostToolUse Input](https://docs.anthropic.com/en/docs/claude-code/hooks#posttooluse-input)
  * [Notification Input](https://docs.anthropic.com/en/docs/claude-code/hooks#notification-input)
  * [UserPromptSubmit Input](https://docs.anthropic.com/en/docs/claude-code/hooks#userpromptsubmit-input)
  * [Stop and SubagentStop Input](https://docs.anthropic.com/en/docs/claude-code/hooks#stop-and-subagentstop-input)
  * [PreCompact Input](https://docs.anthropic.com/en/docs/claude-code/hooks#precompact-input)
  * [SessionStart Input](https://docs.anthropic.com/en/docs/claude-code/hooks#sessionstart-input)
  * [Hook Output](https://docs.anthropic.com/en/docs/claude-code/hooks#hook-output)
  * [Simple: Exit Code](https://docs.anthropic.com/en/docs/claude-code/hooks#simple%3A-exit-code)
  * [Exit Code 2 Behavior](https://docs.anthropic.com/en/docs/claude-code/hooks#exit-code-2-behavior)
  * [Advanced: JSON Output](https://docs.anthropic.com/en/docs/claude-code/hooks#advanced%3A-json-output)
  * [Common JSON Fields](https://docs.anthropic.com/en/docs/claude-code/hooks#common-json-fields)
  * [PreToolUse Decision Control](https://docs.anthropic.com/en/docs/claude-code/hooks#pretooluse-decision-control)
  * [PostToolUse Decision Control](https://docs.anthropic.com/en/docs/claude-code/hooks#posttooluse-decision-control)
  * [UserPromptSubmit Decision Control](https://docs.anthropic.com/en/docs/claude-code/hooks#userpromptsubmit-decision-control)
  * [Stop/SubagentStop Decision Control](https://docs.anthropic.com/en/docs/claude-code/hooks#stop%2Fsubagentstop-decision-control)
  * [SessionStart Decision Control](https://docs.anthropic.com/en/docs/claude-code/hooks#sessionstart-decision-control)
  * [Exit Code Example: Bash Command Validation](https://docs.anthropic.com/en/docs/claude-code/hooks#exit-code-example%3A-bash-command-validation)
  * [JSON Output Example: UserPromptSubmit to Add Context and Validation](https://docs.anthropic.com/en/docs/claude-code/hooks#json-output-example%3A-userpromptsubmit-to-add-context-and-validation)
  * [JSON Output Example: PreToolUse with Approval](https://docs.anthropic.com/en/docs/claude-code/hooks#json-output-example%3A-pretooluse-with-approval)
  * [Working with MCP Tools](https://docs.anthropic.com/en/docs/claude-code/hooks#working-with-mcp-tools)
  * [MCP Tool Naming](https://docs.anthropic.com/en/docs/claude-code/hooks#mcp-tool-naming)
  * [Configuring Hooks for MCP Tools](https://docs.anthropic.com/en/docs/claude-code/hooks#configuring-hooks-for-mcp-tools)
  * [Examples](https://docs.anthropic.com/en/docs/claude-code/hooks#examples)
  * [Security Considerations](https://docs.anthropic.com/en/docs/claude-code/hooks#security-considerations)
  * [Disclaimer](https://docs.anthropic.com/en/docs/claude-code/hooks#disclaimer)
  * [Security Best Practices](https://docs.anthropic.com/en/docs/claude-code/hooks#security-best-practices)
  * [Configuration Safety](https://docs.anthropic.com/en/docs/claude-code/hooks#configuration-safety)
  * [Hook Execution Details](https://docs.anthropic.com/en/docs/claude-code/hooks#hook-execution-details)
  * [Debugging](https://docs.anthropic.com/en/docs/claude-code/hooks#debugging)
  * [Basic Troubleshooting](https://docs.anthropic.com/en/docs/claude-code/hooks#basic-troubleshooting)
  * [Advanced Debugging](https://docs.anthropic.com/en/docs/claude-code/hooks#advanced-debugging)
  * [Debug Output Example](https://docs.anthropic.com/en/docs/claude-code/hooks#debug-output-example)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/iam -->

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
Administration
Identity and Access Management
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


Administration
# Identity and Access Management
Copy page
Learn how to configure user authentication, authorization, and access controls for Claude Code in your organization.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/iam#authentication-methods)
Authentication methods
Setting up Claude Code requires access to Anthropic models. For teams, you can set up Claude Code access in one of three ways:
  * Anthropic API via the Anthropic Console
  * Amazon Bedrock
  * Google Vertex AI


### 
[​](https://docs.anthropic.com/en/docs/claude-code/iam#anthropic-api-authentication)
Anthropic API authentication
**To set up Claude Code access for your team via Anthropic API:**
  1. Use your existing Anthropic Console account or create a new Anthropic Console account
  2. You can add users through either method below: 
     * Bulk invite users from within the Console (Console -> Settings -> Members -> Invite)
     * [Set up SSO](https://support.anthropic.com/en/articles/10280258-setting-up-single-sign-on-on-the-api-console)
  3. When inviting users, they need one of the following roles: 
     * “Claude Code” role means users can only create Claude Code API keys
     * “Developer” role means users can create any kind of API key
  4. Each invited user needs to complete these steps: 
     * Accept the Console invite
     * [Check system requirements](https://docs.anthropic.com/en/docs/claude-code/setup#system-requirements)
     * [Install Claude Code](https://docs.anthropic.com/en/docs/claude-code/setup#installation)
     * Login with Console account credentials


### 
[​](https://docs.anthropic.com/en/docs/claude-code/iam#cloud-provider-authentication)
Cloud provider authentication
**To set up Claude Code access for your team via Bedrock or Vertex:**
  1. Follow the [Bedrock docs](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock) or [Vertex docs](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai)
  2. Distribute the environment variables and instructions for generating cloud credentials to your users. Read more about how to [manage configuration here](https://docs.anthropic.com/en/docs/claude-code/settings).
  3. Users can [install Claude Code](https://docs.anthropic.com/en/docs/claude-code/setup#installation)


## 
[​](https://docs.anthropic.com/en/docs/claude-code/iam#access-control-and-permissions)
Access control and permissions
We support fine-grained permissions so that you’re able to specify exactly what the agent is allowed to do (e.g. run tests, run linter) and what it is not allowed to do (e.g. update cloud infrastructure). These permission settings can be checked into version control and distributed to all developers in your organization, as well as customized by individual developers.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/iam#permission-system)
Permission system
Claude Code uses a tiered permission system to balance power and safety:
Tool Type | Example | Approval Required | ”Yes, don’t ask again” Behavior  
---|---|---|---  
Read-only | File reads, LS, Grep | No | N/A  
Bash Commands | Shell execution | Yes | Permanently per project directory and command  
File Modification | Edit/write files | Yes | Until session end  
### 
[​](https://docs.anthropic.com/en/docs/claude-code/iam#configuring-permissions)
Configuring permissions
You can view & manage Claude Code’s tool permissions with `/permissions`. This UI lists all permission rules and the settings.json file they are sourced from.
  * **Allow** rules will allow Claude Code to use the specified tool without further manual approval.
  * **Ask** rules will ask the user for confirmation whenever Claude Code tries to use the specified tool. Ask rules take precedence over allow rules.
  * **Deny** rules will prevent Claude Code from using the specified tool. Deny rules take precedence over allow and ask rules.
  * **Additional directories** extend Claude’s file access to directories beyond the initial working directory.
  * **Default mode** controls Claude’s permission behavior when encountering new requests.


Permission rules use the format: `Tool` or `Tool(optional-specifier)`
A rule that is just the tool name matches any use of that tool. For example, adding `Bash` to the list of allow rules would allow Claude Code to use the Bash tool without requiring user approval.
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/iam#permission-modes)
Permission modes
Claude Code supports several permission modes that can be set as the `defaultMode` in [settings files](https://docs.anthropic.com/en/docs/claude-code/settings#settings-files):
Mode | Description  
---|---  
`default` | Standard behavior - prompts for permission on first use of each tool  
`acceptEdits` | Automatically accepts file edit permissions for the session  
`plan` | Plan mode - Claude can analyze but not modify files or execute commands  
`bypassPermissions` | Skips all permission prompts (requires safe environment - see warning below)  
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/iam#working-directories)
Working directories
By default, Claude has access to files in the directory where it was launched. You can extend this access:
  * **During startup** : Use `--add-dir <path>` CLI argument
  * **During session** : Use `/add-dir` slash command
  * **Persistent configuration** : Add to `additionalDirectories` in [settings files](https://docs.anthropic.com/en/docs/claude-code/settings#settings-files)


Files in additional directories follow the same permission rules as the original working directory - they become readable without prompts, and file editing permissions follow the current permission mode.
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/iam#tool-specific-permission-rules)
Tool-specific permission rules
Some tools support more fine-grained permission controls:
**Bash**
  * `Bash(npm run build)` Matches the exact Bash command `npm run build`
  * `Bash(npm run test:*)` Matches Bash commands starting with `npm run test`.


Claude Code is aware of shell operators (like `&&`) so a prefix match rule like `Bash(safe-cmd:*)` won’t give it permission to run the command `safe-cmd && other-cmd`
**Read & Edit**
`Edit` rules apply to all built-in tools that edit files. Claude will make a best-effort attempt to apply `Read` rules to all built-in tools that read files like Grep, Glob, and LS.
Read & Edit rules both follow the [gitignore](https://git-scm.com/docs/gitignore) specification. Patterns are resolved relative to the directory containing `.claude/settings.json`. To reference an absolute path, use `//`. For a path relative to your home directory, use `~/`.
  * `Edit(docs/**)` Matches edits to files in the `docs` directory of your project
  * `Read(~/.zshrc)` Matches reads to your `~/.zshrc` file
  * `Edit(//tmp/scratch.txt)` Matches edits to `/tmp/scratch.txt`


**WebFetch**
  * `WebFetch(domain:example.com)` Matches fetch requests to example.com


**MCP**
  * `mcp__puppeteer` Matches any tool provided by the `puppeteer` server (name configured in Claude Code)
  * `mcp__puppeteer__puppeteer_navigate` Matches the `puppeteer_navigate` tool provided by the `puppeteer` server


Unlike other permission types, MCP permissions do NOT support wildcards (`*`).
To approve all tools from an MCP server:
  * ✅ Use: `mcp__github` (approves ALL GitHub tools)
  * ❌ Don’t use: `mcp__github__*` (wildcards are not supported)


To approve specific tools only, list each one:
  * ✅ Use: `mcp__github__get_issue`
  * ✅ Use: `mcp__github__list_issues`


### 
[​](https://docs.anthropic.com/en/docs/claude-code/iam#additional-permission-control-with-hooks)
Additional permission control with hooks
[Claude Code hooks](https://docs.anthropic.com/en/docs/claude-code/hooks-guide) provide a way to register custom shell commands to perform permission evaluation at runtime. When Claude Code makes a tool call, PreToolUse hooks run before the permission system runs, and the hook output can determine whether to approve or deny the tool call in place of the permission system.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/iam#enterprise-managed-policy-settings)
Enterprise managed policy settings
For enterprise deployments of Claude Code, we support enterprise managed policy settings that take precedence over user and project settings. This allows system administrators to enforce security policies that users cannot override.
System administrators can deploy policies to:
  * macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`
  * Linux and WSL: `/etc/claude-code/managed-settings.json`
  * Windows: `C:\ProgramData\ClaudeCode\managed-settings.json`


These policy files follow the same format as regular [settings files](https://docs.anthropic.com/en/docs/claude-code/settings#settings-files) but cannot be overridden by user or project settings. This ensures consistent security policies across your organization.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/iam#settings-precedence)
Settings precedence
When multiple settings sources exist, they are applied in the following order (highest to lowest precedence):
  1. Enterprise policies
  2. Command line arguments
  3. Local project settings (`.claude/settings.local.json`)
  4. Shared project settings (`.claude/settings.json`)
  5. User settings (`~/.claude/settings.json`)


This hierarchy ensures that organizational policies are always enforced while still allowing flexibility at the project and user levels where appropriate.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/iam#credential-management)
Credential management
Claude Code securely manages your authentication credentials:
  * **Storage location** : On macOS, API keys, OAuth tokens, and other credentials are stored in the encrypted macOS Keychain.
  * **Supported authentication types** : Claude.ai credentials, Anthropic API credentials, Bedrock Auth, and Vertex Auth.
  * **Custom credential scripts** : The [`apiKeyHelper`](https://docs.anthropic.com/en/docs/claude-code/settings#available-settings) setting can be configured to run a shell script that returns an API key.
  * **Refresh intervals** : By default, `apiKeyHelper` is called after 5 minutes or on HTTP 401 response. Set `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` environment variable for custom refresh intervals.


Was this page helpful?
YesNo
[Advanced installation](https://docs.anthropic.com/en/docs/claude-code/setup)[Security](https://docs.anthropic.com/en/docs/claude-code/security)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Authentication methods](https://docs.anthropic.com/en/docs/claude-code/iam#authentication-methods)
  * [Anthropic API authentication](https://docs.anthropic.com/en/docs/claude-code/iam#anthropic-api-authentication)
  * [Cloud provider authentication](https://docs.anthropic.com/en/docs/claude-code/iam#cloud-provider-authentication)
  * [Access control and permissions](https://docs.anthropic.com/en/docs/claude-code/iam#access-control-and-permissions)
  * [Permission system](https://docs.anthropic.com/en/docs/claude-code/iam#permission-system)
  * [Configuring permissions](https://docs.anthropic.com/en/docs/claude-code/iam#configuring-permissions)
  * [Permission modes](https://docs.anthropic.com/en/docs/claude-code/iam#permission-modes)
  * [Working directories](https://docs.anthropic.com/en/docs/claude-code/iam#working-directories)
  * [Tool-specific permission rules](https://docs.anthropic.com/en/docs/claude-code/iam#tool-specific-permission-rules)
  * [Additional permission control with hooks](https://docs.anthropic.com/en/docs/claude-code/iam#additional-permission-control-with-hooks)
  * [Enterprise managed policy settings](https://docs.anthropic.com/en/docs/claude-code/iam#enterprise-managed-policy-settings)
  * [Settings precedence](https://docs.anthropic.com/en/docs/claude-code/iam#settings-precedence)
  * [Credential management](https://docs.anthropic.com/en/docs/claude-code/iam#credential-management)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/ide-integrations -->

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


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/interactive-mode -->

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
Interactive mode
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
# Interactive mode
Copy page
Complete reference for keyboard shortcuts, input modes, and interactive features in Claude Code sessions.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/interactive-mode#keyboard-shortcuts)
Keyboard shortcuts
### 
[​](https://docs.anthropic.com/en/docs/claude-code/interactive-mode#general-controls)
General controls
Shortcut | Description | Context  
---|---|---  
`Ctrl+C` | Cancel current input or generation | Standard interrupt  
`Ctrl+D` | Exit Claude Code session | EOF signal  
`Ctrl+L` | Clear terminal screen | Keeps conversation history  
`Up/Down arrows` | Navigate command history | Recall previous inputs  
`Esc` + `Esc` | Edit previous message | Double-escape to modify  
### 
[​](https://docs.anthropic.com/en/docs/claude-code/interactive-mode#multiline-input)
Multiline input
Method | Shortcut | Context  
---|---|---  
Quick escape |  `\` + `Enter` | Works in all terminals  
macOS default | `Option+Enter` | Default on macOS  
Terminal setup | `Shift+Enter` | After `/terminal-setup`  
Control sequence | `Ctrl+J` | Line feed character for multiline  
Paste mode | Paste directly | For code blocks, logs  
### 
[​](https://docs.anthropic.com/en/docs/claude-code/interactive-mode#quick-commands)
Quick commands
Shortcut | Description | Notes  
---|---|---  
`#` at start | Memory shortcut - add to CLAUDE.md | Prompts for file selection  
`/` at start | Slash command | See [slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands)  
## 
[​](https://docs.anthropic.com/en/docs/claude-code/interactive-mode#vim-mode)
Vim mode
Enable vim-style editing with `/vim` command or configure permanently via `/config`.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/interactive-mode#mode-switching)
Mode switching
Command | Action | From mode  
---|---|---  
`Esc` | Enter NORMAL mode | INSERT  
`i` | Insert before cursor | NORMAL  
`I` | Insert at beginning of line | NORMAL  
`a` | Insert after cursor | NORMAL  
`A` | Insert at end of line | NORMAL  
`o` | Open line below | NORMAL  
`O` | Open line above | NORMAL  
### 
[​](https://docs.anthropic.com/en/docs/claude-code/interactive-mode#navigation-normal-mode)
Navigation (NORMAL mode)
Command | Action  
---|---  
`h`/`j`/`k`/`l` | Move left/down/up/right  
`w` | Next word  
`e` | End of word  
`b` | Previous word  
`0` | Beginning of line  
`$` | End of line  
`^` | First non-blank character  
`gg` | Beginning of input  
`G` | End of input  
### 
[​](https://docs.anthropic.com/en/docs/claude-code/interactive-mode#editing-normal-mode)
Editing (NORMAL mode)
Command | Action  
---|---  
`x` | Delete character  
`dd` | Delete line  
`D` | Delete to end of line  
`dw`/`de`/`db` | Delete word/to end/back  
`cc` | Change line  
`C` | Change to end of line  
`cw`/`ce`/`cb` | Change word/to end/back  
`.` | Repeat last change  
Configure your preferred line break behavior in terminal settings. Run `/terminal-setup` to install Shift+Enter binding for iTerm2 and VS Code terminals.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/interactive-mode#command-history)
Command history
Claude Code maintains command history for the current session:
  * History is stored per working directory
  * Cleared with `/clear` command
  * Use Up/Down arrows to navigate (see keyboard shortcuts above)
  * **Ctrl+R** : Reverse search through history (if supported by terminal)
  * **Note** : History expansion (`!`) is disabled by default


## 
[​](https://docs.anthropic.com/en/docs/claude-code/interactive-mode#see-also)
See also
  * [Slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands) - Interactive session commands
  * [CLI reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference) - Command-line flags and options
  * [Settings](https://docs.anthropic.com/en/docs/claude-code/settings) - Configuration options
  * [Memory management](https://docs.anthropic.com/en/docs/claude-code/memory) - Managing CLAUDE.md files


Was this page helpful?
YesNo
[CLI reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference)[Slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Keyboard shortcuts](https://docs.anthropic.com/en/docs/claude-code/interactive-mode#keyboard-shortcuts)
  * [General controls](https://docs.anthropic.com/en/docs/claude-code/interactive-mode#general-controls)
  * [Multiline input](https://docs.anthropic.com/en/docs/claude-code/interactive-mode#multiline-input)
  * [Quick commands](https://docs.anthropic.com/en/docs/claude-code/interactive-mode#quick-commands)
  * [Vim mode](https://docs.anthropic.com/en/docs/claude-code/interactive-mode#vim-mode)
  * [Mode switching](https://docs.anthropic.com/en/docs/claude-code/interactive-mode#mode-switching)
  * [Navigation (NORMAL mode)](https://docs.anthropic.com/en/docs/claude-code/interactive-mode#navigation-normal-mode)
  * [Editing (NORMAL mode)](https://docs.anthropic.com/en/docs/claude-code/interactive-mode#editing-normal-mode)
  * [Command history](https://docs.anthropic.com/en/docs/claude-code/interactive-mode#command-history)
  * [See also](https://docs.anthropic.com/en/docs/claude-code/interactive-mode#see-also)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance -->

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
Resources
Legal and compliance
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


Resources
# Legal and compliance
Copy page
Legal agreements, compliance certifications, and security information for Claude Code.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance#legal-agreements)
Legal agreements
### 
[​](https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance#license)
License
Claude Code is provided under Anthropic’s [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms).
### 
[​](https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance#commercial-agreements)
Commercial agreements
Whether you’re using Anthropic’s API directly (1P) or accessing it through AWS Bedrock or Google Vertex (3P), your existing commercial agreement will apply to Claude Code usage, unless we’ve mutually agreed otherwise.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance#compliance)
Compliance
### 
[​](https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance#healthcare-compliance-baa)
Healthcare compliance (BAA)
If a customer has a Business Associate Agreement (BAA) with us, and wants to use Claude Code, the BAA will automatically extend to cover Claude Code if the customer has executed a BAA and has Zero Data Retention (ZDR) activated. The BAA will be applicable to that customer’s API traffic flowing through Claude Code.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance#security-and-trust)
Security and trust
### 
[​](https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance#trust-and-safety)
Trust and safety
You can find more information in the [Anthropic Trust Center](https://trust.anthropic.com) and [Transparency Hub](https://www.anthropic.com/transparency).
### 
[​](https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance#security-vulnerability-reporting)
Security vulnerability reporting
Anthropic manages our security program through HackerOne. [Use this form to report vulnerabilities](https://hackerone.com/anthropic-vdp/reports/new?type=team&report_type=vulnerability).
* * *
© Anthropic PBC. All rights reserved. Use is subject to Anthropic’s [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms).
Was this page helpful?
YesNo
[Hooks reference](https://docs.anthropic.com/en/docs/claude-code/hooks)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Legal agreements](https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance#legal-agreements)
  * [License](https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance#license)
  * [Commercial agreements](https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance#commercial-agreements)
  * [Compliance](https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance#compliance)
  * [Healthcare compliance (BAA)](https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance#healthcare-compliance-baa)
  * [Security and trust](https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance#security-and-trust)
  * [Trust and safety](https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance#trust-and-safety)
  * [Security vulnerability reporting](https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance#security-vulnerability-reporting)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/llm-gateway -->

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
LLM gateway configuration
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
# LLM gateway configuration
Copy page
Learn how to configure Claude Code with LLM gateway solutions, including LiteLLM setup, authentication methods, and enterprise features like usage tracking and budget management.
LLM gateways provide a centralized proxy layer between Claude Code and model providers, offering:
  * **Centralized authentication** - Single point for API key management
  * **Usage tracking** - Monitor usage across teams and projects
  * **Cost controls** - Implement budgets and rate limits
  * **Audit logging** - Track all model interactions for compliance
  * **Model routing** - Switch between providers without code changes


## 
[​](https://docs.anthropic.com/en/docs/claude-code/llm-gateway#litellm-configuration)
LiteLLM configuration
LiteLLM is a third-party proxy service. Anthropic doesn’t endorse, maintain, or audit LiteLLM’s security or functionality. This guide is provided for informational purposes and may become outdated. Use at your own discretion.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/llm-gateway#prerequisites)
Prerequisites
  * Claude Code updated to the latest version
  * LiteLLM Proxy Server deployed and accessible
  * Access to Claude models through your chosen provider


### 
[​](https://docs.anthropic.com/en/docs/claude-code/llm-gateway#basic-litellm-setup)
Basic LiteLLM setup
**Configure Claude Code** :
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/llm-gateway#authentication-methods)
Authentication methods
##### Static API key
Simplest method using a fixed API key:
Copy
```
# Set in environment
export ANTHROPIC_AUTH_TOKEN=sk-litellm-static-key

# Or in Claude Code settings
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "sk-litellm-static-key"
  }
}

```

This value will be sent as the `Authorization` header.
##### Dynamic API key with helper
For rotating keys or per-user authentication:
  1. Create an API key helper script:


Copy
```
#!/bin/bash
# ~/bin/get-litellm-key.sh

# Example: Fetch key from vault
vault kv get -field=api_key secret/litellm/claude-code

# Example: Generate JWT token
jwt encode \
  --secret="${JWT_SECRET}" \
  --exp="+1h" \
  '{"user":"'${USER}'","team":"engineering"}'

```

  1. Configure Claude Code settings to use the helper:


Copy
```
{
  "apiKeyHelper": "~/bin/get-litellm-key.sh"
}

```

  1. Set token refresh interval:


Copy
```
# Refresh every hour (3600000 ms)
export CLAUDE_CODE_API_KEY_HELPER_TTL_MS=3600000

```

This value will be sent as `Authorization` and `X-Api-Key` headers. The `apiKeyHelper` has lower precedence than `ANTHROPIC_AUTH_TOKEN` or `ANTHROPIC_API_KEY`.
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/llm-gateway#unified-endpoint-recommended)
Unified endpoint (recommended)
Using LiteLLM’s [Anthropic format endpoint](https://docs.litellm.ai/docs/anthropic_unified):
Copy
```
export ANTHROPIC_BASE_URL=https://litellm-server:4000

```

**Benefits of the unified endpoint over pass-through endpoints:**
  * Load balancing
  * Fallbacks
  * Consistent support for cost tracking and end-user tracking


#### 
[​](https://docs.anthropic.com/en/docs/claude-code/llm-gateway#provider-specific-pass-through-endpoints-alternative)
Provider-specific pass-through endpoints (alternative)
##### Anthropic API through LiteLLM
Using [pass-through endpoint](https://docs.litellm.ai/docs/pass_through/anthropic_completion):
Copy
```
export ANTHROPIC_BASE_URL=https://litellm-server:4000/anthropic

```

##### Amazon Bedrock through LiteLLM
Using [pass-through endpoint](https://docs.litellm.ai/docs/pass_through/bedrock):
Copy
```
export ANTHROPIC_BEDROCK_BASE_URL=https://litellm-server:4000/bedrock
export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1
export CLAUDE_CODE_USE_BEDROCK=1

```

##### Google Vertex AI through LiteLLM
Using [pass-through endpoint](https://docs.litellm.ai/docs/pass_through/vertex_ai):
Copy
```
export ANTHROPIC_VERTEX_BASE_URL=https://litellm-server:4000/vertex_ai/v1
export ANTHROPIC_VERTEX_PROJECT_ID=your-gcp-project-id
export CLAUDE_CODE_SKIP_VERTEX_AUTH=1
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/llm-gateway#model-selection)
Model selection
By default, the models will use those specified in [Model configuration](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#model-configuration).
If you have configured custom model names in LiteLLM, set the aforementioned environment variables to those custom names.
For more detailed information, refer to the [LiteLLM documentation](https://docs.litellm.ai/).
## 
[​](https://docs.anthropic.com/en/docs/claude-code/llm-gateway#additional-resources)
Additional resources
  * [LiteLLM documentation](https://docs.litellm.ai/)
  * [Claude Code settings](https://docs.anthropic.com/en/docs/claude-code/settings)
  * [Corporate proxy setup](https://docs.anthropic.com/en/docs/claude-code/corporate-proxy)
  * [Third-party integrations overview](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations)


Was this page helpful?
YesNo
[Corporate proxy](https://docs.anthropic.com/en/docs/claude-code/corporate-proxy)[Development containers](https://docs.anthropic.com/en/docs/claude-code/devcontainer)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [LiteLLM configuration](https://docs.anthropic.com/en/docs/claude-code/llm-gateway#litellm-configuration)
  * [Prerequisites](https://docs.anthropic.com/en/docs/claude-code/llm-gateway#prerequisites)
  * [Basic LiteLLM setup](https://docs.anthropic.com/en/docs/claude-code/llm-gateway#basic-litellm-setup)
  * [Authentication methods](https://docs.anthropic.com/en/docs/claude-code/llm-gateway#authentication-methods)
  * [Unified endpoint (recommended)](https://docs.anthropic.com/en/docs/claude-code/llm-gateway#unified-endpoint-recommended)
  * [Provider-specific pass-through endpoints (alternative)](https://docs.anthropic.com/en/docs/claude-code/llm-gateway#provider-specific-pass-through-endpoints-alternative)
  * [Model selection](https://docs.anthropic.com/en/docs/claude-code/llm-gateway#model-selection)
  * [Additional resources](https://docs.anthropic.com/en/docs/claude-code/llm-gateway#additional-resources)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/mcp -->

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
Connect Claude Code to tools via MCP
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
# Connect Claude Code to tools via MCP
Copy page
Learn how to connect Claude Code to your tools with the Model Context Protocol.
Claude Code can connect to hundreds of external tools and data sources through the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction), an open-source standard for AI-tool integrations. MCP servers give Claude Code access to your tools, databases, and APIs.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#what-you-can-do-with-mcp)
What you can do with MCP
With MCP servers connected, you can ask Claude Code to:
  * **Implement features from issue trackers** : “Add the feature described in JIRA issue ENG-4521 and create a PR on GitHub.”
  * **Analyze monitoring data** : “Check Sentry and Statsig to check the usage of the feature described in ENG-4521.”
  * **Query databases** : “Find emails of 10 random users who used feature ENG-4521, based on our Postgres database.”
  * **Integrate designs** : “Update our standard email template based on the new Figma designs that were posted in Slack”
  * **Automate workflows** : “Create Gmail drafts inviting these 10 users to a feedback session about the new feature.”


## 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#popular-mcp-servers)
Popular MCP servers
Here are some commonly used MCP servers you can connect to Claude Code:
Use third party MCP servers at your own risk - Anthropic has not verified the correctness or security of all these servers. Make sure you trust MCP servers you are installing. Be especially careful when using MCP servers that could fetch untrusted content, as these can expose you to prompt injection risk.
### Development & Testing Tools
[**Sentry**](https://docs.sentry.io/product/sentry-mcp/)
Monitor errors, debug production issues
Command
`claude mcp add --transport http sentry https://mcp.sentry.dev/mcp`
[**Socket**](https://github.com/SocketDev/socket-mcp)
Security analysis for dependencies
Command
`claude mcp add --transport http socket https://mcp.socket.dev/`
### Project Management & Documentation
[**Asana**](https://developers.asana.com/docs/using-asanas-model-control-protocol-mcp-server)
Interact with your Asana workspace to keep projects on track
Command
`claude mcp add --transport sse asana https://mcp.asana.com/sse`
[**Atlassian**](https://www.atlassian.com/platform/remote-mcp-server)
Manage your Jira tickets and Confluence docs
Command
`claude mcp add --transport sse atlassian https://mcp.atlassian.com/v1/sse`
[**ClickUp**](https://github.com/hauptsacheNet/clickup-mcp)
Task management, project tracking
Command
`claude mcp add clickup --env CLICKUP_API_KEY=YOUR_KEY --env CLICKUP_TEAM_ID=YOUR_ID -- npx -y @hauptsache.net/clickup-mcp`
[**Intercom**](https://developers.intercom.com/docs/guides/mcp)
Access real-time customer conversations, tickets, and user data
Command
`claude mcp add --transport http intercom https://mcp.intercom.com/mcp`
[**Linear**](https://linear.app/docs/mcp)
Integrate with Linear's issue tracking and project management
Command
`claude mcp add --transport sse linear https://mcp.linear.app/sse`
[**Notion**](https://developers.notion.com/docs/mcp)
Read docs, update pages, manage tasks
Command
`claude mcp add --transport http notion https://mcp.notion.com/mcp`
### Databases & Data Management
[**Airtable**](https://github.com/domdomegg/airtable-mcp-server)
Read/write records, manage bases and tables
Command
`claude mcp add airtable --env AIRTABLE_API_KEY=YOUR_KEY -- npx -y airtable-mcp-server`
### Payments & Commerce
[**PayPal**](https://www.paypal.ai/)
Integrate PayPal commerce capabilities, payment processing, transaction management
Command
`claude mcp add --transport http paypal https://mcp.paypal.com/mcp`
[**Plaid**](https://plaid.com/blog/plaid-mcp-ai-assistant-claude/)
Analyze, troubleshoot, and optimize Plaid integrations. Banking data, financial account linking
Command
`claude mcp add --transport sse plaid https://api.dashboard.plaid.com/mcp/sse`
[**Square**](https://developer.squareup.com/docs/mcp)
Use an agent to build on Square APIs. Payments, inventory, orders, and more
Command
`claude mcp add --transport sse square https://mcp.squareup.com/sse`
[**Stripe**](https://docs.stripe.com/mcp)
Payment processing, subscription management, and financial transactions
Command
`claude mcp add --transport http stripe https://mcp.stripe.com`
### Design & Media
[**Figma**](https://help.figma.com/hc/en-us/articles/32132100833559)
Access designs, export assetsRequires Figma Desktop with Dev Mode MCP Server
Command
`claude mcp add --transport sse figma http://127.0.0.1:3845/sse`
[**invideo**](https://invideo.io/ai/mcp)
Build video creation capabilities into your applications
Command
`claude mcp add --transport sse invideo https://mcp.invideo.io/sse`
### Infrastructure & DevOps
[**Cloudflare**](https://developers.cloudflare.com/agents/model-context-protocol/mcp-servers-for-cloudflare/)
Build applications, analyze traffic, monitor performance, and manage security settings through CloudflareMultiple services available. See documentation for specific server URLs. Claude Code can use the Cloudflare CLI if installed.
### Automation & Integration
[**Workato**](https://docs.workato.com/mcp.html)
Access any application, workflows or data via Workato, made accessible for AIMCP servers are programmatically generated
[**Zapier**](https://help.zapier.com/hc/en-us/articles/36265392843917)
Connect to nearly 8,000 apps through Zapier's automation platformGenerate a user-specific URL at mcp.zapier.com
**Need a specific integration?** [Find hundreds more MCP servers on GitHub](https://github.com/modelcontextprotocol/servers), or build your own using the [MCP SDK](https://modelcontextprotocol.io/quickstart/server).
## 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#installing-mcp-servers)
Installing MCP servers
MCP servers can be configured in three different ways depending on your needs:
### 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#option-1%3A-add-a-local-stdio-server)
Option 1: Add a local stdio server
Stdio servers run as local processes on your machine. They’re ideal for tools that need direct system access or custom scripts.
Copy
```
# Basic syntax
claude mcp add <name> <command> [args...]

# Real example: Add Airtable server
claude mcp add airtable --env AIRTABLE_API_KEY=YOUR_KEY \
  -- npx -y airtable-mcp-server

```

**Understanding the ”—” parameter:** The `--` (double dash) separates Claude’s own CLI flags from the command and arguments that get passed to the MCP server. Everything before `--` are options for Claude (like `--env`, `--scope`), and everything after `--` is the actual command to run the MCP server.
For example:
  * `claude mcp add myserver -- npx server` → runs `npx server`
  * `claude mcp add myserver --env KEY=value -- python server.py --port 8080` → runs `python server.py --port 8080` with `KEY=value` in environment


This prevents conflicts between Claude’s flags and the server’s flags.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#option-2%3A-add-a-remote-sse-server)
Option 2: Add a remote SSE server
SSE (Server-Sent Events) servers provide real-time streaming connections. Many cloud services use this for live updates.
Copy
```
# Basic syntax
claude mcp add --transport sse <name> <url>

# Real example: Connect to Linear
claude mcp add --transport sse linear https://mcp.linear.app/sse

# Example with authentication header
claude mcp add --transport sse private-api https://api.company.com/mcp \
  --header "X-API-Key: your-key-here"

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#option-3%3A-add-a-remote-http-server)
Option 3: Add a remote HTTP server
HTTP servers use standard request/response patterns. Most REST APIs and web services use this transport.
Copy
```
# Basic syntax
claude mcp add --transport http <name> <url>

# Real example: Connect to Notion
claude mcp add --transport http notion https://mcp.notion.com/mcp

# Example with Bearer token
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#managing-your-servers)
Managing your servers
Once configured, you can manage your MCP servers with these commands:
Copy
```
# List all configured servers
claude mcp list

# Get details for a specific server
claude mcp get github

# Remove a server
claude mcp remove github

# (within Claude Code) Check server status
/mcp

```

Tips:
  * Use the `--scope` flag to specify where the configuration is stored: 
    * `local` (default): Available only to you in the current project (was called `project` in older versions)
    * `project`: Shared with everyone in the project via `.mcp.json` file
    * `user`: Available to you across all projects (was called `global` in older versions)
  * Set environment variables with `--env` flags (e.g., `--env KEY=value`)
  * Configure MCP server startup timeout using the MCP_TIMEOUT environment variable (e.g., `MCP_TIMEOUT=10000 claude` sets a 10-second timeout)
  * Use `/mcp` to authenticate with remote servers that require OAuth 2.0 authentication


**Windows Users** : On native Windows (not WSL), local MCP servers that use `npx` require the `cmd /c` wrapper to ensure proper execution.
Copy
```
# This creates command="cmd" which Windows can execute
claude mcp add my-server -- cmd /c npx -y @some/package

```

Without the `cmd /c` wrapper, you’ll encounter “Connection closed” errors because Windows cannot directly execute `npx`. (See the note above for an explanation of the `--` parameter.)
## 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#mcp-installation-scopes)
MCP installation scopes
MCP servers can be configured at three different scope levels, each serving distinct purposes for managing server accessibility and sharing. Understanding these scopes helps you determine the best way to configure servers for your specific needs.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#local-scope)
Local scope
Local-scoped servers represent the default configuration level and are stored in your project-specific user settings. These servers remain private to you and are only accessible when working within the current project directory. This scope is ideal for personal development servers, experimental configurations, or servers containing sensitive credentials that shouldn’t be shared.
Copy
```
# Add a local-scoped server (default)
claude mcp add my-private-server /path/to/server

# Explicitly specify local scope
claude mcp add my-private-server --scope local /path/to/server

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#project-scope)
Project scope
Project-scoped servers enable team collaboration by storing configurations in a `.mcp.json` file at your project’s root directory. This file is designed to be checked into version control, ensuring all team members have access to the same MCP tools and services. When you add a project-scoped server, Claude Code automatically creates or updates this file with the appropriate configuration structure.
Copy
```
# Add a project-scoped server
claude mcp add shared-server --scope project /path/to/server

```

The resulting `.mcp.json` file follows a standardized format:
Copy
```
{
  "mcpServers": {
    "shared-server": {
      "command": "/path/to/server",
      "args": [],
      "env": {}
    }
  }
}

```

For security reasons, Claude Code prompts for approval before using project-scoped servers from `.mcp.json` files. If you need to reset these approval choices, use the `claude mcp reset-project-choices` command.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#user-scope)
User scope
User-scoped servers provide cross-project accessibility, making them available across all projects on your machine while remaining private to your user account. This scope works well for personal utility servers, development tools, or services you frequently use across different projects.
Copy
```
# Add a user server
claude mcp add my-user-server --scope user /path/to/server

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#choosing-the-right-scope)
Choosing the right scope
Select your scope based on:
  * **Local scope** : Personal servers, experimental configurations, or sensitive credentials specific to one project
  * **Project scope** : Team-shared servers, project-specific tools, or services required for collaboration
  * **User scope** : Personal utilities needed across multiple projects, development tools, or frequently-used services


### 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#scope-hierarchy-and-precedence)
Scope hierarchy and precedence
MCP server configurations follow a clear precedence hierarchy. When servers with the same name exist at multiple scopes, the system resolves conflicts by prioritizing local-scoped servers first, followed by project-scoped servers, and finally user-scoped servers. This design ensures that personal configurations can override shared ones when needed.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#environment-variable-expansion-in-mcp-json)
Environment variable expansion in `.mcp.json`
Claude Code supports environment variable expansion in `.mcp.json` files, allowing teams to share configurations while maintaining flexibility for machine-specific paths and sensitive values like API keys.
**Supported syntax:**
  * `${VAR}` - Expands to the value of environment variable `VAR`
  * `${VAR:-default}` - Expands to `VAR` if set, otherwise uses `default`


**Expansion locations:** Environment variables can be expanded in:
  * `command` - The server executable path
  * `args` - Command-line arguments
  * `env` - Environment variables passed to the server
  * `url` - For SSE/HTTP server types
  * `headers` - For SSE/HTTP server authentication


**Example with variable expansion:**
Copy
```
{
  "mcpServers": {
    "api-server": {
      "type": "sse",
      "url": "${API_BASE_URL:-https://api.example.com}/mcp",
      "headers": {
        "Authorization": "Bearer ${API_KEY}"
      }
    }
  }
}

```

If a required environment variable is not set and has no default value, Claude Code will fail to parse the config.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#practical-examples)
Practical examples
### 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#example%3A-monitor-errors-with-sentry)
Example: Monitor errors with Sentry
Copy
```
# 1. Add the Sentry MCP server
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp

# 2. Use /mcp to authenticate with your Sentry account
> /mcp

# 3. Debug production issues
> "What are the most common errors in the last 24 hours?"
> "Show me the stack trace for error ID abc123"
> "Which deployment introduced these new errors?"

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#authenticate-with-remote-mcp-servers)
Authenticate with remote MCP servers
Many cloud-based MCP servers require authentication. Claude Code supports OAuth 2.0 for secure connections.
1
Add the server that requires authentication
For example:
Copy
```
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp

```

2
Use the /mcp command within Claude Code
In Claude code, use the command:
Copy
```
> /mcp

```

Then follow the steps in your browser to login.
Tips:
  * Authentication tokens are stored securely and refreshed automatically
  * Use “Clear authentication” in the `/mcp` menu to revoke access
  * If your browser doesn’t open automatically, copy the provided URL
  * OAuth authentication works with both SSE and HTTP transports


## 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#add-mcp-servers-from-json-configuration)
Add MCP servers from JSON configuration
If you have a JSON configuration for an MCP server, you can add it directly:
1
Add an MCP server from JSON
Copy
```
# Basic syntax
claude mcp add-json <name> '<json>'

# Example: Adding a stdio server with JSON configuration
claude mcp add-json weather-api '{"type":"stdio","command":"/path/to/weather-cli","args":["--api-key","abc123"],"env":{"CACHE_DIR":"/tmp"}}'

```

2
Verify the server was added
Copy
```
claude mcp get weather-api

```

Tips:
  * Make sure the JSON is properly escaped in your shell
  * The JSON must conform to the MCP server configuration schema
  * You can use `--scope user` to add the server to your user configuration instead of the project-specific one


## 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#import-mcp-servers-from-claude-desktop)
Import MCP servers from Claude Desktop
If you’ve already configured MCP servers in Claude Desktop, you can import them:
1
Import servers from Claude Desktop
Copy
```
# Basic syntax 
claude mcp add-from-claude-desktop 

```

2
Select which servers to import
After running the command, you’ll see an interactive dialog that allows you to select which servers you want to import.
3
Verify the servers were imported
Copy
```
claude mcp list 

```

Tips:
  * This feature only works on macOS and Windows Subsystem for Linux (WSL)
  * It reads the Claude Desktop configuration file from its standard location on those platforms
  * Use the `--scope user` flag to add servers to your user configuration
  * Imported servers will have the same names as in Claude Desktop
  * If servers with the same names already exist, they will get a numerical suffix (e.g., `server_1`)


## 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#use-claude-code-as-an-mcp-server)
Use Claude Code as an MCP server
You can use Claude Code itself as an MCP server that other applications can connect to:
Copy
```
# Start Claude as a stdio MCP server
claude mcp serve

```

You can use this in Claude Desktop by adding this configuration to claude_desktop_config.json:
Copy
```
{
  "mcpServers": {
    "claude-code": {
      "command": "claude",
      "args": ["mcp", "serve"],
      "env": {}
    }
  }
}

```

Tips:
  * The server provides access to Claude’s tools like View, Edit, LS, etc.
  * In Claude Desktop, try asking Claude to read files in a directory, make edits, and more.
  * Note that this MCP server is simply exposing Claude Code’s tools to your MCP client, so your own client is responsible for implementing user confirmation for individual tool calls.


## 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#use-mcp-resources)
Use MCP resources
MCP servers can expose resources that you can reference using @ mentions, similar to how you reference files.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#reference-mcp-resources)
Reference MCP resources
1
List available resources
Type `@` in your prompt to see available resources from all connected MCP servers. Resources appear alongside files in the autocomplete menu.
2
Reference a specific resource
Use the format `@server:protocol://resource/path` to reference a resource:
Copy
```
> Can you analyze @github:issue://123 and suggest a fix?

```

Copy
```
> Please review the API documentation at @docs:file://api/authentication

```

3
Multiple resource references
You can reference multiple resources in a single prompt:
Copy
```
> Compare @postgres:schema://users with @docs:file://database/user-model

```

Tips:
  * Resources are automatically fetched and included as attachments when referenced
  * Resource paths are fuzzy-searchable in the @ mention autocomplete
  * Claude Code automatically provides tools to list and read MCP resources when servers support them
  * Resources can contain any type of content that the MCP server provides (text, JSON, structured data, etc.)


## 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#use-mcp-prompts-as-slash-commands)
Use MCP prompts as slash commands
MCP servers can expose prompts that become available as slash commands in Claude Code.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/mcp#execute-mcp-prompts)
Execute MCP prompts
1
Discover available prompts
Type `/` to see all available commands, including those from MCP servers. MCP prompts appear with the format `/mcp__servername__promptname`.
2
Execute a prompt without arguments
Copy
```
> /mcp__github__list_prs

```

3
Execute a prompt with arguments
Many prompts accept arguments. Pass them space-separated after the command:
Copy
```
> /mcp__github__pr_review 456

```

Copy
```
> /mcp__jira__create_issue "Bug in login flow" high

```

Tips:
  * MCP prompts are dynamically discovered from connected servers
  * Arguments are parsed based on the prompt’s defined parameters
  * Prompt results are injected directly into the conversation
  * Server and prompt names are normalized (spaces become underscores)


Was this page helpful?
YesNo
[GitHub Actions](https://docs.anthropic.com/en/docs/claude-code/github-actions)[Troubleshooting](https://docs.anthropic.com/en/docs/claude-code/troubleshooting)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [What you can do with MCP](https://docs.anthropic.com/en/docs/claude-code/mcp#what-you-can-do-with-mcp)
  * [Popular MCP servers](https://docs.anthropic.com/en/docs/claude-code/mcp#popular-mcp-servers)
  * [Installing MCP servers](https://docs.anthropic.com/en/docs/claude-code/mcp#installing-mcp-servers)
  * [Option 1: Add a local stdio server](https://docs.anthropic.com/en/docs/claude-code/mcp#option-1%3A-add-a-local-stdio-server)
  * [Option 2: Add a remote SSE server](https://docs.anthropic.com/en/docs/claude-code/mcp#option-2%3A-add-a-remote-sse-server)
  * [Option 3: Add a remote HTTP server](https://docs.anthropic.com/en/docs/claude-code/mcp#option-3%3A-add-a-remote-http-server)
  * [Managing your servers](https://docs.anthropic.com/en/docs/claude-code/mcp#managing-your-servers)
  * [MCP installation scopes](https://docs.anthropic.com/en/docs/claude-code/mcp#mcp-installation-scopes)
  * [Local scope](https://docs.anthropic.com/en/docs/claude-code/mcp#local-scope)
  * [Project scope](https://docs.anthropic.com/en/docs/claude-code/mcp#project-scope)
  * [User scope](https://docs.anthropic.com/en/docs/claude-code/mcp#user-scope)
  * [Choosing the right scope](https://docs.anthropic.com/en/docs/claude-code/mcp#choosing-the-right-scope)
  * [Scope hierarchy and precedence](https://docs.anthropic.com/en/docs/claude-code/mcp#scope-hierarchy-and-precedence)
  * [Environment variable expansion in .mcp.json](https://docs.anthropic.com/en/docs/claude-code/mcp#environment-variable-expansion-in-mcp-json)
  * [Practical examples](https://docs.anthropic.com/en/docs/claude-code/mcp#practical-examples)
  * [Example: Monitor errors with Sentry](https://docs.anthropic.com/en/docs/claude-code/mcp#example%3A-monitor-errors-with-sentry)
  * [Authenticate with remote MCP servers](https://docs.anthropic.com/en/docs/claude-code/mcp#authenticate-with-remote-mcp-servers)
  * [Add MCP servers from JSON configuration](https://docs.anthropic.com/en/docs/claude-code/mcp#add-mcp-servers-from-json-configuration)
  * [Import MCP servers from Claude Desktop](https://docs.anthropic.com/en/docs/claude-code/mcp#import-mcp-servers-from-claude-desktop)
  * [Use Claude Code as an MCP server](https://docs.anthropic.com/en/docs/claude-code/mcp#use-claude-code-as-an-mcp-server)
  * [Use MCP resources](https://docs.anthropic.com/en/docs/claude-code/mcp#use-mcp-resources)
  * [Reference MCP resources](https://docs.anthropic.com/en/docs/claude-code/mcp#reference-mcp-resources)
  * [Use MCP prompts as slash commands](https://docs.anthropic.com/en/docs/claude-code/mcp#use-mcp-prompts-as-slash-commands)
  * [Execute MCP prompts](https://docs.anthropic.com/en/docs/claude-code/mcp#execute-mcp-prompts)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/memory -->

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
Manage Claude's memory
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
# Manage Claude's memory
Copy page
Learn how to manage Claude Code’s memory across sessions with different memory locations and best practices.
Claude Code can remember your preferences across sessions, like style guidelines and common commands in your workflow.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/memory#determine-memory-type)
Determine memory type
Claude Code offers four memory locations in a hierarchical structure, each serving a different purpose:
Memory Type | Location | Purpose | Use Case Examples | Shared With  
---|---|---|---|---  
**Enterprise policy** | macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`  
Linux: `/etc/claude-code/CLAUDE.md`  
Windows: `C:\ProgramData\ClaudeCode\CLAUDE.md` | Organization-wide instructions managed by IT/DevOps | Company coding standards, security policies, compliance requirements | All users in organization  
**Project memory** | `./CLAUDE.md` | Team-shared instructions for the project | Project architecture, coding standards, common workflows | Team members via source control  
**User memory** | `~/.claude/CLAUDE.md` | Personal preferences for all projects | Code styling preferences, personal tooling shortcuts | Just you (all projects)  
**Project memory (local)** | `./CLAUDE.local.md` | Personal project-specific preferences |  _(Deprecated, see below)_ Your sandbox URLs, preferred test data | Just you (current project)  
All memory files are automatically loaded into Claude Code’s context when launched. Files higher in the hierarchy take precedence and are loaded first, providing a foundation that more specific memories build upon.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/memory#claude-md-imports)
CLAUDE.md imports
CLAUDE.md files can import additional files using `@path/to/import` syntax. The following example imports 3 files:
Copy
```
See @README for project overview and @package.json for available npm commands for this project.

# Additional Instructions
- git workflow @docs/git-instructions.md

```

Both relative and absolute paths are allowed. In particular, importing files in user’s home dir is a convenient way for your team members to provide individual instructions that are not checked into the repository. Previously CLAUDE.local.md served a similar purpose, but is now deprecated in favor of imports since they work better across multiple git worktrees.
Copy
```
# Individual Preferences
- @~/.claude/my-project-instructions.md

```

To avoid potential collisions, imports are not evaluated inside markdown code spans and code blocks.
Copy
```
This code span will not be treated as an import: `@anthropic-ai/claude-code`

```

Imported files can recursively import additional files, with a max-depth of 5 hops. You can see what memory files are loaded by running `/memory` command.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/memory#how-claude-looks-up-memories)
How Claude looks up memories
Claude Code reads memories recursively: starting in the cwd, Claude Code recurses up to (but not including) the root directory _/_ and reads any CLAUDE.md or CLAUDE.local.md files it finds. This is especially convenient when working in large repositories where you run Claude Code in _foo/bar/_ , and have memories in both _foo/CLAUDE.md_ and _foo/bar/CLAUDE.md_.
Claude will also discover CLAUDE.md nested in subtrees under your current working directory. Instead of loading them at launch, they are only included when Claude reads files in those subtrees.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/memory#quickly-add-memories-with-the-%23-shortcut)
Quickly add memories with the `#` shortcut
The fastest way to add a memory is to start your input with the `#` character:
Copy
```
# Always use descriptive variable names

```

You’ll be prompted to select which memory file to store this in.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/memory#directly-edit-memories-with-%2Fmemory)
Directly edit memories with `/memory`
Use the `/memory` slash command during a session to open any memory file in your system editor for more extensive additions or organization.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/memory#set-up-project-memory)
Set up project memory
Suppose you want to set up a CLAUDE.md file to store important project information, conventions, and frequently used commands.
Bootstrap a CLAUDE.md for your codebase with the following command:
Copy
```
> /init 

```

Tips:
  * Include frequently used commands (build, test, lint) to avoid repeated searches
  * Document code style preferences and naming conventions
  * Add important architectural patterns specific to your project
  * CLAUDE.md memories can be used for both instructions shared with your team and for your individual preferences.


## 
[​](https://docs.anthropic.com/en/docs/claude-code/memory#organization-level-memory-management)
Organization-level memory management
Enterprise organizations can deploy centrally managed CLAUDE.md files that apply to all users.
To set up organization-level memory management:
  1. Create the enterprise memory file in the appropriate location for your operating system:


  * macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`
  * Linux/WSL: `/etc/claude-code/CLAUDE.md`
  * Windows: `C:\ProgramData\ClaudeCode\CLAUDE.md`


  1. Deploy via your configuration management system (MDM, Group Policy, Ansible, etc.) to ensure consistent distribution across all developer machines.


## 
[​](https://docs.anthropic.com/en/docs/claude-code/memory#memory-best-practices)
Memory best practices
  * **Be specific** : “Use 2-space indentation” is better than “Format code properly”.
  * **Use structure to organize** : Format each individual memory as a bullet point and group related memories under descriptive markdown headings.
  * **Review periodically** : Update memories as your project evolves to ensure Claude is always using the most up to date information and context.


Was this page helpful?
YesNo
[Terminal configuration](https://docs.anthropic.com/en/docs/claude-code/terminal-config)[Status line configuration](https://docs.anthropic.com/en/docs/claude-code/statusline)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Determine memory type](https://docs.anthropic.com/en/docs/claude-code/memory#determine-memory-type)
  * [CLAUDE.md imports](https://docs.anthropic.com/en/docs/claude-code/memory#claude-md-imports)
  * [How Claude looks up memories](https://docs.anthropic.com/en/docs/claude-code/memory#how-claude-looks-up-memories)
  * [Quickly add memories with the # shortcut](https://docs.anthropic.com/en/docs/claude-code/memory#quickly-add-memories-with-the-%23-shortcut)
  * [Directly edit memories with /memory](https://docs.anthropic.com/en/docs/claude-code/memory#directly-edit-memories-with-%2Fmemory)
  * [Set up project memory](https://docs.anthropic.com/en/docs/claude-code/memory#set-up-project-memory)
  * [Organization-level memory management](https://docs.anthropic.com/en/docs/claude-code/memory#organization-level-memory-management)
  * [Memory best practices](https://docs.anthropic.com/en/docs/claude-code/memory#memory-best-practices)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/monitoring-usage -->

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
Administration
Monitoring
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


Administration
# Monitoring
Copy page
Learn how to enable and configure OpenTelemetry for Claude Code.
Claude Code supports OpenTelemetry (OTel) metrics and events for monitoring and observability.
All metrics are time series data exported via OpenTelemetry’s standard metrics protocol, and events are exported via OpenTelemetry’s logs/events protocol. It is the user’s responsibility to ensure their metrics and logs backends are properly configured and that the aggregation granularity meets their monitoring requirements.
OpenTelemetry support is currently in beta and details are subject to change.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#quick-start)
Quick Start
Configure OpenTelemetry using environment variables:
Copy
```
# 1. Enable telemetry
export CLAUDE_CODE_ENABLE_TELEMETRY=1

# 2. Choose exporters (both are optional - configure only what you need)
export OTEL_METRICS_EXPORTER=otlp       # Options: otlp, prometheus, console
export OTEL_LOGS_EXPORTER=otlp          # Options: otlp, console

# 3. Configure OTLP endpoint (for OTLP exporter)
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317

# 4. Set authentication (if required)
export OTEL_EXPORTER_OTLP_HEADERS="Authorization=Bearer your-token"

# 5. For debugging: reduce export intervals
export OTEL_METRIC_EXPORT_INTERVAL=10000  # 10 seconds (default: 60000ms)
export OTEL_LOGS_EXPORT_INTERVAL=5000     # 5 seconds (default: 5000ms)

# 6. Run Claude Code
claude

```

The default export intervals are 60 seconds for metrics and 5 seconds for logs. During setup, you may want to use shorter intervals for debugging purposes. Remember to reset these for production use.
For full configuration options, see the [OpenTelemetry specification](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/exporter.md#configuration-options).
## 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#administrator-configuration)
Administrator Configuration
Administrators can configure OpenTelemetry settings for all users through the managed settings file. This allows for centralized control of telemetry settings across an organization. See the [settings precedence](https://docs.anthropic.com/en/docs/claude-code/settings#settings-precedence) for more information about how settings are applied.
The managed settings file is located at:
  * macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`
  * Linux and WSL: `/etc/claude-code/managed-settings.json`
  * Windows: `C:\ProgramData\ClaudeCode\managed-settings.json`


Example managed settings configuration:
Copy
```
{
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp",
    "OTEL_LOGS_EXPORTER": "otlp",
    "OTEL_EXPORTER_OTLP_PROTOCOL": "grpc",
    "OTEL_EXPORTER_OTLP_ENDPOINT": "http://collector.company.com:4317",
    "OTEL_EXPORTER_OTLP_HEADERS": "Authorization=Bearer company-token"
  }
}

```

Managed settings can be distributed via MDM (Mobile Device Management) or other device management solutions. Environment variables defined in the managed settings file have high precedence and cannot be overridden by users.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#configuration-details)
Configuration Details
### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#common-configuration-variables)
Common Configuration Variables
Environment Variable | Description | Example Values  
---|---|---  
`CLAUDE_CODE_ENABLE_TELEMETRY` | Enables telemetry collection (required) | `1`  
`OTEL_METRICS_EXPORTER` | Metrics exporter type(s) (comma-separated) |  `console`, `otlp`, `prometheus`  
`OTEL_LOGS_EXPORTER` | Logs/events exporter type(s) (comma-separated) |  `console`, `otlp`  
`OTEL_EXPORTER_OTLP_PROTOCOL` | Protocol for OTLP exporter (all signals) |  `grpc`, `http/json`, `http/protobuf`  
`OTEL_EXPORTER_OTLP_ENDPOINT` | OTLP collector endpoint (all signals) | `http://localhost:4317`  
`OTEL_EXPORTER_OTLP_METRICS_PROTOCOL` | Protocol for metrics (overrides general) |  `grpc`, `http/json`, `http/protobuf`  
`OTEL_EXPORTER_OTLP_METRICS_ENDPOINT` | OTLP metrics endpoint (overrides general) | `http://localhost:4318/v1/metrics`  
`OTEL_EXPORTER_OTLP_LOGS_PROTOCOL` | Protocol for logs (overrides general) |  `grpc`, `http/json`, `http/protobuf`  
`OTEL_EXPORTER_OTLP_LOGS_ENDPOINT` | OTLP logs endpoint (overrides general) | `http://localhost:4318/v1/logs`  
`OTEL_EXPORTER_OTLP_HEADERS` | Authentication headers for OTLP | `Authorization=Bearer token`  
`OTEL_EXPORTER_OTLP_METRICS_CLIENT_KEY` | Client key for mTLS authentication | Path to client key file  
`OTEL_EXPORTER_OTLP_METRICS_CLIENT_CERTIFICATE` | Client certificate for mTLS authentication | Path to client cert file  
`OTEL_METRIC_EXPORT_INTERVAL` | Export interval in milliseconds (default: 60000) |  `5000`, `60000`  
`OTEL_LOGS_EXPORT_INTERVAL` | Logs export interval in milliseconds (default: 5000) |  `1000`, `10000`  
`OTEL_LOG_USER_PROMPTS` | Enable logging of user prompt content (default: disabled) |  `1` to enable  
### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#metrics-cardinality-control)
Metrics Cardinality Control
The following environment variables control which attributes are included in metrics to manage cardinality:
Environment Variable | Description | Default Value | Example to Disable  
---|---|---|---  
`OTEL_METRICS_INCLUDE_SESSION_ID` | Include session.id attribute in metrics | `true` | `false`  
`OTEL_METRICS_INCLUDE_VERSION` | Include app.version attribute in metrics | `false` | `true`  
`OTEL_METRICS_INCLUDE_ACCOUNT_UUID` | Include user.account_uuid attribute in metrics | `true` | `false`  
These variables help control the cardinality of metrics, which affects storage requirements and query performance in your metrics backend. Lower cardinality generally means better performance and lower storage costs but less granular data for analysis.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#dynamic-headers)
Dynamic Headers
For enterprise environments that require dynamic authentication, you can configure a script to generate headers dynamically:
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#settings-configuration)
Settings Configuration
Add to your `.claude/settings.json`:
Copy
```
{
  "otelHeadersHelper": "/bin/generate_opentelemetry_headers.sh"
}

```

#### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#script-requirements)
Script Requirements
The script must output valid JSON with string key-value pairs representing HTTP headers:
Copy
```
#!/bin/bash
# Example: Multiple headers
echo "{\"Authorization\": \"Bearer $(get-token.sh)\", \"X-API-Key\": \"$(get-api-key.sh)\"}"

```

#### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#important-limitations)
Important Limitations
**Headers are fetched only at startup, not during runtime.** This is due to OpenTelemetry exporter architecture limitations.
For scenarios requiring frequent token refresh, use an OpenTelemetry Collector as a proxy that can refresh its own headers.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#multi-team-organization-support)
Multi-Team Organization Support
Organizations with multiple teams or departments can add custom attributes to distinguish between different groups using the `OTEL_RESOURCE_ATTRIBUTES` environment variable:
Copy
```
# Add custom attributes for team identification
export OTEL_RESOURCE_ATTRIBUTES="department=engineering,team.id=platform,cost_center=eng-123"

```

These custom attributes will be included in all metrics and events, allowing you to:
  * Filter metrics by team or department
  * Track costs per cost center
  * Create team-specific dashboards
  * Set up alerts for specific teams


**Important formatting requirements for OTEL_RESOURCE_ATTRIBUTES:**
The `OTEL_RESOURCE_ATTRIBUTES` environment variable follows the [W3C Baggage specification](https://www.w3.org/TR/baggage/), which has strict formatting requirements:
  * **No spaces allowed** : Values cannot contain spaces. For example, `user.organizationName=My Company` is invalid
  * **Format** : Must be comma-separated key=value pairs: `key1=value1,key2=value2`
  * **Allowed characters** : Only US-ASCII characters excluding control characters, whitespace, double quotes, commas, semicolons, and backslashes
  * **Special characters** : Characters outside the allowed range must be percent-encoded


**Examples:**
Copy
```
# ❌ Invalid - contains spaces
export OTEL_RESOURCE_ATTRIBUTES="org.name=John's Organization"

# ✅ Valid - use underscores or camelCase instead
export OTEL_RESOURCE_ATTRIBUTES="org.name=Johns_Organization"
export OTEL_RESOURCE_ATTRIBUTES="org.name=JohnsOrganization"

# ✅ Valid - percent-encode special characters if needed
export OTEL_RESOURCE_ATTRIBUTES="org.name=John%27s%20Organization"

```

Note: Quoting the entire key=value pair (e.g., `"key=value with spaces"`) is not supported by the OpenTelemetry specification and will result in attributes being prefixed with quotes.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#example-configurations)
Example Configurations
Copy
```
# Console debugging (1-second intervals)
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=console
export OTEL_METRIC_EXPORT_INTERVAL=1000

# OTLP/gRPC
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317

# Prometheus
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=prometheus

# Multiple exporters
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=console,otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=http/json

# Different endpoints/backends for metrics and logs
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=otlp
export OTEL_LOGS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_METRICS_PROTOCOL=http/protobuf
export OTEL_EXPORTER_OTLP_METRICS_ENDPOINT=http://metrics.company.com:4318
export OTEL_EXPORTER_OTLP_LOGS_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_LOGS_ENDPOINT=http://logs.company.com:4317

# Metrics only (no events/logs)
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317

# Events/logs only (no metrics)
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_LOGS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#available-metrics-and-events)
Available Metrics and Events
### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
Standard Attributes
All metrics and events share these standard attributes:
Attribute | Description | Controlled By  
---|---|---  
`session.id` | Unique session identifier |  `OTEL_METRICS_INCLUDE_SESSION_ID` (default: true)  
`app.version` | Current Claude Code version |  `OTEL_METRICS_INCLUDE_VERSION` (default: false)  
`organization.id` | Organization UUID (when authenticated) | Always included when available  
`user.account_uuid` | Account UUID (when authenticated) |  `OTEL_METRICS_INCLUDE_ACCOUNT_UUID` (default: true)  
`terminal.type` | Terminal type (e.g., `iTerm.app`, `vscode`, `cursor`, `tmux`) | Always included when detected  
### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#metrics)
Metrics
Claude Code exports the following metrics:
Metric Name | Description | Unit  
---|---|---  
`claude_code.session.count` | Count of CLI sessions started | count  
`claude_code.lines_of_code.count` | Count of lines of code modified | count  
`claude_code.pull_request.count` | Number of pull requests created | count  
`claude_code.commit.count` | Number of git commits created | count  
`claude_code.cost.usage` | Cost of the Claude Code session | USD  
`claude_code.token.usage` | Number of tokens used | tokens  
`claude_code.code_edit_tool.decision` | Count of code editing tool permission decisions | count  
`claude_code.active_time.total` | Total active time in seconds | s  
### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#metric-details)
Metric Details
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#session-counter)
Session Counter
Incremented at the start of each session.
**Attributes** :
  * All [standard attributes](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)


#### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#lines-of-code-counter)
Lines of Code Counter
Incremented when code is added or removed.
**Attributes** :
  * All [standard attributes](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
  * `type`: (`"added"`, `"removed"`)


#### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#pull-request-counter)
Pull Request Counter
Incremented when creating pull requests via Claude Code.
**Attributes** :
  * All [standard attributes](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)


#### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#commit-counter)
Commit Counter
Incremented when creating git commits via Claude Code.
**Attributes** :
  * All [standard attributes](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)


#### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#cost-counter)
Cost Counter
Incremented after each API request.
**Attributes** :
  * All [standard attributes](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
  * `model`: Model identifier (e.g., “claude-3-5-sonnet-20241022”)


#### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#token-counter)
Token Counter
Incremented after each API request.
**Attributes** :
  * All [standard attributes](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
  * `type`: (`"input"`, `"output"`, `"cacheRead"`, `"cacheCreation"`)
  * `model`: Model identifier (e.g., “claude-3-5-sonnet-20241022”)


#### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#code-edit-tool-decision-counter)
Code Edit Tool Decision Counter
Incremented when user accepts or rejects Edit, MultiEdit, Write, or NotebookEdit tool usage.
**Attributes** :
  * All [standard attributes](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
  * `tool`: Tool name (`"Edit"`, `"MultiEdit"`, `"Write"`, `"NotebookEdit"`)
  * `decision`: User decision (`"accept"`, `"reject"`)
  * `language`: Programming language of the edited file (e.g., `"TypeScript"`, `"Python"`, `"JavaScript"`, `"Markdown"`). Returns `"unknown"` for unrecognized file extensions.


#### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#active-time-counter)
Active Time Counter
Tracks actual time spent actively using Claude Code (not idle time). This metric is incremented during user interactions such as typing prompts or receiving responses.
**Attributes** :
  * All [standard attributes](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)


### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#events)
Events
Claude Code exports the following events via OpenTelemetry logs/events (when `OTEL_LOGS_EXPORTER` is configured):
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#user-prompt-event)
User Prompt Event
Logged when a user submits a prompt.
**Event Name** : `claude_code.user_prompt`
**Attributes** :
  * All [standard attributes](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
  * `event.name`: `"user_prompt"`
  * `event.timestamp`: ISO 8601 timestamp
  * `prompt_length`: Length of the prompt
  * `prompt`: Prompt content (redacted by default, enable with `OTEL_LOG_USER_PROMPTS=1`)


#### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#tool-result-event)
Tool Result Event
Logged when a tool completes execution.
**Event Name** : `claude_code.tool_result`
**Attributes** :
  * All [standard attributes](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
  * `event.name`: `"tool_result"`
  * `event.timestamp`: ISO 8601 timestamp
  * `tool_name`: Name of the tool
  * `success`: `"true"` or `"false"`
  * `duration_ms`: Execution time in milliseconds
  * `error`: Error message (if failed)
  * `decision`: Either `"accept"` or `"reject"`
  * `source`: Decision source - `"config"`, `"user_permanent"`, `"user_temporary"`, `"user_abort"`, or `"user_reject"`
  * `tool_parameters`: JSON string containing tool-specific parameters (when available) 
    * For Bash tool: includes `bash_command`, `full_command`, `timeout`, `description`, `sandbox`


#### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#api-request-event)
API Request Event
Logged for each API request to Claude.
**Event Name** : `claude_code.api_request`
**Attributes** :
  * All [standard attributes](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
  * `event.name`: `"api_request"`
  * `event.timestamp`: ISO 8601 timestamp
  * `model`: Model used (e.g., “claude-3-5-sonnet-20241022”)
  * `cost_usd`: Estimated cost in USD
  * `duration_ms`: Request duration in milliseconds
  * `input_tokens`: Number of input tokens
  * `output_tokens`: Number of output tokens
  * `cache_read_tokens`: Number of tokens read from cache
  * `cache_creation_tokens`: Number of tokens used for cache creation


#### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#api-error-event)
API Error Event
Logged when an API request to Claude fails.
**Event Name** : `claude_code.api_error`
**Attributes** :
  * All [standard attributes](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
  * `event.name`: `"api_error"`
  * `event.timestamp`: ISO 8601 timestamp
  * `model`: Model used (e.g., “claude-3-5-sonnet-20241022”)
  * `error`: Error message
  * `status_code`: HTTP status code (if applicable)
  * `duration_ms`: Request duration in milliseconds
  * `attempt`: Attempt number (for retried requests)


#### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#tool-decision-event)
Tool Decision Event
Logged when a tool permission decision is made (accept/reject).
**Event Name** : `claude_code.tool_decision`
**Attributes** :
  * All [standard attributes](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
  * `event.name`: `"tool_decision"`
  * `event.timestamp`: ISO 8601 timestamp
  * `tool_name`: Name of the tool (e.g., “Read”, “Edit”, “MultiEdit”, “Write”, “NotebookEdit”, etc.)
  * `decision`: Either `"accept"` or `"reject"`
  * `source`: Decision source - `"config"`, `"user_permanent"`, `"user_temporary"`, `"user_abort"`, or `"user_reject"`


## 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#interpreting-metrics-and-events-data)
Interpreting Metrics and Events Data
The metrics exported by Claude Code provide valuable insights into usage patterns and productivity. Here are some common visualizations and analyses you can create:
### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#usage-monitoring)
Usage Monitoring
Metric | Analysis Opportunity  
---|---  
`claude_code.token.usage` | Break down by `type` (input/output), user, team, or model  
`claude_code.session.count` | Track adoption and engagement over time  
`claude_code.lines_of_code.count` | Measure productivity by tracking code additions/removals  
`claude_code.commit.count` & `claude_code.pull_request.count` | Understand impact on development workflows  
### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#cost-monitoring)
Cost Monitoring
The `claude_code.cost.usage` metric helps with:
  * Tracking usage trends across teams or individuals
  * Identifying high-usage sessions for optimization


Cost metrics are approximations. For official billing data, refer to your API provider (Anthropic Console, AWS Bedrock, or Google Cloud Vertex).
### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#alerting-and-segmentation)
Alerting and Segmentation
Common alerts to consider:
  * Cost spikes
  * Unusual token consumption
  * High session volume from specific users


All metrics can be segmented by `user.account_uuid`, `organization.id`, `session.id`, `model`, and `app.version`.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#event-analysis)
Event Analysis
The event data provides detailed insights into Claude Code interactions:
**Tool Usage Patterns** : Analyze tool result events to identify:
  * Most frequently used tools
  * Tool success rates
  * Average tool execution times
  * Error patterns by tool type


**Performance Monitoring** : Track API request durations and tool execution times to identify performance bottlenecks.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#backend-considerations)
Backend Considerations
Your choice of metrics and logs backends will determine the types of analyses you can perform:
### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#for-metrics%3A)
For Metrics:
  * **Time series databases (e.g., Prometheus)** : Rate calculations, aggregated metrics
  * **Columnar stores (e.g., ClickHouse)** : Complex queries, unique user analysis
  * **Full-featured observability platforms (e.g., Honeycomb, Datadog)** : Advanced querying, visualization, alerting


### 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#for-events%2Flogs%3A)
For Events/Logs:
  * **Log aggregation systems (e.g., Elasticsearch, Loki)** : Full-text search, log analysis
  * **Columnar stores (e.g., ClickHouse)** : Structured event analysis
  * **Full-featured observability platforms (e.g., Honeycomb, Datadog)** : Correlation between metrics and events


For organizations requiring Daily/Weekly/Monthly Active User (DAU/WAU/MAU) metrics, consider backends that support efficient unique value queries.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#service-information)
Service Information
All metrics and events are exported with the following resource attributes:
  * `service.name`: `claude-code`
  * `service.version`: Current Claude Code version
  * `os.type`: Operating system type (e.g., `linux`, `darwin`, `windows`)
  * `os.version`: Operating system version string
  * `host.arch`: Host architecture (e.g., `amd64`, `arm64`)
  * `wsl.version`: WSL version number (only present when running on Windows Subsystem for Linux)
  * Meter Name: `com.anthropic.claude_code`


## 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#roi-measurement-resources)
ROI Measurement Resources
For a comprehensive guide on measuring return on investment for Claude Code, including telemetry setup, cost analysis, productivity metrics, and automated reporting, see the [Claude Code ROI Measurement Guide](https://github.com/anthropics/claude-code-monitoring-guide). This repository provides ready-to-use Docker Compose configurations, Prometheus and OpenTelemetry setups, and templates for generating productivity reports integrated with tools like Linear.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#security%2Fprivacy-considerations)
Security/Privacy Considerations
  * Telemetry is opt-in and requires explicit configuration
  * Sensitive information like API keys or file contents are never included in metrics or events
  * User prompt content is redacted by default - only prompt length is recorded. To enable user prompt logging, set `OTEL_LOG_USER_PROMPTS=1`


Was this page helpful?
YesNo
[Data usage](https://docs.anthropic.com/en/docs/claude-code/data-usage)[Costs](https://docs.anthropic.com/en/docs/claude-code/costs)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Quick Start](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#quick-start)
  * [Administrator Configuration](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#administrator-configuration)
  * [Configuration Details](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#configuration-details)
  * [Common Configuration Variables](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#common-configuration-variables)
  * [Metrics Cardinality Control](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#metrics-cardinality-control)
  * [Dynamic Headers](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#dynamic-headers)
  * [Settings Configuration](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#settings-configuration)
  * [Script Requirements](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#script-requirements)
  * [Important Limitations](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#important-limitations)
  * [Multi-Team Organization Support](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#multi-team-organization-support)
  * [Example Configurations](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#example-configurations)
  * [Available Metrics and Events](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#available-metrics-and-events)
  * [Standard Attributes](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
  * [Metrics](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#metrics)
  * [Metric Details](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#metric-details)
  * [Session Counter](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#session-counter)
  * [Lines of Code Counter](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#lines-of-code-counter)
  * [Pull Request Counter](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#pull-request-counter)
  * [Commit Counter](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#commit-counter)
  * [Cost Counter](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#cost-counter)
  * [Token Counter](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#token-counter)
  * [Code Edit Tool Decision Counter](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#code-edit-tool-decision-counter)
  * [Active Time Counter](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#active-time-counter)
  * [Events](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#events)
  * [User Prompt Event](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#user-prompt-event)
  * [Tool Result Event](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#tool-result-event)
  * [API Request Event](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#api-request-event)
  * [API Error Event](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#api-error-event)
  * [Tool Decision Event](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#tool-decision-event)
  * [Interpreting Metrics and Events Data](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#interpreting-metrics-and-events-data)
  * [Usage Monitoring](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#usage-monitoring)
  * [Cost Monitoring](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#cost-monitoring)
  * [Alerting and Segmentation](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#alerting-and-segmentation)
  * [Event Analysis](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#event-analysis)
  * [Backend Considerations](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#backend-considerations)
  * [For Metrics:](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#for-metrics%3A)
  * [For Events/Logs:](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#for-events%2Flogs%3A)
  * [Service Information](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#service-information)
  * [ROI Measurement Resources](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#roi-measurement-resources)
  * [Security/Privacy Considerations](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage#security%2Fprivacy-considerations)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/output-styles -->

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


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/overview -->

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
Getting started
Claude Code overview
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


Getting started
# Claude Code overview
Copy page
Learn about Claude Code, Anthropic’s agentic coding tool that lives in your terminal and helps you turn ideas into code faster than ever before.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#get-started-in-30-seconds)
Get started in 30 seconds
Prerequisites: [Node.js 18 or newer](https://nodejs.org/en/download/)
Copy
```
# Install Claude Code
npm install -g @anthropic-ai/claude-code

# Navigate to your project
cd your-awesome-project

# Start coding with Claude
claude

```

That’s it! You’re ready to start coding with Claude. [Continue with Quickstart (5 mins) →](https://docs.anthropic.com/en/docs/claude-code/quickstart)
(Got specific setup needs or hit issues? See [advanced setup](https://docs.anthropic.com/en/docs/claude-code/setup) or [troubleshooting](https://docs.anthropic.com/en/docs/claude-code/troubleshooting).)
## 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#what-claude-code-does-for-you)
What Claude Code does for you
  * **Build features from descriptions** : Tell Claude what you want to build in plain English. It will make a plan, write the code, and ensure it works.
  * **Debug and fix issues** : Describe a bug or paste an error message. Claude Code will analyze your codebase, identify the problem, and implement a fix.
  * **Navigate any codebase** : Ask anything about your team’s codebase, and get a thoughtful answer back. Claude Code maintains awareness of your entire project structure, can find up-to-date information from the web, and with [MCP](https://docs.anthropic.com/en/docs/claude-code/mcp) can pull from external datasources like Google Drive, Figma, and Slack.
  * **Automate tedious tasks** : Fix fiddly lint issues, resolve merge conflicts, and write release notes. Do all this in a single command from your developer machines, or automatically in CI.


## 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#why-developers-love-claude-code)
Why developers love Claude Code
  * **Works in your terminal** : Not another chat window. Not another IDE. Claude Code meets you where you already work, with the tools you already love.
  * **Takes action** : Claude Code can directly edit files, run commands, and create commits. Need more? [MCP](https://docs.anthropic.com/en/docs/claude-code/mcp) lets Claude read your design docs in Google Drive, update your tickets in Jira, or use _your_ custom developer tooling.
  * **Unix philosophy** : Claude Code is composable and scriptable. `tail -f app.log | claude -p "Slack me if you see any anomalies appear in this log stream"` _works_. Your CI can run `claude -p "If there are new text strings, translate them into French and raise a PR for @lang-fr-team to review"`.
  * **Enterprise-ready** : Use Anthropic’s API, or host on AWS or GCP. Enterprise-grade [security](https://docs.anthropic.com/en/docs/claude-code/security), [privacy](https://docs.anthropic.com/en/docs/claude-code/data-usage), and [compliance](https://trust.anthropic.com/) is built-in.


## 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#next-steps)
Next steps
## [Quickstart See Claude Code in action with practical examples ](https://docs.anthropic.com/en/docs/claude-code/quickstart)## [Common workflows Step-by-step guides for common workflows ](https://docs.anthropic.com/en/docs/claude-code/common-workflows)## [Troubleshooting Solutions for common issues with Claude Code ](https://docs.anthropic.com/en/docs/claude-code/troubleshooting)## [IDE setup Add Claude Code to your IDE ](https://docs.anthropic.com/en/docs/claude-code/ide-integrations)
## 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#additional-resources)
Additional resources
## [Host on AWS or GCP Configure Claude Code with Amazon Bedrock or Google Vertex AI ](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations)## [Settings Customize Claude Code for your workflow ](https://docs.anthropic.com/en/docs/claude-code/settings)## [Commands Learn about CLI commands and controls ](https://docs.anthropic.com/en/docs/claude-code/cli-reference)## [Reference implementation Clone our development container reference implementation ](https://github.com/anthropics/claude-code/tree/main/.devcontainer)## [Security Discover Claude Code’s safeguards and best practices for safe usage ](https://docs.anthropic.com/en/docs/claude-code/security)## [Privacy and data usage Understand how Claude Code handles your data ](https://docs.anthropic.com/en/docs/claude-code/data-usage)
Was this page helpful?
YesNo
[Quickstart](https://docs.anthropic.com/en/docs/claude-code/quickstart)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Get started in 30 seconds](https://docs.anthropic.com/en/docs/claude-code/overview#get-started-in-30-seconds)
  * [What Claude Code does for you](https://docs.anthropic.com/en/docs/claude-code/overview#what-claude-code-does-for-you)
  * [Why developers love Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview#why-developers-love-claude-code)
  * [Next steps](https://docs.anthropic.com/en/docs/claude-code/overview#next-steps)
  * [Additional resources](https://docs.anthropic.com/en/docs/claude-code/overview#additional-resources)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/quickstart -->

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
Getting started
Quickstart
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


Getting started
# Quickstart
Copy page
Welcome to Claude Code!
This quickstart guide will have you using AI-powered coding assistance in just a few minutes. By the end, you’ll understand how to use Claude Code for common development tasks.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/quickstart#before-you-begin)
Before you begin
Make sure you have:
  * A terminal or command prompt open
  * A code project to work with


## 
[​](https://docs.anthropic.com/en/docs/claude-code/quickstart#step-1%3A-install-claude-code)
Step 1: Install Claude Code
### 
[​](https://docs.anthropic.com/en/docs/claude-code/quickstart#npm-install)
NPM Install
If you have [Node.js 18 or newer installed](https://nodejs.org/en/download/):
Copy
```
npm install -g @anthropic-ai/claude-code

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/quickstart#native-install)
Native Install
Alternatively, try our new native install, now in beta.
**macOS, Linux, WSL:**
Copy
```
curl -fsSL claude.ai/install.sh | bash

```

**Windows PowerShell:**
Copy
```
irm https://claude.ai/install.ps1 | iex

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/quickstart#step-2%3A-start-your-first-session)
Step 2: Start your first session
Open your terminal in any project directory and start Claude Code:
Copy
```
cd /path/to/your/project
claude

```

You’ll see the Claude Code prompt inside a new interactive session:
Copy
```
✻ Welcome to Claude Code!

...

> Try "create a util logging.py that..." 

```

Your credentials are securely stored on your system. Learn more in [Credential Management](https://docs.anthropic.com/en/docs/claude-code/iam#credential-management).
## 
[​](https://docs.anthropic.com/en/docs/claude-code/quickstart#step-3%3A-ask-your-first-question)
Step 3: Ask your first question
Let’s start with understanding your codebase. Try one of these commands:
Copy
```
> what does this project do?

```

Claude will analyze your files and provide a summary. You can also ask more specific questions:
Copy
```
> what technologies does this project use?

```

Copy
```
> where is the main entry point?

```

Copy
```
> explain the folder structure

```

You can also ask Claude about its own capabilities:
Copy
```
> what can Claude Code do?

```

Copy
```
> how do I use slash commands in Claude Code?

```

Copy
```
> can Claude Code work with Docker?

```

Claude Code reads your files as needed - you don’t have to manually add context. Claude also has access to its own documentation and can answer questions about its features and capabilities.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/quickstart#step-4%3A-make-your-first-code-change)
Step 4: Make your first code change
Now let’s make Claude Code do some actual coding. Try a simple task:
Copy
```
> add a hello world function to the main file

```

Claude Code will:
  1. Find the appropriate file
  2. Show you the proposed changes
  3. Ask for your approval
  4. Make the edit


Claude Code always asks for permission before modifying files. You can approve individual changes or enable “Accept all” mode for a session.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/quickstart#step-5%3A-use-git-with-claude-code)
Step 5: Use Git with Claude Code
Claude Code makes Git operations conversational:
Copy
```
> what files have I changed?

```

Copy
```
> commit my changes with a descriptive message

```

You can also prompt for more complex Git operations:
Copy
```
> create a new branch called feature/quickstart

```

Copy
```
> show me the last 5 commits

```

Copy
```
> help me resolve merge conflicts

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/quickstart#step-6%3A-fix-a-bug-or-add-a-feature)
Step 6: Fix a bug or add a feature
Claude is proficient at debugging and feature implementation.
Describe what you want in natural language:
Copy
```
> add input validation to the user registration form

```

Or fix existing issues:
Copy
```
> there's a bug where users can submit empty forms - fix it

```

Claude Code will:
  * Locate the relevant code
  * Understand the context
  * Implement a solution
  * Run tests if available


## 
[​](https://docs.anthropic.com/en/docs/claude-code/quickstart#step-7%3A-test-out-other-common-workflows)
Step 7: Test out other common workflows
There are a number of ways to work with Claude:
**Refactor code**
Copy
```
> refactor the authentication module to use async/await instead of callbacks

```

**Write tests**
Copy
```
> write unit tests for the calculator functions

```

**Update documentation**
Copy
```
> update the README with installation instructions

```

**Code review**
Copy
```
> review my changes and suggest improvements

```

**Remember** : Claude Code is your AI pair programmer. Talk to it like you would a helpful colleague - describe what you want to achieve, and it will help you get there.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/quickstart#essential-commands)
Essential commands
Here are the most important commands for daily use:
Command | What it does | Example  
---|---|---  
`claude` | Start interactive mode | `claude`  
`claude "task"` | Run a one-time task | `claude "fix the build error"`  
`claude -p "query"` | Run one-off query, then exit | `claude -p "explain this function"`  
`claude -c` | Continue most recent conversation | `claude -c`  
`claude -r` | Resume a previous conversation | `claude -r`  
`claude commit` | Create a Git commit | `claude commit`  
`/clear` | Clear conversation history | `> /clear`  
`/help` | Show available commands | `> /help`  
`exit` or Ctrl+C | Exit Claude Code | `> exit`  
See the [CLI reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference) for a complete list of commands.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/quickstart#pro-tips-for-beginners)
Pro tips for beginners
Be specific with your requests
Instead of: “fix the bug”
Try: “fix the login bug where users see a blank screen after entering wrong credentials”
Use step-by-step instructions
Break complex tasks into steps:
Copy
```
> 1. create a new database table for user profiles

```

Copy
```
> 2. create an API endpoint to get and update user profiles

```

Copy
```
> 3. build a webpage that allows users to see and edit their information

```

Let Claude explore first
Before making changes, let Claude understand your code:
Copy
```
> analyze the database schema

```

Copy
```
> build a dashboard showing products that are most frequently returned by our UK customers

```

Save time with shortcuts
  * Use Tab for command completion
  * Press ↑ for command history
  * Type `/` to see all slash commands


## 
[​](https://docs.anthropic.com/en/docs/claude-code/quickstart#what%E2%80%99s-next%3F)
What’s next?
Now that you’ve learned the basics, explore more advanced features:
## [Common workflows Step-by-step guides for common tasks ](https://docs.anthropic.com/en/docs/claude-code/common-workflows)## [CLI reference Master all commands and options ](https://docs.anthropic.com/en/docs/claude-code/cli-reference)## [Configuration Customize Claude Code for your workflow ](https://docs.anthropic.com/en/docs/claude-code/settings)
## 
[​](https://docs.anthropic.com/en/docs/claude-code/quickstart#getting-help)
Getting help
  * **In Claude Code** : Type `/help` or ask “how do I…”
  * **Documentation** : You’re here! Browse other guides
  * **Community** : Join our [Discord](https://www.anthropic.com/discord) for tips and support


Was this page helpful?
YesNo
[Overview](https://docs.anthropic.com/en/docs/claude-code/overview)[Common workflows](https://docs.anthropic.com/en/docs/claude-code/common-workflows)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Before you begin](https://docs.anthropic.com/en/docs/claude-code/quickstart#before-you-begin)
  * [Step 1: Install Claude Code](https://docs.anthropic.com/en/docs/claude-code/quickstart#step-1%3A-install-claude-code)
  * [NPM Install](https://docs.anthropic.com/en/docs/claude-code/quickstart#npm-install)
  * [Native Install](https://docs.anthropic.com/en/docs/claude-code/quickstart#native-install)
  * [Step 2: Start your first session](https://docs.anthropic.com/en/docs/claude-code/quickstart#step-2%3A-start-your-first-session)
  * [Step 3: Ask your first question](https://docs.anthropic.com/en/docs/claude-code/quickstart#step-3%3A-ask-your-first-question)
  * [Step 4: Make your first code change](https://docs.anthropic.com/en/docs/claude-code/quickstart#step-4%3A-make-your-first-code-change)
  * [Step 5: Use Git with Claude Code](https://docs.anthropic.com/en/docs/claude-code/quickstart#step-5%3A-use-git-with-claude-code)
  * [Step 6: Fix a bug or add a feature](https://docs.anthropic.com/en/docs/claude-code/quickstart#step-6%3A-fix-a-bug-or-add-a-feature)
  * [Step 7: Test out other common workflows](https://docs.anthropic.com/en/docs/claude-code/quickstart#step-7%3A-test-out-other-common-workflows)
  * [Essential commands](https://docs.anthropic.com/en/docs/claude-code/quickstart#essential-commands)
  * [Pro tips for beginners](https://docs.anthropic.com/en/docs/claude-code/quickstart#pro-tips-for-beginners)
  * [What’s next?](https://docs.anthropic.com/en/docs/claude-code/quickstart#what%E2%80%99s-next%3F)
  * [Getting help](https://docs.anthropic.com/en/docs/claude-code/quickstart#getting-help)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/sdk -->

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
Claude Code SDK
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
# Claude Code SDK
Copy page
Build custom AI agents with the Claude Code SDK
## 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#why-use-the-claude-code-sdk%3F)
Why use the Claude Code SDK?
The Claude Code SDK provides all the building blocks you need to build production-ready agents:
  * **Optimized Claude integration** : Automatic prompt caching and performance optimizations
  * **Rich tool ecosystem** : File operations, code execution, web search, and MCP extensibility
  * **Advanced permissions** : Fine-grained control over agent capabilities
  * **Production essentials** : Built-in error handling, session management, and monitoring


## 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#what-can-you-build-with-the-sdk%3F)
What can you build with the SDK?
Here are some example agent types you can create:
**Coding agents:**
  * SRE agents that diagnose and fix production issues
  * Security review bots that audit code for vulnerabilities
  * Oncall engineering assistants that triage incidents
  * Code review agents that enforce style and best practices


**Business agents:**
  * Legal assistants that review contracts and compliance
  * Finance advisors that analyze reports and forecasts
  * Customer support agents that resolve technical issues
  * Content creation assistants for marketing teams


The SDK is currently available in TypeScript and Python, with a command line interface (CLI) for quick prototyping.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#quick-start)
Quick start
Get your first agent running in under 5 minutes:
1
Install the SDK
  * Command line
  * TypeScript
  * Python


Install `@anthropic-ai/claude-code` from NPM:
Copy
```
npm install -g @anthropic-ai/claude-code

```

Install `@anthropic-ai/claude-code` from NPM:
Copy
```
npm install -g @anthropic-ai/claude-code

```

Install `@anthropic-ai/claude-code` from NPM:
Copy
```
npm install -g @anthropic-ai/claude-code

```

Install `claude-code-sdk` from PyPI and `@anthropic-ai/claude-code` from NPM:
Copy
```
pip install claude-code-sdk
npm install -g @anthropic-ai/claude-code  # Required dependency

```

(Optional) Install IPython for interactive development:
Copy
```
pip install ipython

```

2
Set your API key
Get your API key from the [Anthropic Console](https://console.anthropic.com/) and set the `ANTHROPIC_API_KEY` environment variable:
Copy
```
export ANTHROPIC_API_KEY="your-api-key-here"

```

3
Create your first agent
Create one of these example agents:
  * Command line
  * TypeScript
  * Python


Copy
```
# Create a simple legal assistant
claude -p "Review this contract clause for potential issues: 'The party agrees to unlimited liability...'" \
  --append-system-prompt "You are a legal assistant. Identify risks and suggest improvements."

```

Copy
```
# Create a simple legal assistant
claude -p "Review this contract clause for potential issues: 'The party agrees to unlimited liability...'" \
  --append-system-prompt "You are a legal assistant. Identify risks and suggest improvements."

```

Copy
```
// legal-agent.ts
import { query } from "@anthropic-ai/claude-code";

// Create a simple legal assistant
for await (const message of query({
  prompt: "Review this contract clause for potential issues: 'The party agrees to unlimited liability...'",
  options: {
    systemPrompt: "You are a legal assistant. Identify risks and suggest improvements.",
    maxTurns: 2
  }
})) {
  if (message.type === "result") {
    console.log(message.result);
  }
}

```

Copy
```
# legal-agent.py
import asyncio
from claude_code_sdk import ClaudeSDKClient, ClaudeCodeOptions

async def main():
    async with ClaudeSDKClient(
        options=ClaudeCodeOptions(
            system_prompt="You are a legal assistant. Identify risks and suggest improvements.",
            max_turns=2
        )
    ) as client:
        # Send the query
        await client.query(
            "Review this contract clause for potential issues: 'The party agrees to unlimited liability...'"
        )
        
        # Stream the response
        async for message in client.receive_response():
            if hasattr(message, 'content'):
                # Print streaming content as it arrives
                for block in message.content:
                    if hasattr(block, 'text'):
                        print(block.text, end='', flush=True)

if __name__ == "__main__":
    asyncio.run(main())

```

4
Run the agent
  * Command line
  * TypeScript
  * Python


Copy and paste the command above directly into your terminal.
Copy and paste the command above directly into your terminal.
  1. Set up project:


Copy
```
npm init -y
npm install @anthropic-ai/claude-code tsx

```

  1. Add `"type": "module"` to your package.json
  2. Save the code above as `legal-agent.ts`, then run:


Copy
```
npx tsx legal-agent.ts

```

Save the code above as `legal-agent.py`, then run:
Copy
```
python legal-agent.py

```

For [IPython](https://ipython.org/)/Jupyter notebooks, you can run the code directly in a cell:
Copy
```
await main()

```

Each example above creates a working agent that will:
  * Analyze the prompt using Claude’s reasoning capabilities
  * Plan a multi-step approach to solve the problem
  * Execute actions using tools like file operations, bash commands, and web search
  * Provide actionable recommendations based on the analysis


## 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#core-usage)
Core usage
### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#overview)
Overview
The Claude Code SDK allows you to interface with Claude Code in non-interactive mode from your applications.
  * Command line
  * TypeScript
  * Python


**Prerequisites**
  * Node.js 18+
  * `@anthropic-ai/claude-code` from NPM


**Basic usage**
The primary command-line interface to Claude Code is the `claude` command. Use the `--print` (or `-p`) flag to run in non-interactive mode and print the final result:
Copy
```
claude -p "Analyze system performance" \
  --append-system-prompt "You are a performance engineer" \
  --allowedTools "Bash,Read,WebSearch" \
  --permission-mode acceptEdits \
  --cwd /path/to/project

```

**Configuration**
The SDK leverages all the CLI options available in Claude Code. Here are the key ones for SDK usage:
Flag | Description | Example  
---|---|---  
`--print`, `-p` | Run in non-interactive mode | `claude -p "query"`  
`--output-format` | Specify output format (`text`, `json`, `stream-json`) | `claude -p --output-format json`  
`--resume`, `-r` | Resume a conversation by session ID | `claude --resume abc123`  
`--continue`, `-c` | Continue the most recent conversation | `claude --continue`  
`--verbose` | Enable verbose logging | `claude --verbose`  
`--append-system-prompt` | Append to system prompt (only with `--print`) | `claude --append-system-prompt "Custom instruction"`  
`--allowedTools` | Space-separated list of allowed tools, or   
  
string of comma-separated list of allowed tools |  `claude --allowedTools mcp__slack mcp__filesystem`  
  
`claude --allowedTools "Bash(npm install),mcp__filesystem"`  
`--disallowedTools` | Space-separated list of denied tools, or   
  
string of comma-separated list of denied tools |  `claude --disallowedTools mcp__splunk mcp__github`  
  
`claude --disallowedTools "Bash(git commit),mcp__github"`  
`--mcp-config` | Load MCP servers from a JSON file | `claude --mcp-config servers.json`  
`--permission-prompt-tool` | MCP tool for handling permission prompts (only with `--print`) | `claude --permission-prompt-tool mcp__auth__prompt`  
For a complete list of CLI options and features, see the [CLI reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference) documentation.
**Prerequisites**
  * Node.js 18+
  * `@anthropic-ai/claude-code` from NPM


**Basic usage**
The primary command-line interface to Claude Code is the `claude` command. Use the `--print` (or `-p`) flag to run in non-interactive mode and print the final result:
Copy
```
claude -p "Analyze system performance" \
  --append-system-prompt "You are a performance engineer" \
  --allowedTools "Bash,Read,WebSearch" \
  --permission-mode acceptEdits \
  --cwd /path/to/project

```

**Configuration**
The SDK leverages all the CLI options available in Claude Code. Here are the key ones for SDK usage:
Flag | Description | Example  
---|---|---  
`--print`, `-p` | Run in non-interactive mode | `claude -p "query"`  
`--output-format` | Specify output format (`text`, `json`, `stream-json`) | `claude -p --output-format json`  
`--resume`, `-r` | Resume a conversation by session ID | `claude --resume abc123`  
`--continue`, `-c` | Continue the most recent conversation | `claude --continue`  
`--verbose` | Enable verbose logging | `claude --verbose`  
`--append-system-prompt` | Append to system prompt (only with `--print`) | `claude --append-system-prompt "Custom instruction"`  
`--allowedTools` | Space-separated list of allowed tools, or   
  
string of comma-separated list of allowed tools |  `claude --allowedTools mcp__slack mcp__filesystem`  
  
`claude --allowedTools "Bash(npm install),mcp__filesystem"`  
`--disallowedTools` | Space-separated list of denied tools, or   
  
string of comma-separated list of denied tools |  `claude --disallowedTools mcp__splunk mcp__github`  
  
`claude --disallowedTools "Bash(git commit),mcp__github"`  
`--mcp-config` | Load MCP servers from a JSON file | `claude --mcp-config servers.json`  
`--permission-prompt-tool` | MCP tool for handling permission prompts (only with `--print`) | `claude --permission-prompt-tool mcp__auth__prompt`  
For a complete list of CLI options and features, see the [CLI reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference) documentation.
**Prerequisites**
  * Node.js 18+
  * `@anthropic-ai/claude-code` from NPM


To view the TypeScript SDK source code, visit the [`@anthropic-ai/claude-code` page on NPM](https://www.npmjs.com/package/@anthropic-ai/claude-code?activeTab=code).
**Basic usage**
The primary interface via the TypeScript SDK is the `query` function, which returns an async iterator that streams messages as they arrive:
Copy
```
import { query } from "@anthropic-ai/claude-code";

for await (const message of query({
  prompt: "Analyze system performance",
  abortController: new AbortController(),
  options: {
    maxTurns: 5,
    systemPrompt: "You are a performance engineer",
    allowedTools: ["Bash", "Read", "WebSearch"]
  }
})) {
  if (message.type === "result") {
    console.log(message.result);
  }
}

```

**Configuration**
The TypeScript SDK accepts all arguments supported by the [command line](https://docs.anthropic.com/en/docs/claude-code/cli-reference), as well as the following additional options:
Argument | Description | Default  
---|---|---  
`abortController` | Abort controller | `new AbortController()`  
`cwd` | Current working directory | `process.cwd()`  
`executable` | Which JavaScript runtime to use |  `node` when running with Node.js, `bun` when running with Bun  
`executableArgs` | Arguments to pass to the executable | `[]`  
`pathToClaudeCodeExecutable` | Path to the Claude Code executable | Executable that ships with `@anthropic-ai/claude-code`  
`permissionMode` | Permission mode for the session |  `"default"` (options: `"default"`, `"acceptEdits"`, `"plan"`, `"bypassPermissions"`)  
**Prerequisites**
  * Python 3.10+
  * `claude-code-sdk` from PyPI
  * Node.js 18+
  * `@anthropic-ai/claude-code` from NPM


To view the Python SDK source code, see the [`claude-code-sdk`](https://github.com/anthropics/claude-code-sdk-python) repo.
For interactive development, use [IPython](https://ipython.org/): `pip install ipython`
**Basic usage**
The Python SDK provides two primary interfaces:
  1. The `ClaudeSDKClient` class (Recommended)


Best for streaming responses, multi-turn conversations, and interactive applications:
Copy
```
import asyncio
from claude_code_sdk import ClaudeSDKClient, ClaudeCodeOptions

async def main():
    async with ClaudeSDKClient(
        options=ClaudeCodeOptions(
            system_prompt="You are a performance engineer",
            allowed_tools=["Bash", "Read", "WebSearch"],
            max_turns=5
        )
    ) as client:
        await client.query("Analyze system performance")
        
        # Stream responses
        async for message in client.receive_response():
            if hasattr(message, 'content'):
                for block in message.content:
                    if hasattr(block, 'text'):
                        print(block.text, end='', flush=True)

# Run as script
asyncio.run(main())

# Or in IPython/Jupyter: await main()

```

The SDK also supports passing structured messages and image inputs:
Copy
```
from claude_code_sdk import ClaudeSDKClient, ClaudeCodeOptions

async with ClaudeSDKClient() as client:
    # Text message
    await client.query("Analyze this code for security issues")
    
    # Message with image reference (image will be read by Claude's Read tool)
    await client.query("Explain what's shown in screenshot.png")
    
    # Multiple messages in sequence
    messages = [
        "First, analyze the architecture diagram in diagram.png",
        "Now suggest improvements based on the diagram",
        "Finally, generate implementation code"
    ]
    
    for msg in messages:
        await client.query(msg)
        async for response in client.receive_response():
            # Process each response
            pass

# The SDK handles image files through Claude's built-in Read tool
# Supported formats: PNG, JPG, PDF, and other common formats

```

The Python examples on this page use `asyncio`, but you can also use `anyio`.
  1. The `query` function


For simple, one-shot queries:
Copy
```
from claude_code_sdk import query, ClaudeCodeOptions

async for message in query(
    prompt="Analyze system performance",
    options=ClaudeCodeOptions(system_prompt="You are a performance engineer")
):
    if type(message).__name__ == "ResultMessage":
        print(message.result)

```

**Configuration**
As the Python SDK accepts all arguments supported by the [command line](https://docs.anthropic.com/en/docs/claude-code/cli-reference) through the `ClaudeCodeOptions` class.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#authentication)
Authentication
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#anthropic-api-key)
Anthropic API key
For basic authentication, retrieve an Anthropic API key from the [Anthropic Console](https://console.anthropic.com/) and set the `ANTHROPIC_API_KEY` environment variable, as demonstrated in the [Quick start](https://docs.anthropic.com/en/docs/claude-code/sdk#quick-start).
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#third-party-api-credentials)
Third-party API credentials
The SDK also supports authentication via third-party API providers:
  * **Amazon Bedrock** : Set `CLAUDE_CODE_USE_BEDROCK=1` environment variable and configure AWS credentials
  * **Google Vertex AI** : Set `CLAUDE_CODE_USE_VERTEX=1` environment variable and configure Google Cloud credentials


For detailed configuration instructions for third-party providers, see the [Amazon Bedrock](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock) and [Google Vertex AI](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai) documentation.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#multi-turn-conversations)
Multi-turn conversations
For multi-turn conversations, you can resume conversations or continue from the most recent session:
  * Command line
  * TypeScript
  * Python


Copy
```
# Continue the most recent conversation
claude --continue "Now refactor this for better performance"

# Resume a specific conversation by session ID
claude --resume 550e8400-e29b-41d4-a716-446655440000 "Update the tests"

# Resume in non-interactive mode
claude --resume 550e8400-e29b-41d4-a716-446655440000 "Fix all linting issues" --no-interactive

```

Copy
```
# Continue the most recent conversation
claude --continue "Now refactor this for better performance"

# Resume a specific conversation by session ID
claude --resume 550e8400-e29b-41d4-a716-446655440000 "Update the tests"

# Resume in non-interactive mode
claude --resume 550e8400-e29b-41d4-a716-446655440000 "Fix all linting issues" --no-interactive

```

Copy
```
import { query } from "@anthropic-ai/claude-code";

// Continue most recent conversation
for await (const message of query({
  prompt: "Now refactor this for better performance",
  options: { continueSession: true }
})) {
  if (message.type === "result") console.log(message.result);
}

// Resume specific session
for await (const message of query({
  prompt: "Update the tests",
  options: { 
    resumeSessionId: "550e8400-e29b-41d4-a716-446655440000",
    maxTurns: 3
  }
})) {
  if (message.type === "result") console.log(message.result);
}

```

Copy
```
import asyncio
from claude_code_sdk import ClaudeSDKClient, ClaudeCodeOptions, query

# Method 1: Using ClaudeSDKClient for persistent conversations
async def multi_turn_conversation():
    async with ClaudeSDKClient() as client:
        # First query
        await client.query("Let's refactor the payment module")
        async for msg in client.receive_response():
            # Process first response
            pass
        
        # Continue in same session
        await client.query("Now add comprehensive error handling")
        async for msg in client.receive_response():
            # Process continuation
            pass
        
        # The conversation context is maintained throughout

# Method 2: Using query function with session management
async def resume_session():
    # Continue most recent conversation
    async for message in query(
        prompt="Now refactor this for better performance",
        options=ClaudeCodeOptions(continue_conversation=True)
    ):
        if type(message).__name__ == "ResultMessage":
            print(message.result)

    # Resume specific session
    async for message in query(
        prompt="Update the tests", 
        options=ClaudeCodeOptions(
            resume="550e8400-e29b-41d4-a716-446655440000",
            max_turns=3
        )
    ):
        if type(message).__name__ == "ResultMessage":
            print(message.result)

# Run the examples
asyncio.run(multi_turn_conversation())

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#using-plan-mode)
Using Plan Mode
Plan Mode allows Claude to analyze code without making modifications, useful for code reviews and planning changes.
  * Command line
  * TypeScript
  * Python


Copy
```
claude -p "Review this code" --permission-mode plan

```

Copy
```
claude -p "Review this code" --permission-mode plan

```

Copy
```
import { query } from "@anthropic-ai/claude-code";

for await (const message of query({
  prompt: "Your prompt here",
  options: {
    permissionMode: 'plan'
  }
})) {
  if (message.type === "result") {
    console.log(message.result);
  }
}

```

Copy
```
from claude_code_sdk import ClaudeSDKClient, ClaudeCodeOptions

async with ClaudeSDKClient(
    options=ClaudeCodeOptions(permission_mode='plan')
) as client:
    await client.query("Your prompt here")

```

Plan Mode restricts editing, file creation, and command execution. See [permission modes](https://docs.anthropic.com/en/docs/claude-code/iam#permission-modes) for details.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#custom-system-prompts)
Custom system prompts
System prompts define your agent’s role, expertise, and behavior. This is where you specify what kind of agent you’re building:
  * Command line
  * TypeScript
  * Python


Copy
```
# SRE incident response agent
claude -p "API is down, investigate" \
  --append-system-prompt "You are an SRE expert. Diagnose issues systematically and provide actionable solutions."

# Legal document review agent  
claude -p "Review this contract" \
  --append-system-prompt "You are a corporate lawyer. Identify risks, suggest improvements, and ensure compliance."

# Append to default system prompt
claude -p "Refactor this function" \
  --append-system-prompt "Always include comprehensive error handling and unit tests."

```

Copy
```
# SRE incident response agent
claude -p "API is down, investigate" \
  --append-system-prompt "You are an SRE expert. Diagnose issues systematically and provide actionable solutions."

# Legal document review agent  
claude -p "Review this contract" \
  --append-system-prompt "You are a corporate lawyer. Identify risks, suggest improvements, and ensure compliance."

# Append to default system prompt
claude -p "Refactor this function" \
  --append-system-prompt "Always include comprehensive error handling and unit tests."

```

Copy
```
import { query } from "@anthropic-ai/claude-code";

// SRE incident response agent
for await (const message of query({
  prompt: "API is down, investigate",
  options: {
    systemPrompt: "You are an SRE expert. Diagnose issues systematically and provide actionable solutions.",
    maxTurns: 3
  }
})) {
  if (message.type === "result") console.log(message.result);
}

// Append to default system prompt
for await (const message of query({
  prompt: "Refactor this function",
  options: {
    appendSystemPrompt: "Always include comprehensive error handling and unit tests.",
    maxTurns: 2
  }
})) {
  if (message.type === "result") console.log(message.result);
}

```

Copy
```
import asyncio
from claude_code_sdk import ClaudeSDKClient, ClaudeCodeOptions

async def specialized_agents():
    # SRE incident response agent with streaming
    async with ClaudeSDKClient(
        options=ClaudeCodeOptions(
            system_prompt="You are an SRE expert. Diagnose issues systematically and provide actionable solutions.",
            max_turns=3
        )
    ) as sre_agent:
        await sre_agent.query("API is down, investigate")
        
        # Stream the diagnostic process
        async for message in sre_agent.receive_response():
            if hasattr(message, 'content'):
                for block in message.content:
                    if hasattr(block, 'text'):
                        print(block.text, end='', flush=True)
    
    # Legal review agent with custom prompt
    async with ClaudeSDKClient(
        options=ClaudeCodeOptions(
            append_system_prompt="Always include comprehensive error handling and unit tests.",
            max_turns=2
        )
    ) as dev_agent:
        await dev_agent.query("Refactor this function")
        
        # Collect full response
        full_response = []
        async for message in dev_agent.receive_response():
            if type(message).__name__ == "ResultMessage":
                print(message.result)

asyncio.run(specialized_agents())

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#advanced-usage)
Advanced Usage
### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#custom-tools-via-mcp)
Custom tools via MCP
The Model Context Protocol (MCP) lets you give your agents custom tools and capabilities. This is crucial for building specialized agents that need domain-specific integrations.
**Example agent tool configurations:**
Copy
```
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {"SLACK_TOKEN": "your-slack-token"}
    },
    "jira": {
      "command": "npx", 
      "args": ["-y", "@modelcontextprotocol/server-jira"],
      "env": {"JIRA_TOKEN": "your-jira-token"}
    },
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {"DB_CONNECTION_STRING": "your-db-url"}
    }
  }
}

```

**Usage examples:**
  * Command line
  * TypeScript
  * Python


Copy
```
# SRE agent with monitoring tools
claude -p "Investigate the payment service outage" \
  --mcp-config sre-tools.json \
  --allowedTools "mcp__datadog,mcp__pagerduty,mcp__kubernetes" \
  --append-system-prompt "You are an SRE. Use monitoring data to diagnose issues."

# Customer support agent with CRM access
claude -p "Help resolve customer ticket #12345" \
  --mcp-config support-tools.json \
  --allowedTools "mcp__zendesk,mcp__stripe,mcp__user_db" \
  --append-system-prompt "You are a technical support specialist."

```

Copy
```
# SRE agent with monitoring tools
claude -p "Investigate the payment service outage" \
  --mcp-config sre-tools.json \
  --allowedTools "mcp__datadog,mcp__pagerduty,mcp__kubernetes" \
  --append-system-prompt "You are an SRE. Use monitoring data to diagnose issues."

# Customer support agent with CRM access
claude -p "Help resolve customer ticket #12345" \
  --mcp-config support-tools.json \
  --allowedTools "mcp__zendesk,mcp__stripe,mcp__user_db" \
  --append-system-prompt "You are a technical support specialist."

```

Copy
```
import { query } from "@anthropic-ai/claude-code";

// SRE agent with monitoring tools
for await (const message of query({
  prompt: "Investigate the payment service outage",
  options: {
    mcpConfig: "sre-tools.json",
    allowedTools: ["mcp__datadog", "mcp__pagerduty", "mcp__kubernetes"],
    systemPrompt: "You are an SRE. Use monitoring data to diagnose issues.",
    maxTurns: 4
  }
})) {
  if (message.type === "result") console.log(message.result);
}

```

Copy
```
import asyncio
from claude_code_sdk import ClaudeSDKClient, ClaudeCodeOptions

async def mcp_enabled_agent():
    # Legal agent with document access and streaming
    # Note: Configure your MCP servers as needed
    mcp_servers = {
        # Example configuration - uncomment and configure as needed:
        # "docusign": {
        #     "command": "npx",
        #     "args": ["-y", "@modelcontextprotocol/server-docusign"],
        #     "env": {"API_KEY": "your-key"}
        # }
    }
    
    async with ClaudeSDKClient(
        options=ClaudeCodeOptions(
            mcp_servers=mcp_servers,
            allowed_tools=["mcp__docusign", "mcp__compliance_db"],
            system_prompt="You are a corporate lawyer specializing in contract review.",
            max_turns=4
        )
    ) as client:
        await client.query("Review this contract for compliance risks")
        
        # Monitor tool usage and responses
        async for message in client.receive_response():
            if hasattr(message, 'content'):
                for block in message.content:
                    if hasattr(block, 'type'):
                        if block.type == 'tool_use':
                            print(f"\n[Using tool: {block.name}]\n")
                        elif hasattr(block, 'text'):
                            print(block.text, end='', flush=True)
                    elif hasattr(block, 'text'):
                        print(block.text, end='', flush=True)
            
            if type(message).__name__ == "ResultMessage":
                print(f"\n\nReview complete. Total cost: ${message.total_cost_usd:.4f}")

asyncio.run(mcp_enabled_agent())

```

When using MCP tools, you must explicitly allow them using the `--allowedTools` flag. MCP tool names follow the pattern `mcp__<serverName>__<toolName>` where:
  * `serverName` is the key from your MCP configuration file
  * `toolName` is the specific tool provided by that server


This security measure ensures that MCP tools are only used when explicitly permitted.
If you specify just the server name (i.e., `mcp__<serverName>`), all tools from that server will be allowed.
Glob patterns (e.g., `mcp__go*`) are not supported.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#custom-permission-prompt-tool)
Custom permission prompt tool
Optionally, use `--permission-prompt-tool` to pass in an MCP tool that we will use to check whether or not the user grants the model permissions to invoke a given tool. When the model invokes a tool the following happens:
  1. We first check permission settings: all [settings.json files](https://docs.anthropic.com/en/docs/claude-code/settings), as well as `--allowedTools` and `--disallowedTools` passed into the SDK; if one of these allows or denies the tool call, we proceed with the tool call
  2. Otherwise, we invoke the MCP tool you provided in `--permission-prompt-tool`


The `--permission-prompt-tool` MCP tool is passed the tool name and input, and must return a JSON-stringified payload with the result. The payload must be one of:
Copy
```
// tool call is allowed
{
  "behavior": "allow",
  "updatedInput": {...}, // updated input, or just return back the original input
}

// tool call is denied
{
  "behavior": "deny",
  "message": "..." // human-readable string explaining why the permission was denied
}

```

**Implementation examples:**
  * Command line
  * TypeScript
  * Python


Copy
```
# Use with your MCP server configuration
claude -p "Analyze and fix the security issues" \
  --permission-prompt-tool mcp__security__approval_prompt \
  --mcp-config security-tools.json \
  --allowedTools "Read,Grep" \
  --disallowedTools "Bash(rm*),Write"

# With custom permission rules
claude -p "Refactor the codebase" \
  --permission-prompt-tool mcp__custom__permission_check \
  --mcp-config custom-config.json \
  --output-format json

```

Copy
```
# Use with your MCP server configuration
claude -p "Analyze and fix the security issues" \
  --permission-prompt-tool mcp__security__approval_prompt \
  --mcp-config security-tools.json \
  --allowedTools "Read,Grep" \
  --disallowedTools "Bash(rm*),Write"

# With custom permission rules
claude -p "Refactor the codebase" \
  --permission-prompt-tool mcp__custom__permission_check \
  --mcp-config custom-config.json \
  --output-format json

```

Copy
```
const server = new McpServer({
  name: "Test permission prompt MCP Server",
  version: "0.0.1",
});

server.tool(
  "approval_prompt",
  'Simulate a permission check - approve if the input contains "allow", otherwise deny',
  {
    tool_name: z.string().describe("The name of the tool requesting permission"),
    input: z.object({}).passthrough().describe("The input for the tool"),
    tool_use_id: z.string().optional().describe("The unique tool use request ID"),
  },
  async ({ tool_name, input }) => {
    return {
      content: [
        {
          type: "text",
          text: JSON.stringify(
            JSON.stringify(input).includes("allow")
              ? {
                  behavior: "allow",
                  updatedInput: input,
                }
              : {
                  behavior: "deny",
                  message: "Permission denied by test approval_prompt tool",
                }
          ),
        },
      ],
    };
  }
);

// Use in SDK
import { query } from "@anthropic-ai/claude-code";

for await (const message of query({
  prompt: "Analyze the codebase",
  options: {
    permissionPromptTool: "mcp__test-server__approval_prompt",
    mcpConfig: "my-config.json",
    allowedTools: ["Read", "Grep"]
  }
})) {
  if (message.type === "result") console.log(message.result);
}

```

Copy
```
import asyncio
from claude_code_sdk import ClaudeSDKClient, ClaudeCodeOptions

async def use_permission_prompt():
    """Example using custom permission prompt tool"""
    
    # MCP server configuration
    mcp_servers = {
        # Example configuration - uncomment and configure as needed:
        # "security": {
        #     "command": "npx",
        #     "args": ["-y", "@modelcontextprotocol/server-security"],
        #     "env": {"API_KEY": "your-key"}
        # }
    }
    
    async with ClaudeSDKClient(
        options=ClaudeCodeOptions(
            permission_prompt_tool_name="mcp__security__approval_prompt",  # Changed from permission_prompt_tool
            mcp_servers=mcp_servers,
            allowed_tools=["Read", "Grep"],
            disallowed_tools=["Bash(rm*)", "Write"],
            system_prompt="You are a security auditor"
        )
    ) as client:
        await client.query("Analyze and fix the security issues")
        
        # Monitor tool usage and permissions
        async for message in client.receive_response():
            if hasattr(message, 'content'):
                for block in message.content:
                    if hasattr(block, 'type'):  # Added check for 'type' attribute
                        if block.type == 'tool_use':
                            print(f"[Tool: {block.name}] ", end='')
                    if hasattr(block, 'text'):
                        print(block.text, end='', flush=True)
            
            # Check for permission denials in error messages
            if type(message).__name__ == "ErrorMessage":
                if hasattr(message, 'error') and "Permission denied" in str(message.error):
                    print(f"\n⚠️ Permission denied: {message.error}")

# Example MCP server implementation (Python)
# This would be in your MCP server code
async def approval_prompt(tool_name: str, input: dict, tool_use_id: str = None):
    """Custom permission prompt handler"""
    # Your custom logic here
    if "allow" in str(input):
        return json.dumps({
            "behavior": "allow",
            "updatedInput": input
        })
    else:
        return json.dumps({
            "behavior": "deny",
            "message": f"Permission denied for {tool_name}"
        })

asyncio.run(use_permission_prompt())

```

Usage notes:
  * Use `updatedInput` to tell the model that the permission prompt mutated its input; otherwise, set `updatedInput` to the original input, as in the example above. For example, if the tool shows a file edit diff to the user and lets them edit the diff manually, the permission prompt tool should return that updated edit.
  * The payload must be JSON-stringified


## 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#output-formats)
Output formats
The SDK supports multiple output formats:
### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#text-output-default)
Text output (default)
  * Command line
  * TypeScript
  * Python


Copy
```
claude -p "Explain file src/components/Header.tsx"
# Output: This is a React component showing...

```

Copy
```
claude -p "Explain file src/components/Header.tsx"
# Output: This is a React component showing...

```

Copy
```
// Default text output
for await (const message of query({
  prompt: "Explain file src/components/Header.tsx"
})) {
  if (message.type === "result") {
    console.log(message.result);
    // Output: This is a React component showing...
  }
}

```

Copy
```
# Default text output with streaming
async with ClaudeSDKClient() as client:
    await client.query("Explain file src/components/Header.tsx")
    
    # Stream text as it arrives
    async for message in client.receive_response():
        if hasattr(message, 'content'):
            for block in message.content:
                if hasattr(block, 'text'):
                    print(block.text, end='', flush=True)
                    # Output streams in real-time: This is a React component showing...

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#json-output)
JSON output
Returns structured data including metadata:
  * Command line
  * TypeScript
  * Python


Copy
```
claude -p "How does the data layer work?" --output-format json

```

Copy
```
claude -p "How does the data layer work?" --output-format json

```

Copy
```
// Collect all messages for JSON-like access
const messages = [];
for await (const message of query({
  prompt: "How does the data layer work?"
})) {
  messages.push(message);
}

// Access result message with metadata
const result = messages.find(m => m.type === "result");
console.log({
  result: result.result,
  cost: result.total_cost_usd,
  duration: result.duration_ms
});

```

Copy
```
# Collect all messages with metadata
async with ClaudeSDKClient() as client:
    await client.query("How does the data layer work?")
    
    messages = []
    result_data = None
    
    async for message in client.receive_messages():
        messages.append(message)
        
        # Capture result message with metadata
        if type(message).__name__ == "ResultMessage":
            result_data = {
                "result": message.result,
                "cost": message.total_cost_usd,
                "duration": message.duration_ms,
                "num_turns": message.num_turns,
                "session_id": message.session_id
            }
            break
    
    print(result_data)

```

Response format:
Copy
```
{
  "type": "result",
  "subtype": "success",
  "total_cost_usd": 0.003,
  "is_error": false,
  "duration_ms": 1234,
  "duration_api_ms": 800,
  "num_turns": 6,
  "result": "The response text here...",
  "session_id": "abc123"
}

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#streaming-json-output)
Streaming JSON output
Streams each message as it is received:
Copy
```
$ claude -p "Build an application" --output-format stream-json

```

Each conversation begins with an initial `init` system message, followed by a list of user and assistant messages, followed by a final `result` system message with stats. Each message is emitted as a separate JSON object.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#message-schema)
Message schema
Messages returned from the JSON API are strictly typed according to the following schema:
Copy
```
type SDKMessage =
  // An assistant message
  | {
      type: "assistant";
      message: Message; // from Anthropic SDK
      session_id: string;
    }

  // A user message
  | {
      type: "user";
      message: MessageParam; // from Anthropic SDK
      session_id: string;
    }

  // Emitted as the last message
  | {
      type: "result";
      subtype: "success";
      duration_ms: float;
      duration_api_ms: float;
      is_error: boolean;
      num_turns: int;
      result: string;
      session_id: string;
      total_cost_usd: float;
    }

  // Emitted as the last message, when we've reached the maximum number of turns
  | {
      type: "result";
      subtype: "error_max_turns" | "error_during_execution";
      duration_ms: float;
      duration_api_ms: float;
      is_error: boolean;
      num_turns: int;
      session_id: string;
      total_cost_usd: float;
    }

  // Emitted as the first message at the start of a conversation
  | {
      type: "system";
      subtype: "init";
      apiKeySource: string;
      cwd: string;
      session_id: string;
      tools: string[];
      mcp_servers: {
        name: string;
        status: string;
      }[];
      model: string;
      permissionMode: "default" | "acceptEdits" | "bypassPermissions" | "plan";
    };

```

We will soon publish these types in a JSONSchema-compatible format. We use semantic versioning for the main Claude Code package to communicate breaking changes to this format.
`Message` and `MessageParam` types are available in Anthropic SDKs. For example, see the Anthropic [TypeScript](https://github.com/anthropics/anthropic-sdk-typescript) and [Python](https://github.com/anthropics/anthropic-sdk-python/) SDKs.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#input-formats)
Input formats
The SDK supports multiple input formats:
### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#text-input-default)
Text input (default)
  * Command line
  * TypeScript
  * Python


Copy
```
# Direct argument
claude -p "Explain this code"

# From stdin
echo "Explain this code" | claude -p

```

Copy
```
# Direct argument
claude -p "Explain this code"

# From stdin
echo "Explain this code" | claude -p

```

Copy
```
// Direct prompt
for await (const message of query({
  prompt: "Explain this code"
})) {
  if (message.type === "result") console.log(message.result);
}

// From variable
const userInput = "Explain this code";
for await (const message of query({ prompt: userInput })) {
  if (message.type === "result") console.log(message.result);
}

```

Copy
```
import asyncio
from claude_code_sdk import ClaudeSDKClient

async def process_inputs():
    async with ClaudeSDKClient() as client:
        # Text input
        await client.query("Explain this code")
        async for message in client.receive_response():
            # Process streaming response
            pass
        
        # Image input (Claude will use Read tool automatically)
        await client.query("What's in this diagram? screenshot.png")
        async for message in client.receive_response():
            # Process image analysis
            pass
        
        # Multiple inputs with mixed content
        inputs = [
            "Analyze the architecture in diagram.png",
            "Compare it with best practices",
            "Generate improved version"
        ]
        
        for prompt in inputs:
            await client.query(prompt)
            async for message in client.receive_response():
                # Process each response
                pass

asyncio.run(process_inputs())

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#streaming-json-input)
Streaming JSON input
A stream of messages provided via `stdin` where each message represents a user turn. This allows multiple turns of a conversation without re-launching the `claude` binary and allows providing guidance to the model while it is processing a request.
Each message is a JSON ‘User message’ object, following the same format as the output message schema. Messages are formatted using the [jsonl](https://jsonlines.org/) format where each line of input is a complete JSON object. Streaming JSON input requires `-p` and `--output-format stream-json`.
Currently this is limited to text-only user messages.
Copy
```
$ echo '{"type":"user","message":{"role":"user","content":[{"type":"text","text":"Explain this code"}]}}' | claude -p --output-format=stream-json --input-format=stream-json --verbose

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#agent-integration-examples)
Agent integration examples
### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#sre-incident-response-bot)
SRE incident response bot
  * Command line
  * TypeScript
  * Python


Copy
```
#!/bin/bash

# Automated incident response agent
investigate_incident() {
    local incident_description="$1"
    local severity="${2:-medium}"
    
    claude -p "Incident: $incident_description (Severity: $severity)" \
      --append-system-prompt "You are an SRE expert. Diagnose the issue, assess impact, and provide immediate action items." \
      --output-format json \
      --allowedTools "Bash,Read,WebSearch,mcp__datadog" \
      --mcp-config monitoring-tools.json
}

# Usage
investigate_incident "Payment API returning 500 errors" "high"

```

Copy
```
#!/bin/bash

# Automated incident response agent
investigate_incident() {
    local incident_description="$1"
    local severity="${2:-medium}"
    
    claude -p "Incident: $incident_description (Severity: $severity)" \
      --append-system-prompt "You are an SRE expert. Diagnose the issue, assess impact, and provide immediate action items." \
      --output-format json \
      --allowedTools "Bash,Read,WebSearch,mcp__datadog" \
      --mcp-config monitoring-tools.json
}

# Usage
investigate_incident "Payment API returning 500 errors" "high"

```

Copy
```
import { query } from "@anthropic-ai/claude-code";

// Automated incident response agent
async function investigateIncident(
  incidentDescription: string, 
  severity = "medium"
) {
  const messages = [];
  
  for await (const message of query({
    prompt: `Incident: ${incidentDescription} (Severity: ${severity})`,
    options: {
      systemPrompt: "You are an SRE expert. Diagnose the issue, assess impact, and provide immediate action items.",
      maxTurns: 6,
      allowedTools: ["Bash", "Read", "WebSearch", "mcp__datadog"],
      mcpConfig: "monitoring-tools.json"
    }
  })) {
    messages.push(message);
  }
  
  return messages.find(m => m.type === "result");
}

// Usage
const result = await investigateIncident("Payment API returning 500 errors", "high");
console.log(result.result);

```

Copy
```
import asyncio
from claude_code_sdk import ClaudeSDKClient, ClaudeCodeOptions

async def investigate_incident(incident_description: str, severity: str = "medium"):
    """Automated incident response agent with real-time streaming"""
    
    # MCP server configuration for monitoring tools
    mcp_servers = {
        # Example configuration - uncomment and configure as needed:
        # "datadog": {
        #     "command": "npx",
        #     "args": ["-y", "@modelcontextprotocol/server-datadog"],
        #     "env": {"API_KEY": "your-datadog-key", "APP_KEY": "your-app-key"}
        # }
    }
    
    async with ClaudeSDKClient(
        options=ClaudeCodeOptions(
            system_prompt="You are an SRE expert. Diagnose the issue, assess impact, and provide immediate action items.",
            max_turns=6,
            allowed_tools=["Bash", "Read", "WebSearch", "mcp__datadog"],
            mcp_servers=mcp_servers
        )
    ) as client:
        # Send the incident details
        prompt = f"Incident: {incident_description} (Severity: {severity})"
        print(f"🚨 Investigating: {prompt}\n")
        await client.query(prompt)
        
        # Stream the investigation process
        investigation_log = []
        async for message in client.receive_response():
            if hasattr(message, 'content'):
                for block in message.content:
                    if hasattr(block, 'type'):
                        if block.type == 'tool_use':
                            print(f"[{block.name}] ", end='')
                    if hasattr(block, 'text'):
                        text = block.text
                        print(text, end='', flush=True)
                        investigation_log.append(text)
            
            # Capture final result
            if type(message).__name__ == "ResultMessage":
                return {
                    'analysis': ''.join(investigation_log),
                    'cost': message.total_cost_usd,
                    'duration_ms': message.duration_ms
                }

# Usage
result = await investigate_incident("Payment API returning 500 errors", "high")
print(f"\n\nInvestigation complete. Cost: ${result['cost']:.4f}")

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#automated-security-review)
Automated security review
  * Command line
  * TypeScript
  * Python


Copy
```
# Security audit agent for pull requests
audit_pr() {
    local pr_number="$1"
    
    gh pr diff "$pr_number" | claude -p \
      --append-system-prompt "You are a security engineer. Review this PR for vulnerabilities, insecure patterns, and compliance issues." \
      --output-format json \
      --allowedTools "Read,Grep,WebSearch"
}

# Usage and save to file
audit_pr 123 > security-report.json

```

Copy
```
# Security audit agent for pull requests
audit_pr() {
    local pr_number="$1"
    
    gh pr diff "$pr_number" | claude -p \
      --append-system-prompt "You are a security engineer. Review this PR for vulnerabilities, insecure patterns, and compliance issues." \
      --output-format json \
      --allowedTools "Read,Grep,WebSearch"
}

# Usage and save to file
audit_pr 123 > security-report.json

```

Copy
```
import { query } from "@anthropic-ai/claude-code";
import { execSync } from "child_process";

async function auditPR(prNumber: number) {
  // Get PR diff
  const prDiff = execSync(`gh pr diff ${prNumber}`, { encoding: 'utf8' });
  
  const messages = [];
  for await (const message of query({
    prompt: prDiff,
    options: {
      systemPrompt: "You are a security engineer. Review this PR for vulnerabilities, insecure patterns, and compliance issues.",
      maxTurns: 3,
      allowedTools: ["Read", "Grep", "WebSearch"]
    }
  })) {
    messages.push(message);
  }
  
  return messages.find(m => m.type === "result");
}

// Usage
const report = await auditPR(123);
console.log(JSON.stringify(report, null, 2));

```

Copy
```
import subprocess
import asyncio
import json
from claude_code_sdk import ClaudeSDKClient, ClaudeCodeOptions

async def audit_pr(pr_number: int):
    """Security audit agent for pull requests with streaming feedback"""
    # Get PR diff
    pr_diff = subprocess.check_output(
        ["gh", "pr", "diff", str(pr_number)], 
        text=True
    )
    
    async with ClaudeSDKClient(
        options=ClaudeCodeOptions(
            system_prompt="You are a security engineer. Review this PR for vulnerabilities, insecure patterns, and compliance issues.",
            max_turns=3,
            allowed_tools=["Read", "Grep", "WebSearch"]
        )
    ) as client:
        print(f"🔍 Auditing PR #{pr_number}\n")
        await client.query(pr_diff)
        
        findings = []
        async for message in client.receive_response():
            if hasattr(message, 'content'):
                for block in message.content:
                    if hasattr(block, 'text'):
                        # Stream findings as they're discovered
                        print(block.text, end='', flush=True)
                        findings.append(block.text)
            
            if type(message).__name__ == "ResultMessage":
                return {
                    'pr_number': pr_number,
                    'findings': ''.join(findings),
                    'metadata': {
                        'cost': message.total_cost_usd,
                        'duration': message.duration_ms,
                        'severity': 'high' if 'vulnerability' in ''.join(findings).lower() else 'medium'
                    }
                }

# Usage
report = await audit_pr(123)
print(f"\n\nAudit complete. Severity: {report['metadata']['severity']}")
print(json.dumps(report, indent=2))

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#multi-turn-legal-assistant)
Multi-turn legal assistant
  * Command line
  * TypeScript
  * Python


Copy
```
# Legal document review with session persistence
session_id=$(claude -p "Start legal review session" --output-format json | jq -r '.session_id')

# Review contract in multiple steps
claude -p --resume "$session_id" "Review contract.pdf for liability clauses"
claude -p --resume "$session_id" "Check compliance with GDPR requirements" 
claude -p --resume "$session_id" "Generate executive summary of risks"

```

Copy
```
# Legal document review with session persistence
session_id=$(claude -p "Start legal review session" --output-format json | jq -r '.session_id')

# Review contract in multiple steps
claude -p --resume "$session_id" "Review contract.pdf for liability clauses"
claude -p --resume "$session_id" "Check compliance with GDPR requirements" 
claude -p --resume "$session_id" "Generate executive summary of risks"

```

Copy
```
import { query } from "@anthropic-ai/claude-code";

async function legalReview() {
  // Start legal review session
  let sessionId: string;
  
  for await (const message of query({
    prompt: "Start legal review session",
    options: { maxTurns: 1 }
  })) {
    if (message.type === "system" && message.subtype === "init") {
      sessionId = message.session_id;
    }
  }
  
  // Multi-step review using same session
  const steps = [
    "Review contract.pdf for liability clauses",
    "Check compliance with GDPR requirements",
    "Generate executive summary of risks"
  ];
  
  for (const step of steps) {
    for await (const message of query({
      prompt: step,
      options: { resumeSessionId: sessionId, maxTurns: 2 }
    })) {
      if (message.type === "result") {
        console.log(`Step: ${step}`);
        console.log(message.result);
      }
    }
  }
}

```

Copy
```
import asyncio
from claude_code_sdk import ClaudeSDKClient, ClaudeCodeOptions

async def legal_review():
    """Legal document review with persistent session and streaming"""
    
    async with ClaudeSDKClient(
        options=ClaudeCodeOptions(
            system_prompt="You are a corporate lawyer. Provide detailed legal analysis.",
            max_turns=2
        )
    ) as client:
        # Multi-step review in same session
        steps = [
            "Review contract.pdf for liability clauses",
            "Check compliance with GDPR requirements", 
            "Generate executive summary of risks"
        ]
        
        review_results = []
        
        for step in steps:
            print(f"\n📋 {step}\n")
            await client.query(step)
            
            step_result = []
            async for message in client.receive_response():
                if hasattr(message, 'content'):
                    for block in message.content:
                        if hasattr(block, 'text'):
                            text = block.text
                            print(text, end='', flush=True)
                            step_result.append(text)
                
                if type(message).__name__ == "ResultMessage":
                    review_results.append({
                        'step': step,
                        'analysis': ''.join(step_result),
                        'cost': message.total_cost_usd
                    })
        
        # Summary
        total_cost = sum(r['cost'] for r in review_results)
        print(f"\n\n✅ Legal review complete. Total cost: ${total_cost:.4f}")
        return review_results

# Usage
results = await legal_review()

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#python-specific-best-practices)
Python-Specific Best Practices
### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#key-patterns)
Key Patterns
Copy
```
import asyncio
from claude_code_sdk import ClaudeSDKClient, ClaudeCodeOptions

# Always use context managers
async with ClaudeSDKClient() as client:
    await client.query("Analyze this code")
    async for msg in client.receive_response():
        # Process streaming messages
        pass

# Run multiple agents concurrently
async with ClaudeSDKClient() as reviewer, ClaudeSDKClient() as tester:
    await asyncio.gather(
        reviewer.query("Review main.py"),
        tester.query("Write tests for main.py")
    )

# Error handling
from claude_code_sdk import CLINotFoundError, ProcessError

try:
    async with ClaudeSDKClient() as client:
        # Your code here
        pass
except CLINotFoundError:
    print("Install CLI: npm install -g @anthropic-ai/claude-code")
except ProcessError as e:
    print(f"Process error: {e}")

# Collect full response with metadata
async def get_response(client, prompt):
    await client.query(prompt)
    text = []
    async for msg in client.receive_response():
        if hasattr(msg, 'content'):
            for block in msg.content:
                if hasattr(block, 'text'):
                    text.append(block.text)
        if type(msg).__name__ == "ResultMessage":
            return {'text': ''.join(text), 'cost': msg.total_cost_usd}

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#ipython%2Fjupyter-tips)
IPython/Jupyter Tips
Copy
```
# In Jupyter, use await directly in cells
client = ClaudeSDKClient()
await client.connect()
await client.query("Analyze data.csv")
async for msg in client.receive_response():
    print(msg)
await client.disconnect()

# Create reusable helper functions
async def stream_print(client, prompt):
    await client.query(prompt)
    async for msg in client.receive_response():
        if hasattr(msg, 'content'):
            for block in msg.content:
                if hasattr(block, 'text'):
                    print(block.text, end='', flush=True)

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#best-practices)
Best practices
  * **Use JSON output format** for programmatic parsing of responses:
Copy
```
# Parse JSON response with jq
result=$(claude -p "Generate code" --output-format json)
code=$(echo "$result" | jq -r '.result')
cost=$(echo "$result" | jq -r '.cost_usd')

```

  * **Handle errors gracefully** - check exit codes and stderr:
Copy
```
if ! claude -p "$prompt" 2>error.log; then
    echo "Error occurred:" >&2
    cat error.log >&2
    exit 1
fi

```

  * **Use session management** for maintaining context in multi-turn conversations
  * **Consider timeouts** for long-running operations:
Copy
```
timeout 300 claude -p "$complex_prompt" || echo "Timed out after 5 minutes"

```

  * **Respect rate limits** when making multiple requests by adding delays between calls


## 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#related-resources)
Related resources
  * [CLI usage and controls](https://docs.anthropic.com/en/docs/claude-code/cli-reference) - Complete CLI documentation
  * [GitHub Actions integration](https://docs.anthropic.com/en/docs/claude-code/github-actions) - Automate your GitHub workflow with Claude
  * [Common workflows](https://docs.anthropic.com/en/docs/claude-code/common-workflows) - Step-by-step guides for common use cases


Was this page helpful?
YesNo
[Common workflows](https://docs.anthropic.com/en/docs/claude-code/common-workflows)[Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Why use the Claude Code SDK?](https://docs.anthropic.com/en/docs/claude-code/sdk#why-use-the-claude-code-sdk%3F)
  * [What can you build with the SDK?](https://docs.anthropic.com/en/docs/claude-code/sdk#what-can-you-build-with-the-sdk%3F)
  * [Quick start](https://docs.anthropic.com/en/docs/claude-code/sdk#quick-start)
  * [Core usage](https://docs.anthropic.com/en/docs/claude-code/sdk#core-usage)
  * [Overview](https://docs.anthropic.com/en/docs/claude-code/sdk#overview)
  * [Authentication](https://docs.anthropic.com/en/docs/claude-code/sdk#authentication)
  * [Anthropic API key](https://docs.anthropic.com/en/docs/claude-code/sdk#anthropic-api-key)
  * [Third-party API credentials](https://docs.anthropic.com/en/docs/claude-code/sdk#third-party-api-credentials)
  * [Multi-turn conversations](https://docs.anthropic.com/en/docs/claude-code/sdk#multi-turn-conversations)
  * [Using Plan Mode](https://docs.anthropic.com/en/docs/claude-code/sdk#using-plan-mode)
  * [Custom system prompts](https://docs.anthropic.com/en/docs/claude-code/sdk#custom-system-prompts)
  * [Advanced Usage](https://docs.anthropic.com/en/docs/claude-code/sdk#advanced-usage)
  * [Custom tools via MCP](https://docs.anthropic.com/en/docs/claude-code/sdk#custom-tools-via-mcp)
  * [Custom permission prompt tool](https://docs.anthropic.com/en/docs/claude-code/sdk#custom-permission-prompt-tool)
  * [Output formats](https://docs.anthropic.com/en/docs/claude-code/sdk#output-formats)
  * [Text output (default)](https://docs.anthropic.com/en/docs/claude-code/sdk#text-output-default)
  * [JSON output](https://docs.anthropic.com/en/docs/claude-code/sdk#json-output)
  * [Streaming JSON output](https://docs.anthropic.com/en/docs/claude-code/sdk#streaming-json-output)
  * [Message schema](https://docs.anthropic.com/en/docs/claude-code/sdk#message-schema)
  * [Input formats](https://docs.anthropic.com/en/docs/claude-code/sdk#input-formats)
  * [Text input (default)](https://docs.anthropic.com/en/docs/claude-code/sdk#text-input-default)
  * [Streaming JSON input](https://docs.anthropic.com/en/docs/claude-code/sdk#streaming-json-input)
  * [Agent integration examples](https://docs.anthropic.com/en/docs/claude-code/sdk#agent-integration-examples)
  * [SRE incident response bot](https://docs.anthropic.com/en/docs/claude-code/sdk#sre-incident-response-bot)
  * [Automated security review](https://docs.anthropic.com/en/docs/claude-code/sdk#automated-security-review)
  * [Multi-turn legal assistant](https://docs.anthropic.com/en/docs/claude-code/sdk#multi-turn-legal-assistant)
  * [Python-Specific Best Practices](https://docs.anthropic.com/en/docs/claude-code/sdk#python-specific-best-practices)
  * [Key Patterns](https://docs.anthropic.com/en/docs/claude-code/sdk#key-patterns)
  * [IPython/Jupyter Tips](https://docs.anthropic.com/en/docs/claude-code/sdk#ipython%2Fjupyter-tips)
  * [Best practices](https://docs.anthropic.com/en/docs/claude-code/sdk#best-practices)
  * [Related resources](https://docs.anthropic.com/en/docs/claude-code/sdk#related-resources)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/security -->

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
Administration
Security
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


Administration
# Security
Copy page
Learn about Claude Code’s security safeguards and best practices for safe usage.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/security#how-we-approach-security)
How we approach security
### 
[​](https://docs.anthropic.com/en/docs/claude-code/security#security-foundation)
Security foundation
Your code’s security is paramount. Claude Code is built with security at its core, developed according to Anthropic’s comprehensive security program. Learn more and access resources (SOC 2 Type 2 report, ISO 27001 certificate, etc.) at [Anthropic Trust Center](https://trust.anthropic.com).
### 
[​](https://docs.anthropic.com/en/docs/claude-code/security#permission-based-architecture)
Permission-based architecture
Claude Code uses strict read-only permissions by default. When additional actions are needed (editing files, running tests, executing commands), Claude Code requests explicit permission. Users control whether to approve actions once or allow them automatically.
We designed Claude Code to be transparent and secure. For example, we require approval for bash commands before executing them, giving you direct control. This approach enables users and organizations to configure permissions directly.
For detailed permission configuration, see [Identity and Access Management](https://docs.anthropic.com/en/docs/claude-code/iam).
### 
[​](https://docs.anthropic.com/en/docs/claude-code/security#built-in-protections)
Built-in protections
To mitigate risks in agentic systems:
  * **Write access restriction** : Claude Code can only write to the folder where it was started and its subfolders—it cannot modify files in parent directories. While Claude Code can read files outside the working directory (useful for accessing system libraries and dependencies), write operations are strictly confined to the project scope, creating a clear security boundary
  * **Prompt fatigue mitigation** : Support for allowlisting frequently used safe commands per-user, per-codebase, or per-organization
  * **Accept Edits mode** : Batch accept multiple edits while maintaining permission prompts for commands with side effects


### 
[​](https://docs.anthropic.com/en/docs/claude-code/security#user-responsibility)
User responsibility
Claude Code only has the permissions you grant it. You’re responsible for reviewing proposed code and commands for safety before approval.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/security#protect-against-prompt-injection)
Protect against prompt injection
Prompt injection is a technique where an attacker attempts to override or manipulate an AI assistant’s instructions by inserting malicious text. Claude Code includes several safeguards against these attacks:
### 
[​](https://docs.anthropic.com/en/docs/claude-code/security#core-protections)
Core protections
  * **Permission system** : Sensitive operations require explicit approval
  * **Context-aware analysis** : Detects potentially harmful instructions by analyzing the full request
  * **Input sanitization** : Prevents command injection by processing user inputs
  * **Command blocklist** : Blocks risky commands that fetch arbitrary content from the web like `curl` and `wget`


### 
[​](https://docs.anthropic.com/en/docs/claude-code/security#privacy-safeguards)
Privacy safeguards
We have implemented several safeguards to protect your data, including:
  * Limited retention periods for sensitive information
  * Restricted access to user session data
  * Clear policies against using feedback for model training


For full details, please review our [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and [Privacy Policy](https://www.anthropic.com/legal/privacy).
### 
[​](https://docs.anthropic.com/en/docs/claude-code/security#additional-safeguards)
Additional safeguards
  * **Network request approval** : Tools that make network requests require user approval by default
  * **Isolated context windows** : Web fetch uses a separate context window to avoid injecting potentially malicious prompts
  * **Trust verification** : First-time codebase runs and new MCP servers require trust verification
  * **Command injection detection** : Suspicious bash commands require manual approval even if previously allowlisted
  * **Fail-closed matching** : Unmatched commands default to requiring manual approval
  * **Natural language descriptions** : Complex bash commands include explanations for user understanding
  * **Secure credential storage** : API keys and tokens are encrypted. See [Credential Management](https://docs.anthropic.com/en/docs/claude-code/iam#credential-management)


**Best practices for working with untrusted content** :
  1. Review suggested commands before approval
  2. Avoid piping untrusted content directly to Claude
  3. Verify proposed changes to critical files
  4. Use virtual machines (VMs) to run scripts and make tool calls, especially when interacting with external web services
  5. Report suspicious behavior with `/bug`


While these protections significantly reduce risk, no system is completely immune to all attacks. Always maintain good security practices when working with any AI tool.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/security#mcp-security)
MCP security
Claude Code allows users to configure Model Context Protocol (MCP) servers. The list of allowed MCP servers is configured in your source code, as part of Claude Code settings engineers check into source control.
We encourage either writing your own MCP servers or using MCP servers from providers that you trust. You are able to configure Claude Code permissions for MCP servers. Anthropic does not manage or audit any MCP servers.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/security#security-best-practices)
Security best practices
### 
[​](https://docs.anthropic.com/en/docs/claude-code/security#working-with-sensitive-code)
Working with sensitive code
  * Review all suggested changes before approval
  * Use project-specific permission settings for sensitive repositories
  * Consider using [devcontainers](https://docs.anthropic.com/en/docs/claude-code/devcontainer) for additional isolation
  * Regularly audit your permission settings with `/permissions`


### 
[​](https://docs.anthropic.com/en/docs/claude-code/security#team-security)
Team security
  * Use [enterprise managed policies](https://docs.anthropic.com/en/docs/claude-code/iam#enterprise-managed-policy-settings) to enforce organizational standards
  * Share approved permission configurations through version control
  * Train team members on security best practices
  * Monitor Claude Code usage through [OpenTelemetry metrics](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage)


### 
[​](https://docs.anthropic.com/en/docs/claude-code/security#reporting-security-issues)
Reporting security issues
If you discover a security vulnerability in Claude Code:
  1. Do not disclose it publicly
  2. Report it through our [HackerOne program](https://hackerone.com/anthropic-vdp/reports/new?type=team&report_type=vulnerability)
  3. Include detailed reproduction steps
  4. Allow time for us to address the issue before public disclosure


## 
[​](https://docs.anthropic.com/en/docs/claude-code/security#related-resources)
Related resources
  * [Identity and Access Management](https://docs.anthropic.com/en/docs/claude-code/iam) - Configure permissions and access controls
  * [Monitoring usage](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage) - Track and audit Claude Code activity
  * [Development containers](https://docs.anthropic.com/en/docs/claude-code/devcontainer) - Secure, isolated environments
  * [Anthropic Trust Center](https://trust.anthropic.com) - Security certifications and compliance


Was this page helpful?
YesNo
[Identity and Access Management](https://docs.anthropic.com/en/docs/claude-code/iam)[Data usage](https://docs.anthropic.com/en/docs/claude-code/data-usage)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [How we approach security](https://docs.anthropic.com/en/docs/claude-code/security#how-we-approach-security)
  * [Security foundation](https://docs.anthropic.com/en/docs/claude-code/security#security-foundation)
  * [Permission-based architecture](https://docs.anthropic.com/en/docs/claude-code/security#permission-based-architecture)
  * [Built-in protections](https://docs.anthropic.com/en/docs/claude-code/security#built-in-protections)
  * [User responsibility](https://docs.anthropic.com/en/docs/claude-code/security#user-responsibility)
  * [Protect against prompt injection](https://docs.anthropic.com/en/docs/claude-code/security#protect-against-prompt-injection)
  * [Core protections](https://docs.anthropic.com/en/docs/claude-code/security#core-protections)
  * [Privacy safeguards](https://docs.anthropic.com/en/docs/claude-code/security#privacy-safeguards)
  * [Additional safeguards](https://docs.anthropic.com/en/docs/claude-code/security#additional-safeguards)
  * [MCP security](https://docs.anthropic.com/en/docs/claude-code/security#mcp-security)
  * [Security best practices](https://docs.anthropic.com/en/docs/claude-code/security#security-best-practices)
  * [Working with sensitive code](https://docs.anthropic.com/en/docs/claude-code/security#working-with-sensitive-code)
  * [Team security](https://docs.anthropic.com/en/docs/claude-code/security#team-security)
  * [Reporting security issues](https://docs.anthropic.com/en/docs/claude-code/security#reporting-security-issues)
  * [Related resources](https://docs.anthropic.com/en/docs/claude-code/security#related-resources)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/settings -->

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
Claude Code settings
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
# Claude Code settings
Copy page
Configure Claude Code with global and project-level settings, and environment variables.
Claude Code offers a variety of settings to configure its behavior to meet your needs. You can configure Claude Code by running the `/config` command when using the interactive REPL.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/settings#settings-files)
Settings files
The `settings.json` file is our official mechanism for configuring Claude Code through hierarchical settings:
  * **User settings** are defined in `~/.claude/settings.json` and apply to all projects.
  * **Project settings** are saved in your project directory: 
    * `.claude/settings.json` for settings that are checked into source control and shared with your team
    * `.claude/settings.local.json` for settings that are not checked in, useful for personal preferences and experimentation. Claude Code will configure git to ignore `.claude/settings.local.json` when it is created.
  * For enterprise deployments of Claude Code, we also support **enterprise managed policy settings**. These take precedence over user and project settings. System administrators can deploy policies to: 
    * macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`
    * Linux and WSL: `/etc/claude-code/managed-settings.json`
    * Windows: `C:\ProgramData\ClaudeCode\managed-settings.json`


Example settings.json
Copy
```
{
  "permissions": {
    "allow": [
      "Bash(npm run lint)",
      "Bash(npm run test:*)",
      "Read(~/.zshrc)"
    ],
    "deny": [
      "Bash(curl:*)",
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)"
    ]
  },
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp"
  }
}

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/settings#available-settings)
Available settings
`settings.json` supports a number of options:
Key | Description | Example  
---|---|---  
`apiKeyHelper` | Custom script, to be executed in `/bin/sh`, to generate an auth value. This value will be sent as `X-Api-Key` and `Authorization: Bearer` headers for model requests | `/bin/generate_temp_api_key.sh`  
`cleanupPeriodDays` | How long to locally retain chat transcripts based on last activity date (default: 30 days) | `20`  
`env` | Environment variables that will be applied to every session | `{"FOO": "bar"}`  
`includeCoAuthoredBy` | Whether to include the `co-authored-by Claude` byline in git commits and pull requests (default: `true`) | `false`  
`permissions` | See table below for structure of permissions. |   
`hooks` | Configure custom commands to run before or after tool executions. See [hooks documentation](https://docs.anthropic.com/en/docs/claude-code/hooks) | `{"PreToolUse": {"Bash": "echo 'Running command...'"}}`  
`model` | Override the default model to use for Claude Code | `"claude-3-5-sonnet-20241022"`  
`statusLine` | Configure a custom status line to display context. See [statusLine documentation](https://docs.anthropic.com/en/docs/claude-code/statusline) | `{"type": "command", "command": "~/.claude/statusline.sh"}`  
`forceLoginMethod` | Use `claudeai` to restrict login to Claude.ai accounts, `console` to restrict login to Anthropic Console (API usage billing) accounts | `claudeai`  
`enableAllProjectMcpServers` | Automatically approve all MCP servers defined in project `.mcp.json` files | `true`  
`enabledMcpjsonServers` | List of specific MCP servers from `.mcp.json` files to approve | `["memory", "github"]`  
`disabledMcpjsonServers` | List of specific MCP servers from `.mcp.json` files to reject | `["filesystem"]`  
`awsAuthRefresh` | Custom script that modifies the `.aws` directory (see [advanced credential configuration](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#advanced-credential-configuration)) | `aws sso login --profile myprofile`  
`awsCredentialExport` | Custom script that outputs JSON with AWS credentials (see [advanced credential configuration](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock#advanced-credential-configuration)) | `/bin/generate_aws_grant.sh`  
### 
[​](https://docs.anthropic.com/en/docs/claude-code/settings#permission-settings)
Permission settings
Keys | Description | Example  
---|---|---  
`allow` | Array of [permission rules](https://docs.anthropic.com/en/docs/claude-code/iam#configuring-permissions) to allow tool use | `[ "Bash(git diff:*)" ]`  
`ask` | Array of [permission rules](https://docs.anthropic.com/en/docs/claude-code/iam#configuring-permissions) to ask for confirmation upon tool use. | `[ "Bash(git push:*)" ]`  
`deny` | Array of [permission rules](https://docs.anthropic.com/en/docs/claude-code/iam#configuring-permissions) to deny tool use. Use this to also exclude sensitive files from Claude Code access. | `[ "WebFetch", "Bash(curl:*)", "Read(./.env)", "Read(./secrets/**)" ]`  
`additionalDirectories` | Additional [working directories](https://docs.anthropic.com/en/docs/claude-code/iam#working-directories) that Claude has access to | `[ "../docs/" ]`  
`defaultMode` | Default [permission mode](https://docs.anthropic.com/en/docs/claude-code/iam#permission-modes) when opening Claude Code | `"acceptEdits"`  
`disableBypassPermissionsMode` | Set to `"disable"` to prevent `bypassPermissions` mode from being activated. See [managed policy settings](https://docs.anthropic.com/en/docs/claude-code/iam#enterprise-managed-policy-settings) | `"disable"`  
### 
[​](https://docs.anthropic.com/en/docs/claude-code/settings#settings-precedence)
Settings precedence
Settings are applied in order of precedence (highest to lowest):
  1. **Enterprise managed policies** (`managed-settings.json`)
     * Deployed by IT/DevOps
     * Cannot be overridden
  2. **Command line arguments**
     * Temporary overrides for a specific session
  3. **Local project settings** (`.claude/settings.local.json`)
     * Personal project-specific settings
  4. **Shared project settings** (`.claude/settings.json`)
     * Team-shared project settings in source control
  5. **User settings** (`~/.claude/settings.json`)
     * Personal global settings


This hierarchy ensures that enterprise security policies are always enforced while still allowing teams and individuals to customize their experience.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/settings#key-points-about-the-configuration-system)
Key points about the configuration system
  * **Memory files (CLAUDE.md)** : Contain instructions and context that Claude loads at startup
  * **Settings files (JSON)** : Configure permissions, environment variables, and tool behavior
  * **Slash commands** : Custom commands that can be invoked during a session with `/command-name`
  * **MCP servers** : Extend Claude Code with additional tools and integrations
  * **Precedence** : Higher-level configurations (Enterprise) override lower-level ones (User/Project)
  * **Inheritance** : Settings are merged, with more specific settings adding to or overriding broader ones


### 
[​](https://docs.anthropic.com/en/docs/claude-code/settings#system-prompt-availability)
System prompt availability
Unlike for claude.ai, we do not publish Claude Code’s internal system prompt on this website. Use CLAUDE.md files or `--append-system-prompt` to add custom instructions to Claude Code’s behavior.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/settings#excluding-sensitive-files)
Excluding sensitive files
To prevent Claude Code from accessing files containing sensitive information (e.g., API keys, secrets, environment files), use the `permissions.deny` setting in your `.claude/settings.json` file:
Copy
```
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)",
      "Read(./config/credentials.json)",
      "Read(./build)"
    ]
  }
}

```

This replaces the deprecated `ignorePatterns` configuration. Files matching these patterns will be completely invisible to Claude Code, preventing any accidental exposure of sensitive data.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/settings#subagent-configuration)
Subagent configuration
Claude Code supports custom AI subagents that can be configured at both user and project levels. These subagents are stored as Markdown files with YAML frontmatter:
  * **User subagents** : `~/.claude/agents/` - Available across all your projects
  * **Project subagents** : `.claude/agents/` - Specific to your project and can be shared with your team


Subagent files define specialized AI assistants with custom prompts and tool permissions. Learn more about creating and using subagents in the [subagents documentation](https://docs.anthropic.com/en/docs/claude-code/sub-agents).
## 
[​](https://docs.anthropic.com/en/docs/claude-code/settings#environment-variables)
Environment variables
Claude Code supports the following environment variables to control its behavior:
All environment variables can also be configured in [`settings.json`](https://docs.anthropic.com/en/docs/claude-code/settings#available-settings). This is useful as a way to automatically set environment variables for each session, or to roll out a set of environment variables for your whole team or organization.
Variable | Purpose  
---|---  
`ANTHROPIC_API_KEY` | API key sent as `X-Api-Key` header, typically for the Claude SDK (for interactive usage, run `/login`)  
`ANTHROPIC_AUTH_TOKEN` | Custom value for the `Authorization` header (the value you set here will be prefixed with `Bearer `)  
`ANTHROPIC_CUSTOM_HEADERS` | Custom headers you want to add to the request (in `Name: Value` format)  
`ANTHROPIC_MODEL` | Name of custom model to use (see [Model Configuration](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#model-configuration))  
`ANTHROPIC_SMALL_FAST_MODEL` | Name of [Haiku-class model for background tasks](https://docs.anthropic.com/en/docs/claude-code/costs)  
`ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION` | Override AWS region for the small/fast model when using Bedrock  
`AWS_BEARER_TOKEN_BEDROCK` | Bedrock API key for authentication (see [Bedrock API keys](https://aws.amazon.com/blogs/machine-learning/accelerate-ai-development-with-amazon-bedrock-api-keys/))  
`BASH_DEFAULT_TIMEOUT_MS` | Default timeout for long-running bash commands  
`BASH_MAX_TIMEOUT_MS` | Maximum timeout the model can set for long-running bash commands  
`BASH_MAX_OUTPUT_LENGTH` | Maximum number of characters in bash outputs before they are middle-truncated  
`CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR` | Return to the original working directory after each Bash command  
`CLAUDE_CODE_API_KEY_HELPER_TTL_MS` | Interval in milliseconds at which credentials should be refreshed (when using `apiKeyHelper`)  
`CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL` | Skip auto-installation of IDE extensions  
`CLAUDE_CODE_MAX_OUTPUT_TOKENS` | Set the maximum number of output tokens for most requests  
`CLAUDE_CODE_USE_BEDROCK` | Use [Bedrock](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock)  
`CLAUDE_CODE_USE_VERTEX` | Use [Vertex](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai)  
`CLAUDE_CODE_SKIP_BEDROCK_AUTH` | Skip AWS authentication for Bedrock (e.g. when using an LLM gateway)  
`CLAUDE_CODE_SKIP_VERTEX_AUTH` | Skip Google authentication for Vertex (e.g. when using an LLM gateway)  
`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` | Equivalent of setting `DISABLE_AUTOUPDATER`, `DISABLE_BUG_COMMAND`, `DISABLE_ERROR_REPORTING`, and `DISABLE_TELEMETRY`  
`CLAUDE_CODE_DISABLE_TERMINAL_TITLE` | Set to `1` to disable automatic terminal title updates based on conversation context  
`DISABLE_AUTOUPDATER` | Set to `1` to disable automatic updates. This takes precedence over the `autoUpdates` configuration setting.  
`DISABLE_BUG_COMMAND` | Set to `1` to disable the `/bug` command  
`DISABLE_COST_WARNINGS` | Set to `1` to disable cost warning messages  
`DISABLE_ERROR_REPORTING` | Set to `1` to opt out of Sentry error reporting  
`DISABLE_NON_ESSENTIAL_MODEL_CALLS` | Set to `1` to disable model calls for non-critical paths like flavor text  
`DISABLE_TELEMETRY` | Set to `1` to opt out of Statsig telemetry (note that Statsig events do not include user data like code, file paths, or bash commands)  
`HTTP_PROXY` | Specify HTTP proxy server for network connections  
`HTTPS_PROXY` | Specify HTTPS proxy server for network connections  
`MAX_THINKING_TOKENS` | Force a thinking for the model budget  
`MCP_TIMEOUT` | Timeout in milliseconds for MCP server startup  
`MCP_TOOL_TIMEOUT` | Timeout in milliseconds for MCP tool execution  
`MAX_MCP_OUTPUT_TOKENS` | Maximum number of tokens allowed in MCP tool responses (default: 25000)  
`USE_BUILTIN_RIPGREP` | Set to `1` to ignore system-installed `rg` and use `rg` included with Claude Code  
`VERTEX_REGION_CLAUDE_3_5_HAIKU` | Override region for Claude 3.5 Haiku when using Vertex AI  
`VERTEX_REGION_CLAUDE_3_5_SONNET` | Override region for Claude Sonnet 3.5 when using Vertex AI  
`VERTEX_REGION_CLAUDE_3_7_SONNET` | Override region for Claude 3.7 Sonnet when using Vertex AI  
`VERTEX_REGION_CLAUDE_4_0_OPUS` | Override region for Claude 4.0 Opus when using Vertex AI  
`VERTEX_REGION_CLAUDE_4_0_SONNET` | Override region for Claude 4.0 Sonnet when using Vertex AI  
`VERTEX_REGION_CLAUDE_4_1_OPUS` | Override region for Claude 4.1 Opus when using Vertex AI  
## 
[​](https://docs.anthropic.com/en/docs/claude-code/settings#configuration-options)
Configuration options
To manage your configurations, use the following commands:
  * List settings: `claude config list`
  * See a setting: `claude config get <key>`
  * Change a setting: `claude config set <key> <value>`
  * Push to a setting (for lists): `claude config add <key> <value>`
  * Remove from a setting (for lists): `claude config remove <key> <value>`


By default `config` changes your project configuration. To manage your global configuration, use the `--global` (or `-g`) flag.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/settings#global-configuration)
Global configuration
To set a global configuration, use `claude config set -g <key> <value>`:
Key | Description | Example  
---|---|---  
`autoUpdates` | Whether to enable automatic updates (default: `true`). When enabled, Claude Code automatically downloads and installs updates in the background. Updates are applied when you restart Claude Code. | `false`  
`preferredNotifChannel` | Where you want to receive notifications (default: `iterm2`) |  `iterm2`, `iterm2_with_bell`, `terminal_bell`, or `notifications_disabled`  
`theme` | Color theme |  `dark`, `light`, `light-daltonized`, or `dark-daltonized`  
`verbose` | Whether to show full bash and command outputs (default: `false`) | `true`  
## 
[​](https://docs.anthropic.com/en/docs/claude-code/settings#tools-available-to-claude)
Tools available to Claude
Claude Code has access to a set of powerful tools that help it understand and modify your codebase:
Tool | Description | Permission Required  
---|---|---  
**Bash** | Executes shell commands in your environment | Yes  
**Edit** | Makes targeted edits to specific files | Yes  
**Glob** | Finds files based on pattern matching | No  
**Grep** | Searches for patterns in file contents | No  
**LS** | Lists files and directories | No  
**MultiEdit** | Performs multiple edits on a single file atomically | Yes  
**NotebookEdit** | Modifies Jupyter notebook cells | Yes  
**NotebookRead** | Reads and displays Jupyter notebook contents | No  
**Read** | Reads the contents of files | No  
**Task** | Runs a sub-agent to handle complex, multi-step tasks | No  
**TodoWrite** | Creates and manages structured task lists | No  
**WebFetch** | Fetches content from a specified URL | Yes  
**WebSearch** | Performs web searches with domain filtering | Yes  
**Write** | Creates or overwrites files | Yes  
Permission rules can be configured using `/allowed-tools` or in [permission settings](https://docs.anthropic.com/en/docs/claude-code/settings#available-settings).
### 
[​](https://docs.anthropic.com/en/docs/claude-code/settings#extending-tools-with-hooks)
Extending tools with hooks
You can run custom commands before or after any tool executes using [Claude Code hooks](https://docs.anthropic.com/en/docs/claude-code/hooks-guide).
For example, you could automatically run a Python formatter after Claude modifies Python files, or prevent modifications to production configuration files by blocking Write operations to certain paths.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/settings#see-also)
See also
  * [Identity and Access Management](https://docs.anthropic.com/en/docs/claude-code/iam#configuring-permissions) - Learn about Claude Code’s permission system
  * [IAM and access control](https://docs.anthropic.com/en/docs/claude-code/iam#enterprise-managed-policy-settings) - Enterprise policy management
  * [Troubleshooting](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#auto-updater-issues) - Solutions for common configuration issues


Was this page helpful?
YesNo
[Analytics](https://docs.anthropic.com/en/docs/claude-code/analytics)[Add Claude Code to your IDE](https://docs.anthropic.com/en/docs/claude-code/ide-integrations)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Settings files](https://docs.anthropic.com/en/docs/claude-code/settings#settings-files)
  * [Available settings](https://docs.anthropic.com/en/docs/claude-code/settings#available-settings)
  * [Permission settings](https://docs.anthropic.com/en/docs/claude-code/settings#permission-settings)
  * [Settings precedence](https://docs.anthropic.com/en/docs/claude-code/settings#settings-precedence)
  * [Key points about the configuration system](https://docs.anthropic.com/en/docs/claude-code/settings#key-points-about-the-configuration-system)
  * [System prompt availability](https://docs.anthropic.com/en/docs/claude-code/settings#system-prompt-availability)
  * [Excluding sensitive files](https://docs.anthropic.com/en/docs/claude-code/settings#excluding-sensitive-files)
  * [Subagent configuration](https://docs.anthropic.com/en/docs/claude-code/settings#subagent-configuration)
  * [Environment variables](https://docs.anthropic.com/en/docs/claude-code/settings#environment-variables)
  * [Configuration options](https://docs.anthropic.com/en/docs/claude-code/settings#configuration-options)
  * [Global configuration](https://docs.anthropic.com/en/docs/claude-code/settings#global-configuration)
  * [Tools available to Claude](https://docs.anthropic.com/en/docs/claude-code/settings#tools-available-to-claude)
  * [Extending tools with hooks](https://docs.anthropic.com/en/docs/claude-code/settings#extending-tools-with-hooks)
  * [See also](https://docs.anthropic.com/en/docs/claude-code/settings#see-also)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/setup -->

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
Administration
Set up Claude Code
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


Administration
# Set up Claude Code
Copy page
Install, authenticate, and start using Claude Code on your development machine.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/setup#system-requirements)
System requirements
  * **Operating Systems** : macOS 10.15+, Ubuntu 20.04+/Debian 10+, or Windows 10+ (with WSL 1, WSL 2, or Git for Windows)
  * **Hardware** : 4GB+ RAM
  * **Software** : [Node.js 18+](https://nodejs.org/en/download)
  * **Network** : Internet connection required for authentication and AI processing
  * **Shell** : Works best in Bash, Zsh or Fish
  * **Location** : [Anthropic supported countries](https://www.anthropic.com/supported-countries)


### 
[​](https://docs.anthropic.com/en/docs/claude-code/setup#additional-dependencies)
Additional dependencies
  * **ripgrep** : Claude Code depends on `ripgrep` for core functionality. While it is typically included in your Claude Code installation, you may need to independently install `ripgrep` on some distributions (like Alpine Linux or other musl-based distributions).


## 
[​](https://docs.anthropic.com/en/docs/claude-code/setup#standard-installation)
Standard installation
To install Claude Code, run the following command:
Copy
```
npm install -g @anthropic-ai/claude-code

```

Do NOT use `sudo npm install -g` as this can lead to permission issues and security risks. If you encounter permission errors, see [configure Claude Code](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#linux-permission-issues) for recommended solutions.
Some users may be automatically migrated to an improved installation method. Run `claude doctor` after installation to check your installation type.
After the installation process completes, navigate to your project and start Claude Code:
Copy
```
cd your-awesome-project
claude

```

Claude Code offers the following authentication options:
  1. **Anthropic Console** : The default option. Connect through the Anthropic Console and complete the OAuth process. Requires active billing at [console.anthropic.com](https://console.anthropic.com).
  2. **Claude App (with Pro or Max plan)** : Subscribe to Claude’s [Pro or Max plan](https://www.anthropic.com/pricing) for a unified subscription that includes both Claude Code and the web interface. Get more value at the same price point while managing your account in one place. Log in with your Claude.ai account. During launch, choose the option that matches your subscription type.
  3. **Enterprise platforms** : Configure Claude Code to use [Amazon Bedrock or Google Vertex AI](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations) for enterprise deployments with your existing cloud infrastructure.


Claude Code securely stores your credentials. See [Credential Management](https://docs.anthropic.com/en/docs/claude-code/iam#credential-management) for details.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/setup#windows-setup)
Windows setup
**Option 1: Claude Code within WSL**
  * Both WSL 1 and WSL 2 are supported


**Option 2: Claude Code on native Windows with Git Bash**
  * Requires [Git for Windows](https://git-scm.com/downloads/win)
  * For portable Git installations, specify the path to your `bash.exe`: 
Copy
```
$env:CLAUDE_CODE_GIT_BASH_PATH="C:\Program Files\Git\bin\bash.exe"

```



## 
[​](https://docs.anthropic.com/en/docs/claude-code/setup#alternative-installation-methods)
Alternative installation methods
Claude Code offers multiple installation methods to suit different environments.
If you encounter any issues during installation, consult the [troubleshooting guide](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#linux-permission-issues).
Run `claude doctor` after installation to check your installation type and version.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/setup#global-npm-installation)
Global npm installation
Traditional method shown in the [install steps above](https://docs.anthropic.com/en/docs/claude-code/setup#install-and-authenticate)
### 
[​](https://docs.anthropic.com/en/docs/claude-code/setup#native-binary-installation-beta)
Native binary installation (Beta)
If you have an existing installation of Claude Code, use `claude install` to start the native binary installation.
For a fresh install, run the following command:
**macOS, Linux, WSL:**
Copy
```
# Install stable version (default)
curl -fsSL https://claude.ai/install.sh | bash

# Install latest version
curl -fsSL https://claude.ai/install.sh | bash -s latest

# Install specific version number
curl -fsSL https://claude.ai/install.sh | bash -s 1.0.58

```

**Windows PowerShell:**
Copy
```
# Install stable version (default)
irm https://claude.ai/install.ps1 | iex

# Install latest version
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) latest

# Install specific version number
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) 1.0.58


```

The native Claude Code installer is supported on macOS, Linux, and Windows.
Make sure that you remove any outdated aliases or symlinks. Once your installation is complete, run `claude doctor` to verify the installation.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/setup#local-installation)
Local installation
  * After global install via npm, use `claude migrate-installer` to move to local
  * Avoids autoupdater npm permission issues
  * Some users may be automatically migrated to this method


## 
[​](https://docs.anthropic.com/en/docs/claude-code/setup#running-on-aws-or-gcp)
Running on AWS or GCP
By default, Claude Code uses Anthropic’s API.
For details on running Claude Code on AWS or GCP, see [third-party integrations](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations).
## 
[​](https://docs.anthropic.com/en/docs/claude-code/setup#update-claude-code)
Update Claude Code
### 
[​](https://docs.anthropic.com/en/docs/claude-code/setup#auto-updates)
Auto updates
Claude Code automatically keeps itself up to date to ensure you have the latest features and security fixes.
  * **Update checks** : Performed on startup and periodically while running
  * **Update process** : Downloads and installs automatically in the background
  * **Notifications** : You’ll see a notification when updates are installed
  * **Applying updates** : Updates take effect the next time you start Claude Code


**Disable auto-updates:**
Copy
```
# Via configuration
claude config set autoUpdates false --global

# Or via environment variable
export DISABLE_AUTOUPDATER=1

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/setup#update-manually)
Update manually
Copy
```
claude update

```

Was this page helpful?
YesNo
[Development containers](https://docs.anthropic.com/en/docs/claude-code/devcontainer)[Identity and Access Management](https://docs.anthropic.com/en/docs/claude-code/iam)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [System requirements](https://docs.anthropic.com/en/docs/claude-code/setup#system-requirements)
  * [Additional dependencies](https://docs.anthropic.com/en/docs/claude-code/setup#additional-dependencies)
  * [Standard installation](https://docs.anthropic.com/en/docs/claude-code/setup#standard-installation)
  * [Windows setup](https://docs.anthropic.com/en/docs/claude-code/setup#windows-setup)
  * [Alternative installation methods](https://docs.anthropic.com/en/docs/claude-code/setup#alternative-installation-methods)
  * [Global npm installation](https://docs.anthropic.com/en/docs/claude-code/setup#global-npm-installation)
  * [Native binary installation (Beta)](https://docs.anthropic.com/en/docs/claude-code/setup#native-binary-installation-beta)
  * [Local installation](https://docs.anthropic.com/en/docs/claude-code/setup#local-installation)
  * [Running on AWS or GCP](https://docs.anthropic.com/en/docs/claude-code/setup#running-on-aws-or-gcp)
  * [Update Claude Code](https://docs.anthropic.com/en/docs/claude-code/setup#update-claude-code)
  * [Auto updates](https://docs.anthropic.com/en/docs/claude-code/setup#auto-updates)
  * [Update manually](https://docs.anthropic.com/en/docs/claude-code/setup#update-manually)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/slash-commands -->

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


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/statusline -->

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
Status line configuration
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
# Status line configuration
Copy page
Create a custom status line for Claude Code to display contextual information
Make Claude Code your own with a custom status line that displays at the bottom of the Claude Code interface, similar to how terminal prompts (PS1) work in shells like Oh-my-zsh.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/statusline#create-a-custom-status-line)
Create a custom status line
You can either:
  * Run `/statusline` to ask Claude Code to help you set up a custom status line. By default, it will try to reproduce your terminal’s prompt, but you can provide additional instructions about the behavior you want to Claude Code, such as `/statusline show the model name in orange`
  * Directly add a `statusLine` command to your `.claude/settings.json`:


Copy
```
{
  "statusLine": {
    "type": "command",
    "command": "~/.claude/statusline.sh",
    "padding": 0 // Optional: set to 0 to let status line go to edge
  }
}

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/statusline#how-it-works)
How it Works
  * The status line is updated when the conversation messages update
  * Updates run at most every 300ms
  * The first line of stdout from your command becomes the status line text
  * ANSI color codes are supported for styling your status line
  * Claude Code passes contextual information about the current session (model, directories, etc.) as JSON to your script via stdin


## 
[​](https://docs.anthropic.com/en/docs/claude-code/statusline#json-input-structure)
JSON Input Structure
Your status line command receives structured data via stdin in JSON format:
Copy
```
{
  "hook_event_name": "Status",
  "session_id": "abc123...",
  "transcript_path": "/path/to/transcript.json",
  "cwd": "/current/working/directory",
  "model": {
    "id": "claude-opus-4-1",
    "display_name": "Opus"
  },
  "workspace": {
    "current_dir": "/current/working/directory",
    "project_dir": "/original/project/directory"
  },
  "version": "1.0.80",
  "output_style": {
    "name": "default"
  }
}

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/statusline#example-scripts)
Example Scripts
### 
[​](https://docs.anthropic.com/en/docs/claude-code/statusline#simple-status-line)
Simple Status Line
Copy
```
#!/bin/bash
# Read JSON input from stdin
input=$(cat)

# Extract values using jq
MODEL_DISPLAY=$(echo "$input" | jq -r '.model.display_name')
CURRENT_DIR=$(echo "$input" | jq -r '.workspace.current_dir')

echo "[$MODEL_DISPLAY] 📁 ${CURRENT_DIR##*/}"

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/statusline#git-aware-status-line)
Git-Aware Status Line
Copy
```
#!/bin/bash
# Read JSON input from stdin
input=$(cat)

# Extract values using jq
MODEL_DISPLAY=$(echo "$input" | jq -r '.model.display_name')
CURRENT_DIR=$(echo "$input" | jq -r '.workspace.current_dir')

# Show git branch if in a git repo
GIT_BRANCH=""
if git rev-parse --git-dir > /dev/null 2>&1; then
    BRANCH=$(git branch --show-current 2>/dev/null)
    if [ -n "$BRANCH" ]; then
        GIT_BRANCH=" | 🌿 $BRANCH"
    fi
fi

echo "[$MODEL_DISPLAY] 📁 ${CURRENT_DIR##*/}$GIT_BRANCH"

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/statusline#python-example)
Python Example
Copy
```
#!/usr/bin/env python3
import json
import sys
import os

# Read JSON from stdin
data = json.load(sys.stdin)

# Extract values
model = data['model']['display_name']
current_dir = os.path.basename(data['workspace']['current_dir'])

# Check for git branch
git_branch = ""
if os.path.exists('.git'):
    try:
        with open('.git/HEAD', 'r') as f:
            ref = f.read().strip()
            if ref.startswith('ref: refs/heads/'):
                git_branch = f" | 🌿 {ref.replace('ref: refs/heads/', '')}"
    except:
        pass

print(f"[{model}] 📁 {current_dir}{git_branch}")

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/statusline#node-js-example)
Node.js Example
Copy
```
#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

// Read JSON from stdin
let input = '';
process.stdin.on('data', chunk => input += chunk);
process.stdin.on('end', () => {
    const data = JSON.parse(input);
    
    // Extract values
    const model = data.model.display_name;
    const currentDir = path.basename(data.workspace.current_dir);
    
    // Check for git branch
    let gitBranch = '';
    try {
        const headContent = fs.readFileSync('.git/HEAD', 'utf8').trim();
        if (headContent.startsWith('ref: refs/heads/')) {
            gitBranch = ` | 🌿 ${headContent.replace('ref: refs/heads/', '')}`;
        }
    } catch (e) {
        // Not a git repo or can't read HEAD
    }
    
    console.log(`[${model}] 📁 ${currentDir}${gitBranch}`);
});

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/statusline#helper-function-approach)
Helper Function Approach
For more complex bash scripts, you can create helper functions:
Copy
```
#!/bin/bash
# Read JSON input once
input=$(cat)

# Helper functions for common extractions
get_model_name() { echo "$input" | jq -r '.model.display_name'; }
get_current_dir() { echo "$input" | jq -r '.workspace.current_dir'; }
get_project_dir() { echo "$input" | jq -r '.workspace.project_dir'; }
get_version() { echo "$input" | jq -r '.version'; }

# Use the helpers
MODEL=$(get_model_name)
DIR=$(get_current_dir)
echo "[$MODEL] 📁 ${DIR##*/}"

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/statusline#tips)
Tips
  * Keep your status line concise - it should fit on one line
  * Use emojis (if your terminal supports them) and colors to make information scannable
  * Use `jq` for JSON parsing in Bash (see examples above)
  * Test your script by running it manually with mock JSON input: `echo '{"model":{"display_name":"Test"},"workspace":{"current_dir":"/test"}}' | ./statusline.sh`
  * Consider caching expensive operations (like git status) if needed


## 
[​](https://docs.anthropic.com/en/docs/claude-code/statusline#troubleshooting)
Troubleshooting
  * If your status line doesn’t appear, check that your script is executable (`chmod +x`)
  * Ensure your script outputs to stdout (not stderr)


Was this page helpful?
YesNo
[Memory management](https://docs.anthropic.com/en/docs/claude-code/memory)[CLI reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Create a custom status line](https://docs.anthropic.com/en/docs/claude-code/statusline#create-a-custom-status-line)
  * [How it Works](https://docs.anthropic.com/en/docs/claude-code/statusline#how-it-works)
  * [JSON Input Structure](https://docs.anthropic.com/en/docs/claude-code/statusline#json-input-structure)
  * [Example Scripts](https://docs.anthropic.com/en/docs/claude-code/statusline#example-scripts)
  * [Simple Status Line](https://docs.anthropic.com/en/docs/claude-code/statusline#simple-status-line)
  * [Git-Aware Status Line](https://docs.anthropic.com/en/docs/claude-code/statusline#git-aware-status-line)
  * [Python Example](https://docs.anthropic.com/en/docs/claude-code/statusline#python-example)
  * [Node.js Example](https://docs.anthropic.com/en/docs/claude-code/statusline#node-js-example)
  * [Helper Function Approach](https://docs.anthropic.com/en/docs/claude-code/statusline#helper-function-approach)
  * [Tips](https://docs.anthropic.com/en/docs/claude-code/statusline#tips)
  * [Troubleshooting](https://docs.anthropic.com/en/docs/claude-code/statusline#troubleshooting)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/sub-agents -->

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
Subagents
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
# Subagents
Copy page
Create and use specialized AI subagents in Claude Code for task-specific workflows and improved context management.
Custom subagents in Claude Code are specialized AI assistants that can be invoked to handle specific types of tasks. They enable more efficient problem-solving by providing task-specific configurations with customized system prompts, tools and a separate context window.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#what-are-subagents%3F)
What are subagents?
Subagents are pre-configured AI personalities that Claude Code can delegate tasks to. Each subagent:
  * Has a specific purpose and expertise area
  * Uses its own context window separate from the main conversation
  * Can be configured with specific tools it’s allowed to use
  * Includes a custom system prompt that guides its behavior


When Claude Code encounters a task that matches a subagent’s expertise, it can delegate that task to the specialized subagent, which works independently and returns results.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#key-benefits)
Key benefits
## Context preservation
Each subagent operates in its own context, preventing pollution of the main conversation and keeping it focused on high-level objectives.
## Specialized expertise
Subagents can be fine-tuned with detailed instructions for specific domains, leading to higher success rates on designated tasks.
## Reusability
Once created, subagents can be used across different projects and shared with your team for consistent workflows.
## Flexible permissions
Each subagent can have different tool access levels, allowing you to limit powerful tools to specific subagent types.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#quick-start)
Quick start
To create your first subagent:
1
Open the subagents interface
Run the following command:
Copy
```
/agents

```

2
Select 'Create New Agent'
Choose whether to create a project-level or user-level subagent
3
Define the subagent
  * **Recommended** : Generate with Claude first, then customize to make it yours
  * Describe your subagent in detail and when it should be used
  * Select the tools you want to grant access to (or leave blank to inherit all tools)
  * The interface shows all available tools, making selection easy
  * If you’re generating with Claude, you can also edit the system prompt in your own editor by pressing `e`


4
Save and use
Your subagent is now available! Claude will use it automatically when appropriate, or you can invoke it explicitly:
Copy
```
> Use the code-reviewer subagent to check my recent changes

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#subagent-configuration)
Subagent configuration
### 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#file-locations)
File locations
Subagents are stored as Markdown files with YAML frontmatter in two possible locations:
Type | Location | Scope | Priority  
---|---|---|---  
**Project subagents** | `.claude/agents/` | Available in current project | Highest  
**User subagents** | `~/.claude/agents/` | Available across all projects | Lower  
When subagent names conflict, project-level subagents take precedence over user-level subagents.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#file-format)
File format
Each subagent is defined in a Markdown file with this structure:
Copy
```
---
name: your-sub-agent-name
description: Description of when this subagent should be invoked
tools: tool1, tool2, tool3  # Optional - inherits all tools if omitted
---

Your subagent's system prompt goes here. This can be multiple paragraphs
and should clearly define the subagent's role, capabilities, and approach
to solving problems.

Include specific instructions, best practices, and any constraints
the subagent should follow.

```

#### 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#configuration-fields)
Configuration fields
Field | Required | Description  
---|---|---  
`name` | Yes | Unique identifier using lowercase letters and hyphens  
`description` | Yes | Natural language description of the subagent’s purpose  
`tools` | No | Comma-separated list of specific tools. If omitted, inherits all tools from the main thread  
### 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#available-tools)
Available tools
Subagents can be granted access to any of Claude Code’s internal tools. See the [tools documentation](https://docs.anthropic.com/en/docs/claude-code/settings#tools-available-to-claude) for a complete list of available tools.
**Recommended:** Use the `/agents` command to modify tool access - it provides an interactive interface that lists all available tools, including any connected MCP server tools, making it easier to select the ones you need.
You have two options for configuring tools:
  * **Omit the`tools` field** to inherit all tools from the main thread (default), including MCP tools
  * **Specify individual tools** as a comma-separated list for more granular control (can be edited manually or via `/agents`)


**MCP Tools** : Subagents can access MCP tools from configured MCP servers. When the `tools` field is omitted, subagents inherit all MCP tools available to the main thread.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#managing-subagents)
Managing subagents
### 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#using-the-%2Fagents-command-recommended)
Using the /agents command (Recommended)
The `/agents` command provides a comprehensive interface for subagent management:
Copy
```
/agents

```

This opens an interactive menu where you can:
  * View all available subagents (built-in, user, and project)
  * Create new subagents with guided setup
  * Edit existing custom subagents, including their tool access
  * Delete custom subagents
  * See which subagents are active when duplicates exist
  * **Easily manage tool permissions** with a complete list of available tools


### 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#direct-file-management)
Direct file management
You can also manage subagents by working directly with their files:
Copy
```
# Create a project subagent
mkdir -p .claude/agents
echo '---
name: test-runner
description: Use proactively to run tests and fix failures
---

You are a test automation expert. When you see code changes, proactively run the appropriate tests. If tests fail, analyze the failures and fix them while preserving the original test intent.' > .claude/agents/test-runner.md

# Create a user subagent
mkdir -p ~/.claude/agents
# ... create subagent file

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#using-subagents-effectively)
Using subagents effectively
### 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#automatic-delegation)
Automatic delegation
Claude Code proactively delegates tasks based on:
  * The task description in your request
  * The `description` field in subagent configurations
  * Current context and available tools


To encourage more proactive subagent use, include phrases like “use PROACTIVELY” or “MUST BE USED” in your `description` field.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#explicit-invocation)
Explicit invocation
Request a specific subagent by mentioning it in your command:
Copy
```
> Use the test-runner subagent to fix failing tests
> Have the code-reviewer subagent look at my recent changes
> Ask the debugger subagent to investigate this error

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#example-subagents)
Example subagents
### 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#code-reviewer)
Code reviewer
Copy
```
---
name: code-reviewer
description: Expert code review specialist. Proactively reviews code for quality, security, and maintainability. Use immediately after writing or modifying code.
tools: Read, Grep, Glob, Bash
---

You are a senior code reviewer ensuring high standards of code quality and security.

When invoked:
1. Run git diff to see recent changes
2. Focus on modified files
3. Begin review immediately

Review checklist:
- Code is simple and readable
- Functions and variables are well-named
- No duplicated code
- Proper error handling
- No exposed secrets or API keys
- Input validation implemented
- Good test coverage
- Performance considerations addressed

Provide feedback organized by priority:
- Critical issues (must fix)
- Warnings (should fix)
- Suggestions (consider improving)

Include specific examples of how to fix issues.

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#debugger)
Debugger
Copy
```
---
name: debugger
description: Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues.
tools: Read, Edit, Bash, Grep, Glob
---

You are an expert debugger specializing in root cause analysis.

When invoked:
1. Capture error message and stack trace
2. Identify reproduction steps
3. Isolate the failure location
4. Implement minimal fix
5. Verify solution works

Debugging process:
- Analyze error messages and logs
- Check recent code changes
- Form and test hypotheses
- Add strategic debug logging
- Inspect variable states

For each issue, provide:
- Root cause explanation
- Evidence supporting the diagnosis
- Specific code fix
- Testing approach
- Prevention recommendations

Focus on fixing the underlying issue, not just symptoms.

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#data-scientist)
Data scientist
Copy
```
---
name: data-scientist
description: Data analysis expert for SQL queries, BigQuery operations, and data insights. Use proactively for data analysis tasks and queries.
tools: Bash, Read, Write
---

You are a data scientist specializing in SQL and BigQuery analysis.

When invoked:
1. Understand the data analysis requirement
2. Write efficient SQL queries
3. Use BigQuery command line tools (bq) when appropriate
4. Analyze and summarize results
5. Present findings clearly

Key practices:
- Write optimized SQL queries with proper filters
- Use appropriate aggregations and joins
- Include comments explaining complex logic
- Format results for readability
- Provide data-driven recommendations

For each analysis:
- Explain the query approach
- Document any assumptions
- Highlight key findings
- Suggest next steps based on data

Always ensure queries are efficient and cost-effective.

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#best-practices)
Best practices
  * **Start with Claude-generated agents** : We highly recommend generating your initial subagent with Claude and then iterating on it to make it personally yours. This approach gives you the best results - a solid foundation that you can customize to your specific needs.
  * **Design focused subagents** : Create subagents with single, clear responsibilities rather than trying to make one subagent do everything. This improves performance and makes subagents more predictable.
  * **Write detailed prompts** : Include specific instructions, examples, and constraints in your system prompts. The more guidance you provide, the better the subagent will perform.
  * **Limit tool access** : Only grant tools that are necessary for the subagent’s purpose. This improves security and helps the subagent focus on relevant actions.
  * **Version control** : Check project subagents into version control so your team can benefit from and improve them collaboratively.


## 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#advanced-usage)
Advanced usage
### 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#chaining-subagents)
Chaining subagents
For complex workflows, you can chain multiple subagents:
Copy
```
> First use the code-analyzer subagent to find performance issues, then use the optimizer subagent to fix them

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#dynamic-subagent-selection)
Dynamic subagent selection
Claude Code intelligently selects subagents based on context. Make your `description` fields specific and action-oriented for best results.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#performance-considerations)
Performance considerations
  * **Context efficiency** : Agents help preserve main context, enabling longer overall sessions
  * **Latency** : Subagents start off with a clean slate each time they are invoked and may add latency as they gather context that they require to do their job effectively.


## 
[​](https://docs.anthropic.com/en/docs/claude-code/sub-agents#related-documentation)
Related documentation
  * [Slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands) - Learn about other built-in commands
  * [Settings](https://docs.anthropic.com/en/docs/claude-code/settings) - Configure Claude Code behavior
  * [Hooks](https://docs.anthropic.com/en/docs/claude-code/hooks) - Automate workflows with event handlers


Was this page helpful?
YesNo
[Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code/sdk)[Output styles](https://docs.anthropic.com/en/docs/claude-code/output-styles)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [What are subagents?](https://docs.anthropic.com/en/docs/claude-code/sub-agents#what-are-subagents%3F)
  * [Key benefits](https://docs.anthropic.com/en/docs/claude-code/sub-agents#key-benefits)
  * [Quick start](https://docs.anthropic.com/en/docs/claude-code/sub-agents#quick-start)
  * [Subagent configuration](https://docs.anthropic.com/en/docs/claude-code/sub-agents#subagent-configuration)
  * [File locations](https://docs.anthropic.com/en/docs/claude-code/sub-agents#file-locations)
  * [File format](https://docs.anthropic.com/en/docs/claude-code/sub-agents#file-format)
  * [Configuration fields](https://docs.anthropic.com/en/docs/claude-code/sub-agents#configuration-fields)
  * [Available tools](https://docs.anthropic.com/en/docs/claude-code/sub-agents#available-tools)
  * [Managing subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents#managing-subagents)
  * [Using the /agents command (Recommended)](https://docs.anthropic.com/en/docs/claude-code/sub-agents#using-the-%2Fagents-command-recommended)
  * [Direct file management](https://docs.anthropic.com/en/docs/claude-code/sub-agents#direct-file-management)
  * [Using subagents effectively](https://docs.anthropic.com/en/docs/claude-code/sub-agents#using-subagents-effectively)
  * [Automatic delegation](https://docs.anthropic.com/en/docs/claude-code/sub-agents#automatic-delegation)
  * [Explicit invocation](https://docs.anthropic.com/en/docs/claude-code/sub-agents#explicit-invocation)
  * [Example subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents#example-subagents)
  * [Code reviewer](https://docs.anthropic.com/en/docs/claude-code/sub-agents#code-reviewer)
  * [Debugger](https://docs.anthropic.com/en/docs/claude-code/sub-agents#debugger)
  * [Data scientist](https://docs.anthropic.com/en/docs/claude-code/sub-agents#data-scientist)
  * [Best practices](https://docs.anthropic.com/en/docs/claude-code/sub-agents#best-practices)
  * [Advanced usage](https://docs.anthropic.com/en/docs/claude-code/sub-agents#advanced-usage)
  * [Chaining subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents#chaining-subagents)
  * [Dynamic subagent selection](https://docs.anthropic.com/en/docs/claude-code/sub-agents#dynamic-subagent-selection)
  * [Performance considerations](https://docs.anthropic.com/en/docs/claude-code/sub-agents#performance-considerations)
  * [Related documentation](https://docs.anthropic.com/en/docs/claude-code/sub-agents#related-documentation)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/terminal-config -->

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
Optimize your terminal setup
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
# Optimize your terminal setup
Copy page
Claude Code works best when your terminal is properly configured. Follow these guidelines to optimize your experience.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/terminal-config#themes-and-appearance)
Themes and appearance
Claude cannot control the theme of your terminal. That’s handled by your terminal application. You can match Claude Code’s theme to your terminal any time via the `/config` command.
For additional customization of the Claude Code interface itself, you can configure a [custom status line](https://docs.anthropic.com/en/docs/claude-code/statusline) to display contextual information like the current model, working directory, or git branch at the bottom of your terminal.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/terminal-config#line-breaks)
Line breaks
You have several options for entering linebreaks into Claude Code:
  * **Quick escape** : Type `\` followed by Enter to create a newline
  * **Keyboard shortcut** : Set up a keybinding to insert a newline


#### 
[​](https://docs.anthropic.com/en/docs/claude-code/terminal-config#set-up-shift%2Benter-vs-code-or-iterm2-%3A)
Set up Shift+Enter (VS Code or iTerm2):
Run `/terminal-setup` within Claude Code to automatically configure Shift+Enter.
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/terminal-config#set-up-option%2Benter-vs-code%2C-iterm2-or-macos-terminal-app-%3A)
Set up Option+Enter (VS Code, iTerm2 or macOS Terminal.app):
**For Mac Terminal.app:**
  1. Open Settings → Profiles → Keyboard
  2. Check “Use Option as Meta Key”


**For iTerm2 and VS Code terminal:**
  1. Open Settings → Profiles → Keys
  2. Under General, set Left/Right Option key to “Esc+“


### 
[​](https://docs.anthropic.com/en/docs/claude-code/terminal-config#notification-setup)
Notification setup
Never miss when Claude completes a task with proper notification configuration:
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/terminal-config#terminal-bell-notifications)
Terminal bell notifications
Enable sound alerts when tasks complete:
Copy
```
claude config set --global preferredNotifChannel terminal_bell

```

**For macOS users** : Don’t forget to enable notification permissions in System Settings → Notifications → [Your Terminal App].
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/terminal-config#iterm-2-system-notifications)
iTerm 2 system notifications
For iTerm 2 alerts when tasks complete:
  1. Open iTerm 2 Preferences
  2. Navigate to Profiles → Terminal
  3. Enable “Silence bell” and Filter Alerts → “Send escape sequence-generated alerts”
  4. Set your preferred notification delay


Note that these notifications are specific to iTerm 2 and not available in the default macOS Terminal.
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/terminal-config#custom-notification-hooks)
Custom notification hooks
For advanced notification handling, you can create [notification hooks](https://docs.anthropic.com/en/docs/claude-code/hooks#notification) to run your own logic.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/terminal-config#handling-large-inputs)
Handling large inputs
When working with extensive code or long instructions:
  * **Avoid direct pasting** : Claude Code may struggle with very long pasted content
  * **Use file-based workflows** : Write content to a file and ask Claude to read it
  * **Be aware of VS Code limitations** : The VS Code terminal is particularly prone to truncating long pastes


### 
[​](https://docs.anthropic.com/en/docs/claude-code/terminal-config#vim-mode)
Vim Mode
Claude Code supports a subset of Vim keybindings that can be enabled with `/vim` or configured via `/config`.
The supported subset includes:
  * Mode switching: `Esc` (to NORMAL), `i`/`I`, `a`/`A`, `o`/`O` (to INSERT)
  * Navigation: `h`/`j`/`k`/`l`, `w`/`e`/`b`, `0`/`$`/`^`, `gg`/`G`
  * Editing: `x`, `dw`/`de`/`db`/`dd`/`D`, `cw`/`ce`/`cb`/`cc`/`C`, `.` (repeat)


Was this page helpful?
YesNo
[Add Claude Code to your IDE](https://docs.anthropic.com/en/docs/claude-code/ide-integrations)[Memory management](https://docs.anthropic.com/en/docs/claude-code/memory)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Themes and appearance](https://docs.anthropic.com/en/docs/claude-code/terminal-config#themes-and-appearance)
  * [Line breaks](https://docs.anthropic.com/en/docs/claude-code/terminal-config#line-breaks)
  * [Set up Shift+Enter (VS Code or iTerm2):](https://docs.anthropic.com/en/docs/claude-code/terminal-config#set-up-shift%2Benter-vs-code-or-iterm2-%3A)
  * [Set up Option+Enter (VS Code, iTerm2 or macOS Terminal.app):](https://docs.anthropic.com/en/docs/claude-code/terminal-config#set-up-option%2Benter-vs-code%2C-iterm2-or-macos-terminal-app-%3A)
  * [Notification setup](https://docs.anthropic.com/en/docs/claude-code/terminal-config#notification-setup)
  * [Terminal bell notifications](https://docs.anthropic.com/en/docs/claude-code/terminal-config#terminal-bell-notifications)
  * [iTerm 2 system notifications](https://docs.anthropic.com/en/docs/claude-code/terminal-config#iterm-2-system-notifications)
  * [Custom notification hooks](https://docs.anthropic.com/en/docs/claude-code/terminal-config#custom-notification-hooks)
  * [Handling large inputs](https://docs.anthropic.com/en/docs/claude-code/terminal-config#handling-large-inputs)
  * [Vim Mode](https://docs.anthropic.com/en/docs/claude-code/terminal-config#vim-mode)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/third-party-integrations -->

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](https://docs.anthropic.com/)
English
Search...
  * [Research](https://www.anthropic.com/research)
  * [Login](https://console.anthropic.com/login)
  * [Support](https://support.anthropic.com/)
  * [Discord](https://www.anthropic.com/discord)
  * [Sign up](https://console.anthropic.com/login)
  * [Sign up](https://console.anthropic.com/login)


Search...
Navigation
Deployment
Enterprise deployment overview
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
# Enterprise deployment overview
Copy page
Learn how Claude Code can integrate with various third-party services and infrastructure to meet enterprise deployment requirements.
This page provides an overview of available deployment options and helps you choose the right configuration for your organization.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#provider-comparison)
Provider comparison
Feature | Anthropic | Amazon Bedrock | Google Vertex AI  
---|---|---|---  
Regions | Supported [countries](https://www.anthropic.com/supported-countries) | Multiple AWS [regions](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) | Multiple GCP [regions](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations)  
Prompt caching | Enabled by default | Enabled by default | Enabled by default  
Authentication | API key | AWS credentials (IAM) | GCP credentials (OAuth/Service Account)  
Cost tracking | Dashboard | AWS Cost Explorer | GCP Billing  
Enterprise features | Teams, usage monitoring | IAM policies, CloudTrail | IAM roles, Cloud Audit Logs  
## 
[​](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#cloud-providers)
Cloud providers
## [Amazon Bedrock Use Claude models through AWS infrastructure with IAM-based authentication and AWS-native monitoring ](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock)## [Google Vertex AI Access Claude models via Google Cloud Platform with enterprise-grade security and compliance ](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai)
## 
[​](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#corporate-infrastructure)
Corporate infrastructure
## [Corporate Proxy Configure Claude Code to work with your organization’s proxy servers and SSL/TLS requirements ](https://docs.anthropic.com/en/docs/claude-code/corporate-proxy)## [LLM Gateway Deploy centralized model access with usage tracking, budgeting, and audit logging ](https://docs.anthropic.com/en/docs/claude-code/llm-gateway)
## 
[​](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#configuration-overview)
Configuration overview
Claude Code supports flexible configuration options that allow you to combine different providers and infrastructure:
Understand the difference between:
  * **Corporate proxy** : An HTTP/HTTPS proxy for routing traffic (set via `HTTPS_PROXY` or `HTTP_PROXY`)
  * **LLM Gateway** : A service that handles authentication and provides provider-compatible endpoints (set via `ANTHROPIC_BASE_URL`, `ANTHROPIC_BEDROCK_BASE_URL`, or `ANTHROPIC_VERTEX_BASE_URL`)


Both configurations can be used in tandem.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#using-bedrock-with-corporate-proxy)
Using Bedrock with corporate proxy
Route Bedrock traffic through a corporate HTTP/HTTPS proxy:
```
# Enable Bedrock
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=us-east-1

# Configure corporate proxy
export HTTPS_PROXY='https://proxy.example.com:8080'

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#using-bedrock-with-llm-gateway)
Using Bedrock with LLM Gateway
Use a gateway service that provides Bedrock-compatible endpoints:
```
# Enable Bedrock
export CLAUDE_CODE_USE_BEDROCK=1

# Configure LLM gateway
export ANTHROPIC_BEDROCK_BASE_URL='https://your-llm-gateway.com/bedrock'
export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1  # If gateway handles AWS auth

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#using-vertex-ai-with-corporate-proxy)
Using Vertex AI with corporate proxy
Route Vertex AI traffic through a corporate HTTP/HTTPS proxy:
```
# Enable Vertex
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5
export ANTHROPIC_VERTEX_PROJECT_ID=your-project-id

# Configure corporate proxy
export HTTPS_PROXY='https://proxy.example.com:8080'

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#using-vertex-ai-with-llm-gateway)
Using Vertex AI with LLM Gateway
Combine Google Vertex AI models with an LLM gateway for centralized management:
```
# Enable Vertex
export CLAUDE_CODE_USE_VERTEX=1

# Configure LLM gateway
export ANTHROPIC_VERTEX_BASE_URL='https://your-llm-gateway.com/vertex'
export CLAUDE_CODE_SKIP_VERTEX_AUTH=1  # If gateway handles GCP auth

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#authentication-configuration)
Authentication configuration
Claude Code uses the `ANTHROPIC_AUTH_TOKEN` for the `Authorization` header when needed. The `SKIP_AUTH` flags (`CLAUDE_CODE_SKIP_BEDROCK_AUTH`, `CLAUDE_CODE_SKIP_VERTEX_AUTH`) are used in LLM gateway scenarios where the gateway handles provider authentication.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#choosing-the-right-deployment-configuration)
Choosing the right deployment configuration
Consider these factors when selecting your deployment approach:
### 
[​](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#direct-provider-access)
Direct provider access
Best for organizations that:
  * Want the simplest setup
  * Have existing AWS or GCP infrastructure
  * Need provider-native monitoring and compliance


### 
[​](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#corporate-proxy)
Corporate proxy
Best for organizations that:
  * Have existing corporate proxy requirements
  * Need traffic monitoring and compliance
  * Must route all traffic through specific network paths


### 
[​](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#llm-gateway)
LLM Gateway
Best for organizations that:
  * Need usage tracking across teams
  * Want to dynamically switch between models
  * Require custom rate limiting or budgets
  * Need centralized authentication management


## 
[​](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#debugging)
Debugging
When debugging your deployment:
  * Use the `claude /status` [slash command](https://docs.anthropic.com/en/docs/claude-code/slash-commands). This command provides observability into any applied authentication, proxy, and URL settings.
  * Set environment variable `export ANTHROPIC_LOG=debug` to log requests.


## 
[​](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#best-practices-for-organizations)
Best practices for organizations
### 
[​](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#1-invest-in-documentation-and-memory)
1. Invest in documentation and memory
We strongly recommend investing in documentation so that Claude Code understands your codebase. Organizations can deploy CLAUDE.md files at multiple levels:
  * **Organization-wide** : Deploy to system directories like `/Library/Application Support/ClaudeCode/CLAUDE.md` (macOS) for company-wide standards
  * **Repository-level** : Create `CLAUDE.md` files in repository roots containing project architecture, build commands, and contribution guidelines. Check these into source control so all users benefit
[Learn more](https://docs.anthropic.com/en/docs/claude-code/memory).


### 
[​](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#2-simplify-deployment)
2. Simplify deployment
If you have a custom development environment, we find that creating a “one click” way to install Claude Code is key to growing adoption across an organization.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#3-start-with-guided-usage)
3. Start with guided usage
Encourage new users to try Claude Code for codebase Q&A, or on smaller bug fixes or feature requests. Ask Claude Code to make a plan. Check Claude’s suggestions and give feedback if it’s off-track. Over time, as users understand this new paradigm better, then they’ll be more effective at letting Claude Code run more agentically.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#4-configure-security-policies)
4. Configure security policies
Security teams can configure managed permissions for what Claude Code is and is not allowed to do, which cannot be overwritten by local configuration. [Learn more](https://docs.anthropic.com/en/docs/claude-code/security).
### 
[​](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#5-leverage-mcp-for-integrations)
5. Leverage MCP for integrations
MCP is a great way to give Claude Code more information, such as connecting to ticket management systems or error logs. We recommend that one central team configures MCP servers and checks a `.mcp.json` configuration into the codebase so that all users benefit. [Learn more](https://docs.anthropic.com/en/docs/claude-code/mcp).
At Anthropic, we trust Claude Code to power development across every Anthropic codebase. We hope you enjoy using Claude Code as much as we do!
## 
[​](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#next-steps)
Next steps
  * [Set up Amazon Bedrock](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock) for AWS-native deployment
  * [Configure Google Vertex AI](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai) for GCP deployment
  * [Implement Corporate Proxy](https://docs.anthropic.com/en/docs/claude-code/corporate-proxy) for network requirements
  * [Deploy LLM Gateway](https://docs.anthropic.com/en/docs/claude-code/llm-gateway) for enterprise management
  * [Settings](https://docs.anthropic.com/en/docs/claude-code/settings) for configuration options and environment variables


Was this page helpful?
YesNo
[Troubleshooting](https://docs.anthropic.com/en/docs/claude-code/troubleshooting)[Amazon Bedrock](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Provider comparison](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#provider-comparison)
  * [Cloud providers](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#cloud-providers)
  * [Corporate infrastructure](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#corporate-infrastructure)
  * [Configuration overview](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#configuration-overview)
  * [Using Bedrock with corporate proxy](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#using-bedrock-with-corporate-proxy)
  * [Using Bedrock with LLM Gateway](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#using-bedrock-with-llm-gateway)
  * [Using Vertex AI with corporate proxy](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#using-vertex-ai-with-corporate-proxy)
  * [Using Vertex AI with LLM Gateway](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#using-vertex-ai-with-llm-gateway)
  * [Authentication configuration](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#authentication-configuration)
  * [Choosing the right deployment configuration](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#choosing-the-right-deployment-configuration)
  * [Direct provider access](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#direct-provider-access)
  * [Corporate proxy](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#corporate-proxy)
  * [LLM Gateway](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#llm-gateway)
  * [Debugging](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#debugging)
  * [Best practices for organizations](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#best-practices-for-organizations)
  * [1. Invest in documentation and memory](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#1-invest-in-documentation-and-memory)
  * [2. Simplify deployment](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#2-simplify-deployment)
  * [3. Start with guided usage](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#3-start-with-guided-usage)
  * [4. Configure security policies](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#4-configure-security-policies)
  * [5. Leverage MCP for integrations](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#5-leverage-mcp-for-integrations)
  * [Next steps](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations#next-steps)


---


<!-- Source: https://docs.anthropic.com/en/docs/claude-code/troubleshooting -->

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
Troubleshooting
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
# Troubleshooting
Copy page
Discover solutions to common issues with Claude Code installation and usage.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#common-installation-issues)
Common installation issues
### 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#windows-installation-issues%3A-errors-in-wsl)
Windows installation issues: errors in WSL
You might encounter the following issues in WSL:
**OS/platform detection issues** : If you receive an error during installation, WSL may be using Windows `npm`. Try:
  * Run `npm config set os linux` before installation
  * Install with `npm install -g @anthropic-ai/claude-code --force --no-os-check` (Do NOT use `sudo`)


**Node not found errors** : If you see `exec: node: not found` when running `claude`, your WSL environment may be using a Windows installation of Node.js. You can confirm this with `which npm` and `which node`, which should point to Linux paths starting with `/usr/` rather than `/mnt/c/`. To fix this, try installing Node via your Linux distribution’s package manager or via [`nvm`](https://github.com/nvm-sh/nvm).
### 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#linux-and-mac-installation-issues%3A-permission-or-command-not-found-errors)
Linux and Mac installation issues: permission or command not found errors
When installing Claude Code with npm, `PATH` problems may prevent access to `claude`. You may also encounter permission errors if your npm global prefix is not user writable (eg. `/usr`, or `/usr/local`).
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#recommended-solution%3A-native-claude-code-installation)
Recommended solution: Native Claude Code installation
Claude Code has a native installation that doesn’t depend on npm or Node.js.
The native Claude Code installer is currently in beta.
Use the following command to run the native installer.
**macOS, Linux, WSL:**
Copy
```
# Install stable version (default)
curl -fsSL https://claude.ai/install.sh | bash

# Install latest version
curl -fsSL https://claude.ai/install.sh | bash -s latest

# Install specific version number
curl -fsSL https://claude.ai/install.sh | bash -s 1.0.58

```

**Windows PowerShell:**
Copy
```
# Install stable version (default)
irm https://claude.ai/install.ps1 | iex

# Install latest version
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) latest

# Install specific version number
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) 1.0.58


```

This command installs the appropriate build of Claude Code for your operating system and architecture and adds a symlink to the installation at `~/.local/bin/claude`.
Make sure that you have the installation directory in your system PATH.
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#alternative-solution%3A-migrate-to-local-installation)
Alternative solution: Migrate to local installation
Alternatively, if Claude Code will run, you can migrate to a local installation:
Copy
```
claude migrate-installer

```

This moves Claude Code to `~/.claude/local/` and sets up an alias in your shell configuration. No `sudo` is required for future updates.
After migration, restart your shell, and then verify your installation:
On macOS/Linux/WSL:
Copy
```
which claude  # Should show an alias to ~/.claude/local/claude

```

On Windows:
Copy
```
where claude  # Should show path to claude executable

```

Verify installation:
Copy
```
claude doctor # Check installation health

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#permissions-and-authentication)
Permissions and authentication
### 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#repeated-permission-prompts)
Repeated permission prompts
If you find yourself repeatedly approving the same commands, you can allow specific tools to run without approval using the `/permissions` command. See [Permissions docs](https://docs.anthropic.com/en/docs/claude-code/iam#configuring-permissions).
### 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#authentication-issues)
Authentication issues
If you’re experiencing authentication problems:
  1. Run `/logout` to sign out completely
  2. Close Claude Code
  3. Restart with `claude` and complete the authentication process again


If problems persist, try:
Copy
```
rm -rf ~/.config/claude-code/auth.json
claude

```

This removes your stored authentication information and forces a clean login.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#performance-and-stability)
Performance and stability
### 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#high-cpu-or-memory-usage)
High CPU or memory usage
Claude Code is designed to work with most development environments, but may consume significant resources when processing large codebases. If you’re experiencing performance issues:
  1. Use `/compact` regularly to reduce context size
  2. Close and restart Claude Code between major tasks
  3. Consider adding large build directories to your `.gitignore` file


### 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#command-hangs-or-freezes)
Command hangs or freezes
If Claude Code seems unresponsive:
  1. Press Ctrl+C to attempt to cancel the current operation
  2. If unresponsive, you may need to close the terminal and restart


### 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#esc-key-not-working-in-jetbrains-intellij%2C-pycharm%2C-etc-terminals)
ESC key not working in JetBrains (IntelliJ, PyCharm, etc.) terminals
If you’re using Claude Code in JetBrains terminals and the ESC key doesn’t interrupt the agent as expected, this is likely due to a keybinding clash with JetBrains’ default shortcuts.
To fix this issue:
  1. Go to Settings → Tools → Terminal
  2. Click the “Configure terminal keybindings” hyperlink next to “Override IDE Shortcuts”
  3. Within the terminal keybindings, scroll down to “Switch focus to Editor” and delete that shortcut


This will allow the ESC key to properly function for canceling Claude Code operations instead of being captured by PyCharm’s “Switch focus to Editor” action.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#markdown-formatting-issues)
Markdown formatting issues
Claude Code sometimes generates markdown files with missing language tags on code fences, which can affect syntax highlighting and readability in GitHub, editors, and documentation tools.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#missing-language-tags-in-code-blocks)
Missing language tags in code blocks
If you notice code blocks like this in generated markdown:
Copy
```
```
function example() {
  return "hello";
}
```

```

Instead of properly tagged blocks like:
Copy
```
```javascript
function example() {
  return "hello";
}
```

```

**Solutions:**
  1. **Ask Claude to add language tags** : Simply request “Please add appropriate language tags to all code blocks in this markdown file.”
  2. **Use post-processing hooks** : Set up automatic formatting hooks to detect and add missing language tags. See the [markdown formatting hook example](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#markdown-formatting-hook) for implementation details.
  3. **Manual verification** : After generating markdown files, review them for proper code block formatting and request corrections if needed.


### 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#inconsistent-spacing-and-formatting)
Inconsistent spacing and formatting
If generated markdown has excessive blank lines or inconsistent spacing:
**Solutions:**
  1. **Request formatting corrections** : Ask Claude to “Fix spacing and formatting issues in this markdown file.”
  2. **Use formatting tools** : Set up hooks to run markdown formatters like `prettier` or custom formatting scripts on generated markdown files.
  3. **Specify formatting preferences** : Include formatting requirements in your prompts or project [memory](https://docs.anthropic.com/en/docs/claude-code/memory) files.


### 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#best-practices-for-markdown-generation)
Best practices for markdown generation
To minimize formatting issues:
  * **Be explicit in requests** : Ask for “properly formatted markdown with language-tagged code blocks”
  * **Use project conventions** : Document your preferred markdown style in [CLAUDE.md](https://docs.anthropic.com/en/docs/claude-code/memory)
  * **Set up validation hooks** : Use post-processing hooks to automatically verify and fix common formatting issues


## 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#getting-more-help)
Getting more help
If you’re experiencing issues not covered here:
  1. Use the `/bug` command within Claude Code to report problems directly to Anthropic
  2. Check the [GitHub repository](https://github.com/anthropics/claude-code) for known issues
  3. Run `/doctor` to check the health of your Claude Code installation
  4. Ask Claude directly about its capabilities and features - Claude has built-in access to its documentation


Was this page helpful?
YesNo
[Model Context Protocol (MCP)](https://docs.anthropic.com/en/docs/claude-code/mcp)[Overview](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Common installation issues](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#common-installation-issues)
  * [Windows installation issues: errors in WSL](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#windows-installation-issues%3A-errors-in-wsl)
  * [Linux and Mac installation issues: permission or command not found errors](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#linux-and-mac-installation-issues%3A-permission-or-command-not-found-errors)
  * [Recommended solution: Native Claude Code installation](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#recommended-solution%3A-native-claude-code-installation)
  * [Alternative solution: Migrate to local installation](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#alternative-solution%3A-migrate-to-local-installation)
  * [Permissions and authentication](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#permissions-and-authentication)
  * [Repeated permission prompts](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#repeated-permission-prompts)
  * [Authentication issues](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#authentication-issues)
  * [Performance and stability](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#performance-and-stability)
  * [High CPU or memory usage](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#high-cpu-or-memory-usage)
  * [Command hangs or freezes](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#command-hangs-or-freezes)
  * [ESC key not working in JetBrains (IntelliJ, PyCharm, etc.) terminals](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#esc-key-not-working-in-jetbrains-intellij%2C-pycharm%2C-etc-terminals)
  * [Markdown formatting issues](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#markdown-formatting-issues)
  * [Missing language tags in code blocks](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#missing-language-tags-in-code-blocks)
  * [Inconsistent spacing and formatting](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#inconsistent-spacing-and-formatting)
  * [Best practices for markdown generation](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#best-practices-for-markdown-generation)
  * [Getting more help](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#getting-more-help)


---
