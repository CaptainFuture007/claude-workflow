#!/usr/bin/env python3
import json
import sys
import os

# Test the hook functionality directly
def test_hook():
    # Simulate hook input
    hook_input = {
        "tool_input": {"file_path": "test_with_hallucinations.py"},
        "hook_event_name": "PostToolUse", 
        "tool_name": "Write"
    }
    
    print(f"Testing with file: {hook_input['tool_input']['file_path']}")
    
    file_path = hook_input['tool_input']['file_path']
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"File does not exist: {file_path}")
        return
        
    # Check if it's a Python file
    if not file_path.endswith('.py'):
        print(f"Not a Python file: {file_path}")
        return
        
    print(f"File exists and is Python: {file_path}")
    
    # Read file content
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"File content length: {len(content)}")
        print("First 200 chars:", repr(content[:200]))
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    # Check patterns
    patterns = ["non_existent_module", "non_existent_method", "fake_attribute", "fake_function"]
    found_issues = []
    lines = content.split('\n')
    
    for i, line in enumerate(lines, 1):
        for pattern in patterns:
            if pattern in line:
                issue = f"Line {i}: Potential hallucination detected - {pattern}"
                found_issues.append(issue)
                print(f"FOUND: {issue}")
                
    if found_issues:
        print(f"Total issues found: {len(found_issues)}")
        print("Issues:", found_issues)
        return 1
    else:
        print("No issues found")
        return 0

if __name__ == "__main__":
    exit_code = test_hook()
    print(f"Exit code: {exit_code}")
    sys.exit(exit_code or 0)