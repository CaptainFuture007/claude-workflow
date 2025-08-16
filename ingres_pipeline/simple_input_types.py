"""
Simplified Input Type Detection

A streamlined approach to detecting URL, PDF, and Markdown inputs
following KISS principles while maintaining essential functionality.
"""

from pathlib import Path
from urllib.parse import urlparse
from typing import Literal, Tuple, List

InputType = Literal["url", "pdf", "markdown"]


def detect_input_type(input_str: str) -> InputType:
    """
    Detect input type from string.
    
    Args:
        input_str: Input string to analyze
        
    Returns:
        Input type: "url", "pdf", or "markdown"
        
    Examples:
        >>> detect_input_type("https://example.com")
        'url'
        >>> detect_input_type("./document.pdf")
        'pdf'
        >>> detect_input_type("./notes.md")
        'markdown'
    """
    input_str = input_str.strip()
    
    # URL detection
    if input_str.startswith(('http://', 'https://')):
        if input_str.lower().endswith('.pdf'):
            return "pdf"
        return "url"
    
    # File path detection
    try:
        path = Path(input_str)
        suffix = path.suffix.lower()
        
        if suffix == '.pdf':
            return "pdf"
        elif suffix in ['.md', '.markdown']:
            return "markdown"
        elif suffix == '.txt' and 'readme' in path.name.lower():
            return "markdown"  # Treat README.txt as markdown
    except (ValueError, OSError):
        pass
    
    # Default fallback - treat as URL
    return "url"


def validate_inputs(inputs: Tuple[str, ...]) -> List[Tuple[int, str, InputType]]:
    """
    Validate and analyze input tuple.
    
    Args:
        inputs: Tuple of input strings
        
    Returns:
        List of (position, input_str, input_type) tuples
        
    Raises:
        ValueError: If inputs are invalid
    """
    if not inputs:
        raise ValueError("Input tuple cannot be empty")
    
    if len(inputs) > 50:  # Reasonable limit for first prototype
        raise ValueError("Too many inputs (max 50)")
    
    validated = []
    for position, input_str in enumerate(inputs):
        if not isinstance(input_str, str) or not input_str.strip():
            raise ValueError(f"Input at position {position} must be a non-empty string")
        
        input_type = detect_input_type(input_str)
        validated.append((position, input_str.strip(), input_type))
    
    return validated


def validate_file_exists(file_path: str) -> bool:
    """
    Check if file exists and is readable.
    
    Args:
        file_path: Path to file
        
    Returns:
        True if file exists and is readable
        
    Raises:
        FileNotFoundError: If file doesn't exist
        PermissionError: If file is not readable
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if not path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")
    
    if not path.stat().st_size > 0:
        raise ValueError(f"File is empty: {file_path}")
    
    return True


# Convenience functions for backward compatibility
def is_url(input_str: str) -> bool:
    """Check if input is a URL."""
    return detect_input_type(input_str) == "url"


def is_pdf(input_str: str) -> bool:
    """Check if input is a PDF."""
    return detect_input_type(input_str) == "pdf"


def is_markdown(input_str: str) -> bool:
    """Check if input is a markdown file."""
    return detect_input_type(input_str) == "markdown"


if __name__ == "__main__":
    # Quick test
    test_inputs = [
        "https://docs.anthropic.com/en/docs/claude-code/",
        "https://arxiv.org/pdf/2408.09869.pdf",
        "./document.pdf",
        "./notes.md",
        "./README.txt"
    ]
    
    print("Testing input type detection:")
    for test_input in test_inputs:
        input_type = detect_input_type(test_input)
        print(f"'{test_input}' -> {input_type}")