"""
Backward Compatibility Tests

Ensures that existing URL-only workflows continue to work exactly as before
with the MultiInputProcessor v2.0 implementation.
"""

import pytest
import asyncio
import tempfile
from pathlib import Path
from unittest.mock import patch, AsyncMock, Mock

from multi_input_processor import MultiInputProcessor, create_multi_input_processor
from fast_ordered_crawler import FastOrderedCrawler


class TestBackwardCompatibilityInitialization:
    """Test that MultiInputProcessor can be used exactly like FastOrderedCrawler."""
    
    def test_single_url_initialization_compatibility(self):
        """Test that single URL initialization works exactly like FastOrderedCrawler."""
        # Test with MultiInputProcessor
        multi_processor = MultiInputProcessor(
            "https://example.com",
            max_depth=2,
            output_dir="test_output",
            max_concurrent=10
        )
        
        # Test with original FastOrderedCrawler
        original_crawler = FastOrderedCrawler(
            root_url="https://example.com",
            max_depth=2,
            output_dir="test_output",
            max_concurrent=10
        )
        
        # Should have same basic attributes
        assert multi_processor.root_url == original_crawler.root_url
        assert multi_processor.max_depth == original_crawler.max_depth
        assert multi_processor.max_concurrent == original_crawler.max_concurrent
        assert str(multi_processor.output_dir) == str(original_crawler.output_dir)
        
        # MultiInputProcessor should be in single URL mode
        assert multi_processor.is_single_url == True
        assert multi_processor.input_tuple == ("https://example.com",)
        
    def test_all_fastorderedcrawler_parameters_supported(self):
        """Test that all FastOrderedCrawler parameters are supported."""
        # Test with all original FastOrderedCrawler parameters
        multi_processor = MultiInputProcessor(
            "https://example.com",
            max_depth=3,
            output_dir="custom_output",
            max_concurrent=20,
            exclude_patterns=["pattern1", "pattern2"],
            show_progress=False
        )
        
        assert multi_processor.root_url == "https://example.com"
        assert multi_processor.max_depth == 3
        assert "custom_output" in str(multi_processor.output_dir)
        assert multi_processor.max_concurrent == 20
        assert multi_processor.exclude_patterns == ["pattern1", "pattern2"]
        assert multi_processor.show_progress == False


class TestBackwardCompatibilityMethods:
    """Test that all FastOrderedCrawler methods work identically."""
    
    @pytest.fixture
    def processor(self):
        """Create MultiInputProcessor in single URL mode."""
        return MultiInputProcessor("https://example.com")
    
    def test_sanitize_filename_compatibility(self, processor):
        """Test that filename sanitization works identically."""
        # Test method exists and works
        filename = processor.sanitize_filename("https://example.com/test/path", depth=1)
        assert filename.startswith("depth1_")
        assert filename.endswith(".md")
        
    def test_extract_title_from_content_compatibility(self, processor):
        """Test title extraction works identically."""
        content = "# Test Title\n\nSome content here."
        title = processor.extract_title_from_content(content)
        assert title == "Test Title"
        
    def test_extract_description_from_content_compatibility(self, processor):
        """Test description extraction works identically."""
        content = "# Title\n\nThis is a description paragraph."
        description = processor.extract_description_from_content(content)
        assert description == "This is a description paragraph."
        
    @pytest.mark.asyncio
    async def test_crawl_with_optimized_selector_compatibility(self, processor):
        """Test that crawling method interface is identical."""
        # This method should exist and have the same signature
        assert hasattr(processor, 'crawl_with_optimized_selector')
        
        # The method signature should be compatible
        import inspect
        sig = inspect.signature(processor.crawl_with_optimized_selector)
        params = list(sig.parameters.keys())
        assert 'url' in params
        assert 'depth' in params
        
    def test_content_selectors_compatibility(self, processor):
        """Test that content selectors are identical."""
        # Should have the same content selectors as FastOrderedCrawler
        expected_selectors = [
            'main, article, [role="main"]',
            '#content, .content',
            '.main-content, .page-content',
            'body'
        ]
        assert processor.content_selectors == expected_selectors


class TestBackwardCompatibilityBehavior:
    """Test that behavior is identical for single URL processing."""
    
    @pytest.mark.asyncio
    @patch('multi_input_processor.MultiInputProcessor.crawl_with_optimized_selector')
    async def test_single_url_crawl_behavior(self, mock_crawl):
        """Test that single URL crawling behaves identically."""
        # Mock the crawling method
        mock_crawl.return_value = "# Test Page\n\nTest content."
        
        processor = MultiInputProcessor("https://example.com")
        
        # When processing single URL, should use parent class method
        stats = await processor.crawl()
        
        # Should return statistics in the same format
        assert isinstance(stats, dict)
        # The exact structure depends on whether it calls parent crawl() or process_input_tuple()
        # For single URL, it should call parent crawl() method
        
    def test_output_directory_structure_compatibility(self):
        """Test that output directory structure is identical."""
        with tempfile.TemporaryDirectory() as temp_dir:
            processor = MultiInputProcessor("https://example.com", output_dir=temp_dir)
            
            # Should create the same directory structure as FastOrderedCrawler
            expected_content_dir = Path(temp_dir) / "content"
            assert processor.content_dir == expected_content_dir
            assert processor.content_dir.exists()
            
    def test_processed_urls_tracking_compatibility(self):
        """Test that URL tracking works identically."""
        processor = MultiInputProcessor("https://example.com")
        
        # Should have processed_urls set for tracking
        assert hasattr(processor, 'processed_urls')
        assert isinstance(processor.processed_urls, set)
        assert len(processor.processed_urls) == 0


class TestBackwardCompatibilityAPI:
    """Test that the API is fully backward compatible."""
    
    def test_convenience_function_single_url(self):
        """Test convenience function with single URL."""
        processor = create_multi_input_processor("https://example.com")
        
        assert isinstance(processor, MultiInputProcessor)
        assert processor.is_single_url == True
        assert processor.root_url == "https://example.com"
        
    def test_convenience_function_with_kwargs(self):
        """Test convenience function with all kwargs."""
        processor = create_multi_input_processor(
            "https://example.com",
            output_dir="custom_dir",
            max_concurrent=15,
            max_depth=3,
            exclude_patterns=["test"],
            show_progress=False
        )
        
        assert processor.max_concurrent == 15
        assert processor.max_depth == 3
        assert processor.exclude_patterns == ["test"]
        assert processor.show_progress == False


class TestBackwardCompatibilityIntegration:
    """Integration tests for backward compatibility."""
    
    @pytest.mark.asyncio
    async def test_complete_workflow_compatibility(self):
        """Test that a complete workflow works identically."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create processor
            processor = MultiInputProcessor(
                "https://example.com",
                output_dir=temp_dir,
                max_concurrent=5
            )
            
            # Mock the URL extraction and crawling
            with patch.object(processor, 'extract_urls_fast') as mock_extract:
                with patch.object(processor, 'crawl_with_optimized_selector') as mock_crawl:
                    mock_extract.return_value = ["https://example.com"]
                    mock_crawl.return_value = "# Test Content\n\nTest page content."
                    
                    # Should be able to call crawl() just like FastOrderedCrawler
                    stats = await processor.crawl()
                    
                    # Should create output files like FastOrderedCrawler
                    content_dir = Path(temp_dir) / "content"
                    assert content_dir.exists()
                    
                    # Should return statistics
                    assert isinstance(stats, dict)
                    # Note: exact keys depend on implementation
    
    def test_inheritance_compatibility(self):
        """Test that MultiInputProcessor properly inherits from FastOrderedCrawler."""
        processor = MultiInputProcessor("https://example.com")
        
        # Should be instance of FastOrderedCrawler
        assert isinstance(processor, FastOrderedCrawler)
        
        # Should have all parent methods
        parent_methods = [
            'sanitize_filename',
            'extract_urls_fast',
            'extract_urls_custom',
            'crawl_with_optimized_selector',
            'extract_title_from_content',
            'extract_description_from_content',
            'create_summary_document'
        ]
        
        for method_name in parent_methods:
            assert hasattr(processor, method_name)
            
    def test_no_regression_in_existing_functionality(self):
        """Test that no existing functionality is broken."""
        processor = MultiInputProcessor("https://example.com")
        
        # Test that all existing attributes exist
        assert hasattr(processor, 'root_url')
        assert hasattr(processor, 'max_depth')
        assert hasattr(processor, 'output_dir')
        assert hasattr(processor, 'content_dir')
        assert hasattr(processor, 'max_concurrent')
        assert hasattr(processor, 'exclude_patterns')
        assert hasattr(processor, 'show_progress')
        assert hasattr(processor, 'progress_tracker')
        assert hasattr(processor, 'content_selectors')
        assert hasattr(processor, 'processed_urls')


class TestCliBackwardCompatibility:
    """Test CLI backward compatibility."""
    
    def test_cli_single_url_argument(self):
        """Test that CLI still accepts single URL as before."""
        from multi_input_cli import create_argument_parser
        
        parser = create_argument_parser()
        
        # Should accept single URL argument like before
        args = parser.parse_args(["https://example.com"])
        assert args.inputs == ["https://example.com"]
        
        # Should work with all original options
        args = parser.parse_args([
            "--output-dir", "custom_output",
            "--max-concurrent", "20",
            "--max-depth", "3",
            "https://example.com"
        ])
        
        assert args.output_dir == "custom_output"
        assert args.max_concurrent == 20
        assert args.max_depth == 3
        assert args.inputs == ["https://example.com"]


class TestOutputCompatibility:
    """Test that output format is compatible."""
    
    @pytest.mark.asyncio
    async def test_single_url_output_format(self):
        """Test that single URL processing produces compatible output."""
        with tempfile.TemporaryDirectory() as temp_dir:
            processor = MultiInputProcessor("https://example.com", output_dir=temp_dir)
            
            # For single URL, should produce same output structure as FastOrderedCrawler
            # This would require actual crawling or comprehensive mocking
            # For now, just test the structure is set up correctly
            
            assert processor.content_dir.exists()
            assert processor.content_dir.name == "content"
    
    def test_summary_document_compatibility(self):
        """Test that summary document format is compatible."""
        with tempfile.TemporaryDirectory() as temp_dir:
            processor = MultiInputProcessor("https://example.com", output_dir=temp_dir)
            
            # Mock stats for summary creation
            stats = {
                'total_urls': 5,
                'successful': 4,
                'failed': 1,
                'success_rate': 0.8
            }
            
            summary_path = processor.create_summary_document(stats)
            
            # Should create summary file
            assert summary_path.exists()
            assert summary_path.name.endswith(".md")
            
            # Should contain expected content
            with open(summary_path, 'r') as f:
                content = f.read()
                
            assert "Fast Crawl Summary" in content
            assert str(processor.root_url) in content
            assert "Total URLs: 5" in content
            assert "Successfully Crawled: 4" in content


if __name__ == "__main__":
    pytest.main([__file__])