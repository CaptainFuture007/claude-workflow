#!/usr/bin/env python3
"""
Test file with intentional hallucinations to verify detection works.
"""

import os
from non_existent_module import fake_function

def test_hallucinations():
    """Function with intentional hallucinations."""
    
    # This should trigger hallucination detection
    result = os.non_existent_method()
    data = os.fake_attribute
    
    # Another hallucination
    fake_function()
    
    return result

if __name__ == "__main__":
    test_hallucinations()