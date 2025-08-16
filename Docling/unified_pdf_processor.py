"""
Unified PDF Processor

Provides a standardized interface for high-quality PDF processing with AI-enhanced 
markdown generation across all application entry points (Streamlit, CLI, MCP server).

This module wraps the enhanced_markdown_processor and provides:
- Consistent output directory structures
- AI-powered figure summarization
- High-quality table and figure extraction
- Unified configuration management
- Progress tracking and error handling
"""

import os
import time
import logging
import tempfile
from pathlib import Path
from typing import Dict, List, Optional, Union, Tuple, Any
from dataclasses import dataclass, asdict
import shutil

# Import enhanced processing components
from .enhanced_markdown_processor import create_enhanced_processor, ProcessingResult
from ..utils.pdf_parser import ProcessingConfig
from .document_storage import DocumentStorage

# Configuration
from ..config import get_config, get_processing_config

logger = logging.getLogger(__name__)


@dataclass
class UnifiedProcessingConfig:
    """Unified configuration for all PDF processing operations."""
    
    # Output directories
    parsed_output_dir: str = "./parsed_output"
    markdown_output_dir: str = "./parsed_output"  # Aligned with parsed_output for consistency
    create_subdirectories: bool = False  # Simplified: only main markdown files
    
    # AI processing settings
    enable_ai_summarization: bool = False  # No summary files
    
    # Quality settings
    image_scale: float = 3.0
    image_dpi: int = 900
    
    # Processing features
    enable_table_structure: bool = True
    enable_formula_enrichment: bool = True
    enable_picture_classification: bool = True
    
    # Performance settings
    max_workers: int = 4
    batch_size: int = 10
    timeout_seconds: int = None
    
    # Output formats
    generate_markdown: bool = True
    generate_json: bool = False  # Simplified: disable JSON output
    generate_chunks: bool = True
    save_figures: bool = False  # Simplified: disable figure saving
    save_tables: bool = False   # Simplified: disable table saving
    
    def __post_init__(self):
        """Validate and set defaults for configuration."""
        # Load timeout from configuration if not provided
        if self.timeout_seconds is None:
            processing_config = get_processing_config()
            self.timeout_seconds = processing_config['processing']['max_processing_time']
        
        # Create output directories
        Path(self.parsed_output_dir).mkdir(parents=True, exist_ok=True)
        Path(self.markdown_output_dir).mkdir(parents=True, exist_ok=True)
        
        # Validate ranges
        if self.image_scale <= 0 or self.image_scale > 10:
            raise ValueError("image_scale must be between 0.1 and 10.0")
        if self.image_dpi < 50 or self.image_dpi > 1200:
            raise ValueError("image_dpi must be between 50 and 1200")


@dataclass
class ProcessingStats:
    """Statistics from PDF processing operations."""
    files_processed: int = 0
    files_successful: int = 0
    files_failed: int = 0
    total_pages: int = 0
    total_figures: int = 0
    total_tables: int = 0
    total_formulas: int = 0
    ai_summaries_generated: int = 0
    total_processing_time: float = 0.0
    markdown_files_created: int = 0
    
    @property
    def success_rate(self) -> float:
        """Calculate success rate as percentage."""
        if self.files_processed == 0:
            return 0.0
        return (self.files_successful / self.files_processed) * 100


@dataclass
class UnifiedProcessingResult:
    """Result from unified PDF processing operation."""
    success: bool
    stats: ProcessingStats
    output_directory: Path
    processed_files: List[Dict[str, Any]]
    error_message: Optional[str] = None
    error_details: Optional[str] = None
    
    def get_markdown_files(self) -> List[Path]:
        """Get list of generated markdown files."""
        markdown_files = []
        for file_info in self.processed_files:
            if file_info.get('markdown_path'):
                markdown_files.append(Path(file_info['markdown_path']))
        return markdown_files
    
    def get_figure_directories(self) -> List[Path]:
        """Get list of figure directories."""
        figure_dirs = []
        for file_info in self.processed_files:
            if file_info.get('figures_dir'):
                figure_dirs.append(Path(file_info['figures_dir']))
        return figure_dirs


class UnifiedPDFProcessor:
    """
    Unified PDF processor that provides consistent high-quality processing
    across all application interfaces.
    """
    
    def __init__(self, config: UnifiedProcessingConfig):
        """
        Initialize the unified processor.
        
        Args:
            config: Processing configuration
        """
        self.config = config
        self.logger = logging.getLogger(f"{__name__}.UnifiedPDFProcessor")
        
        # Initialize statistics
        self.stats = ProcessingStats()
        
        # Create output directory structure
        self._setup_output_directories()
    
    def _setup_output_directories(self):
        """Create the standard output directory structure."""
        base_dir = Path(self.config.parsed_output_dir)
        base_dir.mkdir(parents=True, exist_ok=True)
        
        if self.config.create_subdirectories:
            # Create standard subdirectories
            for subdir in ['figures', 'tables', 'metadata']:
                (base_dir / subdir).mkdir(exist_ok=True)
    
    def process_single_pdf(
        self, 
        pdf_path: Union[str, Path],
        output_name: Optional[str] = None
    ) -> Tuple[bool, Dict[str, Any]]:
        """
        Process a single PDF file with enhanced markdown generation.
        
        Args:
            pdf_path: Path to the PDF file
            output_name: Optional custom output name (without extension)
            
        Returns:
            Tuple of (success, file_info_dict)
        """
        pdf_path = Path(pdf_path)
        start_time = time.time()
        
        # Generate output paths
        if output_name:
            base_name = output_name
        else:
            base_name = pdf_path.stem
        
        output_dir = Path(self.config.parsed_output_dir)
        
        # Create document-specific directory if configured
        if self.config.create_subdirectories:
            doc_dir = output_dir / base_name
            doc_dir.mkdir(exist_ok=True)
        else:
            doc_dir = output_dir
        
        file_info = {
            'input_path': str(pdf_path),
            'base_name': base_name,
            'output_dir': str(doc_dir),
            'success': False,
            'error_message': None,
            'processing_time': 0.0,
            'pages': 0,
            'figures': 0,
            'tables': 0,
            'formulas': 0,
            'ai_summaries': 0,
            'markdown_path': None,
            'json_path': None,
            'chunks_path': None,
            'figures_dir': None,
            'tables_dir': None
        }
        
        try:
            self.logger.info(f"Processing PDF: {pdf_path.name}")
            
            # Create temporary directory for enhanced processor
            with tempfile.TemporaryDirectory() as temp_dir:
                # Get AI configuration from config.toml
                config = get_config()
                ai_config = config.get('ai', {})
                ollama_config = ai_config.get('ollama', {})
                
                # Initialize enhanced processor
                processor = create_enhanced_processor(
                    output_dir=temp_dir,
                    final_markdown_dir=str(doc_dir),
                    ollama_host=ollama_config.get('host', 'http://localhost:11434'),
                    ollama_model=ollama_config.get('models', {}).get('vision_model', 'qwen2.5vl:7b'),
                    ollama_timeout=ollama_config.get('timeout', 120.0),
                    enable_ai_summarization=self.config.enable_ai_summarization,
                    image_scale=self.config.image_scale,
                    image_dpi=self.config.image_dpi
                )
                
                # Process the PDF
                result = processor.process_pdf(pdf_path)
                
                if result.success:
                    # Update file info with results
                    file_info.update({
                        'success': True,
                        'processing_time': result.processing_time,
                        'pages': result.pages_processed,
                        'figures': result.figures_extracted,
                        'tables': result.tables_extracted,
                        'ai_summaries': result.ai_summaries_generated,
                        'figures_metadata': [
                            {
                                'figure_id': fig.figure_id,
                                'page_number': fig.page_number,
                                'caption': fig.caption,
                                'figure_type': fig.figure_type,
                                'file_path': fig.file_path,
                                'ai_summary': fig.ai_summary
                            }
                            for fig in result.figures_metadata
                        ],
                        'tables_metadata': [
                            {
                                'table_id': table.table_id,
                                'page_number': table.page_number,
                                'caption': table.caption,
                                'table_markdown': table.table_markdown,
                                'row_count': table.row_count,
                                'column_count': table.column_count,
                                'section_title': table.section_title,
                                'table_index': table.table_index
                            }
                            for table in result.tables_metadata
                        ]
                    })
                    
                    # Set up output paths
                    markdown_path = doc_dir / f"{base_name}.md"
                    json_path = doc_dir / f"{base_name}.json"
                    chunks_path = doc_dir / f"{base_name}_chunks.json"
                    
                    # Also save to markdown_files directory for easy access
                    markdown_files_dir = Path(self.config.markdown_output_dir)
                    markdown_files_path = markdown_files_dir / f"{base_name}.md"
                    
                    # Copy/move files to final locations
                    if result.final_markdown_path and Path(result.final_markdown_path).exists():
                        # Copy to both locations
                        shutil.copy2(result.final_markdown_path, markdown_path)
                        shutil.copy2(result.final_markdown_path, markdown_files_path)
                        file_info['markdown_path'] = str(markdown_path)
                        file_info['markdown_files_path'] = str(markdown_files_path)
                    
                    # Handle figures and tables
                    if result.figures_extracted > 0:
                        figures_dir = doc_dir / 'figures'
                        figures_dir.mkdir(exist_ok=True)
                        file_info['figures_dir'] = str(figures_dir)
                        
                        # Copy figure files from temp directory
                        temp_figures = Path(temp_dir) / 'figures'
                        if temp_figures.exists():
                            for figure_file in temp_figures.iterdir():
                                if figure_file.is_file():
                                    shutil.copy2(figure_file, figures_dir / figure_file.name)
                    
                    if result.tables_extracted > 0:
                        tables_dir = doc_dir / 'tables'
                        tables_dir.mkdir(exist_ok=True)
                        file_info['tables_dir'] = str(tables_dir)
                    
                    # Update statistics
                    self.stats.files_successful += 1
                    self.stats.total_pages += result.pages_processed
                    self.stats.total_figures += result.figures_extracted
                    self.stats.total_tables += result.tables_extracted
                    self.stats.ai_summaries_generated += result.ai_summaries_generated
                    if markdown_path.exists():
                        self.stats.markdown_files_created += 1
                    
                    self.logger.info(f"Successfully processed {pdf_path.name}")
                    
                else:
                    # Handle processing failure
                    file_info['error_message'] = result.error_message
                    self.stats.files_failed += 1
                    self.logger.error(f"Failed to process {pdf_path.name}: {result.error_message}")
        
        except Exception as e:
            file_info['error_message'] = str(e)
            self.stats.files_failed += 1
            self.logger.error(f"Exception processing {pdf_path.name}: {e}")
        
        finally:
            file_info['processing_time'] = time.time() - start_time
            self.stats.files_processed += 1
            self.stats.total_processing_time += file_info['processing_time']
        
        return file_info['success'], file_info
    
    def process_directory(
        self, 
        input_dir: Union[str, Path],
        file_pattern: str = "*.pdf"
    ) -> UnifiedProcessingResult:
        """
        Process all PDF files in a directory.
        
        Args:
            input_dir: Directory containing PDF files
            file_pattern: File pattern to match (default: "*.pdf")
            
        Returns:
            UnifiedProcessingResult with processing statistics and file info
        """
        input_dir = Path(input_dir)
        start_time = time.time()
        
        # Reset statistics
        self.stats = ProcessingStats()
        processed_files = []
        
        try:
            # Find PDF files
            pdf_files = list(input_dir.glob(file_pattern))
            if not pdf_files:
                self.logger.warning(f"No PDF files found in {input_dir}")
                return UnifiedProcessingResult(
                    success=True,
                    stats=self.stats,
                    output_directory=Path(self.config.parsed_output_dir),
                    processed_files=[],
                    error_message="No PDF files found"
                )
            
            self.logger.info(f"Found {len(pdf_files)} PDF files to process")
            
            # Process each PDF file
            for pdf_file in pdf_files:
                success, file_info = self.process_single_pdf(pdf_file)
                processed_files.append(file_info)
                
                # Log progress
                progress = (len(processed_files) / len(pdf_files)) * 100
                self.logger.info(f"Progress: {progress:.1f}% ({len(processed_files)}/{len(pdf_files)})")
            
            # Calculate final statistics
            self.stats.total_processing_time = time.time() - start_time
            
            self.logger.info(f"Processing complete. Success rate: {self.stats.success_rate:.1f}%")
            
            return UnifiedProcessingResult(
                success=True,
                stats=self.stats,
                output_directory=Path(self.config.parsed_output_dir),
                processed_files=processed_files
            )
        
        except Exception as e:
            self.logger.error(f"Error processing directory {input_dir}: {e}")
            return UnifiedProcessingResult(
                success=False,
                stats=self.stats,
                output_directory=Path(self.config.parsed_output_dir),
                processed_files=processed_files,
                error_message=str(e)
            )


def create_unified_processor(
    parsed_output_dir: str = "./parsed_output",
    markdown_output_dir: Optional[str] = None,
    enable_ai_summarization: bool = None,
    openai_api_key: Optional[str] = None,
    **kwargs
) -> UnifiedPDFProcessor:
    """
    Convenience function to create a unified PDF processor.
    
    Args:
        parsed_output_dir: Directory for processed output
        enable_ai_summarization: Enable AI figure summarization
        openai_api_key: OpenAI API key
        **kwargs: Additional configuration options
        
    Returns:
        UnifiedPDFProcessor instance
    """
    # Determine AI summarization setting
    if enable_ai_summarization is None:
        # Auto-detect based on API key availability
        api_key = openai_api_key or os.getenv('OPENAI_API_KEY')
        enable_ai_summarization = bool(api_key)
    
    # Set markdown output directory from environment if not provided
    if markdown_output_dir is None:
        markdown_output_dir = os.getenv('MARKDOWN_PATH', './parsed_output')
    
    config = UnifiedProcessingConfig(
        parsed_output_dir=parsed_output_dir,
        markdown_output_dir=markdown_output_dir,
        enable_ai_summarization=enable_ai_summarization,
        openai_api_key=openai_api_key,
        **kwargs
    )
    
    return UnifiedPDFProcessor(config)


if __name__ == "__main__":
    # Example usage
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python unified_pdf_processor.py <pdf_path_or_directory>")
        sys.exit(1)
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    input_path = Path(sys.argv[1])
    
    # Create processor
    processor = create_unified_processor(
        parsed_output_dir="./parsed_output",
        enable_ai_summarization=True
    )
    
    # Process input
    if input_path.is_file():
        success, file_info = processor.process_single_pdf(input_path)
        print(f"Processing {'successful' if success else 'failed'}")
        if success:
            print(f"Markdown: {file_info.get('markdown_path', 'Not created')}")
            print(f"Figures: {file_info.get('figures', 0)}")
            print(f"Tables: {file_info.get('tables', 0)}")
    else:
        result = processor.process_directory(input_path)
        print(f"Processed {result.stats.files_processed} files")
        print(f"Success rate: {result.stats.success_rate:.1f}%")
        print(f"Markdown files created: {result.stats.markdown_files_created}")
        print(f"Total figures: {result.stats.total_figures}")
        print(f"Total tables: {result.stats.total_tables}")
        print(f"AI summaries: {result.stats.ai_summaries_generated}")