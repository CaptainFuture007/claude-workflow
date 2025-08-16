# 🕸️ Ordered Web Crawler Suite

A comprehensive solution for crawling websites and creating properly sequenced documentation that preserves the intended reading order based on site navigation.

## 🎯 Overview

This crawler suite solves a common problem: when crawling documentation sites or blogs, the pages are often saved in random order based on discovery depth rather than the logical reading sequence. This solution:

1. **Extracts the navigation structure** from the website (sidebar, menu, etc.)
2. **Crawls all content** to a specified depth
3. **Matches crawled pages** to their navigation positions
4. **Stitches everything together** in the correct reading order

## 📦 Components

### 1. **OrderedCrawler** (`ordered_crawler.py`)
The main orchestrator that combines all components for a complete crawling solution.

```python
from crawlers.ordered_crawler import OrderedCrawler

crawler = OrderedCrawler(
    root_url="https://docs.example.com",
    max_depth=2,
    output_dir="docs_output",
    extract_navigation=True,
    create_stitched=True
)

results = await crawler.run()
```

### 2. **NavigationExtractor** (`navigation_extractor.py`)
Uses Playwright to extract the navigation hierarchy from websites.

- Detects navigation using multiple strategies
- Handles sidebars, menus, and various navigation patterns
- Creates a hierarchical tree structure
- Exports navigation as JSON

### 3. **DocumentStitcher** (`document_stitcher.py`)
Combines multiple markdown files into a single, well-organized document.

- Matches crawled pages to navigation positions
- Creates table of contents with internal links
- Preserves content hierarchy
- Includes unmatched pages in an appendix

### 4. **DepthCrawler** (`depth_crawler.py`)
The core crawling engine with advanced features.

- Configurable depth-based crawling
- Memory-adaptive resource management
- Content extraction using Crawl4AI
- Automatic markdown conversion

## 🚀 Quick Start

### Installation

```bash
pip install crawl4ai playwright pydantic pyyaml
playwright install chromium
```

### Basic Usage

```python
import asyncio
from crawlers.ordered_crawler import OrderedCrawler

async def crawl_docs():
    crawler = OrderedCrawler(
        root_url="https://docs.example.com",
        max_depth=2,
        output_dir="my_docs"
    )
    
    results = await crawler.run()
    print(f"Crawl complete! Check {results['stages']['stitching']['output_file']}")

asyncio.run(crawl_docs())
```

### Command Line Usage

```bash
python ordered_crawler.py https://docs.example.com 2 output_dir
```

## 📁 Output Structure

After running the crawler, you'll get:

```
output_dir/
├── content/                      # Individual page files
│   ├── depth0_index.md
│   ├── depth1_getting_started.md
│   └── ...
├── stitched_document.md         # 📚 Complete documentation in order
├── reading_guide.md             # 📖 Recommended reading sequence
├── navigation_structure.json    # 🗺️ Site navigation map
├── crawl_summary.md            # 📊 Crawl statistics
└── master_summary.md           # 📋 Overall summary
```

## 🎨 Key Features

### Navigation-Aware Ordering
- Extracts the actual navigation structure from the website
- Orders content based on how users would naturally read it
- Preserves the hierarchical relationships between pages

### Intelligent Content Extraction
- Uses Crawl4AI's advanced extraction strategies
- Filters out navigation, ads, and other non-content elements
- Preserves formatting, code blocks, and important metadata

### Flexible Configuration
- Specify crawl depth
- Exclude URL patterns
- Control concurrent sessions
- Memory-adaptive processing

### Comprehensive Output
- Individual markdown files for each page
- Single stitched document with proper ordering
- Navigation structure export
- Reading guides and summaries

## 🔧 Advanced Configuration

### Exclude Patterns

```python
crawler = OrderedCrawler(
    root_url="https://example.com",
    exclude_patterns=[
        "/admin",
        "/login",
        "/api",
        "*.pdf"
    ]
)
```

### Custom Navigation Extraction

```python
from crawlers.navigation_extractor import NavigationExtractor

extractor = NavigationExtractor("https://example.com")
navigation = await extractor.extract()
extractor.print_structure()
ordered_urls = extractor.get_ordered_urls()
```

### Manual Document Stitching

```python
from crawlers.document_stitcher import stitch_crawled_content

output = stitch_crawled_content(
    content_dir="crawled_content",
    navigation_tree=navigation,
    ordered_urls=ordered_urls,
    include_unmatched=True
)
```

## 📊 How It Works

### 1. Navigation Extraction
The crawler first visits the root URL and attempts to extract the navigation structure using multiple strategies:
- Semantic HTML elements (`<nav>`, `role="navigation"`)
- Common CSS selectors (`.sidebar`, `#menu`)
- Pattern recognition (lists of links)
- Sitemap fallback

### 2. Content Crawling
Pages are crawled to the specified depth, with:
- Parallel processing for efficiency
- Memory management to prevent overload
- Duplicate detection
- Content extraction and markdown conversion

### 3. Matching & Ordering
Crawled pages are matched to their navigation positions using:
- Exact URL matching
- Fuzzy matching for redirects
- Path-based matching for different domains

### 4. Document Assembly
The final document is assembled with:
- Table of contents with anchor links
- Properly ordered sections
- Navigation breadcrumbs
- Clean formatting and structure

## 🎯 Use Cases

- **Documentation Sites**: Create offline copies of entire documentation
- **Knowledge Bases**: Archive knowledge bases with proper structure
- **Blogs**: Download blog archives in chronological order
- **Research**: Collect and organize web content for research
- **Archival**: Preserve websites with their intended structure

## ⚙️ Requirements

- Python 3.8+
- crawl4ai
- playwright
- pydantic
- pyyaml

## 📝 Example Output

The stitched document includes:

```markdown
# 📚 Complete Documentation

## 📑 Table of Contents

### Getting Started
- Overview
- Installation
- Quick Start

### User Guide
- Basic Usage
- Advanced Features
- Configuration

### API Reference
- Core Functions
- Utilities
- Extensions

---

### 📄 Overview
*Getting Started > Overview*

[Content of the overview page...]

---

### 📄 Installation
*Getting Started > Installation*

[Content of the installation page...]
```

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional navigation detection strategies
- Support for dynamic/JavaScript-heavy sites
- Export formats (PDF, EPUB, etc.)
- Enhanced content cleaning
- Multi-language support

## 📄 License

MIT License - See LICENSE file for details

---

*Built with ❤️ using Crawl4AI and Playwright*