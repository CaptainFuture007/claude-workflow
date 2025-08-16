"""
Tests for multi_input_processor module

Tests the main MultiInputProcessor class and its components.
"""

import pytest
import asyncio
import tempfile
import os
from pathlib import Path
from unittest.mock import Mock, patch, AsyncMock

from multi_input_processor import (
    MultiInputProcessor, MarkdownProcessor, PDFProcessor,
    create_multi_input_processor
)
from multi_input_types import InputType, ProcessingResult


class TestMarkdownProcessor:
    """Test MarkdownProcessor functionality."""
    
    @pytest.fixture
    def processor(self):
        """Create MarkdownProcessor instance."""
        return MarkdownProcessor()
    
    @pytest.fixture
    def sample_markdown_file(self):
        """Create a sample markdown file for testing."""
        content = """# Test Document

This is a test markdown document with some content.

## Section 1

Some content here.

## Section 2

More content here.
"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write(content)
            f.flush()
            yield f.name
        os.unlink(f.name)
    
    @pytest.mark.asyncio
    async def test_process_markdown_success(self, processor, sample_markdown_file):
        """Test successful markdown processing."""
        result = await processor.process_markdown(sample_markdown_file, 0)
        
        assert result.success == True
        assert result.position == 0
        assert result.input_type == InputType.MARKDOWN
        assert result.source == sample_markdown_file
        assert result.content is not None
        assert "# Test Document" in result.content
        assert result.metadata is not None
        assert result.metadata['title'] == "Test Document"
        assert result.processing_time > 0
        
    @pytest.mark.asyncio
    async def test_process_nonexistent_file(self, processor):
        """Test processing non-existent markdown file."""
        result = await processor.process_markdown("/nonexistent/file.md", 0)
        
        assert result.success == False
        assert result.error_message is not None
        assert "Failed to process markdown file" in result.error_message
        
    def test_extract_title_from_content(self, processor):
        """Test title extraction from markdown content."""
        content = "# Main Title\n\nSome content"
        title = processor._extract_title_from_content(content)
        assert title == "Main Title"
        
        # Test with no title
        content = "Just some content without a title"
        title = processor._extract_title_from_content(content)
        assert title == "Untitled Markdown Document"
        
    def test_extract_description_from_content(self, processor):
        """Test description extraction from markdown content."""
        content = "# Title\n\nThis is a description paragraph."
        description = processor._extract_description_from_content(content)
        assert description == "This is a description paragraph."
        
        # Test with short content
        content = "# Title\n\nShort"
        description = processor._extract_description_from_content(content)
        assert description == "No description available"


class TestPDFProcessor:
    """Test PDFProcessor functionality."""
    
    @pytest.fixture
    def processor(self):
        """Create PDFProcessor instance."""
        with tempfile.TemporaryDirectory() as temp_dir:
            yield PDFProcessor(temp_dir)
    
    @pytest.mark.asyncio
    async def test_pdf_processor_initialization(self):
        """Test PDF processor initialization."""
        with tempfile.TemporaryDirectory() as temp_dir:
            processor = PDFProcessor(temp_dir)
            assert processor.output_dir.exists()
            assert processor.temp_dir.exists()
    
    @pytest.mark.asyncio
    @patch('multi_input_processor.UnifiedPDFProcessor')
    async def test_process_pdf_success(self, mock_unified_processor, processor):
        """Test successful PDF processing."""
        # Mock the unified processor
        mock_instance = Mock()
        mock_unified_processor.return_value = mock_instance
        
        # Mock successful processing
        mock_instance.process_single_pdf.return_value = (True, {
            'success': True,
            'markdown_path': str(processor.temp_dir / 'test.md'),
            'base_name': 'test',
            'pages': 5,
            'error_message': None
        })
        
        # Create mock markdown file
        markdown_path = processor.temp_dir / 'test.md'
        with open(markdown_path, 'w') as f:
            f.write("# Test PDF Content\n\nConverted from PDF.")
        
        result = await processor.process_pdf("test.pdf", 0)
        
        assert result.success == True
        assert result.position == 0
        assert result.input_type == InputType.PDF
        assert result.source == "test.pdf"
        assert result.content is not None
        assert "Test PDF Content" in result.content
        
    @pytest.mark.asyncio
    @patch('multi_input_processor.UnifiedPDFProcessor')
    async def test_process_pdf_failure(self, mock_unified_processor, processor):
        """Test PDF processing failure."""
        # Mock the unified processor
        mock_instance = Mock()
        mock_unified_processor.return_value = mock_instance
        
        # Mock failed processing
        mock_instance.process_single_pdf.return_value = (False, {
            'success': False,
            'error_message': 'Invalid PDF format'
        })
        
        result = await processor.process_pdf("invalid.pdf", 0)
        
        assert result.success == False
        assert result.error_message is not None
        assert "Failed to process PDF" in result.error_message


class TestMultiInputProcessor:
    """Test MultiInputProcessor functionality."""
    
    def test_single_url_initialization(self):
        """Test initialization with single URL (backward compatibility)."""
        processor = MultiInputProcessor("https://example.com")
        
        assert processor.is_single_url == True
        assert processor.input_tuple == ("https://example.com",)
        assert processor.root_url == "https://example.com"
        
    def test_multi_input_initialization(self):
        """Test initialization with multiple inputs."""
        inputs = ("https://example.com", "./test.pdf", "./notes.md")
        processor = MultiInputProcessor(inputs)
        
        assert processor.is_single_url == False
        assert processor.input_tuple == inputs
        assert len(processor.validated_inputs) == 3
        
    def test_find_first_url(self):
        """Test finding first URL in input tuple."""
        inputs = ("./test.pdf", "https://example.com", "./notes.md")
        processor = MultiInputProcessor(inputs)
        
        first_url = processor._find_first_url(inputs)
        assert first_url == "https://example.com"
        
        # Test with no URLs
        inputs_no_url = ("./test.pdf", "./notes.md")
        first_url = processor._find_first_url(inputs_no_url)
        assert first_url is None
        
    def test_create_anchor(self):
        """Test anchor creation for TOC."""
        processor = MultiInputProcessor("https://example.com")
        
        assert processor._create_anchor("Test Title") == "test-title"
        assert processor._create_anchor("Complex Title with Special! Characters@") == "complex-title-with-special-characters"
        assert processor._create_anchor("  Multiple   Spaces  ") == "multiple-spaces"
        
    @pytest.mark.asyncio
    async def test_process_markdown_files(self):
        """Test processing multiple markdown files."""
        # Create sample markdown files
        files = []
        for i in range(3):
            content = f"# Document {i}\n\nContent for document {i}."
            with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
                f.write(content)
                f.flush()
                files.append((i, f.name))
        
        try:
            processor = MultiInputProcessor("https://example.com")
            results = await processor._process_markdown_files(files)
            
            assert len(results) == 3
            for i, result in enumerate(results):
                assert result.success == True
                assert result.position == i
                assert result.input_type == InputType.MARKDOWN
                assert f"Document {i}" in result.content
        finally:
            for _, file_path in files:
                os.unlink(file_path)
                
    @pytest.mark.asyncio
    @patch('multi_input_processor.MultiInputProcessor.crawl_with_optimized_selector')
    async def test_process_urls(self, mock_crawl, sample_markdown_file):
        """Test processing URLs."""
        # Mock the crawling method
        mock_crawl.return_value = "# Test Page\n\nTest content from URL."
        
        url_inputs = [(0, "https://example.com")]
        processor = MultiInputProcessor("https://example.com")
        
        results = await processor._process_urls(url_inputs)
        
        assert len(results) == 1
        assert results[0].success == True
        assert results[0].input_type == InputType.URL
        assert results[0].source == "https://example.com"
        assert "Test Page" in results[0].content
        
    @pytest.mark.asyncio
    async def test_create_mixed_content_document(self):
        """Test creating mixed content document."""
        # Create sample results
        results = [
            ProcessingResult(
                success=True,
                position=0,
                input_type=InputType.URL,
                source="https://example.com",
                content="# Web Page\n\nContent from web.",
                metadata={'title': 'Web Page'},
                processing_time=1.0
            ),
            ProcessingResult(
                success=True,
                position=1,
                input_type=InputType.PDF,
                source="test.pdf",
                content="# PDF Document\n\nContent from PDF.",
                metadata={'title': 'PDF Document'},
                processing_time=2.0
            ),
            ProcessingResult(
                success=False,
                position=2,
                input_type=InputType.MARKDOWN,
                source="missing.md",
                error_message="File not found"
            )
        ]
        
        with tempfile.TemporaryDirectory() as temp_dir:
            processor = MultiInputProcessor("https://example.com", output_dir=temp_dir)
            
            output_file = await processor._create_mixed_content_document(results)
            
            assert output_file.exists()
            
            with open(output_file, 'r') as f:
                content = f.read()
                
            # Check TOC is present
            assert "Table of Contents" in content
            assert "🌐 [Web Page]" in content
            assert "📄 [PDF Document]" in content
            assert "❌ Failed: missing.md" in content
            
            # Check content sections are present
            assert "## 🌐 Web Page" in content
            assert "## 📄 PDF Document" in content
            assert "## ❌ Failed: missing.md" in content
            assert "Content from web." in content
            assert "Content from PDF." in content


class TestCreateMultiInputProcessor:
    """Test convenience function for creating processor."""
    
    def test_create_with_single_url(self):
        """Test creating processor with single URL."""
        processor = create_multi_input_processor("https://example.com")
        
        assert isinstance(processor, MultiInputProcessor)
        assert processor.is_single_url == True
        
    def test_create_with_tuple(self):
        """Test creating processor with input tuple."""
        inputs = ("https://example.com", "./test.pdf")
        processor = create_multi_input_processor(inputs)
        
        assert isinstance(processor, MultiInputProcessor)
        assert processor.is_single_url == False
        assert len(processor.validated_inputs) == 2
        
    def test_create_with_custom_settings(self):
        """Test creating processor with custom settings."""
        processor = create_multi_input_processor(
            "https://example.com",
            output_dir="custom_output",
            max_concurrent=20
        )
        
        assert processor.max_concurrent == 20
        assert "custom_output" in str(processor.output_dir)


class TestErrorHandling:
    """Test error handling scenarios."""
    
    def test_invalid_input_tuple(self):
        """Test handling of invalid input tuple."""
        with pytest.raises(ValueError):
            MultiInputProcessor(())  # Empty tuple
            
        with pytest.raises(ValueError):
            MultiInputProcessor(("valid", "", "also_valid"))  # Empty string
            
    @pytest.mark.asyncio
    async def test_mixed_success_failure_processing(self):
        """Test handling mixed success and failure results."""
        # This would be an integration test that requires mocking
        # multiple components, but demonstrates the concept
        pass


if __name__ == "__main__":
    pytest.main([__file__])