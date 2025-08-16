#!/usr/bin/env python3
"""
Test file to verify the hallucination detection hook works correctly.
This file intentionally contains some hallucinated method calls to trigger the hook.
"""

import os
import sys
# This is a real import - should pass validation

def test_function():
    """A simple test function with some intentional hallucinations."""
    
    # This should be fine - real method
    print("Testing hallucination detection")
    
    # These are intentional hallucinations that should be caught:
    # result = os.non_existent_method()  # Uncomment to test hallucination detection
    # data = sys.fake_attribute          # Uncomment to test hallucination detection
    
    return "Hook test completed"

if __name__ == "__main__":
    result = test_function()
    print(result)