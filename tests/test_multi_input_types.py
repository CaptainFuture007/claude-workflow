"""
Tests for multi_input_types module

Tests input type detection, validation, and metadata creation functionality.
"""

import pytest
import tempfile
import os
from pathlib import Path
from datetime import datetime

from multi_input_types import (
    InputType, ProcessingResult, EnhancedMetadata,
    detect_input_type, validate_input_tuple, validate_file_input,
    create_processing_metadata, is_url, is_pdf, is_markdown
)


class TestInputTypeDetection:
    """Test input type detection functionality."""
    
    def test_detect_url_http(self):
        """Test URL detection for HTTP URLs."""
        assert detect_input_type("http://example.com") == InputType.URL
        assert detect_input_type("https://docs.anthropic.com/") == InputType.URL
        
    def test_detect_url_with_path(self):
        """Test URL detection with paths."""
        assert detect_input_type("https://docs.anthropic.com/en/docs/claude-code/") == InputType.URL
        
    def test_detect_pdf_url(self):
        """Test PDF URL detection."""
        assert detect_input_type("https://arxiv.org/pdf/2408.09869.pdf") == InputType.PDF
        assert detect_input_type("http://example.com/document.pdf") == InputType.PDF
        
    def test_detect_pdf_file(self):
        """Test local PDF file detection."""
        assert detect_input_type("./document.pdf") == InputType.PDF
        assert detect_input_type("/path/to/file.pdf") == InputType.PDF
        assert detect_input_type("Document.PDF") == InputType.PDF  # Case insensitive
        
    def test_detect_markdown_file(self):
        """Test markdown file detection."""
        assert detect_input_type("./notes.md") == InputType.MARKDOWN
        assert detect_input_type("/path/to/file.markdown") == InputType.MARKDOWN
        assert detect_input_type("README.MD") == InputType.MARKDOWN  # Case insensitive
        
    def test_detect_fallback_to_url(self):
        """Test fallback to URL for ambiguous inputs."""
        assert detect_input_type("example.com") == InputType.URL
        assert detect_input_type("some random text") == InputType.URL
        
    def test_backward_compatibility_functions(self):
        """Test backward compatibility helper functions."""
        assert is_url("https://example.com") == True
        assert is_url("./file.pdf") == False
        
        assert is_pdf("./document.pdf") == True
        assert is_pdf("https://example.com/doc.pdf") == True
        assert is_pdf("https://example.com") == False
        
        assert is_markdown("./notes.md") == True
        assert is_markdown("./document.pdf") == False


class TestInputValidation:
    """Test input validation functionality."""
    
    def test_validate_input_tuple_success(self):
        """Test successful input tuple validation."""
        inputs = ("https://example.com", "./test.pdf", "./notes.md")
        result = validate_input_tuple(inputs)
        
        assert len(result) == 3
        assert result[0] == (0, "https://example.com", InputType.URL)
        assert result[1] == (1, "./test.pdf", InputType.PDF)
        assert result[2] == (2, "./notes.md", InputType.MARKDOWN)
        
    def test_validate_empty_tuple(self):
        """Test validation with empty tuple."""
        with pytest.raises(ValueError, match="Input tuple cannot be empty"):
            validate_input_tuple(())
            
    def test_validate_too_many_inputs(self):
        """Test validation with too many inputs."""
        inputs = tuple(f"input_{i}" for i in range(101))
        with pytest.raises(ValueError, match="Input tuple too large"):
            validate_input_tuple(inputs)
            
    def test_validate_non_string_input(self):
        """Test validation with non-string input."""
        with pytest.raises(ValueError, match="must be a string"):
            validate_input_tuple(("valid_string", 123, "another_string"))
            
    def test_validate_empty_string_input(self):
        """Test validation with empty string."""
        with pytest.raises(ValueError, match="cannot be empty"):
            validate_input_tuple(("valid_string", "", "another_string"))
            
    def test_validate_whitespace_input(self):
        """Test validation with whitespace-only string."""
        with pytest.raises(ValueError, match="cannot be empty"):
            validate_input_tuple(("valid_string", "   ", "another_string"))


class TestFileValidation:
    """Test file validation functionality."""
    
    def test_validate_existing_file(self):
        """Test validation of existing file."""
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            tmp.write(b"test content")
            tmp_path = tmp.name
            
        try:
            assert validate_file_input(tmp_path, InputType.PDF) == True
        finally:
            os.unlink(tmp_path)
            
    def test_validate_nonexistent_file(self):
        """Test validation of non-existent file."""
        with pytest.raises(FileNotFoundError):
            validate_file_input("/nonexistent/file.pdf", InputType.PDF)
            
    def test_validate_directory_as_file(self):
        """Test validation when path is a directory."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            with pytest.raises(ValueError, match="Path is not a file"):
                validate_file_input(tmp_dir, InputType.PDF)


class TestProcessingResult:
    """Test ProcessingResult dataclass."""
    
    def test_processing_result_creation(self):
        """Test creating ProcessingResult."""
        result = ProcessingResult(
            success=True,
            position=0,
            input_type=InputType.URL,
            source="https://example.com",
            content="# Test Content",
            processing_time=1.5
        )
        
        assert result.success == True
        assert result.position == 0
        assert result.input_type == InputType.URL
        assert result.source == "https://example.com"
        assert result.content == "# Test Content"
        assert result.processing_time == 1.5
        
    def test_source_indicator_property(self):
        """Test source indicator property."""
        url_result = ProcessingResult(True, 0, InputType.URL, "test", None)
        pdf_result = ProcessingResult(True, 0, InputType.PDF, "test", None)
        md_result = ProcessingResult(True, 0, InputType.MARKDOWN, "test", None)
        
        assert url_result.source_indicator == "🌐"
        assert pdf_result.source_indicator == "📄"
        assert md_result.source_indicator == "📝"
        
    def test_type_description_property(self):
        """Test type description property."""
        url_result = ProcessingResult(True, 0, InputType.URL, "test", None)
        pdf_result = ProcessingResult(True, 0, InputType.PDF, "test", None)
        md_result = ProcessingResult(True, 0, InputType.MARKDOWN, "test", None)
        
        assert url_result.type_description == "Web Page"
        assert pdf_result.type_description == "PDF Document"
        assert md_result.type_description == "Markdown File"


class TestEnhancedMetadata:
    """Test EnhancedMetadata dataclass."""
    
    def test_enhanced_metadata_creation(self):
        """Test creating EnhancedMetadata."""
        metadata = EnhancedMetadata(
            source="https://example.com",
            input_type="url",
            position=0,
            processed_at="2025-08-16T12:00:00",
            title="Test Page",
            description="Test description"
        )
        
        assert metadata.source == "https://example.com"
        assert metadata.input_type == "url"
        assert metadata.position == 0
        assert metadata.title == "Test Page"
        assert metadata.description == "Test description"


class TestMetadataCreation:
    """Test metadata creation functionality."""
    
    def test_create_url_metadata(self):
        """Test creating metadata for URL input."""
        metadata = create_processing_metadata(
            source="https://example.com",
            input_type=InputType.URL,
            position=0,
            title="Test Page",
            description="Test description",
            processing_time=1.5,
            success=True
        )
        
        assert metadata.source == "https://example.com"
        assert metadata.input_type == "url"
        assert metadata.url == "https://example.com"
        assert metadata.file_path is None
        assert metadata.processing_time == 1.5
        assert metadata.success == True
        
    def test_create_pdf_metadata(self):
        """Test creating metadata for PDF input."""
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            tmp.write(b"test content")
            tmp_path = tmp.name
            
        try:
            metadata = create_processing_metadata(
                source=tmp_path,
                input_type=InputType.PDF,
                position=1,
                title="Test PDF",
                pdf_pages=10
            )
            
            assert metadata.input_type == "pdf"
            assert metadata.file_path == tmp_path
            assert metadata.url is None
            assert metadata.file_size is not None
            assert metadata.pdf_pages == 10
        finally:
            os.unlink(tmp_path)
            
    def test_create_markdown_metadata(self):
        """Test creating metadata for markdown input."""
        with tempfile.NamedTemporaryFile(suffix='.md', delete=False) as tmp:
            tmp.write(b"# Test Markdown")
            tmp_path = tmp.name
            
        try:
            metadata = create_processing_metadata(
                source=tmp_path,
                input_type=InputType.MARKDOWN,
                position=2,
                title="Test Markdown"
            )
            
            assert metadata.input_type == "markdown"
            assert metadata.file_path == tmp_path
            assert metadata.url is None
            assert metadata.file_size is not None
        finally:
            os.unlink(tmp_path)
            
    def test_create_metadata_with_error(self):
        """Test creating metadata for failed processing."""
        metadata = create_processing_metadata(
            source="invalid_file.pdf",
            input_type=InputType.PDF,
            position=0,
            success=False,
            error_message="File not found"
        )
        
        assert metadata.success == False
        assert metadata.error_message == "File not found"


class TestEdgeCases:
    """Test edge cases and error conditions."""
    
    def test_whitespace_handling(self):
        """Test handling of whitespace in inputs."""
        # Should strip whitespace
        inputs = ("  https://example.com  ", "\t./test.pdf\n")
        result = validate_input_tuple(inputs)
        
        assert result[0][1] == "https://example.com"
        assert result[1][1] == "./test.pdf"
        
    def test_case_insensitive_extensions(self):
        """Test case-insensitive file extension detection."""
        assert detect_input_type("file.PDF") == InputType.PDF
        assert detect_input_type("file.Md") == InputType.MARKDOWN
        assert detect_input_type("file.MARKDOWN") == InputType.MARKDOWN
        
    def test_complex_paths(self):
        """Test complex file paths."""
        assert detect_input_type("/home/user/documents/research.pdf") == InputType.PDF
        assert detect_input_type("../relative/path/notes.md") == InputType.MARKDOWN
        assert detect_input_type("./folder with spaces/file.pdf") == InputType.PDF


if __name__ == "__main__":
    pytest.main([__file__])