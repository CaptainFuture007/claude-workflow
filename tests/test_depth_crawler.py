"""
Unit tests for DepthCrawler module.

Tests the depth-based URL crawler with main content extraction functionality.
"""

import pytest
import asyncio
from pathlib import Path
from unittest.mock import Mock, AsyncMock, patch, MagicMock
import tempfile
import shutil
from datetime import datetime

import sys
sys.path.append(str(Path(__file__).parent.parent))

from crawlers.depth_crawler import DepthCrawler


class TestDepthCrawler:
    """Test suite for DepthCrawler class."""
    
    @pytest.fixture
    def temp_dir(self):
        """Create a temporary directory for test outputs."""
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)
    
    @pytest.fixture
    def crawler(self, temp_dir):
        """Create a DepthCrawler instance for testing."""
        return DepthCrawler(
            root_url="https://example.com",
            max_depth=2,
            output_dir=temp_dir,
            max_concurrent=3,
            exclude_patterns=["/admin", "/login"]
        )
    
    def test_initialization(self, crawler):
        """Test proper initialization of DepthCrawler."""
        assert crawler.root_url == "https://example.com"
        assert crawler.max_depth == 2
        assert crawler.max_concurrent == 3
        assert "/admin" in crawler.exclude_patterns
        assert crawler.root_domain == "example.com"
        assert crawler.output_dir.exists()
    
    def test_normalize_url(self, crawler):
        """Test URL normalization."""
        # Test fragment removal
        assert crawler._normalize_url("https://example.com#section") == "https://example.com"
        
        # Test trailing slash removal
        assert crawler._normalize_url("https://example.com/") == "https://example.com"
        
        # Test combined
        assert crawler._normalize_url("https://example.com/page/#section") == "https://example.com/page"
    
    def test_is_valid_url(self, crawler):
        """Test URL validation logic."""
        # Valid internal URLs
        assert crawler._is_valid_url("https://example.com/page") is True
        assert crawler._is_valid_url("https://example.com/blog/post") is True
        
        # Invalid: external domain
        assert crawler._is_valid_url("https://other.com/page") is False
        
        # Invalid: excluded patterns
        assert crawler._is_valid_url("https://example.com/admin/panel") is False
        assert crawler._is_valid_url("https://example.com/login") is False
        
        # Invalid: file extensions
        assert crawler._is_valid_url("https://example.com/file.pdf") is False
        assert crawler._is_valid_url("https://example.com/doc.docx") is False
    
    def test_generate_filename(self, crawler):
        """Test filename generation from URLs."""
        # Basic URL
        filepath = crawler._generate_filename("https://example.com/blog/post", 1)
        assert "depth1_blog_post" in str(filepath)
        assert filepath.suffix == ".md"
        
        # Index page
        filepath = crawler._generate_filename("https://example.com", 0)
        assert "depth0_index" in str(filepath)
        
        # Long URL - should be truncated
        long_url = "https://example.com/" + "very_long_path/" * 10
        filepath = crawler._generate_filename(long_url, 2)
        assert len(filepath.stem) <= 60  # 50 chars + hash
    
    def test_save_markdown(self, crawler):
        """Test markdown file saving with metadata."""
        url = "https://example.com/test"
        content = "This is the main content of the page."
        metadata = {
            'title': 'Test Page',
            'description': 'A test page description'
        }
        
        filepath = crawler._save_markdown(url, content, 1, metadata)
        
        # Check file exists
        assert filepath.exists()
        
        # Check content
        saved_content = filepath.read_text()
        assert "url: https://example.com/test" in saved_content
        assert "depth: 1" in saved_content
        assert "title: Test Page" in saved_content
        assert "This is the main content" in saved_content
        
        # Check URL tracking
        assert crawler.url_to_filepath[url] == filepath
    
    def test_save_markdown_unique_filenames(self, crawler):
        """Test that duplicate URLs get unique filenames."""
        url = "https://example.com/duplicate"
        content = "Content"
        metadata = {'title': 'Test'}
        
        # Save twice with same URL
        filepath1 = crawler._save_markdown(url, content, 1, metadata)
        filepath2 = crawler._save_markdown(url, content, 1, metadata)
        
        # Should create different files
        assert filepath1 != filepath2
        assert filepath1.exists()
        assert filepath2.exists()
    
    @pytest.mark.asyncio
    async def test_crawl_basic(self, crawler):
        """Test basic crawling functionality."""
        # Mock the AsyncWebCrawler
        with patch('crawlers.depth_crawler.AsyncWebCrawler') as MockCrawler:
            mock_crawler_instance = AsyncMock()
            MockCrawler.return_value.__aenter__.return_value = mock_crawler_instance
            
            # Mock crawl results
            mock_result = Mock()
            mock_result.success = True
            mock_result.url = "https://example.com"
            mock_result.markdown = "# Test Content\n\nThis is test content with more than 50 words. " * 10
            mock_result.metadata = {'title': 'Test Page', 'description': 'Test'}
            mock_result.links = {'internal': []}
            mock_result.error_message = None
            
            mock_crawler_instance.arun_many.return_value = [mock_result]
            
            results = await crawler.crawl()
            
            # Verify results
            assert results['total_crawled'] == 1
            assert results['successful'] == 1
            assert results['failed'] == 0
            assert len(results['files_created']) == 1
    
    @pytest.mark.asyncio
    async def test_crawl_with_depth(self, crawler):
        """Test crawling with multiple depth levels."""
        with patch('crawlers.depth_crawler.AsyncWebCrawler') as MockCrawler:
            mock_crawler_instance = AsyncMock()
            MockCrawler.return_value.__aenter__.return_value = mock_crawler_instance
            
            # First depth results
            mock_result1 = Mock()
            mock_result1.success = True
            mock_result1.url = "https://example.com"
            mock_result1.markdown = "Root page content " * 20
            mock_result1.metadata = {'title': 'Root', 'description': 'Root page'}
            mock_result1.links = {
                'internal': [
                    {'href': 'https://example.com/page1'},
                    {'href': 'https://example.com/page2'}
                ]
            }
            
            # Second depth results
            mock_result2 = Mock()
            mock_result2.success = True
            mock_result2.url = "https://example.com/page1"
            mock_result2.markdown = "Page 1 content " * 20
            mock_result2.metadata = {'title': 'Page 1', 'description': 'First page'}
            mock_result2.links = {'internal': []}
            
            mock_result3 = Mock()
            mock_result3.success = True
            mock_result3.url = "https://example.com/page2"
            mock_result3.markdown = "Page 2 content " * 20
            mock_result3.metadata = {'title': 'Page 2', 'description': 'Second page'}
            mock_result3.links = {'internal': []}
            
            # Configure mock to return different results for each call
            mock_crawler_instance.arun_many.side_effect = [
                [mock_result1],  # Depth 0
                [mock_result2, mock_result3]  # Depth 1
            ]
            
            results = await crawler.crawl()
            
            # Verify multi-depth crawling
            assert results['total_crawled'] == 3
            assert results['successful'] == 3
            assert len(results['files_created']) == 3
    
    @pytest.mark.asyncio
    async def test_crawl_with_failures(self, crawler):
        """Test handling of failed crawls."""
        with patch('crawlers.depth_crawler.AsyncWebCrawler') as MockCrawler:
            mock_crawler_instance = AsyncMock()
            MockCrawler.return_value.__aenter__.return_value = mock_crawler_instance
            
            # Mix of successful and failed results
            mock_success = Mock()
            mock_success.success = True
            mock_success.url = "https://example.com/success"
            mock_success.markdown = "Success content " * 20
            mock_success.metadata = {'title': 'Success', 'description': 'OK'}
            mock_success.links = {'internal': []}
            
            mock_failure = Mock()
            mock_failure.success = False
            mock_failure.url = "https://example.com/fail"
            mock_failure.error_message = "Connection timeout"
            
            mock_crawler_instance.arun_many.return_value = [mock_success, mock_failure]
            
            results = await crawler.crawl()
            
            # Verify error handling
            assert results['total_crawled'] == 2
            assert results['successful'] == 1
            assert results['failed'] == 1
            assert len(results['errors']) == 1
            assert "Connection timeout" in results['errors'][0]
    
    @pytest.mark.asyncio
    async def test_crawl_excludes_patterns(self, crawler):
        """Test that excluded patterns are not crawled."""
        with patch('crawlers.depth_crawler.AsyncWebCrawler') as MockCrawler:
            mock_crawler_instance = AsyncMock()
            MockCrawler.return_value.__aenter__.return_value = mock_crawler_instance
            
            mock_result = Mock()
            mock_result.success = True
            mock_result.url = "https://example.com"
            mock_result.markdown = "Content " * 20
            mock_result.metadata = {'title': 'Test', 'description': 'Test'}
            mock_result.links = {
                'internal': [
                    {'href': 'https://example.com/page'},  # Valid
                    {'href': 'https://example.com/admin/panel'},  # Should be excluded
                    {'href': 'https://example.com/login'}  # Should be excluded
                ]
            }
            
            mock_crawler_instance.arun_many.side_effect = [
                [mock_result],  # First call
                []  # Should not crawl excluded URLs
            ]
            
            await crawler.crawl()
            
            # Verify excluded URLs were not added to crawl queue
            assert "https://example.com/admin/panel" not in crawler.visited_urls
            assert "https://example.com/login" not in crawler.visited_urls
    
    def test_generate_summary(self, crawler, temp_dir):
        """Test summary generation."""
        # Create some mock results
        results = {
            'total_crawled': 5,
            'successful': 4,
            'failed': 1,
            'files_created': [
                str(Path(temp_dir) / "depth0_index.md"),
                str(Path(temp_dir) / "depth1_page1.md"),
                str(Path(temp_dir) / "depth1_page2.md"),
                str(Path(temp_dir) / "depth2_subpage.md")
            ],
            'errors': ["https://example.com/error: Connection failed"]
        }
        
        # Mock the url_to_filepath mapping
        for filepath in results['files_created']:
            url = f"https://example.com/{Path(filepath).stem.split('_', 1)[1]}"
            crawler.url_to_filepath[url] = Path(filepath)
        
        crawler._generate_summary(results)
        
        # Check summary file exists
        summary_path = Path(temp_dir) / "crawl_summary.md"
        assert summary_path.exists()
        
        # Check summary content
        summary_content = summary_path.read_text()
        assert "Root URL: https://example.com" in summary_content
        assert "Total URLs Crawled: 5" in summary_content
        assert "Successful: 4" in summary_content
        assert "Failed: 1" in summary_content
        assert "Connection failed" in summary_content


@pytest.mark.asyncio
async def test_main_function():
    """Test the main function example."""
    with patch('crawlers.depth_crawler.DepthCrawler') as MockCrawler:
        mock_instance = Mock()
        MockCrawler.return_value = mock_instance
        
        mock_instance.crawl = AsyncMock(return_value={
            'total_crawled': 10,
            'successful': 8,
            'failed': 2,
            'files_created': [],
            'errors': []
        })
        
        # Import and run main
        from crawlers.depth_crawler import main
        await main()
        
        # Verify crawler was created and called
        MockCrawler.assert_called_once()
        mock_instance.crawl.assert_called_once()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])