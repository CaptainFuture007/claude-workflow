"""
Multi-Input Type Detection and Processing Models

This module provides input type detection and data models for the Multi-Input Document Processor.
Supports URLs, PDF files, and markdown files with automatic type detection.
"""

from enum import Enum
from urllib.parse import urlparse
from pathlib import Path
from typing import Optional, Union, Tuple, List, Dict, Any
from dataclasses import dataclass
from datetime import datetime
import re
import os
import logging

logger = logging.getLogger(__name__)


class InputType(Enum):
    """Enumeration of supported input types."""
    URL = "url"
    PDF = "pdf"
    MARKDOWN = "markdown"


@dataclass
class ProcessingResult:
    """
    Result from processing any input type.
    
    Provides unified structure for results from URL crawling, PDF processing,
    and markdown file reading.
    """
    success: bool
    position: int
    input_type: InputType
    source: str
    content: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    error_message: Optional[str] = None
    processing_time: float = 0.0
    
    @property
    def source_indicator(self) -> str:
        """Generate source type indicator for TOC."""
        indicators = {
            InputType.URL: "🌐",
            InputType.PDF: "📄", 
            InputType.MARKDOWN: "📝"
        }
        return indicators[self.input_type]
    
    @property
    def type_description(self) -> str:
        """Get human-readable type description."""
        descriptions = {
            InputType.URL: "Web Page",
            InputType.PDF: "PDF Document",
            InputType.MARKDOWN: "Markdown File"
        }
        return descriptions[self.input_type]


@dataclass
class EnhancedMetadata:
    """
    Extended metadata for all input types.
    
    Provides comprehensive metadata that works across different input sources
    while maintaining type-specific information.
    """
    source: str
    input_type: str
    position: int
    processed_at: str
    title: str
    description: str
    
    # Type-specific fields
    url: Optional[str] = None          # For URLs
    file_path: Optional[str] = None    # For files
    pdf_pages: Optional[int] = None    # For PDFs
    file_size: Optional[int] = None    # For files
    
    # Processing details
    processing_time: float = 0.0
    success: bool = True
    error_message: Optional[str] = None


def detect_input_type(input_str: str) -> InputType:
    """
    Detect input type based on string content.
    
    Uses pattern matching to determine if input is a URL, PDF file, or markdown file.
    Supports both local file paths and URLs pointing to PDFs.
    
    Args:
        input_str: Input string to analyze
        
    Returns:
        InputType enum value
        
    Examples:
        >>> detect_input_type("https://example.com/page")
        InputType.URL
        >>> detect_input_type("https://example.com/document.pdf")
        InputType.PDF
        >>> detect_input_type("./document.pdf")
        InputType.PDF
        >>> detect_input_type("./notes.md")
        InputType.MARKDOWN
    """
    input_str = input_str.strip()
    
    # URL pattern detection
    if input_str.startswith(('http://', 'https://')):
        # Check if URL points to a PDF
        if input_str.lower().endswith('.pdf'):
            return InputType.PDF
        # Check for PDF in URL path (common pattern)
        if '/pdf/' in input_str.lower() or '.pdf' in input_str.lower():
            return InputType.PDF
        return InputType.URL
    
    # File path detection
    try:
        path = Path(input_str)
        suffix = path.suffix.lower()
        
        if suffix == '.pdf':
            return InputType.PDF
        elif suffix in ['.md', '.markdown']:
            return InputType.MARKDOWN
        elif suffix in ['.txt'] and 'readme' in path.name.lower():
            # Treat README.txt files as markdown
            return InputType.MARKDOWN
    except (ValueError, OSError):
        # Invalid path, treat as URL
        pass
    
    # Default fallback - treat as URL
    logger.warning(f"Could not definitively detect type for '{input_str}', defaulting to URL")
    return InputType.URL


def validate_input_tuple(input_tuple: Tuple[str, ...]) -> List[Tuple[int, str, InputType]]:
    """
    Validate and analyze input tuple for processing.
    
    Args:
        input_tuple: Tuple of input strings
        
    Returns:
        List of (position, input_str, input_type) tuples
        
    Raises:
        ValueError: If input tuple is empty or contains invalid entries
    """
    if not input_tuple:
        raise ValueError("Input tuple cannot be empty")
    
    if len(input_tuple) > 100:  # Reasonable limit
        raise ValueError("Input tuple too large (max 100 items)")
    
    validated_inputs = []
    
    for position, input_str in enumerate(input_tuple):
        if not isinstance(input_str, str):
            raise ValueError(f"Input at position {position} must be a string, got {type(input_str)}")
        
        input_str = input_str.strip()
        if not input_str:
            raise ValueError(f"Input at position {position} cannot be empty")
        
        input_type = detect_input_type(input_str)
        validated_inputs.append((position, input_str, input_type))
    
    return validated_inputs


def validate_file_input(file_path: str, input_type: InputType) -> bool:
    """
    Validate file-based input exists and is accessible.
    
    Args:
        file_path: Path to the file
        input_type: Expected input type
        
    Returns:
        True if file is valid and accessible
        
    Raises:
        FileNotFoundError: If file doesn't exist
        PermissionError: If file is not readable
        ValueError: If file type doesn't match expected type
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if not path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")
    
    if not os.access(path, os.R_OK):
        raise PermissionError(f"File is not readable: {file_path}")
    
    # Validate file extension matches expected type
    detected_type = detect_input_type(file_path)
    if detected_type != input_type:
        logger.warning(f"File type mismatch: expected {input_type.value}, detected {detected_type.value}")
    
    return True


def create_processing_metadata(
    source: str,
    input_type: InputType,
    position: int,
    title: str = "Untitled",
    description: str = "No description available",
    processing_time: float = 0.0,
    success: bool = True,
    error_message: Optional[str] = None,
    **kwargs
) -> EnhancedMetadata:
    """
    Create enhanced metadata for processed input.
    
    Args:
        source: Source identifier (URL or file path)
        input_type: Type of input processed
        position: Position in input tuple
        title: Document title
        description: Document description
        processing_time: Time taken to process
        success: Whether processing succeeded
        error_message: Error message if processing failed
        **kwargs: Additional type-specific metadata
        
    Returns:
        EnhancedMetadata instance
    """
    metadata = EnhancedMetadata(
        source=source,
        input_type=input_type.value,
        position=position,
        processed_at=datetime.now().isoformat(),
        title=title,
        description=description,
        processing_time=processing_time,
        success=success,
        error_message=error_message
    )
    
    # Add type-specific fields
    if input_type == InputType.URL:
        metadata.url = source
    elif input_type in [InputType.PDF, InputType.MARKDOWN]:
        metadata.file_path = source
        
        # Add file size if available
        try:
            path = Path(source)
            metadata.file_size = path.stat().st_size
        except (OSError, ValueError):
            pass
    
    # Add any additional type-specific metadata
    for key, value in kwargs.items():
        if hasattr(metadata, key):
            setattr(metadata, key, value)
    
    return metadata


# For backward compatibility
def is_url(input_str: str) -> bool:
    """Check if input string is a URL."""
    return detect_input_type(input_str) == InputType.URL


def is_pdf(input_str: str) -> bool:
    """Check if input string is a PDF file or URL."""
    return detect_input_type(input_str) == InputType.PDF


def is_markdown(input_str: str) -> bool:
    """Check if input string is a markdown file."""
    return detect_input_type(input_str) == InputType.MARKDOWN


if __name__ == "__main__":
    # Test input detection
    test_inputs = [
        "https://docs.anthropic.com/en/docs/claude-code/",
        "https://arxiv.org/pdf/2408.09869.pdf",
        "./document.pdf",
        "./notes.md",
        "./README.txt",
        "invalid input"
    ]
    
    print("Testing input type detection:")
    for test_input in test_inputs:
        input_type = detect_input_type(test_input)
        print(f"'{test_input}' -> {input_type.value}")