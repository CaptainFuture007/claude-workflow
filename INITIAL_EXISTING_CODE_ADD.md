
## Existing Codebase and app status
# Project File Analysis Summary

## 1. Business / User Goal

**High-level purpose**: Create a high-performance web documentation crawler that automatically extracts, organizes, and converts website documentation into clean, searchable markdown files for offline use.

**Who benefits and why**:
- **Developers & Technical Writers**: Need offline access to documentation, faster searching, and consolidated reference materials
- **Organizations**: Want to archive documentation, create internal knowledge bases, and ensure continuity of access to critical technical information
- **Researchers & Students**: Require comprehensive documentation collections for analysis, learning, and reference without internet dependency

## 2. System Design Architecture & Tech Stack

**Architecture**: Modular Python application with concurrent processing pipeline
- **Pattern**: Asynchronous processing with configurable concurrency control
- **Processing Flow**: URL Discovery → Concurrent Crawling → Content Extraction → Output Generation

**Tech Stack**:
- **Language**: Python 3.8+
- **Core Frameworks**: 
  - `crawl4ai` - Web crawling and content extraction
  - `asyncio` - Asynchronous processing and concurrency
  - `langchain-community` - Advanced URL discovery via RecursiveUrlLoader
- **Supporting Libraries**:
  - `BeautifulSoup4` - HTML parsing and link extraction
  - `requests` - HTTP requests for fallback URL discovery
  - `pathlib` - Modern file system operations
  - `pydantic` - Data validation (via crawl4ai)

## 3. Main Features & Benefits

**Core Features**:
- **High-speed concurrent crawling** (2+ pages/second, 246x faster than sequential)
- **Hybrid URL discovery** with automatic fallback mechanisms
- **Smart content extraction** using multiple CSS selector strategies
- **Automatic markdown conversion** with metadata enrichment
- **Progress tracking** with real-time statistics
- **Configurable depth control** and pattern-based filtering
- **Dual output formats** (individual files + concatenated document)

**Key Benefits**:
- **Performance**: Dramatically reduces crawling time from hours to minutes
- **Reliability**: Fallback mechanisms ensure maximum page discovery
- **Organization**: Structured output with metadata, TOC, and source attribution
- **Flexibility**: Configurable for different sites and use cases
- **Quality**: Clean content extraction focused on main documentation content

## 4. Path to Existing Code

**Core Logic Locations**:

**Main Crawler Engine** (`fast_ordered_crawler.py`):
- `FastOrderedCrawler` class (lines 75-494) - Primary crawler implementation
- `extract_urls_fast()` (lines 139-198) - Hybrid URL discovery logic
- `crawl_all_concurrent()` (lines 334-389) - Concurrent processing engine
- `process_url()` (lines 277-316) - Individual page processing

**Content Organization** (`create_concatenated_docs.py`):
- `create_concatenated_docs()` (lines 38-156) - Document assembly logic
- Frontmatter processing functions (lines 11-36) - Metadata extraction
- Table of contents generation (lines 91-119) - Navigation structure

**Entry Points**:
- `fast_ordered_crawler.py` - Main CLI application with argument parsing
- `crawl_anthropic_docs.py` - Example usage script for Anthropic documentation
- `create_concatenated_docs.py` - Standalone document concatenation utility

**Key Directories**:
- `/content/` - Individual crawled markdown files with metadata
- Output directories configurable via `--output-dir` parameter
- Progress tracking and summary files generated automatically

**Configuration Points**:
- CLI arguments (lines 469-487 in fast_ordered_crawler.py)
- CSS selectors for content extraction (lines 114-119)
- Concurrency and performance settings (constructor parameters)


## NEW FEATURE TO BE DEVELOPED:

- The current app only takes in urls. The v2 version should also take in pdf and markdowns
- The app will use Docling to transform pdfs into markdown
- The input will be a tuple of strings, with the url and/or the path to the pdf or markdown. The position of urls/path in the tuple is determining the position in the final cocatenated document
- For now we stop at generation of markdown and don't chunk the files and store them in supabase. This will be the next feature

## EXAMPLES:

The `examples/` folder provide code examples for the Docling pipeline at "./Docling"



## DOCUMENTATION:

**Docling documentation: https://docling-project.github.io/docling/**
**Use the perform_query_rag to critically review the Docling and Crawl4ai code blocks**



## OTHER CONSIDERATIONS:

- Include a .env.example, README with instructions for setup including 
- Include the project structure in the README.
- Virtual environment has already been set up with the necessary dependencies.
- Use uv for package, virtual environment and dependency management
- Use python_dotenv and load_env() for environment variables
- Check if all dependencies have been installed, if not use uv to add them
