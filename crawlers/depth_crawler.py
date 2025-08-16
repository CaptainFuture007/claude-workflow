"""
Depth-based URL Crawler with Main Content Extraction

This module crawls URLs to a specified depth, extracts main content from each page,
and saves the content as markdown files.
"""

import asyncio
import os
from pathlib import Path
from typing import List, Dict, Set, Optional, Any
from urllib.parse import urlparse, urljoin, urldefrag
from datetime import datetime
import hashlib

from crawl4ai import (
    AsyncWebCrawler,
    BrowserConfig,
    CrawlerRunConfig,
    CacheMode,
    MemoryAdaptiveDispatcher
)


class DepthCrawler:
    """
    Crawls URLs to a specified depth, extracts main content, and saves as markdown.
    
    Args:
        root_url: The starting URL to crawl
        max_depth: Maximum depth to crawl (default: 2)
        output_dir: Directory to save markdown files (default: 'crawled_content')
        max_concurrent: Maximum concurrent browser sessions (default: 5)
        memory_threshold: Memory usage threshold percentage (default: 70.0)
        exclude_patterns: List of URL patterns to exclude from crawling
    """
    
    def __init__(
        self,
        root_url: str,
        max_depth: int = 2,
        output_dir: str = "crawled_content",
        max_concurrent: int = 5,
        memory_threshold: float = 70.0,
        exclude_patterns: Optional[List[str]] = None,
        progress_tracker: Optional[Any] = None
    ):
        self.root_url = self._normalize_url(root_url)
        self.max_depth = max_depth
        self.output_dir = Path(output_dir)
        self.max_concurrent = max_concurrent
        self.memory_threshold = memory_threshold
        self.exclude_patterns = exclude_patterns or []
        self.progress_tracker = progress_tracker
        
        # Parse root domain for internal link checking
        self.root_domain = urlparse(self.root_url).netloc
        
        # Track visited URLs
        self.visited_urls: Set[str] = set()
        self.url_to_filepath: Dict[str, Path] = {}
        
        # Create output directory
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize crawler configs
        self.browser_config = BrowserConfig(
            headless=True,
            verbose=False,
            extra_args=["--disable-gpu", "--disable-dev-shm-usage"]
        )
        
        self.run_config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            stream=False,
            exclude_external_links=True,
            exclude_social_media_links=True
        )
        
        self.dispatcher = MemoryAdaptiveDispatcher(
            memory_threshold_percent=self.memory_threshold,
            check_interval=1.0,
            max_session_permit=self.max_concurrent
        )
    
    def _normalize_url(self, url: str) -> str:
        """Remove fragment and trailing slash from URL."""
        url = urldefrag(url)[0]
        if url.endswith('/'):
            url = url[:-1]
        return url
    
    def _is_valid_url(self, url: str) -> bool:
        """Check if URL should be crawled."""
        # Check if URL is internal
        parsed = urlparse(url)
        if parsed.netloc != self.root_domain:
            return False
        
        # Check exclude patterns
        for pattern in self.exclude_patterns:
            if pattern in url:
                return False
        
        # Exclude common non-content URLs
        exclude_extensions = ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.zip', '.tar', '.gz']
        for ext in exclude_extensions:
            if url.lower().endswith(ext):
                return False
        
        return True
    
    def _generate_filename(self, url: str, depth: int) -> Path:
        """Generate a unique filename for the URL."""
        parsed = urlparse(url)
        
        # Create a readable filename from the URL path
        path_parts = [p for p in parsed.path.split('/') if p]
        
        if not path_parts:
            filename = "index"
        else:
            filename = "_".join(path_parts[-3:])  # Use last 3 path components
        
        # Add depth prefix for organization
        filename = f"depth{depth}_{filename}"
        
        # Ensure uniqueness with hash if needed
        if len(filename) > 50:
            url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
            filename = f"{filename[:50]}_{url_hash}"
        
        # Clean filename
        filename = "".join(c if c.isalnum() or c in '-_' else '_' for c in filename)
        
        return self.output_dir / f"{filename}.md"
    
    def _save_markdown(self, url: str, content: str, depth: int, metadata: Dict) -> Path:
        """Save crawled content as markdown with metadata."""
        filepath = self._generate_filename(url, depth)
        
        # Ensure unique filepath
        counter = 1
        original_filepath = filepath
        while filepath.exists():
            filepath = original_filepath.with_stem(f"{original_filepath.stem}_{counter}")
            counter += 1
        
        # Create markdown with metadata header
        markdown_content = f"""---
url: {url}
crawled_at: {datetime.now().isoformat()}
depth: {depth}
title: {metadata.get('title', 'Untitled')}
description: {metadata.get('description', '')}
---

# {metadata.get('title', 'Untitled')}

{content}
"""
        
        filepath.write_text(markdown_content, encoding='utf-8')
        self.url_to_filepath[url] = filepath
        
        return filepath
    
    async def crawl(self) -> Dict[str, any]:
        """
        Perform depth-based crawling starting from root URL.
        
        Returns:
            Dictionary containing crawl statistics and results
        """
        results = {
            'total_crawled': 0,
            'successful': 0,
            'failed': 0,
            'files_created': [],
            'errors': []
        }
        
        current_urls = {self.root_url}
        
        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            for depth in range(self.max_depth + 1):
                # Create depth-specific progress tracking
                if self.progress_tracker:
                    depth_task = self.progress_tracker.create_task(
                        f"depth_{depth}",
                        f"📊 Crawling Depth {depth}/{self.max_depth}",
                        total=None  # We'll update this once we know the count
                    )
                else:
                    print(f"\n{'='*50}")
                    print(f"Crawling Depth {depth}/{self.max_depth}")
                    print(f"{'='*50}")
                
                # Filter out already visited URLs
                urls_to_crawl = [
                    url for url in current_urls 
                    if url not in self.visited_urls
                ]
                
                if not urls_to_crawl:
                    if self.progress_tracker:
                        self.progress_tracker.complete_task(f"depth_{depth}", "No new URLs to crawl")
                    else:
                        print("No new URLs to crawl at this depth")
                    break
                
                # Update progress with actual count
                if self.progress_tracker:
                    self.progress_tracker.update_task(
                        f"depth_{depth}",
                        total=len(urls_to_crawl),
                        advance=0  # Don't advance yet
                    )
                    self.progress_tracker.log(f"Processing {len(urls_to_crawl)} URLs at depth {depth}")
                else:
                    print(f"Crawling {len(urls_to_crawl)} URLs...")
                
                # Batch crawl all URLs at current depth
                crawl_results = await crawler.arun_many(
                    urls=urls_to_crawl,
                    config=self.run_config,
                    dispatcher=self.dispatcher
                )
                
                next_level_urls = set()
                processed_count = 0
                
                for result in crawl_results:
                    url = self._normalize_url(result.url)
                    self.visited_urls.add(url)
                    results['total_crawled'] += 1
                    processed_count += 1
                    
                    if result.success:
                        # Extract metadata
                        metadata = {
                            'title': result.metadata.get('title', 'Untitled'),
                            'description': result.metadata.get('description', ''),
                            'word_count': len(result.markdown.split()) if result.markdown else 0
                        }
                        
                        # Save content if it has substantial text
                        if result.markdown and metadata['word_count'] > 50:
                            filepath = self._save_markdown(
                                url, 
                                result.markdown, 
                                depth, 
                                metadata
                            )
                            results['successful'] += 1
                            results['files_created'].append(str(filepath))
                            
                            if self.progress_tracker:
                                self.progress_tracker.update_task(
                                    f"depth_{depth}",
                                    advance=1,
                                    current_item=f"✓ {metadata['title']} ({metadata['word_count']} words)"
                                )
                                self.progress_tracker.increment_stats(processed=1, successful=1)
                            else:
                                print(f"✓ {url}")
                                print(f"  → Saved to: {filepath.name}")
                                print(f"  → Words: {metadata['word_count']}")
                        else:
                            if self.progress_tracker:
                                self.progress_tracker.update_task(
                                    f"depth_{depth}",
                                    advance=1,
                                    current_item=f"⚠ {url} - Insufficient content"
                                )
                                self.progress_tracker.increment_stats(processed=1, skipped=1)
                            else:
                                print(f"⚠ {url} - Insufficient content")
                        
                        # Collect internal links for next depth
                        if depth < self.max_depth:
                            for link in result.links.get("internal", []):
                                next_url = self._normalize_url(link["href"])
                                if self._is_valid_url(next_url) and next_url not in self.visited_urls:
                                    next_level_urls.add(next_url)
                    else:
                        results['failed'] += 1
                        error_msg = f"{url}: {result.error_message}"
                        results['errors'].append(error_msg)
                        
                        if self.progress_tracker:
                            self.progress_tracker.update_task(
                                f"depth_{depth}",
                                advance=1,
                                current_item=f"✗ {error_msg}"
                            )
                            self.progress_tracker.increment_stats(processed=1, failed=1)
                        else:
                            print(f"✗ {error_msg}")
                
                # Complete depth task
                if self.progress_tracker:
                    self.progress_tracker.complete_task(
                        f"depth_{depth}",
                        f"✅ Depth {depth} complete - {len(next_level_urls)} new URLs discovered"
                    )
                else:
                    print(f"\nDepth {depth} complete: {len(next_level_urls)} new URLs discovered")
                
                # Prepare URLs for next depth
                current_urls = next_level_urls
        
        # Generate summary
        self._generate_summary(results)
        
        return results
    
    def _generate_summary(self, results: Dict):
        """Generate a summary file of the crawl."""
        summary_path = self.output_dir / "crawl_summary.md"
        
        summary = f"""# Crawl Summary

**Root URL**: {self.root_url}
**Max Depth**: {self.max_depth}
**Crawl Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Statistics
- Total URLs Crawled: {results['total_crawled']}
- Successful: {results['successful']}
- Failed: {results['failed']}
- Files Created: {len(results['files_created'])}

## Crawled Pages

"""
        
        # Group files by depth
        for depth in range(self.max_depth + 1):
            depth_files = [
                f for f in results['files_created'] 
                if f"depth{depth}_" in Path(f).name
            ]
            
            if depth_files:
                summary += f"\n### Depth {depth} ({len(depth_files)} pages)\n\n"
                for filepath in sorted(depth_files):
                    filename = Path(filepath).name
                    # Find URL for this file
                    url = next(
                        (url for url, fp in self.url_to_filepath.items() 
                         if str(fp) == filepath),
                        "Unknown"
                    )
                    summary += f"- [{filename}]({filename}) - {url}\n"
        
        if results['errors']:
            summary += "\n## Errors\n\n"
            for error in results['errors']:
                summary += f"- {error}\n"
        
        summary_path.write_text(summary, encoding='utf-8')
        print(f"\n📊 Summary saved to: {summary_path}")


async def main():
    """Example usage of DepthCrawler."""
    # Example configuration
    crawler = DepthCrawler(
        root_url="https://example.com",
        max_depth=2,
        output_dir="crawled_content",
        max_concurrent=5,
        exclude_patterns=["/login", "/signup", "/admin"]
    )
    
    results = await crawler.crawl()
    
    print("\n" + "="*50)
    print("CRAWL COMPLETE")
    print("="*50)
    print(f"Total pages crawled: {results['total_crawled']}")
    print(f"Successfully saved: {results['successful']}")
    print(f"Failed: {results['failed']}")


if __name__ == "__main__":
    asyncio.run(main())