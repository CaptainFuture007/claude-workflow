# Docling PDF Processing Best Practices

This directory contains reference implementations demonstrating best practices for PDF parsing with Docling.

## Files Overview

### Core Processing Files
- **`unified_pdf_processor.py`** - Main unified interface for PDF processing with comprehensive configuration
- **`enhanced_markdown_processor.py`** - Advanced processor with figure extraction and AI summarization
- **`markdown_processor.py`** - Core markdown generation functionality

### Supporting Components
- **`document_storage.py`** - Document storage and retrieval utilities
- **`document_chunker.py`** - Document chunking for RAG applications

## Key Best Practices Demonstrated

### 1. Configuration Management
- **Unified configuration** with dataclasses for type safety
- **Environment variable integration** for flexible deployment
- **Validation and defaults** for robust configuration handling

### 2. Error Handling & Logging
- **Comprehensive error tracking** with detailed error messages
- **Progress tracking** with statistics and performance metrics
- **Graceful failure handling** with fallback mechanisms

### 3. Performance Optimization
- **Concurrent processing** capabilities
- **Memory management** with temporary directories
- **Configurable timeouts** and resource limits

### 4. Output Management
- **Structured output directories** with consistent naming
- **Multiple output formats** (markdown, JSON, chunks)
- **Metadata preservation** with comprehensive tracking

### 5. AI Integration
- **Optional AI summarization** for figures and content
- **Configurable AI models** (OpenAI, Ollama) with fallbacks
- **Context-aware processing** for better results

### 6. Quality Features
- **High-quality image extraction** with configurable DPI/scaling
- **Table structure preservation** with markdown formatting
- **Figure classification** and metadata extraction
- **Document structure analysis** with section tracking

## Integration Patterns

### Basic Usage
```python
from unified_pdf_processor import create_unified_processor

processor = create_unified_processor(
    parsed_output_dir="./output",
    enable_ai_summarization=True
)

success, file_info = processor.process_single_pdf("document.pdf")
```

### Batch Processing
```python
result = processor.process_directory("./pdfs/")
print(f"Success rate: {result.stats.success_rate:.1f}%")
```

### Configuration Examples
```python
config = UnifiedProcessingConfig(
    image_scale=3.0,           # High quality images
    image_dpi=900,             # Publication quality
    enable_ai_summarization=True,
    create_subdirectories=True,
    generate_chunks=True
)
```

## Dependencies

- **docling** - Core PDF processing
- **docling-core** - Document models
- **ollama** (optional) - Local AI summarization
- **openai** (optional) - Cloud AI summarization

These files demonstrate production-ready patterns for integrating Docling into web crawling applications.