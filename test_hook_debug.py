#!/usr/bin/env python3
"""
Debug version of the hook to see what's happening.
"""

import json
import sys
import os

def main():
    # Read input
    try:
        hook_data = json.load(sys.stdin)
        print(f"DEBUG: Parsed hook data: {hook_data}", file=sys.stderr)
        
        tool_input = hook_data.get('tool_input', {})
        file_path = tool_input.get('file_path', '')
        print(f"DEBUG: File path: {file_path}", file=sys.stderr)
        
        if not file_path:
            print("DEBUG: No file path, exiting 0", file=sys.stderr)
            sys.exit(0)
            
        if not file_path.endswith('.py'):
            print(f"DEBUG: Not a Python file: {file_path}, exiting 0", file=sys.stderr)
            sys.exit(0)
            
        if not os.path.exists(file_path):
            print(f"DEBUG: File doesn't exist: {file_path}, exiting 0", file=sys.stderr)
            sys.exit(0)
            
        print(f"DEBUG: Processing Python file: {file_path}", file=sys.stderr)
        
        # Read file
        with open(file_path, 'r') as f:
            content = f.read()
            
        print(f"DEBUG: File content length: {len(content)}", file=sys.stderr)
        
        # Check patterns
        patterns = ["non_existent_module", "non_existent_method", "fake_attribute", "fake_function"]
        found_issues = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            for pattern in patterns:
                if pattern in line:
                    issue = f"Line {i}: Potential hallucination detected - {pattern}"
                    found_issues.append(issue)
                    print(f"DEBUG: Found issue: {issue}", file=sys.stderr)
                    
        if found_issues:
            print(f"DEBUG: Total issues: {len(found_issues)}, exiting 2", file=sys.stderr)
            error_msg = f"Hallucination detected in {file_path}:\n" + "\n".join(found_issues)
            print(error_msg, file=sys.stderr)
            sys.exit(2)
        else:
            print("DEBUG: No issues found, exiting 0", file=sys.stderr)
            sys.exit(0)
            
    except Exception as e:
        print(f"DEBUG: Exception: {e}", file=sys.stderr)
        sys.exit(0)

if __name__ == "__main__":
    main()