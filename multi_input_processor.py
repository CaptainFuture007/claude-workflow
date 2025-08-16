"""
Multi-Input Document Processor v2.0

Extends FastOrderedCrawler to support mixed input types (URLs, PDFs, markdown files)
with tuple-based ordering for comprehensive document compilation.

This processor maintains backward compatibility while adding support for:
- PDF files (local and URL-based) using Docling
- Markdown files (local)
- Mixed input tuples with preserved ordering
- Enhanced concatenation with source attribution
"""

import asyncio
import os
import time
from typing import List, Dict, Optional, Set, Tuple, Any, Union
from urllib.parse import urlparse
from pathlib import Path
import logging
from datetime import datetime
import tempfile
import shutil

# Import base crawler
from fast_ordered_crawler import FastOrderedCrawler

# Import multi-input types
from multi_input_types import (
    InputType, ProcessingResult, EnhancedMetadata,
    detect_input_type, validate_input_tuple, validate_file_input,
    create_processing_metadata
)

# Import existing Docling integration
from Docling.unified_pdf_processor import (
    UnifiedPDFProcessor, UnifiedProcessingConfig
)

logger = logging.getLogger(__name__)


class MarkdownProcessor:
    """
    Simple processor for markdown files.
    
    Reads markdown files directly and creates ProcessingResult objects
    with appropriate metadata.
    """
    
    def __init__(self):
        self.logger = logging.getLogger(f"{__name__}.MarkdownProcessor")
    
    async def process_markdown(self, file_path: str, position: int) -> ProcessingResult:
        """
        Process a markdown file.
        
        Args:
            file_path: Path to the markdown file
            position: Position in input tuple
            
        Returns:
            ProcessingResult with file content and metadata
        """
        start_time = time.time()
        
        try:
            # Validate file
            validate_file_input(file_path, InputType.MARKDOWN)
            
            path = Path(file_path)
            
            # Read file content
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract title from content
            title = self._extract_title_from_content(content)
            
            # Extract description
            description = self._extract_description_from_content(content)
            
            # Create metadata
            processing_time = time.time() - start_time
            metadata = create_processing_metadata(
                source=file_path,
                input_type=InputType.MARKDOWN,
                position=position,
                title=title,
                description=description,
                processing_time=processing_time,
                success=True,
                file_size=path.stat().st_size
            )
            
            self.logger.info(f"Successfully processed markdown file: {path.name}")
            
            return ProcessingResult(
                success=True,
                position=position,
                input_type=InputType.MARKDOWN,
                source=file_path,
                content=content,
                metadata=metadata.__dict__,
                processing_time=processing_time
            )
            
        except Exception as e:
            processing_time = time.time() - start_time
            error_msg = f"Failed to process markdown file {file_path}: {str(e)}"
            self.logger.error(error_msg)
            
            metadata = create_processing_metadata(
                source=file_path,
                input_type=InputType.MARKDOWN,
                position=position,
                processing_time=processing_time,
                success=False,
                error_message=str(e)
            )
            
            return ProcessingResult(
                success=False,
                position=position,
                input_type=InputType.MARKDOWN,
                source=file_path,
                error_message=error_msg,
                metadata=metadata.__dict__,
                processing_time=processing_time
            )
    
    def _extract_title_from_content(self, content: str) -> str:
        """Extract title from markdown content."""
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('# '):
                return line[2:].strip()
        return "Untitled Markdown Document"
    
    def _extract_description_from_content(self, content: str) -> str:
        """Extract description from markdown content."""
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#') and len(line) > 20:
                return line[:200] + "..." if len(line) > 200 else line
        return "No description available"


class PDFProcessor:
    """
    PDF processor using existing Docling integration.
    
    Wraps the UnifiedPDFProcessor to provide consistent interface
    with other input processors.
    """
    
    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)
        self.logger = logging.getLogger(f"{__name__}.PDFProcessor")
        
        # Create temporary directory for PDF processing
        self.temp_dir = self.output_dir / "temp_pdf_processing"
        self.temp_dir.mkdir(exist_ok=True)
    
    async def process_pdf(self, pdf_source: str, position: int) -> ProcessingResult:
        """
        Process a PDF file (local or URL).
        
        Args:
            pdf_source: Path to PDF file or URL
            position: Position in input tuple
            
        Returns:
            ProcessingResult with converted markdown content
        """
        start_time = time.time()
        
        try:
            # Handle URL vs local file
            if pdf_source.startswith(('http://', 'https://')):
                # Download PDF from URL first
                pdf_path = await self._download_pdf_from_url(pdf_source)
            else:
                # Local file
                validate_file_input(pdf_source, InputType.PDF)
                pdf_path = pdf_source
            
            # Create PDF processor with temporary output
            config = UnifiedProcessingConfig(
                parsed_output_dir=str(self.temp_dir),
                markdown_output_dir=str(self.temp_dir),
                enable_ai_summarization=False,  # Disable for speed
                create_subdirectories=False,
                generate_json=False,
                save_figures=False,
                save_tables=False
            )
            
            processor = UnifiedPDFProcessor(config)
            
            # Process PDF
            success, file_info = processor.process_single_pdf(pdf_path)
            
            if success and file_info.get('markdown_path'):
                # Read generated markdown
                markdown_path = Path(file_info['markdown_path'])
                with open(markdown_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Clean up temporary files
                if markdown_path.exists():
                    markdown_path.unlink()
                
                # Create metadata
                processing_time = time.time() - start_time
                metadata = create_processing_metadata(
                    source=pdf_source,
                    input_type=InputType.PDF,
                    position=position,
                    title=file_info.get('base_name', 'Untitled PDF'),
                    description=f"PDF document with {file_info.get('pages', 0)} pages",
                    processing_time=processing_time,
                    success=True,
                    pdf_pages=file_info.get('pages', 0)
                )
                
                self.logger.info(f"Successfully processed PDF: {Path(pdf_source).name}")
                
                return ProcessingResult(
                    success=True,
                    position=position,
                    input_type=InputType.PDF,
                    source=pdf_source,
                    content=content,
                    metadata=metadata.__dict__,
                    processing_time=processing_time
                )
            else:
                error_msg = file_info.get('error_message', 'Unknown PDF processing error')
                raise Exception(error_msg)
                
        except Exception as e:
            processing_time = time.time() - start_time
            error_msg = f"Failed to process PDF {pdf_source}: {str(e)}"
            self.logger.error(error_msg)
            
            metadata = create_processing_metadata(
                source=pdf_source,
                input_type=InputType.PDF,
                position=position,
                processing_time=processing_time,
                success=False,
                error_message=str(e)
            )
            
            return ProcessingResult(
                success=False,
                position=position,
                input_type=InputType.PDF,
                source=pdf_source,
                error_message=error_msg,
                metadata=metadata.__dict__,
                processing_time=processing_time
            )
    
    async def _download_pdf_from_url(self, pdf_url: str) -> str:
        """Download PDF from URL to temporary file."""
        import requests
        
        response = requests.get(pdf_url, timeout=30)
        response.raise_for_status()
        
        # Create temporary file
        temp_file = self.temp_dir / f"temp_pdf_{int(time.time())}.pdf"
        
        with open(temp_file, 'wb') as f:
            f.write(response.content)
        
        return str(temp_file)
    
    def cleanup(self):
        """Clean up temporary files."""
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)


class MultiInputProcessor(FastOrderedCrawler):
    """
    Extended processor supporting URLs, PDFs, and markdown files.
    
    Maintains backward compatibility with FastOrderedCrawler while adding
    support for mixed input types with tuple-based ordering.
    """
    
    def __init__(
        self,
        input_data: Union[str, Tuple[str, ...]],
        output_dir: str = "multi_input_crawl",
        max_concurrent: int = 10,
        **kwargs
    ):
        """
        Initialize the multi-input processor.
        
        Args:
            input_data: Single URL (backward compatibility) or tuple of mixed inputs
            output_dir: Output directory for results
            max_concurrent: Maximum concurrent operations
            **kwargs: Additional arguments passed to FastOrderedCrawler
        """
        # Handle backward compatibility
        if isinstance(input_data, str):
            # Single URL - use parent class initialization
            super().__init__(
                root_url=input_data,
                output_dir=output_dir,
                max_concurrent=max_concurrent,
                **kwargs
            )
            self.input_tuple = (input_data,)
            self.is_single_url = True
        else:
            # Mixed input tuple - initialize with first URL or dummy URL
            first_url = self._find_first_url(input_data)
            super().__init__(
                root_url=first_url or "https://example.com",
                output_dir=output_dir,
                max_concurrent=max_concurrent,
                **kwargs
            )
            self.input_tuple = input_data
            self.is_single_url = False
        
        # Initialize processors
        self.markdown_processor = MarkdownProcessor()
        self.pdf_processor = PDFProcessor(output_dir)
        
        # Validate inputs
        self.validated_inputs = validate_input_tuple(self.input_tuple)
        
        self.logger = logging.getLogger(f"{__name__}.MultiInputProcessor")
    
    def _find_first_url(self, input_tuple: Tuple[str, ...]) -> Optional[str]:
        """Find the first URL in the input tuple for backward compatibility."""
        for input_str in input_tuple:
            if detect_input_type(input_str) == InputType.URL:
                return input_str
        return None
    
    async def process_input_tuple(self) -> Dict[str, Any]:
        """
        Main processing orchestrator for mixed input types.
        
        Returns:
            Dictionary with processing statistics and results
        """
        start_time = datetime.now()
        
        self.logger.info(f"Starting multi-input processing...")
        self.logger.info(f"Input count: {len(self.validated_inputs)}")
        self.logger.info(f"Output directory: {self.output_dir}")
        
        # Group inputs by type for processing strategy
        url_inputs = []
        pdf_inputs = []
        markdown_inputs = []
        
        for position, input_str, input_type in self.validated_inputs:
            if input_type == InputType.URL:
                url_inputs.append((position, input_str))
            elif input_type == InputType.PDF:
                pdf_inputs.append((position, input_str))
            elif input_type == InputType.MARKDOWN:
                markdown_inputs.append((position, input_str))
        
        self.logger.info(f"URLs: {len(url_inputs)}, PDFs: {len(pdf_inputs)}, Markdown: {len(markdown_inputs)}")
        
        # Process all inputs
        all_results = []
        
        # Process URLs (can be done concurrently)
        if url_inputs:
            url_results = await self._process_urls(url_inputs)
            all_results.extend(url_results)
        
        # Process PDFs (sequential for resource management)
        if pdf_inputs:
            pdf_results = await self._process_pdfs(pdf_inputs)
            all_results.extend(pdf_results)
        
        # Process markdown files (fast, can be concurrent)
        if markdown_inputs:
            markdown_results = await self._process_markdown_files(markdown_inputs)
            all_results.extend(markdown_results)
        
        # Sort results by position to maintain tuple order
        all_results.sort(key=lambda x: x.position)
        
        # Create concatenated document
        concatenated_file = await self._create_mixed_content_document(all_results)
        
        # Calculate statistics
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        successful_results = [r for r in all_results if r.success]
        failed_results = [r for r in all_results if not r.success]
        
        stats = {
            "total_inputs": len(self.validated_inputs),
            "successful": len(successful_results),
            "failed": len(failed_results),
            "success_rate": len(successful_results) / len(self.validated_inputs) if self.validated_inputs else 0,
            "duration_seconds": duration,
            "inputs_per_second": len(successful_results) / duration if duration > 0 else 0,
            "concatenated_file": str(concatenated_file),
            "results_by_type": {
                "urls": len([r for r in successful_results if r.input_type == InputType.URL]),
                "pdfs": len([r for r in successful_results if r.input_type == InputType.PDF]),
                "markdown": len([r for r in successful_results if r.input_type == InputType.MARKDOWN])
            }
        }
        
        self.logger.info(f"Multi-input processing completed in {duration:.1f} seconds!")
        self.logger.info(f"Success rate: {stats['success_rate']:.1%}")
        self.logger.info(f"Speed: {stats['inputs_per_second']:.1f} inputs/second")
        
        return stats
    
    async def _process_urls(self, url_inputs: List[Tuple[int, str]]) -> List[ProcessingResult]:
        """Process URL inputs using existing FastOrderedCrawler functionality."""
        results = []
        
        # Use existing concurrent crawling capability
        urls = [url for _, url in url_inputs]
        url_positions = {url: pos for pos, url in url_inputs}
        
        if len(urls) == 1:
            # Single URL - use existing method
            content = await self.crawl_with_optimized_selector(urls[0])
            if content:
                title = self.extract_title_from_content(content)
                description = self.extract_description_from_content(content)
                
                metadata = create_processing_metadata(
                    source=urls[0],
                    input_type=InputType.URL,
                    position=url_positions[urls[0]],
                    title=title,
                    description=description,
                    success=True
                )
                
                results.append(ProcessingResult(
                    success=True,
                    position=url_positions[urls[0]],
                    input_type=InputType.URL,
                    source=urls[0],
                    content=content,
                    metadata=metadata.__dict__
                ))
        else:
            # Multiple URLs - use existing concurrent crawling
            # This is more complex and would require adapting the existing crawl_all_concurrent method
            # For now, process sequentially
            for url in urls:
                content = await self.crawl_with_optimized_selector(url)
                if content:
                    title = self.extract_title_from_content(content)
                    description = self.extract_description_from_content(content)
                    
                    metadata = create_processing_metadata(
                        source=url,
                        input_type=InputType.URL,
                        position=url_positions[url],
                        title=title,
                        description=description,
                        success=True
                    )
                    
                    results.append(ProcessingResult(
                        success=True,
                        position=url_positions[url],
                        input_type=InputType.URL,
                        source=url,
                        content=content,
                        metadata=metadata.__dict__
                    ))
        
        return results
    
    async def _process_pdfs(self, pdf_inputs: List[Tuple[int, str]]) -> List[ProcessingResult]:
        """Process PDF inputs sequentially."""
        results = []
        
        for position, pdf_source in pdf_inputs:
            result = await self.pdf_processor.process_pdf(pdf_source, position)
            results.append(result)
        
        return results
    
    async def _process_markdown_files(self, markdown_inputs: List[Tuple[int, str]]) -> List[ProcessingResult]:
        """Process markdown files (can be concurrent due to fast I/O)."""
        results = []
        
        # Process concurrently since markdown processing is fast
        tasks = []
        for position, file_path in markdown_inputs:
            task = self.markdown_processor.process_markdown(file_path, position)
            tasks.append(task)
        
        if tasks:
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Handle any exceptions
            processed_results = []
            for i, result in enumerate(results):
                if isinstance(result, Exception):
                    position, file_path = markdown_inputs[i]
                    error_result = ProcessingResult(
                        success=False,
                        position=position,
                        input_type=InputType.MARKDOWN,
                        source=file_path,
                        error_message=str(result)
                    )
                    processed_results.append(error_result)
                else:
                    processed_results.append(result)
            
            results = processed_results
        
        return results
    
    async def _create_mixed_content_document(self, results: List[ProcessingResult]) -> Path:
        """Create concatenated document from mixed input results."""
        # Sort by position to maintain tuple order
        ordered_results = sorted(results, key=lambda x: x.position)
        
        # Generate TOC
        toc_lines = ["# Multi-Input Document Compilation", "", "## Table of Contents", ""]
        
        for i, result in enumerate(ordered_results, 1):
            if result.success:
                title = result.metadata.get('title', 'Untitled') if result.metadata else 'Untitled'
                indicator = result.source_indicator
                toc_lines.append(f"{i}. {indicator} [{title}](#{self._create_anchor(title)}) - {result.type_description}")
            else:
                toc_lines.append(f"{i}. ❌ Failed: {result.source} - {result.error_message or 'Unknown error'}")
        
        toc_lines.extend(["", "---", ""])
        
        # Assemble content
        content_lines = []
        
        for i, result in enumerate(ordered_results, 1):
            if result.success and result.content:
                # Add section header
                title = result.metadata.get('title', 'Untitled') if result.metadata else 'Untitled'
                content_lines.extend([
                    f"## {result.source_indicator} {title}",
                    "",
                    f"**Source**: {result.source}",
                    f"**Type**: {result.type_description}",
                    f"**Position**: {result.position + 1}",
                    f"**Processing Time**: {result.processing_time:.2f}s",
                    "",
                    "---",
                    "",
                    result.content,
                    "",
                    "---",
                    ""
                ])
            elif not result.success:
                # Add error section
                content_lines.extend([
                    f"## ❌ Failed: {result.source}",
                    "",
                    f"**Type**: {result.type_description}",
                    f"**Position**: {result.position + 1}",
                    f"**Error**: {result.error_message or 'Unknown error'}",
                    "",
                    "---",
                    ""
                ])
        
        # Combine TOC and content
        final_content = "\n".join(toc_lines + content_lines)
        
        # Save to file
        output_file = self.output_dir / "multi_input_compilation.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        return output_file
    
    def _create_anchor(self, title: str) -> str:
        """Create URL anchor from title."""
        import re
        anchor = re.sub(r'[^\w\s-]', '', title.lower())
        anchor = re.sub(r'[-\s]+', '-', anchor)
        return anchor.strip('-')
    
    async def crawl(self) -> Dict[str, Any]:
        """
        Main crawling method - enhanced for multi-input support.
        
        Maintains backward compatibility while supporting mixed inputs.
        """
        if self.is_single_url:
            # Single URL - use parent class method for full compatibility
            return await super().crawl()
        else:
            # Multi-input processing
            return await self.process_input_tuple()
    
    def cleanup(self):
        """Clean up temporary resources."""
        if hasattr(self, 'pdf_processor'):
            self.pdf_processor.cleanup()


# Convenience function for creating processor
def create_multi_input_processor(
    input_data: Union[str, Tuple[str, ...]],
    output_dir: str = "multi_input_crawl",
    max_concurrent: int = 10,
    **kwargs
) -> MultiInputProcessor:
    """
    Create a multi-input processor.
    
    Args:
        input_data: Single URL or tuple of mixed inputs (URLs, PDFs, markdown files)
        output_dir: Output directory
        max_concurrent: Maximum concurrent operations
        **kwargs: Additional arguments
        
    Returns:
        MultiInputProcessor instance
    """
    return MultiInputProcessor(
        input_data=input_data,
        output_dir=output_dir,
        max_concurrent=max_concurrent,
        **kwargs
    )