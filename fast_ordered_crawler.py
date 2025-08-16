#!/usr/bin/env python3
"""
Fast Ordered Crawler - Optimized version based on performance analysis

This implementation incorporates performance optimizations from existing scraping examples:
1. RecursiveUrlLoader for faster URL discovery (from smart_content_scraper.py)
2. Concurrent processing with proper resource management
3. CSS selector optimization for main content extraction
4. Simplified extraction strategy focused on speed
5. Progress tracking with better performance metrics

Key optimizations:
- Uses RecursiveUrlLoader instead of custom navigation extraction
- Concurrent processing with configurable limits
- CSS selector-based content extraction
- Streamlined markdown generation
- Memory-efficient processing
"""

import asyncio
import os
import re
from typing import List, Dict, Optional, Set
from urllib.parse import urlparse, urljoin
from pathlib import Path
import logging
from datetime import datetime
import json

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from langchain_community.document_loaders import RecursiveUrlLoader
from bs4 import BeautifulSoup
import requests

# from progress_tracker import ProgressTracker

class SimpleProgressTracker:
    """Simple progress tracker for when rich is not available."""
    
    def __init__(self):
        self.tasks = {}
    
    def create_task(self, name: str, description: str, total: Optional[int] = None) -> str:
        self.tasks[name] = {"description": description, "total": total, "current": 0}
        print(f"📊 {description}")
        return name
    
    def update_task(self, name: str, advance: int = 1, description: Optional[str] = None, **kwargs):
        if name in self.tasks:
            self.tasks[name]["current"] += advance
            if description:
                self.tasks[name]["description"] = description
            
            task = self.tasks[name]
            current = task["current"]
            total = task["total"]
            
            if total:
                percentage = (current / total) * 100
                print(f"   {task['description']}: {current}/{total} ({percentage:.1f}%)")
            else:
                print(f"   {task['description']}: {current}")

ProgressTracker = SimpleProgressTracker

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class FastOrderedCrawler:
    """Fast crawler optimized for performance using patterns from existing examples."""
    
    def __init__(
        self, 
        root_url: str, 
        max_depth: int = 2, 
        output_dir: str = "fast_crawl", 
        max_concurrent: int = 10,  # Increased from 1
        exclude_patterns: Optional[List[str]] = None,
        show_progress: bool = True
    ):
        """
        Initialize the fast crawler.
        
        Args:
            root_url: Starting URL for crawling
            max_depth: Maximum crawl depth
            output_dir: Output directory for results
            max_concurrent: Maximum concurrent crawls (increased for speed)
            exclude_patterns: URL patterns to exclude
            show_progress: Whether to show progress bars
        """
        self.root_url = root_url
        self.max_depth = max_depth
        self.output_dir = Path(output_dir)
        self.max_concurrent = max_concurrent
        self.exclude_patterns = exclude_patterns or []
        self.show_progress = show_progress
        
        # Create output directories
        self.output_dir.mkdir(exist_ok=True)
        self.content_dir = self.output_dir / "content"
        self.content_dir.mkdir(exist_ok=True)
        
        # Progress tracking
        self.progress_tracker = ProgressTracker() if show_progress else None
        
        # Content selectors optimized for main content (from smart_content_scraper.py)
        self.content_selectors = [
            'main, article, [role="main"]',
            '#content, .content',
            '.main-content, .page-content',
            'body'
        ]
        
        # Processed URLs tracking
        self.processed_urls: Set[str] = set()
        
    def sanitize_filename(self, url: str, depth: int = 0) -> str:
        """Convert URL to a safe filename with depth prefix."""
        parsed = urlparse(url)
        domain = parsed.netloc.replace('www.', '').replace('.', '-')
        path = parsed.path.strip('/').replace('/', '_').replace('.', '-')
        
        if path:
            filename = f"depth{depth}_{domain}_{path}"
        else:
            filename = f"depth{depth}_{domain}"
            
        # Clean and limit length
        filename = re.sub(r'[^a-zA-Z0-9-_]', '', filename)
        return f"{filename[:80]}.md"
    
    def extract_urls_fast(self) -> List[str]:
        """
        Extract URLs using hybrid approach: RecursiveUrlLoader + custom extraction.
        Based on smart_content_scraper.py approach with fallback.
        """
        if self.progress_tracker:
            task_id = self.progress_tracker.create_task(
                "url_discovery", 
                "Discovering URLs with hybrid approach", 
                total=None
            )
        
        all_urls = set()
        
        try:
            logger.info(f"Extracting URLs from {self.root_url} with max_depth={self.max_depth}")
            
            # Method 1: Try RecursiveUrlLoader first
            try:
                loader = RecursiveUrlLoader(
                    url=self.root_url,
                    max_depth=self.max_depth,
                    exclude_dirs=self.exclude_patterns,
                    extractor=lambda x: BeautifulSoup(x, "html.parser").get_text()
                )
                
                docs = loader.load()
                all_urls.add(self.root_url)
                
                for doc in docs:
                    if hasattr(doc, 'metadata') and 'source' in doc.metadata:
                        url = doc.metadata['source']
                        if not any(pattern in url for pattern in self.exclude_patterns):
                            all_urls.add(url)
                            
                logger.info(f"RecursiveUrlLoader found {len(all_urls)} URLs")
                
            except Exception as e:
                logger.warning(f"RecursiveUrlLoader failed: {e}")
            
            # Method 2: If we only got 1 URL, use custom extraction
            if len(all_urls) <= 1:
                logger.info("Using custom link extraction as fallback...")
                all_urls = self.extract_urls_custom()
            
            if self.progress_tracker:
                self.progress_tracker.update_task(
                    "url_discovery", 
                    description=f"Found {len(all_urls)} URLs",
                    total=len(all_urls),
                    advance=len(all_urls)
                )
                
        except Exception as e:
            logger.error(f"Error extracting URLs: {e}")
            all_urls.add(self.root_url)
        
        discovered_urls = list(all_urls)
        logger.info(f"Hybrid URL discovery found {len(discovered_urls)} URLs")
        return discovered_urls
    
    def extract_urls_custom(self) -> Set[str]:
        """Custom URL extraction using requests + BeautifulSoup."""
        all_urls = set()
        all_urls.add(self.root_url)
        
        try:
            # Get the main page
            response = requests.get(self.root_url, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Extract links from navigation and content areas
                links = soup.find_all('a', href=True)
                
                for link in links:
                    href = link['href']
                    
                    # Convert relative URLs to absolute
                    if href.startswith('/'):
                        full_url = f"https://docs.anthropic.com{href}"
                    elif href.startswith('http'):
                        full_url = href
                    else:
                        continue
                    
                    # Filter for relevant URLs
                    if (full_url.startswith('https://docs.anthropic.com/en/docs/claude-code/') and 
                        full_url != self.root_url and
                        not any(pattern in full_url for pattern in self.exclude_patterns)):
                        all_urls.add(full_url)
                        
                logger.info(f"Custom extraction found {len(all_urls)} URLs")
                
        except Exception as e:
            logger.error(f"Custom URL extraction failed: {e}")
        
        return all_urls
    
    async def crawl_with_optimized_selector(self, url: str, depth: int = 0) -> Optional[str]:
        """
        Crawl URL with optimized CSS selectors for main content.
        Based on approach from smart_content_scraper.py.
        """
        try:
            # Try each selector until we find content
            for selector in self.content_selectors:
                config = CrawlerRunConfig(
                    css_selector=selector,
                    markdown_generator=DefaultMarkdownGenerator(
                        options={"body_width": 0}  # No text wrapping for speed
                    )
                )
                
                async with AsyncWebCrawler() as crawler:
                    result = await crawler.arun(url, config=config)
                    
                    if result.success and result.markdown and len(result.markdown.strip()) > 100:
                        # Found good content, return it
                        return result.markdown
            
            # If no selector worked, try without selector
            config = CrawlerRunConfig(
                markdown_generator=DefaultMarkdownGenerator(
                    options={"body_width": 0}
                )
            )
            
            async with AsyncWebCrawler() as crawler:
                result = await crawler.arun(url, config=config)
                if result.success and result.markdown:
                    return result.markdown
                    
        except Exception as e:
            logger.error(f"Error crawling {url}: {e}")
            
        return None
    
    async def process_url(self, url: str, depth: int, semaphore: asyncio.Semaphore) -> bool:
        """Process a single URL with concurrency control."""
        async with semaphore:
            if url in self.processed_urls:
                return False
                
            try:
                # Crawl the URL
                content = await self.crawl_with_optimized_selector(url, depth)
                
                if content:
                    # Save content
                    filename = self.sanitize_filename(url, depth)
                    filepath = self.content_dir / filename
                    
                    # Create metadata
                    metadata = f"""---
url: {url}
crawled_at: {datetime.now().isoformat()}
depth: {depth}
title: {self.extract_title_from_content(content)}
description: {self.extract_description_from_content(content)}
---

"""
                    
                    # Save file
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(metadata + content)
                    
                    self.processed_urls.add(url)
                    logger.info(f"Saved: {filename}")
                    return True
                else:
                    logger.warning(f"No content extracted from {url}")
                    return False
                    
            except Exception as e:
                logger.error(f"Error processing {url}: {e}")
                return False
    
    def extract_title_from_content(self, content: str) -> str:
        """Extract title from markdown content."""
        lines = content.split('\n')
        for line in lines:
            if line.startswith('# '):
                return line[2:].strip()
        return "Untitled"
    
    def extract_description_from_content(self, content: str) -> str:
        """Extract description from markdown content."""
        lines = content.split('\n')
        for line in lines:
            if line.strip() and not line.startswith('#') and len(line) > 20:
                return line.strip()[:200] + "..." if len(line) > 200 else line.strip()
        return "No description available"
    
    async def crawl_all_concurrent(self, urls: List[str]) -> Dict[str, any]:
        """Crawl all URLs concurrently for maximum speed."""
        if self.progress_tracker:
            crawl_task = self.progress_tracker.create_task(
                "crawling", 
                "Crawling pages concurrently", 
                total=len(urls)
            )
        
        # Create semaphore for concurrency control
        semaphore = asyncio.Semaphore(self.max_concurrent)
        
        # Create tasks for all URLs
        tasks = []
        for i, url in enumerate(urls):
            depth = 0 if url == self.root_url else 1  # Simple depth assignment
            task = asyncio.create_task(self.process_url(url, depth, semaphore))
            tasks.append((url, task))
        
        # Process tasks with progress updates
        completed = 0
        successful = 0
        
        for url, task in tasks:
            try:
                success = await task
                if success:
                    successful += 1
                completed += 1
                
                if self.progress_tracker:
                    self.progress_tracker.update_task(
                        "crawling",
                        advance=1,
                        current_item=f"Processed: {url}",
                        success_rate=f"{successful}/{completed}"
                    )
                    
            except Exception as e:
                logger.error(f"Task failed for {url}: {e}")
                completed += 1
                
                if self.progress_tracker:
                    self.progress_tracker.update_task(
                        "crawling",
                        advance=1,
                        current_item=f"Failed: {url}",
                        success_rate=f"{successful}/{completed}"
                    )
        
        return {
            "total_urls": len(urls),
            "successful": successful,
            "failed": completed - successful,
            "success_rate": successful / completed if completed > 0 else 0
        }
    
    def create_summary_document(self, stats: Dict[str, any]) -> Path:
        """Create a summary document with crawl statistics."""
        summary_content = f"""# Fast Crawl Summary

**Source**: {self.root_url}
**Generated**: {datetime.now().strftime('%Y-%m-%d at %I:%M %p')}
**Max Depth**: {self.max_depth}
**Concurrency**: {self.max_concurrent}

## Performance Statistics

- **Total URLs**: {stats['total_urls']}
- **Successfully Crawled**: {stats['successful']}
- **Failed**: {stats['failed']}
- **Success Rate**: {stats['success_rate']:.1%}

## Optimization Features

✅ **RecursiveUrlLoader**: Fast URL discovery
✅ **Concurrent Processing**: {self.max_concurrent} simultaneous crawls
✅ **CSS Selector Optimization**: Targeted main content extraction
✅ **Streamlined Pipeline**: Reduced processing overhead

## Files Created

All crawled content saved to: `{self.content_dir}`

---

*Generated by FastOrderedCrawler - Optimized for Performance*
"""
        
        summary_path = self.output_dir / "fast_crawl_summary.md"
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(summary_content)
        
        return summary_path
    
    async def crawl(self) -> Dict[str, any]:
        """Main crawling method optimized for speed."""
        start_time = datetime.now()
        
        logger.info(f"Starting Fast Ordered Crawler...")
        logger.info(f"Root URL: {self.root_url}")
        logger.info(f"Max Depth: {self.max_depth}")
        logger.info(f"Concurrency: {self.max_concurrent}")
        logger.info(f"Output: {self.output_dir}")
        
        # Step 1: Fast URL discovery
        urls = self.extract_urls_fast()
        
        # Step 2: Concurrent crawling
        stats = await self.crawl_all_concurrent(urls)
        
        # Step 3: Create summary
        summary_path = self.create_summary_document(stats)
        
        # Calculate timing
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        stats.update({
            "duration_seconds": duration,
            "pages_per_second": stats['successful'] / duration if duration > 0 else 0,
            "summary_file": str(summary_path)
        })
        
        logger.info(f"\nFast crawl completed in {duration:.1f} seconds!")
        logger.info(f"Speed: {stats['pages_per_second']:.1f} pages/second")
        logger.info(f"Summary: {summary_path}")
        
        return stats


async def main():
    """Example usage of FastOrderedCrawler."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Fast Ordered Crawler - High-performance web crawling')
    parser.add_argument('url', help='Starting URL to crawl')
    parser.add_argument('--output-dir', '-o', default='fast_crawl', help='Output directory')
    parser.add_argument('--max-depth', '-d', type=int, default=1, help='Maximum crawl depth')
    parser.add_argument('--max-concurrent', '-c', type=int, default=10, help='Maximum concurrent crawls')
    parser.add_argument('--exclude', '-e', nargs='*', default=[], help='Patterns to exclude')
    parser.add_argument('--no-progress', action='store_true', help='Disable progress bars')
    
    args = parser.parse_args()
    
    # Create and run crawler
    crawler = FastOrderedCrawler(
        root_url=args.url,
        max_depth=args.max_depth,
        output_dir=args.output_dir,
        max_concurrent=args.max_concurrent,
        exclude_patterns=args.exclude,
        show_progress=not args.no_progress
    )
    
    stats = await crawler.crawl()
    print(f"\nCrawl completed: {stats['successful']}/{stats['total_urls']} pages in {stats['duration_seconds']:.1f}s")


if __name__ == "__main__":
    asyncio.run(main())