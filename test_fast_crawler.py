#!/usr/bin/env python3
"""
Test script for the FastOrderedCrawler on Anthropic Claude Code docs.
"""

import asyncio
from fast_ordered_crawler import FastOrderedCrawler

async def test_anthropic_docs():
    """Test the fast crawler on Anthropic docs."""
    
    print("🚀 Testing FastOrderedCrawler on Anthropic Claude Code docs...")
    print("📊 Performance improvements:")
    print("   ✅ RecursiveUrlLoader for faster URL discovery")
    print("   ✅ Concurrent processing (10 simultaneous crawls)")
    print("   ✅ CSS selector optimization")
    print("   ✅ Streamlined extraction pipeline")
    print()
    
    # Create fast crawler with optimized settings
    crawler = FastOrderedCrawler(
        root_url="https://docs.anthropic.com/en/docs/claude-code/",
        max_depth=1,
        output_dir="fast_anthropic_crawl",
        max_concurrent=10,  # Much higher than the slow version (was 1)
        exclude_patterns=["/api/", "*.pdf", "#"],
        show_progress=True
    )
    
    # Run the crawl
    stats = await crawler.crawl()
    
    print("\n" + "="*60)
    print("🎉 FAST CRAWL RESULTS")
    print("="*60)
    print(f"📈 Total URLs: {stats['total_urls']}")
    print(f"✅ Successful: {stats['successful']}")
    print(f"❌ Failed: {stats['failed']}")
    print(f"📊 Success Rate: {stats['success_rate']:.1%}")
    print(f"⏱️  Duration: {stats['duration_seconds']:.1f} seconds")
    print(f"🚄 Speed: {stats['pages_per_second']:.1f} pages/second")
    print(f"📁 Summary: {stats['summary_file']}")
    print("="*60)
    
    # Compare with previous slow performance
    print("\n📈 PERFORMANCE COMPARISON:")
    print("   Previous (slow): ~2 minutes per page, 1 concurrent")
    print(f"   Current (fast): {stats['pages_per_second']:.1f} pages/second, 10 concurrent")
    print(f"   Improvement: ~{stats['pages_per_second'] * 120:.0f}x faster!")

if __name__ == "__main__":
    asyncio.run(test_anthropic_docs())