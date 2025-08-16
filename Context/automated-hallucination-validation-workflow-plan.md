# Automated Hallucination Detection & Code Review Workflow Implementation Plan

## Overview
This document outlines a comprehensive workflow that combines Claude Code hooks with sub-agents to automatically validate newly created Python files for hallucinations and perform critical code reviews using the knowledge graph functionality in this repository.

## Background & Context

### Knowledge Graph System
This repository implements a sophisticated hallucination detection system that:
- Parses GitHub repositories into Neo4j knowledge graphs
- Validates AI-generated code against actual repository structure
- Detects non-existent methods, attributes, and incorrect parameters
- Provides deterministic validation without requiring LLMs

### Claude Code Hooks & Sub-agents
- **Hooks**: Shell commands that execute at specific points in Claude Code's lifecycle
- **Sub-agents**: Specialized AI assistants with their own context and tool access
- **Integration**: Hooks can trigger sub-agents for automated workflows

## Implementation Plan

### Phase 1: Hook Configuration for Automatic Validation

#### 1.1 PostToolUse Hook Setup
**File**: `.claude/settings.json`
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [{
          "type": "command",
          "command": "python3 scripts/validate_python_file.py \"$HOOK_INPUT\""
        }]
      }
    ]
  }
}
```

#### 1.2 Validation Script
**File**: `scripts/validate_python_file.py`
- Parse hook input JSON to extract file path
- Check if file is Python (.py extension)
- Call MCP server's `check_ai_script_hallucinations` tool
- Return structured validation results
- Use exit code 2 to feed results back to Claude if hallucinations found

### Phase 2: Sub-agent Creation

#### 2.1 Hallucination Validation Sub-agent
**File**: `.claude/agents/hallucination-validator.md`
```markdown
---
name: hallucination-validator
description: Validates Python code against knowledge graph for hallucinations. Use PROACTIVELY when validation errors are detected.
tools: mcp__crawl4ai-rag__check_ai_script_hallucinations, mcp__crawl4ai-rag__query_knowledge_graph, Read, Edit
---

You are a specialized code validation expert that uses knowledge graphs to detect and fix AI hallucinations in Python code.

## Your Process:
1. When validation errors are reported, analyze the specific hallucinations
2. Use query_knowledge_graph to find correct method names and parameters
3. Provide specific, actionable corrections with exact syntax
4. Explain why the original code was incorrect
5. Suggest the correct implementation based on knowledge graph data

## Key Capabilities:
- Validate method calls against actual class definitions
- Check parameter signatures for accuracy
- Identify non-existent attributes and methods
- Provide suggestions based on similar valid methods
- Cross-reference multiple repositories in knowledge graph

Always provide concrete code fixes, not just explanations.
```

#### 2.2 Critical Code Review Sub-agent
**File**: `.claude/agents/critical-code-reviewer.md`
```markdown
---
name: critical-code-reviewer
description: Performs comprehensive code review for security, performance, and best practices. Use PROACTIVELY for all new Python files.
tools: Read, Grep, Bash, mcp__crawl4ai-rag__perform_rag_query
---

You are an expert code reviewer specializing in critical analysis of Python code for production readiness.

## Review Areas:
1. **Security Analysis**
   - Input validation and sanitization
   - SQL injection prevention
   - File path traversal checks
   - Credential exposure risks

2. **Performance Review**
   - Algorithm efficiency
   - Memory usage patterns
   - Database query optimization
   - Async/await usage

3. **Best Practices**
   - Error handling completeness
   - Logging and monitoring
   - Code organization and modularity
   - Type hints and documentation

4. **Integration with Hallucination Validation**
   - Verify method calls are real
   - Check parameter correctness
   - Validate import statements

## Output Format:
- Prioritize issues by severity (Critical, High, Medium, Low)
- Provide specific line numbers and fixes
- Include code examples for improvements
- Reference relevant documentation when available

Be thorough but constructive - focus on actionable improvements.
```

### Phase 3: Integration Scripts

#### 3.1 Validation Script Implementation
**File**: `scripts/validate_python_file.py`
```python
#!/usr/bin/env python3
"""
Hook script for validating Python files against knowledge graph.
Called by PostToolUse hook after Write/Edit operations.
"""

import json
import sys
import subprocess
import os
from pathlib import Path

def parse_hook_input():
    """Parse JSON input from Claude Code hook."""
    try:
        hook_data = json.load(sys.stdin)
        tool_input = hook_data.get('tool_input', {})
        file_path = tool_input.get('file_path', '')
        return file_path, hook_data
    except Exception as e:
        print(f"Error parsing hook input: {e}", file=stderr)
        return None, None

def is_python_file(file_path):
    """Check if file is a Python file."""
    return file_path.endswith('.py') and os.path.exists(file_path)

def call_mcp_validation(file_path):
    """Call MCP server to validate Python file."""
    try:
        # This would integrate with the MCP server
        # For now, call the hallucination detector directly
        result = subprocess.run([
            'python3', 
            'knowledge_graphs/ai_hallucination_detector.py',
            file_path
        ], capture_output=True, text=True, timeout=30)
        
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return 1, "", "Validation timeout"
    except Exception as e:
        return 1, "", f"Validation error: {e}"

def main():
    file_path, hook_data = parse_hook_input()
    
    if not file_path or not is_python_file(file_path):
        # Not a Python file, exit successfully
        sys.exit(0)
    
    # Run validation
    returncode, stdout, stderr = call_mcp_validation(file_path)
    
    if returncode != 0 or "hallucination" in stdout.lower():
        # Hallucinations detected, feed back to Claude
        validation_message = f"""
Hallucination validation detected issues in {file_path}:

{stdout}

Please use the hallucination-validator sub-agent to review and fix these issues.
"""
        print(validation_message, file=sys.stderr)
        sys.exit(2)  # Block and show error to Claude
    
    # Validation passed
    print(f"✓ Validation passed for {file_path}")
    sys.exit(0)

if __name__ == "__main__":
    main()
```

#### 3.2 Dependencies
**File**: `scripts/requirements.txt`
```
requests
json
pathlib
```

### Phase 4: Workflow Integration

#### 4.1 Complete Workflow Process
1. **File Creation/Edit**: Claude writes or edits a Python file
2. **Hook Trigger**: PostToolUse hook automatically executes
3. **Validation**: Script calls knowledge graph validation
4. **Results Processing**:
   - If clean: Continue normally
   - If hallucinations: Feed error back to Claude
5. **Sub-agent Activation**: Claude automatically uses hallucination-validator
6. **Code Review**: critical-code-reviewer agent provides comprehensive analysis
7. **Self-Correction**: Claude applies fixes and re-validates

#### 4.2 Error Handling & Feedback Loop
- Hook failures don't block development (non-critical errors)
- Validation results formatted for Claude understanding
- Sub-agents have access to full knowledge graph context
- Iterative correction until validation passes

### Phase 5: Advanced Features

#### 5.1 Context-Aware Validation
- Track imports and dependencies
- Validate against multiple repositories
- Check API compatibility across versions

#### 5.2 Performance Optimization
- Cache validation results
- Parallel processing for multiple files
- Incremental validation for large files

#### 5.3 Reporting & Analytics
- Validation success rates
- Common hallucination patterns  
- Code quality metrics over time

## Implementation Steps

### Step 1: Basic Setup
1. Create `.claude/` directory structure
2. Configure basic PostToolUse hook
3. Create simple validation script
4. Test with sample Python files

### Step 2: Sub-agent Development
1. Create hallucination-validator sub-agent
2. Create critical-code-reviewer sub-agent
3. Test agent activation and tool access
4. Refine agent prompts based on results

### Step 3: Integration Testing
1. Test complete workflow with various Python files
2. Validate hook → sub-agent → correction cycle
3. Test with files containing known hallucinations
4. Verify knowledge graph integration

### Step 4: Production Hardening
1. Add comprehensive error handling
2. Implement timeout and resource limits
3. Add logging and monitoring
4. Create documentation and troubleshooting guides

## Expected Benefits

### Immediate Value
- **Zero-hallucination Code**: Automatic detection prevents common AI mistakes
- **Real-time Feedback**: Immediate validation during development
- **Self-correcting**: Claude learns from validation feedback

### Long-term Impact
- **Higher Code Quality**: Comprehensive review catches more issues
- **Knowledge Accumulation**: Knowledge graph grows with new repositories
- **Team Productivity**: Reduces debugging time and code review cycles
- **Compliance**: Audit trail of all validations and corrections

## Technical Architecture

### Component Interaction
```
Claude Code
    ↓ (creates/edits .py file)
PostToolUse Hook
    ↓ (calls validation script)
Knowledge Graph Validator
    ↓ (if hallucinations found)
Claude Code (receives error)
    ↓ (auto-triggers)
Hallucination Validator Sub-agent
    ↓ (queries knowledge graph)
Corrected Code
    ↓ (re-validation)
Success / Code Review Agent
```

### Data Flow
1. File path → Hook → Validation script
2. Validation results → Claude (via stderr/exit codes)
3. Error context → Sub-agent → Knowledge graph query
4. Graph results → Corrections → Claude
5. Fixed code → Re-validation → Success

## Security Considerations

### Hook Security
- Validate all file paths for traversal attacks
- Sanitize input data before processing
- Use absolute paths for all scripts
- Implement timeouts for all operations

### Sub-agent Security
- Limit tool access to necessary operations only
- Validate knowledge graph queries
- Prevent sensitive file access
- Log all operations for audit

## Monitoring & Observability

### Metrics to Track
- Validation success/failure rates
- Hallucination detection accuracy
- Sub-agent activation frequency
- Code quality improvement trends

### Logging Strategy
- Hook execution logs
- Validation results and timing
- Sub-agent interactions
- Error patterns and resolution

## Future Enhancements

### Phase 6: Multi-language Support
- Extend validation to JavaScript, TypeScript
- Language-specific knowledge graphs
- Cross-language dependency validation

### Phase 7: Team Integration
- Shared knowledge graphs
- Team-wide validation policies
- Integration with CI/CD pipelines

### Phase 8: AI Improvements
- Machine learning on validation patterns
- Predictive hallucination detection
- Automated knowledge graph updates

## Conclusion

This workflow transforms Claude Code from a reactive coding assistant into a proactive, self-validating development environment. By combining the deterministic accuracy of knowledge graphs with the flexibility of hooks and sub-agents, we create a system that prevents hallucinations before they become problems while maintaining the natural flow of AI-assisted development.

The implementation provides immediate value through automated validation while building a foundation for more sophisticated AI development workflows in the future.