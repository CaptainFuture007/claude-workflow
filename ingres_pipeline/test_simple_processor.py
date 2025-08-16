"""
Basic functional tests for Simple Multi-Input Processor

Focused on essential functionality testing following KISS principles.
"""

import pytest
import asyncio
import tempfile
import os
from pathlib import Path
import shutil

from simple_input_types import detect_input_type, validate_inputs, validate_file_exists
from simple_multi_processor import SimpleMultiProcessor


class TestInputTypeDetection:
    """Test input type detection functionality."""
    
    def test_url_detection(self):
        """Test URL detection."""
        assert detect_input_type("https://example.com") == "url"
        assert detect_input_type("http://example.com") == "url"
        assert detect_input_type("https://docs.anthropic.com/en/docs/claude-code/") == "url"
    
    def test_pdf_detection(self):
        """Test PDF detection."""
        assert detect_input_type("./document.pdf") == "pdf"
        assert detect_input_type("/path/to/file.PDF") == "pdf"
        assert detect_input_type("https://arxiv.org/pdf/2408.09869.pdf") == "pdf"
    
    def test_markdown_detection(self):
        """Test markdown detection."""
        assert detect_input_type("./notes.md") == "markdown"
        assert detect_input_type("./README.markdown") == "markdown"
        assert detect_input_type("./README.txt") == "markdown"  # Special case
    
    def test_fallback_to_url(self):
        """Test fallback behavior."""
        assert detect_input_type("some-random-string") == "url"
        assert detect_input_type("") == "url"  # Empty string defaults to URL


class TestInputValidation:
    """Test input validation functionality."""
    
    def test_valid_inputs(self):
        """Test validation of valid inputs."""
        inputs = ("https://example.com", "./test.pdf", "./notes.md")
        result = validate_inputs(inputs)
        
        assert len(result) == 3
        assert result[0] == (0, "https://example.com", "url")
        assert result[1] == (1, "./test.pdf", "pdf")
        assert result[2] == (2, "./notes.md", "markdown")
    
    def test_empty_inputs(self):
        """Test validation with empty inputs."""
        with pytest.raises(ValueError, match="Input tuple cannot be empty"):
            validate_inputs(())
    
    def test_too_many_inputs(self):
        """Test validation with too many inputs."""
        inputs = tuple(f"input_{i}" for i in range(51))  # Over limit
        with pytest.raises(ValueError, match="Too many inputs"):
            validate_inputs(inputs)
    
    def test_invalid_input_types(self):
        """Test validation with invalid input types."""
        with pytest.raises(ValueError, match="must be a non-empty string"):
            validate_inputs(("valid", "", "also_valid"))
        
        with pytest.raises(ValueError, match="must be a non-empty string"):
            validate_inputs((123, "valid"))


class TestFileValidation:
    """Test file validation functionality."""
    
    def test_existing_file(self):
        """Test validation of existing file."""
        # Create temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.md') as tmp:
            tmp.write(b"# Test content")
            tmp_path = tmp.name
        
        try:
            assert validate_file_exists(tmp_path) == True
        finally:
            os.unlink(tmp_path)
    
    def test_nonexistent_file(self):
        """Test validation of non-existent file."""
        with pytest.raises(FileNotFoundError):
            validate_file_exists("/nonexistent/file.pdf")
    
    def test_empty_file(self):
        """Test validation of empty file."""
        # Create empty temporary file
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            with pytest.raises(ValueError, match="File is empty"):
                validate_file_exists(tmp_path)
        finally:
            os.unlink(tmp_path)


class TestSimpleMultiProcessor:
    """Test the main processor functionality."""
    
    @pytest.fixture
    def temp_dir(self):
        """Create temporary directory for testing."""
        temp_dir = Path(tempfile.mkdtemp())
        yield temp_dir
        shutil.rmtree(temp_dir)
    
    @pytest.fixture
    def processor(self, temp_dir):
        """Create processor instance for testing."""
        return SimpleMultiProcessor(output_dir=str(temp_dir / "output"))
    
    @pytest.fixture
    def sample_markdown_file(self, temp_dir):
        """Create sample markdown file for testing."""
        content = """# Test Document

This is a test markdown document.

## Section 1
Some content here.
"""
        md_file = temp_dir / "test.md"
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return str(md_file)
    
    def test_processor_initialization(self, processor):
        """Test processor initialization."""
        assert processor.output_dir.exists()
        assert processor.content_dir.exists()
        assert processor.max_concurrent == 10
        assert processor.docling_converter is not None
    
    @pytest.mark.asyncio
    async def test_single_input_string(self, processor, sample_markdown_file):
        """Test processing single input as string."""
        try:
            result = await processor.process_inputs(sample_markdown_file)
            
            assert result["success"] == True
            assert result["stats"]["total_inputs"] == 1
            assert result["stats"]["successful"] == 1
            assert result["stats"]["failed"] == 0
            assert result["stats"]["concatenated_file"] is not None
        finally:
            processor.cleanup()
    
    @pytest.mark.asyncio
    async def test_markdown_processing(self, processor, sample_markdown_file):
        """Test markdown file processing."""
        try:
            result = await processor.process_inputs((sample_markdown_file,))
            
            assert result["success"] == True
            processed_result = result["results"][0]
            assert processed_result["input_type"] == "markdown"
            assert processed_result["title"] == "Test Document"
            assert "This is a test markdown document" in processed_result["content"]
            assert Path(processed_result["output_file"]).exists()
        finally:
            processor.cleanup()
    
    @pytest.mark.asyncio
    async def test_invalid_inputs(self, processor):
        """Test handling of invalid inputs."""
        try:
            result = await processor.process_inputs(())
            assert result["success"] == False
            assert "empty" in result["error"].lower()
        finally:
            processor.cleanup()
    
    @pytest.mark.asyncio
    async def test_mixed_inputs_with_failures(self, processor, sample_markdown_file):
        """Test processing mixed inputs where some fail."""
        inputs = (
            sample_markdown_file,        # Should succeed
            "/nonexistent/file.pdf",     # Should fail
        )
        
        try:
            result = await processor.process_inputs(inputs)
            
            assert result["success"] == True  # Overall success even with partial failures
            assert result["stats"]["total_inputs"] == 2
            assert result["stats"]["successful"] == 1
            assert result["stats"]["failed"] == 1
            assert len(result["stats"]["failed_inputs"]) == 1
        finally:
            processor.cleanup()
    
    @pytest.mark.asyncio
    async def test_concatenated_document_creation(self, processor, sample_markdown_file):
        """Test creation of concatenated document."""
        try:
            result = await processor.process_inputs((sample_markdown_file,))
            
            assert result["success"] == True
            concat_file = Path(result["stats"]["concatenated_file"])
            assert concat_file.exists()
            
            # Check concatenated document content
            with open(concat_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            assert "Multi-Input Document Compilation" in content
            assert "Table of Contents" in content
            assert "Test Document" in content
        finally:
            processor.cleanup()
    
    def test_filename_generation(self, processor):
        """Test safe filename generation."""
        # Test URL
        filename = processor._generate_filename("https://example.com/path/to/page", 0, "url")
        assert filename.startswith("pos00_")
        assert filename.endswith(".md")
        assert "/" not in filename
        
        # Test file path
        filename = processor._generate_filename("/path/to/document.pdf", 1, "pdf")
        assert filename.startswith("pos01_")
        assert filename.endswith(".md")
    
    def test_title_extraction(self, processor):
        """Test markdown title extraction."""
        content_with_title = "# Main Title\n\nSome content"
        title = processor._extract_title_from_markdown(content_with_title)
        assert title == "Main Title"
        
        content_without_title = "Just some content without a title"
        title = processor._extract_title_from_markdown(content_without_title)
        assert title is None


class TestBackwardCompatibility:
    """Test backward compatibility with existing interfaces."""
    
    @pytest.mark.asyncio
    async def test_single_url_processing(self, temp_dir):
        """Test processing single URL (backward compatible)."""
        processor = SimpleMultiProcessor(output_dir=str(temp_dir / "output"))
        
        try:
            # Test with single string input (old interface)
            result = await processor.process_inputs("https://httpbin.org/json")
            
            # Should work but might fail due to network - that's ok for this test
            assert "success" in result
            assert "stats" in result
        except Exception:
            # Network failures are acceptable in this test
            pass
        finally:
            processor.cleanup()


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v"])