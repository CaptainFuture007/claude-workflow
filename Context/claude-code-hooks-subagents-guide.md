# Claude Code Hooks and Sub-agents: Complete Guide
*This guide provides a comprehensive understanding of Claude Code's hooks and sub-agents features based on official Anthropic documentation*

## Overview

Claude Code offers two powerful features for extending and customizing its behavior:
1. **Hooks**: User-defined shell commands that execute at various points in Claude Code's lifecycle
2. **Sub-agents**: Specialized AI assistants that handle specific types of tasks with their own context

## Part 1: Claude Code Hooks

### What are Hooks?

Hooks are shell commands that provide deterministic control over Claude Code's behavior. Instead of relying on the LLM to choose actions, hooks ensure certain actions always happen at specific points.

### Key Benefits
- **Automatic execution**: No need to remind Claude to run specific commands
- **Customizable workflows**: Integrate with your existing tools and processes
- **Security controls**: Block dangerous operations before they execute
- **Logging and monitoring**: Track all operations for compliance

### Hook Events

Claude Code supports 8 different hook events:

#### 1. **PreToolUse**
- **When**: Before any tool execution
- **Purpose**: Validate, block, or modify tool calls
- **Exit code 2**: Blocks the tool call and shows error to Claude
- **Common uses**: Security checks, permission validation

#### 2. **PostToolUse**
- **When**: After successful tool completion
- **Purpose**: Process results, format code, log operations
- **Exit code 2**: Shows error to Claude (tool already ran)
- **Common uses**: Auto-formatting, result validation

#### 3. **Notification**
- **When**: Claude sends notifications (needs permission, idle prompt)
- **Purpose**: Custom notification systems
- **Common uses**: Desktop alerts, sound notifications

#### 4. **Stop**
- **When**: Claude finishes responding
- **Purpose**: Final cleanup, summary generation
- **Exit code 2**: Blocks stoppage, Claude continues
- **Common uses**: Session summaries, final checks

#### 5. **SubagentStop**
- **When**: Sub-agents finish responding
- **Purpose**: Sub-agent specific cleanup
- **Exit code 2**: Blocks sub-agent from stopping

#### 6. **PreCompact**
- **When**: Before context compaction
- **Purpose**: Backup transcripts, save context
- **Common uses**: Transcript archival

#### 7. **SessionStart**
- **When**: New session starts or resumes
- **Purpose**: Initialize environment, load context
- **Common uses**: Load git status, recent issues

#### 8. **UserPromptSubmit**
- **When**: User submits a prompt
- **Purpose**: Validate/enhance prompts before Claude sees them
- **Common uses**: Context injection, prompt validation

### Hook Configuration

Hooks are configured in JSON settings files:
- `~/.claude/settings.json` - Global user settings
- `.claude/settings.json` - Project settings (version controlled)
- `.claude/settings.local.json` - Local project settings (not committed)

#### Basic Structure
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'File modification detected' >> audit.log"
          }
        ]
      }
    ]
  }
}
```

#### Matchers
- **Exact match**: `"Write"` matches only Write tool
- **Regex**: `"Edit|Write"` or `"Notebook.*"`
- **All tools**: Empty string or omitted matcher

### Hook Input/Output

#### Input (via stdin)
All hooks receive JSON data containing:
- Session information (id, timestamp)
- Event-specific data (tool_name, tool_input, etc.)

#### Output Options

1. **Simple Exit Codes**:
   - `0`: Success (stdout shown in transcript mode)
   - `2`: Blocking error (stderr fed to Claude)
   - Other: Non-blocking error (stderr shown to user)

2. **Advanced JSON Output**:
```json
{
  "continue": true,
  "stopReason": "Optional message",
  "decision": "approve|block",
  "reason": "Explanation for Claude",
  "suppressOutput": false
}
```

### Security Considerations

⚠️ **Important**: Hooks execute with your full user permissions without confirmation!

**Best Practices**:
- Always quote shell variables: `"$VAR"` not `$VAR`
- Validate inputs - never trust data blindly
- Use absolute paths for scripts
- Check for path traversal (`..` in paths)
- Avoid sensitive files (.env, .git/, keys)
- Test hooks in safe environments first

### Practical Examples

#### 1. Auto-format TypeScript files
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [{
          "type": "command",
          "command": "file=$(echo '$HOOK_INPUT' | jq -r '.tool_input.file_path'); [[ $file == *.ts ]] && prettier --write \"$file\""
        }]
      }
    ]
  }
}
```

#### 2. Block sensitive file access
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write|Read",
        "hooks": [{
          "type": "command",
          "command": "python3 -c \"import json, sys; data=json.load(sys.stdin); path=data.get('tool_input',{}).get('file_path',''); sys.exit(2 if '.env' in path or '.git/' in path else 0)\""
        }]
      }
    ]
  }
}
```

#### 3. Custom notifications
```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [{
          "type": "command",
          "command": "notify-send 'Claude Code' \"$(jq -r '.message' < /dev/stdin)\""
        }]
      }
    ]
  }
}
```

## Part 2: Claude Code Sub-agents

### What are Sub-agents?

Sub-agents are specialized AI assistants that Claude Code can delegate specific tasks to. Each sub-agent has:
- Its own context window (prevents main conversation pollution)
- Specific expertise area and custom system prompt
- Configurable tool access
- Reusable across projects

### Key Benefits

1. **Context Preservation**: Separate context prevents cluttering main conversation
2. **Specialized Expertise**: Domain-specific instructions improve task performance
3. **Reusability**: Share agents across projects and teams
4. **Flexible Permissions**: Limit tool access per agent

### Creating Sub-agents

#### Quick Start
1. Run `/agents` command
2. Select "Create New Agent"
3. Choose project or user level
4. Define agent (recommend: generate with Claude first)
5. Select allowed tools
6. Save and use

#### File Structure
Sub-agents are Markdown files with YAML frontmatter:

```markdown
---
name: code-reviewer
description: Reviews code for style, bugs, and best practices. Use PROACTIVELY for all code changes.
tools: Read, Grep, Bash
---

You are an expert code reviewer specializing in finding bugs, style issues, and suggesting improvements.

## Your approach:
1. Analyze code structure and patterns
2. Check for common bugs and edge cases
3. Verify naming conventions and style guidelines
4. Suggest performance optimizations
5. Ensure proper error handling

## Key practices:
- Be constructive but thorough
- Prioritize critical issues over style preferences
- Provide specific examples for improvements
- Consider the broader codebase context

Always explain WHY something should be changed, not just what to change.
```

### Configuration Fields

| Field | Required | Description |
|-------|----------|-------------|
| name | Yes | Unique identifier (lowercase, hyphens) |
| description | Yes | When to use this agent |
| tools | No | Comma-separated tools (inherits all if omitted) |

### File Locations

- **Project agents**: `.claude/agents/` (highest priority)
- **User agents**: `~/.claude/agents/` (available globally)

### Using Sub-agents

#### Automatic Delegation
Claude Code automatically uses sub-agents based on:
- Task description in your request
- Agent's description field
- Current context

**Tip**: Include "use PROACTIVELY" or "MUST BE USED" in descriptions for more frequent use.

#### Explicit Invocation
```bash
# Direct request
"Use the debugger agent to fix this error"

# Chaining agents
"First analyze with data-scientist, then optimize with performance-expert"
```

### Example Sub-agents

#### 1. Debugger Agent
```markdown
---
name: debugger
description: Expert at debugging errors and fixing issues. Use PROACTIVELY for any error messages or bugs.
tools: Read, Edit, Bash, Grep
---

You are a debugging specialist. When encountering errors:

1. Read the full error message and stack trace
2. Identify the root cause, not just symptoms
3. Search for similar patterns in the codebase
4. Implement a fix that addresses the core issue
5. Verify the fix resolves the problem
6. Check for similar issues elsewhere

Always test your fixes before confirming they work.
```

#### 2. Test Writer
```markdown
---
name: test-writer
description: Writes comprehensive unit and integration tests
tools: Write, Read, Bash
---

You are a test-driven development expert. Your approach:

1. Analyze the code to understand all use cases
2. Write tests for happy paths and edge cases
3. Include negative test cases
4. Ensure good test coverage
5. Use descriptive test names
6. Mock external dependencies appropriately

Follow the project's existing test patterns and frameworks.
```

#### 3. Data Analyst
```markdown
---
name: data-analyst
description: Analyzes data files, creates visualizations, and provides insights
tools: Read, Write, Bash
---

You are a data scientist specializing in exploratory data analysis.

When given data files:
1. First understand the structure and schema
2. Check for data quality issues
3. Generate summary statistics
4. Create meaningful visualizations
5. Identify patterns and anomalies
6. Provide actionable insights

Use pandas, matplotlib, and other Python data tools effectively.
```

### Best Practices

1. **Start with Claude**: Generate initial agents with Claude, then customize
2. **Single Responsibility**: Each agent should have one clear purpose
3. **Detailed Prompts**: Include specific instructions, examples, constraints
4. **Limited Tools**: Only grant necessary tools for security and focus
5. **Version Control**: Commit project agents for team collaboration
6. **Clear Descriptions**: Make descriptions action-oriented for better selection

### Advanced Patterns

#### Agent Chaining
```bash
# Complex workflow with multiple agents
"Use security-scanner to audit the code, then code-formatter to clean it up, and finally doc-writer to update the documentation"
```

#### Meta-agent
Create an agent that generates other agents:
```markdown
---
name: meta-agent
description: Creates new sub-agents from descriptions
tools: Write
---

You specialize in creating well-structured sub-agents for Claude Code...
```

### Integration with Hooks

Sub-agents work seamlessly with hooks:
- Hooks can run before/after sub-agent operations
- SubagentStop hook specifically for sub-agent completion
- Sub-agents respect hook configurations

### Performance Considerations

- **Context Efficiency**: Preserves main context for longer sessions
- **Latency**: Sub-agents start fresh each time (may need to gather context)
- **Tool Access**: Limiting tools improves focus and security

## Common Patterns and Workflows

### 1. Automated Code Review Pipeline
```json
// Hook configuration
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [{
          "type": "command",
          "command": "echo 'trigger:code-review' >> .claude/pending-reviews.txt"
        }]
      }
    ]
  }
}
```

### 2. Security-First Development
- PreToolUse hooks block sensitive operations
- Security-scanner sub-agent reviews changes
- Audit logs track all modifications

### 3. Test-Driven Development
- test-writer agent creates tests first
- Main Claude implements features
- test-runner agent verifies implementation

## Troubleshooting

### Hooks Not Running?
1. Check `/hooks` menu shows configuration
2. Verify valid JSON in settings files
3. Test commands manually
4. Check exit codes and output format
5. Use transcript mode (Ctrl-R) to see progress

### Sub-agents Not Being Used?
1. Make descriptions more specific
2. Add "use PROACTIVELY" to description
3. Check tool availability
4. Verify file locations and naming
5. Use explicit invocation to test

## Conclusion

Claude Code's hooks and sub-agents transform it from a coding assistant into a customizable development platform. By combining:
- **Hooks** for deterministic automation and control
- **Sub-agents** for specialized, context-preserving expertise

You can build sophisticated development workflows that match your team's specific needs while maintaining security and efficiency.