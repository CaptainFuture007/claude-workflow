"""
Simple Multi-Input Document Processor

A streamlined implementation that maintains Docling for PDF processing 
and async concurrency while following KISS principles.
"""

import asyncio
import time
from pathlib import Path
from typing import Union, Tuple, Dict, List, Any, Optional
from urllib.parse import urlparse
import tempfile
import shutil
import logging

# Keep essential dependencies for quality and performance
from docling.document_converter import DocumentConverter
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig

# Import our simplified type detection
from simple_input_types import detect_input_type, validate_inputs, validate_file_exists

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class SimpleMultiProcessor:
    """
    Simplified multi-input processor that maintains quality and performance
    while reducing architectural complexity.
    """
    
    def __init__(
        self, 
        output_dir: str = "./simple_output",
        max_concurrent: int = 10
    ):
        """
        Initialize the processor.
        
        Args:
            output_dir: Directory for output files
            max_concurrent: Maximum concurrent operations
        """
        self.output_dir = Path(output_dir)
        self.max_concurrent = max_concurrent
        self.temp_dir = None
        
        # Create output directory
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.content_dir = self.output_dir / "content"
        self.content_dir.mkdir(exist_ok=True)
        
        # Initialize Docling for high-quality PDF processing
        self.docling_converter = DocumentConverter()
        
        logger.info(f"SimpleMultiProcessor initialized with output_dir: {output_dir}")
    
    async def process_inputs(
        self, 
        inputs: Union[str, Tuple[str, ...]]
    ) -> Dict[str, Any]:
        """
        Process mixed inputs (URLs, PDFs, markdown files).
        
        Args:
            inputs: Single input string or tuple of input strings
            
        Returns:
            Dictionary with processing results and statistics
        """
        start_time = time.time()
        
        # Handle single input (backward compatibility)
        if isinstance(inputs, str):
            inputs = (inputs,)
        
        # Validate inputs
        try:
            validated_inputs = validate_inputs(inputs)
        except ValueError as e:
            return {"success": False, "error": str(e)}
        
        logger.info(f"Processing {len(validated_inputs)} inputs")
        
        # Create temporary directory for processing
        self.temp_dir = Path(tempfile.mkdtemp(prefix="simple_processor_"))
        
        try:
            # Process inputs concurrently with semaphore
            semaphore = asyncio.Semaphore(self.max_concurrent)
            tasks = [
                self._process_single(position, input_str, input_type, semaphore)
                for position, input_str, input_type in validated_inputs
            ]
            
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Separate successful results from exceptions
            successful_results = []
            failed_results = []
            
            for i, result in enumerate(results):
                if isinstance(result, Exception):
                    failed_results.append({
                        "position": validated_inputs[i][0],
                        "input": validated_inputs[i][1],
                        "error": str(result)
                    })
                else:
                    successful_results.append(result)
            
            # Generate concatenated document if we have successful results
            concatenated_file = None
            if successful_results:
                concatenated_file = await self._create_concatenated_document(successful_results)
            
            # Calculate statistics
            total_time = time.time() - start_time
            stats = {
                "total_inputs": len(validated_inputs),
                "successful": len(successful_results),
                "failed": len(failed_results),
                "duration_seconds": round(total_time, 2),
                "inputs_per_second": round(len(successful_results) / total_time, 2) if total_time > 0 else 0,
                "concatenated_file": str(concatenated_file) if concatenated_file else None,
                "output_directory": str(self.output_dir),
                "failed_inputs": failed_results if failed_results else None
            }
            
            logger.info(f"Processing complete: {stats['successful']}/{stats['total_inputs']} successful")
            
            return {
                "success": True,
                "stats": stats,
                "results": successful_results
            }
            
        finally:
            # Cleanup temporary directory
            if self.temp_dir and self.temp_dir.exists():
                shutil.rmtree(self.temp_dir)
    
    async def _process_single(
        self, 
        position: int, 
        input_str: str, 
        input_type: str, 
        semaphore: asyncio.Semaphore
    ) -> Dict[str, Any]:
        """Process a single input with concurrency control."""
        async with semaphore:
            start_time = time.time()
            
            try:
                if input_type == "pdf":
                    result = await self._process_pdf(input_str, position)
                elif input_type == "url":
                    result = await self._process_url(input_str, position)
                elif input_type == "markdown":
                    result = await self._process_markdown(input_str, position)
                else:
                    raise ValueError(f"Unsupported input type: {input_type}")
                
                processing_time = time.time() - start_time
                result["processing_time"] = round(processing_time, 2)
                
                logger.info(f"Processed {input_type} input {position + 1}: {input_str[:50]}...")
                return result
                
            except Exception as e:
                logger.error(f"Failed to process {input_str}: {str(e)}")
                raise e
    
    async def _process_pdf(self, pdf_path: str, position: int) -> Dict[str, Any]:
        """Process PDF using Docling for high quality."""
        # Handle PDF URLs by downloading first
        if pdf_path.startswith(('http://', 'https://')):
            pdf_path = await self._download_pdf(pdf_path)
        else:
            validate_file_exists(pdf_path)
        
        # Use Docling for high-quality PDF processing
        result = self.docling_converter.convert(pdf_path)
        content = result.document.export_to_markdown()
        
        # Extract title from document
        title = getattr(result.document, 'title', None) or f"PDF Document {position + 1}"
        
        # Save individual file
        filename = self._generate_filename(pdf_path, position, "pdf")
        output_path = self.content_dir / filename
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return {
            "position": position,
            "input_type": "pdf",
            "source": pdf_path,
            "title": title,
            "content": content,
            "output_file": str(output_path),
            "success": True
        }
    
    async def _process_url(self, url: str, position: int) -> Dict[str, Any]:
        """Process URL using Crawl4AI."""
        config = CrawlerRunConfig(
            only_text=True,
            word_count_threshold=10
        )
        
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url=url, config=config)
            
            if not result.success:
                raise Exception(f"Failed to crawl URL: {result.error_message}")
            
            content = result.markdown or result.cleaned_html or "No content extracted"
            title = result.metadata.get('title', f"Web Page {position + 1}")
            
            # Save individual file
            filename = self._generate_filename(url, position, "url")
            output_path = self.content_dir / filename
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return {
                "position": position,
                "input_type": "url",
                "source": url,
                "title": title,
                "content": content,
                "output_file": str(output_path),
                "success": True
            }
    
    async def _process_markdown(self, md_path: str, position: int) -> Dict[str, Any]:
        """Process markdown file."""
        validate_file_exists(md_path)
        
        path = Path(md_path)
        
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract title from first heading
        title = self._extract_title_from_markdown(content) or path.stem
        
        # Save individual file (copy to content directory)
        filename = self._generate_filename(md_path, position, "markdown")
        output_path = self.content_dir / filename
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return {
            "position": position,
            "input_type": "markdown",
            "source": md_path,
            "title": title,
            "content": content,
            "output_file": str(output_path),
            "success": True
        }
    
    async def _download_pdf(self, url: str) -> str:
        """Download PDF from URL to temporary location."""
        import aiohttp
        
        filename = f"downloaded_pdf_{int(time.time())}.pdf"
        temp_path = self.temp_dir / filename
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    raise Exception(f"Failed to download PDF: HTTP {response.status}")
                
                with open(temp_path, 'wb') as f:
                    async for chunk in response.content.iter_chunked(8192):
                        f.write(chunk)
        
        return str(temp_path)
    
    def _generate_filename(self, source: str, position: int, input_type: str) -> str:
        """Generate safe filename for output."""
        if input_type == "url":
            parsed = urlparse(source)
            base = f"{parsed.netloc}_{parsed.path}".replace('/', '_').replace('.', '-')
        else:
            base = Path(source).stem
        
        # Clean filename and add position prefix
        safe_base = ''.join(c for c in base if c.isalnum() or c in '-_')[:50]
        return f"pos{position:02d}_{safe_base}.md"
    
    def _extract_title_from_markdown(self, content: str) -> Optional[str]:
        """Extract title from markdown content."""
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('# '):
                return line[2:].strip()
        return None
    
    async def _create_concatenated_document(self, results: List[Dict[str, Any]]) -> Path:
        """Create concatenated document from all results."""
        # Sort results by position to maintain order
        results.sort(key=lambda x: x['position'])
        
        output_path = self.output_dir / "concatenated_document.md"
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("# Multi-Input Document Compilation\n\n")
            f.write(f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            # Table of contents
            f.write("## Table of Contents\n\n")
            for result in results:
                icon = {"pdf": "📄", "url": "🌐", "markdown": "📝"}.get(result['input_type'], "📄")
                f.write(f"{result['position'] + 1}. {icon} [{result['title']}](#{self._to_anchor(result['title'])}) - {result['input_type'].title()}\n")
            
            f.write("\n---\n\n")
            
            # Content sections
            for result in results:
                icon = {"pdf": "📄", "url": "🌐", "markdown": "📝"}.get(result['input_type'], "📄")
                f.write(f"## {icon} {result['title']}\n\n")
                f.write(f"**Source**: {result['source']}\n")
                f.write(f"**Type**: {result['input_type'].title()}\n")
                f.write(f"**Position**: {result['position'] + 1}\n\n")
                f.write(result['content'])
                f.write("\n\n---\n\n")
        
        return output_path
    
    def _to_anchor(self, title: str) -> str:
        """Convert title to markdown anchor."""
        return title.lower().replace(' ', '-').replace('.', '').replace(',', '')
    
    def cleanup(self):
        """Cleanup temporary resources."""
        if self.temp_dir and self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)


# Factory function for backward compatibility
def create_simple_processor(
    inputs: Union[str, Tuple[str, ...]], 
    output_dir: str = "./simple_output",
    max_concurrent: int = 10
) -> SimpleMultiProcessor:
    """
    Create a simple processor instance.
    
    Args:
        inputs: Input(s) to process (for configuration, actual processing happens later)
        output_dir: Output directory
        max_concurrent: Maximum concurrent operations
        
    Returns:
        Configured SimpleMultiProcessor instance
    """
    return SimpleMultiProcessor(output_dir=output_dir, max_concurrent=max_concurrent)


if __name__ == "__main__":
    # Example usage
    async def example():
        processor = SimpleMultiProcessor(output_dir="./example_output")
        
        # Example with mixed inputs
        inputs = (
            "https://docs.anthropic.com/en/docs/claude-code/overview",
            "./document.pdf",  # If it exists
            "./README.md"       # If it exists
        )
        
        try:
            result = await processor.process_inputs(inputs)
            print(f"Success: {result['success']}")
            if result['success']:
                stats = result['stats']
                print(f"Processed: {stats['successful']}/{stats['total_inputs']} inputs")
                print(f"Duration: {stats['duration_seconds']}s")
                print(f"Output: {stats['concatenated_file']}")
        finally:
            processor.cleanup()
    
    # Run example
    # asyncio.run(example())