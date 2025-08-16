"""
Ordered Crawler - Complete solution for crawling and stitching web content

Combines depth-based crawling with navigation extraction to create
properly ordered documentation from any website.
"""

import asyncio
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime

from .depth_crawler import DepthCrawler
from .navigation_extractor import NavigationExtractor
from .document_stitcher import stitch_crawled_content
from .progress_tracker import ProgressTracker


class OrderedCrawler:
    """
    Crawls a website and creates a properly ordered, stitched document
    based on the site's navigation structure.
    """
    
    def __init__(
        self,
        root_url: str,
        max_depth: int = 2,
        output_dir: str = "ordered_crawl",
        max_concurrent: int = 5,
        exclude_patterns: Optional[List[str]] = None,
        extract_navigation: bool = True,
        create_stitched: bool = True,
        show_progress: bool = True
    ):
        """
        Initialize the OrderedCrawler.
        
        Args:
            root_url: Starting URL to crawl
            max_depth: Maximum crawl depth
            output_dir: Directory for output files
            max_concurrent: Maximum concurrent browser sessions
            exclude_patterns: URL patterns to exclude
            extract_navigation: Whether to extract navigation structure
            create_stitched: Whether to create a stitched document
            show_progress: Whether to show progress bars
        """
        self.root_url = root_url
        self.max_depth = max_depth
        self.output_dir = Path(output_dir)
        self.max_concurrent = max_concurrent
        self.exclude_patterns = exclude_patterns or []
        self.extract_navigation = extract_navigation
        self.create_stitched = create_stitched
        self.show_progress = show_progress
        
        # Results storage
        self.navigation_tree = None
        self.ordered_urls = None
        self.crawl_results = None
        
        # Progress tracking
        self.progress = ProgressTracker(enable_rich=show_progress) if show_progress else None
        
    async def run(self) -> Dict:
        """
        Run the complete ordered crawling process.
        
        Returns:
            Dictionary with results and statistics
        """
        # Initialize progress tracking
        if self.progress:
            self.progress.start()
            self.progress.print_stage_header(
                "STARTING ORDERED CRAWL",
                f"🌐 {self.root_url} | 📊 Depth: {self.max_depth} | 📁 Output: {self.output_dir}"
            )
        else:
            print("\n" + "="*60)
            print("🚀 STARTING ORDERED CRAWL")
            print("="*60)
            print(f"Root URL: {self.root_url}")
            print(f"Max Depth: {self.max_depth}")
            print(f"Output Directory: {self.output_dir}")
            print("="*60 + "\n")
        
        results = {
            'start_time': datetime.now(),
            'root_url': self.root_url,
            'stages': {}
        }
        
        # Stage 1: Extract Navigation Structure
        if self.extract_navigation:
            if self.progress:
                with self.progress.stage("Stage 1: Extracting Navigation", "🗺️ Analyzing site structure"):
                    nav_task = self.progress.create_task(
                        "nav_extraction", 
                        "🔍 Extracting navigation structure", 
                        total=None
                    )
            else:
                print("📍 Stage 1: Extracting Navigation Structure")
                print("-" * 40)
            
            nav_extractor = NavigationExtractor(self.root_url, progress_tracker=self.progress)
            try:
                self.navigation_tree = await nav_extractor.extract()
                
                if self.navigation_tree:
                    self.ordered_urls = nav_extractor.get_ordered_urls()
                    
                    if self.progress:
                        self.progress.complete_task("nav_extraction", 
                            f"✅ Found {len(self.ordered_urls)} pages in navigation")
                        self.progress.update_stats(total_discovered=len(self.ordered_urls))
                    else:
                        nav_extractor.print_structure()
                        print(f"✅ Found {len(self.ordered_urls)} pages in navigation")
                    
                    # Save navigation structure
                    nav_file = self.output_dir / "navigation_structure.json"
                    nav_file.parent.mkdir(parents=True, exist_ok=True)
                    nav_extractor.export_structure(str(nav_file))
                    
                    results['stages']['navigation'] = {
                        'success': True,
                        'pages_found': len(self.ordered_urls),
                        'structure_file': str(nav_file)
                    }
                else:
                    if self.progress:
                        self.progress.fail_task("nav_extraction", "Could not extract navigation structure")
                    else:
                        print("⚠️  Could not extract navigation structure")
                    results['stages']['navigation'] = {
                        'success': False,
                        'error': 'No navigation structure found'
                    }
            except Exception as e:
                if self.progress:
                    self.progress.fail_task("nav_extraction", f"Navigation extraction failed: {e}")
                else:
                    print(f"❌ Navigation extraction failed: {e}")
                results['stages']['navigation'] = {
                    'success': False,
                    'error': str(e)
                }
        
        # Stage 2: Crawl Website
        if self.progress:
            with self.progress.stage("Stage 2: Crawling Website", "📊 Downloading page content"):
                pass
        else:
            print("\n📊 Stage 2: Crawling Website Content")
            print("-" * 40)
        
        crawler = DepthCrawler(
            root_url=self.root_url,
            max_depth=self.max_depth,
            output_dir=str(self.output_dir / "content"),
            max_concurrent=self.max_concurrent,
            exclude_patterns=self.exclude_patterns,
            progress_tracker=self.progress
        )
        
        try:
            self.crawl_results = await crawler.crawl()
            
            results['stages']['crawling'] = {
                'success': True,
                'total_crawled': self.crawl_results['total_crawled'],
                'successful': self.crawl_results['successful'],
                'failed': self.crawl_results['failed'],
                'files_created': len(self.crawl_results['files_created'])
            }
            
            if self.progress:
                self.progress.log(
                    f"Crawled {self.crawl_results['total_crawled']} pages "
                    f"({self.crawl_results['successful']} successful, {self.crawl_results['failed']} failed)",
                    "success"
                )
            else:
                print(f"✅ Crawled {self.crawl_results['total_crawled']} pages")
                print(f"   - Successful: {self.crawl_results['successful']}")
                print(f"   - Failed: {self.crawl_results['failed']}")
            
        except Exception as e:
            if self.progress:
                self.progress.log(f"Crawling failed: {e}", "error")
            else:
                print(f"❌ Crawling failed: {e}")
            results['stages']['crawling'] = {
                'success': False,
                'error': str(e)
            }
            results['end_time'] = datetime.now()
            results['duration'] = str(results['end_time'] - results['start_time'])
            if self.progress:
                self.progress.stop()
            return results
        
        # Stage 3: Create Stitched Document
        if self.create_stitched and self.crawl_results['successful'] > 0:
            print("\n📝 Stage 3: Creating Stitched Document")
            print("-" * 40)
            
            try:
                content_dir = self.output_dir / "content"
                
                # Create stitched document
                stitched_path = stitch_crawled_content(
                    content_dir=str(content_dir),
                    navigation_tree=self.navigation_tree,
                    ordered_urls=self.ordered_urls,
                    output_file="stitched_document.md",
                    include_unmatched=True,
                    progress_tracker=self.progress
                )
                
                results['stages']['stitching'] = {
                    'success': True,
                    'output_file': str(stitched_path)
                }
                
                print(f"✅ Stitched document created: {stitched_path.name}")
                
                # Create a master summary
                await self._create_master_summary(results)
                
            except Exception as e:
                print(f"❌ Document stitching failed: {e}")
                results['stages']['stitching'] = {
                    'success': False,
                    'error': str(e)
                }
        
        # Calculate final statistics
        results['end_time'] = datetime.now()
        results['duration'] = str(results['end_time'] - results['start_time'])
        
        # Update final stats and print summary
        if self.progress:
            if self.crawl_results:
                self.progress.update_stats(
                    total_processed=self.crawl_results['total_crawled'],
                    successful=self.crawl_results['successful'],
                    failed=self.crawl_results['failed']
                )
            self.progress.print_summary()
            self.progress.stop()
        else:
            self._print_final_summary(results)
        
        return results
    
    async def _create_master_summary(self, results: Dict):
        """Create a master summary file with all results."""
        summary_path = self.output_dir / "master_summary.md"
        
        summary_lines = [
            f"# 📚 Ordered Crawl Summary",
            f"",
            f"**Root URL**: {self.root_url}",
            f"**Crawl Date**: {results['start_time'].strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Duration**: {results['duration']}",
            f"",
            f"## 📊 Results",
            f""
        ]
        
        # Navigation results
        if 'navigation' in results['stages']:
            nav = results['stages']['navigation']
            if nav['success']:
                summary_lines.extend([
                    f"### ✅ Navigation Extraction",
                    f"- Pages found in navigation: {nav['pages_found']}",
                    f"- Structure saved to: `{Path(nav['structure_file']).name}`",
                    f""
                ])
            else:
                summary_lines.extend([
                    f"### ⚠️ Navigation Extraction",
                    f"- Failed: {nav.get('error', 'Unknown error')}",
                    f""
                ])
        
        # Crawling results
        if 'crawling' in results['stages']:
            crawl = results['stages']['crawling']
            if crawl['success']:
                summary_lines.extend([
                    f"### ✅ Content Crawling",
                    f"- Total pages crawled: {crawl['total_crawled']}",
                    f"- Successfully saved: {crawl['successful']}",
                    f"- Failed: {crawl['failed']}",
                    f"- Files created: {crawl['files_created']}",
                    f""
                ])
            else:
                summary_lines.extend([
                    f"### ❌ Content Crawling",
                    f"- Failed: {crawl.get('error', 'Unknown error')}",
                    f""
                ])
        
        # Stitching results
        if 'stitching' in results['stages']:
            stitch = results['stages']['stitching']
            if stitch['success']:
                summary_lines.extend([
                    f"### ✅ Document Stitching",
                    f"- Stitched document: `{Path(stitch['output_file']).name}`",
                    f""
                ])
            else:
                summary_lines.extend([
                    f"### ❌ Document Stitching",
                    f"- Failed: {stitch.get('error', 'Unknown error')}",
                    f""
                ])
        
        # Output files
        summary_lines.extend([
            f"## 📁 Output Files",
            f"",
            f"### Main Documents",
            f"- `stitched_document.md` - Complete documentation in reading order",
            f"- `reading_guide.md` - Recommended reading sequence",
            f"- `crawl_summary.md` - Detailed crawl statistics",
            f"",
            f"### Supporting Files",
            f"- `navigation_structure.json` - Site navigation hierarchy",
            f"- `master_summary.md` - This summary file",
            f"",
            f"### Content Directory",
            f"- `content/*.md` - Individual page files",
            f"",
            f"## 🎯 Next Steps",
            f"",
            f"1. Open `stitched_document.md` for the complete, ordered documentation",
            f"2. Review `reading_guide.md` to understand the document structure",
            f"3. Check `crawl_summary.md` for detailed crawl statistics",
            f""
        ])
        
        summary_path.write_text("\n".join(summary_lines), encoding='utf-8')
        print(f"📄 Master summary saved to: {summary_path.name}")
    
    def _print_final_summary(self, results: Dict):
        """Print a final summary to the console."""
        print("\n" + "="*60)
        print("✨ ORDERED CRAWL COMPLETE")
        print("="*60)
        
        if 'navigation' in results['stages'] and results['stages']['navigation']['success']:
            print(f"📍 Navigation pages: {results['stages']['navigation']['pages_found']}")
        
        if 'crawling' in results['stages'] and results['stages']['crawling']['success']:
            crawl = results['stages']['crawling']
            print(f"📊 Crawled pages: {crawl['total_crawled']} ({crawl['successful']} saved)")
        
        if 'stitching' in results['stages'] and results['stages']['stitching']['success']:
            print(f"📝 Stitched document created")
        
        print(f"⏱️  Duration: {results['duration']}")
        print(f"📁 Output directory: {self.output_dir}")
        print("\n" + "="*60)


async def main():
    """Example usage of OrderedCrawler."""
    
    # Example 1: Crawl documentation site with navigation
    crawler = OrderedCrawler(
        root_url="https://docs.example.com",
        max_depth=2,
        output_dir="docs_crawl",
        exclude_patterns=["/api/", "/reference/"],
        extract_navigation=True,
        create_stitched=True
    )
    
    results = await crawler.run()
    
    # The results dictionary contains all statistics and file paths
    print("\n📋 Results summary:")
    print(f"- Total duration: {results['duration']}")
    
    if results['stages'].get('stitching', {}).get('success'):
        print(f"- Output file: {results['stages']['stitching']['output_file']}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Allow command-line usage
        url = sys.argv[1]
        depth = int(sys.argv[2]) if len(sys.argv) > 2 else 2
        output = sys.argv[3] if len(sys.argv) > 3 else "ordered_crawl"
        
        crawler = OrderedCrawler(
            root_url=url,
            max_depth=depth,
            output_dir=output
        )
        
        asyncio.run(crawler.run())
    else:
        # Run example
        asyncio.run(main())