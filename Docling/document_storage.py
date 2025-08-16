"""
Document Storage Module with Supabase Integration

This module provides functionality to store processed documents, chunks, tables,
and figures in Supabase with OpenAI embeddings for vector similarity search.

Key Features:
- Batch operations for efficient storage
- OpenAI embedding generation (text-embedding-3-small)
- Error handling and retry logic
- Connection pooling and transaction management
- Integration with existing pdf_hashes table
- Support for hybrid search (vector + full-text)
"""

import logging
import asyncio
import time
import os
from typing import List, Dict, Any, Optional, Union, Tuple
from dataclasses import dataclass
from pathlib import Path
import json
import hashlib
import uuid
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

try:
    from supabase import create_client, Client
    SUPABASE_AVAILABLE = True
except ImportError:
    create_client = None
    Client = None
    SUPABASE_AVAILABLE = False

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    openai = None
    OPENAI_AVAILABLE = False

# Import our custom types
from ..utils.metadata_extractor import DocumentMetadata
from ..utils.document_chunker import DocumentChunk, ChunkMetadata

logger = logging.getLogger(__name__)


@dataclass
class StorageResult:
    """Result of a storage operation."""
    
    success: bool
    document_id: Optional[str] = None
    chunks_stored: int = 0
    tables_stored: int = 0
    figures_stored: int = 0
    error_message: Optional[str] = None
    processing_time: float = 0.0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            'success': self.success,
            'document_id': self.document_id,
            'chunks_stored': self.chunks_stored,
            'tables_stored': self.tables_stored,
            'figures_stored': self.figures_stored,
            'error_message': self.error_message,
            'processing_time': self.processing_time
        }


@dataclass
class EmbeddingConfig:
    """Configuration for embedding generation."""
    
    model: str = "text-embedding-3-small"
    dimensions: Optional[int] = 1536
    batch_size: int = 50
    
    def __post_init__(self):
        """Validate configuration after initialization."""
        if self.model == "text-embedding-3-small" and self.dimensions:
            if self.dimensions not in [512, 1024, 1536]:
                raise ValueError("text-embedding-3-small supports dimensions: 512, 1024, 1536")
        
        if self.batch_size <= 0:
            raise ValueError("batch_size must be positive")


class EmbeddingGenerator:
    """
    Generate embeddings using OpenAI's text-embedding-3-small model.
    
    This class handles batching, rate limiting, and error handling for
    embedding generation with OpenAI's API.
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = None,
        batch_size: int = 100,
        max_retries: int = 3,
        retry_delay: float = 1.0,
        dimensions: Optional[int] = None
    ):
        """
        Initialize the embedding generator.
        
        Args:
            api_key: OpenAI API key (if None, uses environment variable)
            model: Embedding model to use (defaults to text-embedding-3-small)
            batch_size: Number of texts to embed in one API call
            max_retries: Maximum number of retries on failure
            retry_delay: Delay between retries in seconds
            dimensions: Optional dimensions for embeddings (text-embedding-3-small supports 512, 1024, 1536)
        """
        # Get model from environment or use default
        self.model = model or os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
        self.batch_size = batch_size
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        
        # Get dimensions from environment or use default (1536 for compatibility)
        self.dimensions = dimensions or int(os.getenv("EMBEDDING_DIMENSIONS", "1536"))
        
        self.logger = logging.getLogger(__name__)
        
        # Initialize OpenAI client
        if OPENAI_AVAILABLE:
            # Get API key from parameter or environment
            api_key = api_key or os.getenv("OPENAI_API_KEY")
            if not api_key:
                self.logger.error("No OpenAI API key provided. Set OPENAI_API_KEY environment variable.")
                self.client = None
                return
                
            try:
                # Use the newer OpenAI client initialization
                from openai import OpenAI
                self.client = OpenAI(api_key=api_key)
                self.logger.info(f"OpenAI embedding generator initialized with model: {self.model}, dimensions: {self.dimensions}")
            except Exception as e:
                self.logger.error(f"Failed to initialize OpenAI client: {e}")
                self.client = None
        else:
            self.logger.error("OpenAI library not available")
            self.client = None
    
    def generate_embedding(self, text: str) -> Optional[List[float]]:
        """
        Generate embedding for a single text.
        
        Args:
            text: Text to embed
            
        Returns:
            Embedding vector or None if failed
        """
        if not self.client:
            return None
        
        # Clean and truncate text if necessary
        text = self._clean_text(text)
        if not text:
            return None
        
        for attempt in range(self.max_retries):
            try:
                # Prepare parameters for the API call
                params = {
                    "input": text,
                    "model": self.model
                }
                
                # Add dimensions parameter if using text-embedding-3-small
                if self.model == "text-embedding-3-small" and self.dimensions != 1536:
                    params["dimensions"] = self.dimensions
                
                response = self.client.embeddings.create(**params)
                return response.data[0].embedding
                
            except Exception as e:
                self.logger.warning(f"Embedding generation attempt {attempt + 1} failed: {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay * (2 ** attempt))  # Exponential backoff
                else:
                    self.logger.error(f"Failed to generate embedding after {self.max_retries} attempts")
        
        return None
    
    def generate_embeddings_batch(self, texts: List[str]) -> List[Optional[List[float]]]:
        """
        Generate embeddings for multiple texts in batches.
        
        Args:
            texts: List of texts to embed
            
        Returns:
            List of embedding vectors (None for failed embeddings)
        """
        if not self.client:
            return [None] * len(texts)
        
        embeddings = []
        
        # Process in batches
        for i in range(0, len(texts), self.batch_size):
            batch = texts[i:i + self.batch_size]
            batch_embeddings = self._generate_batch(batch)
            embeddings.extend(batch_embeddings)
        
        return embeddings
    
    def _generate_batch(self, texts: List[str]) -> List[Optional[List[float]]]:
        """Generate embeddings for a single batch."""
        # Clean texts
        cleaned_texts = [self._clean_text(text) for text in texts]
        valid_texts = [text for text in cleaned_texts if text]
        
        if not valid_texts:
            return [None] * len(texts)
        
        for attempt in range(self.max_retries):
            try:
                # Prepare parameters for the API call
                params = {
                    "input": valid_texts,
                    "model": self.model
                }
                
                # Add dimensions parameter if using text-embedding-3-small
                if self.model == "text-embedding-3-small" and self.dimensions != 1536:
                    params["dimensions"] = self.dimensions
                
                response = self.client.embeddings.create(**params)
                
                # Map embeddings back to original text positions
                embeddings = []
                valid_idx = 0
                
                for text in cleaned_texts:
                    if text:
                        embeddings.append(response.data[valid_idx].embedding)
                        valid_idx += 1
                    else:
                        embeddings.append(None)
                
                return embeddings
                
            except Exception as e:
                self.logger.warning(f"Batch embedding attempt {attempt + 1} failed: {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay * (2 ** attempt))
                else:
                    self.logger.error(f"Failed to generate batch embeddings after {self.max_retries} attempts")
        
        return [None] * len(texts)
    
    def _clean_text(self, text: str) -> str:
        """Clean and prepare text for embedding."""
        if not text:
            return ""
        
        # Remove excessive whitespace
        cleaned = ' '.join(text.split())
        
        # Truncate if too long (OpenAI has token limits)
        max_chars = 8000  # Conservative estimate for token limit
        if len(cleaned) > max_chars:
            cleaned = cleaned[:max_chars]
            self.logger.warning(f"Text truncated to {max_chars} characters for embedding")
        
        return cleaned


class DocumentStorage:
    """
    Handle document storage operations with Supabase.
    
    This class manages the storage of processed documents, their chunks,
    tables, and figures with proper embedding generation and error handling.
    """
    
    def __init__(
        self,
        supabase_url: str,
        supabase_key: str,
        openai_api_key: Optional[str] = None,
        embedding_model: str = None,
        batch_size: int = 50,
        embedding_dimensions: Optional[int] = None
    ):
        """
        Initialize the document storage handler.
        
        Args:
            supabase_url: Supabase project URL
            supabase_key: Supabase API key
            openai_api_key: OpenAI API key for embeddings
            embedding_model: OpenAI embedding model to use (defaults to text-embedding-3-small)
            batch_size: Batch size for database operations
            embedding_dimensions: Optional dimensions for embeddings
        """
        self.batch_size = batch_size
        self.logger = logging.getLogger(__name__)
        
        # Initialize Supabase client
        if SUPABASE_AVAILABLE:
            try:
                self.supabase = create_client(supabase_url, supabase_key)
                self.logger.info("Supabase client initialized")
            except Exception as e:
                self.logger.error(f"Failed to initialize Supabase client: {e}")
                self.supabase = None
        else:
            self.logger.error("Supabase library not available")
            self.supabase = None
        
        # Initialize embedding generator
        self.embedding_generator = EmbeddingGenerator(
            api_key=openai_api_key,
            model=embedding_model,
            batch_size=batch_size,
            dimensions=embedding_dimensions
        )
    
    def store_document_complete(
        self,
        metadata: DocumentMetadata,
        chunks: List[DocumentChunk],
        tables: List[Dict[str, Any]] = None,
        figures: List[Dict[str, Any]] = None,
        file_path: str = "",
        file_hash: str = ""
    ) -> StorageResult:
        """
        Store a complete document with all its components.
        
        Args:
            metadata: Document metadata
            chunks: List of document chunks
            tables: List of table data (optional)
            figures: List of figure data (optional)
            file_path: Original file path
            file_hash: SHA-256 hash of the file
            
        Returns:
            StorageResult with operation details
        """
        start_time = time.time()
        
        if not self.supabase:
            return StorageResult(
                success=False,
                error_message="Supabase client not available",
                processing_time=time.time() - start_time
            )
        
        try:
            # 1. Store document metadata
            document_id = self._store_document_metadata(metadata, file_path, file_hash)
            if not document_id:
                return StorageResult(
                    success=False,
                    error_message="Failed to store document metadata",
                    processing_time=time.time() - start_time
                )
            
            # 2. Store chunks with embeddings
            chunks_stored = self._store_chunks(document_id, chunks)
            
            # 3. Store tables if provided
            tables_stored = 0
            if tables:
                tables_stored = self._store_tables(document_id, tables)
            
            # 4. Store figures if provided
            figures_stored = 0
            if figures:
                figures_stored = self._store_figures(document_id, figures)
            
            # 5. Update document status
            self._update_document_status(document_id, 'completed')
            
            processing_time = time.time() - start_time
            
            self.logger.info(
                f"Document {document_id} stored successfully: "
                f"{chunks_stored} chunks, {tables_stored} tables, {figures_stored} figures "
                f"in {processing_time:.2f}s"
            )
            
            return StorageResult(
                success=True,
                document_id=document_id,
                chunks_stored=chunks_stored,
                tables_stored=tables_stored,
                figures_stored=figures_stored,
                processing_time=processing_time
            )
            
        except Exception as e:
            self.logger.error(f"Error storing document: {e}")
            return StorageResult(
                success=False,
                error_message=str(e),
                processing_time=time.time() - start_time
            )
    
    def _store_document_metadata(
        self, 
        metadata: DocumentMetadata, 
        file_path: str, 
        file_hash: str
    ) -> Optional[str]:
        """Store document metadata and return document ID."""
        try:
            # Prepare simplified document data with only non-null fields
            document_data = {
                'file_path': file_path,
                'page_count': metadata.page_count,
                'processing_status': 'processing',
                'metadata': metadata.to_dict(),
                'download_source': metadata.download_source,
                'url_verified': metadata.url_verified
            }
            
            # Add file hash if provided and exists in pdf_hashes table
            if file_hash:
                document_data['file_hash'] = file_hash
            
            # Insert document
            result = self.supabase.table('documents').insert(document_data).execute()
            
            if result.data:
                document_id = result.data[0]['id']
                self.logger.info(f"Document metadata stored with ID: {document_id}")
                return document_id
            else:
                self.logger.error("No document ID returned from insert")
                return None
                
        except Exception as e:
            self.logger.error(f"Error storing document metadata: {e}")
            return None
    
    def _store_chunks(self, document_id: str, chunks: List[DocumentChunk]) -> int:
        """Store document chunks with embeddings."""
        if not chunks:
            return 0
        
        try:
            # Prepare texts for embedding
            texts_for_embedding = []
            chunk_data = []
            
            for chunk in chunks:
                # Use enriched content if available, otherwise use regular content
                embedding_text = chunk.enriched_content or chunk.content
                texts_for_embedding.append(embedding_text)
                
                # Prepare chunk data
                chunk_record = {
                    'document_id': document_id,
                    'content': chunk.content,
                    'chunk_type': chunk.metadata.chunk_type,
                    'chunk_index': chunk.metadata.chunk_index,
                    'section_hierarchy': chunk.metadata.section_hierarchy,
                    'token_count': chunk.metadata.token_count,
                    'page_numbers': chunk.metadata.page_numbers,
                    'metadata': chunk.metadata.to_dict()
                }
                chunk_data.append(chunk_record)
            
            # Generate embeddings in batches
            self.logger.info(f"Generating embeddings for {len(texts_for_embedding)} chunks")
            embeddings = self.embedding_generator.generate_embeddings_batch(texts_for_embedding)
            
            # Add embeddings to chunk data
            for i, embedding in enumerate(embeddings):
                if embedding:
                    chunk_data[i]['embedding'] = embedding
                else:
                    self.logger.warning(f"No embedding generated for chunk {i}")
            
            # Store chunks in batches
            chunks_stored = 0
            for i in range(0, len(chunk_data), self.batch_size):
                batch = chunk_data[i:i + self.batch_size]
                
                result = self.supabase.table('document_chunks').insert(batch).execute()
                
                if result.data:
                    chunks_stored += len(result.data)
                else:
                    self.logger.warning(f"Batch {i//self.batch_size + 1} insert returned no data")
            
            self.logger.info(f"Stored {chunks_stored} chunks for document {document_id}")
            return chunks_stored
            
        except Exception as e:
            self.logger.error(f"Error storing chunks: {e}")
            return 0
    
    def _store_tables(self, document_id: str, tables: List[Dict[str, Any]]) -> int:
        """Store document tables with embeddings."""
        if not tables:
            return 0
        
        try:
            # Prepare table data and texts for embedding
            texts_for_embedding = []
            table_data = []
            
            for i, table in enumerate(tables):
                # Create embedding text from table content
                embedding_text = ""
                if table.get('table_markdown'):
                    embedding_text += table['table_markdown']
                elif table.get('markdown'):
                    embedding_text += table['markdown']
                if table.get('context'):
                    embedding_text += f"\nContext: {table['context']}"
                
                texts_for_embedding.append(embedding_text)
                
                # Prepare table record
                table_record = {
                    'document_id': document_id,
                    'table_markdown': table.get('table_markdown', '') or table.get('markdown', ''),
                    'table_context': table.get('context'),
                    'section_title': table.get('section_title'),
                    'page_number': table.get('page_number'),
                    'table_index': i,
                    'row_count': table.get('row_count', 0),
                    'column_count': table.get('column_count', 0),
                    'metadata': table.get('metadata', {})
                }
                table_data.append(table_record)
            
            # Generate embeddings
            self.logger.info(f"Generating embeddings for {len(tables)} tables")
            embeddings = self.embedding_generator.generate_embeddings_batch(texts_for_embedding)
            
            # Add embeddings to table data
            for i, embedding in enumerate(embeddings):
                if embedding:
                    table_data[i]['embedding'] = embedding
            
            # Store tables
            result = self.supabase.table('document_tables').insert(table_data).execute()
            
            tables_stored = len(result.data) if result.data else 0
            self.logger.info(f"Stored {tables_stored} tables for document {document_id}")
            return tables_stored
            
        except Exception as e:
            self.logger.error(f"Error storing tables: {e}")
            return 0
    
    def _store_figures(self, document_id: str, figures: List[Dict[str, Any]]) -> int:
        """Store document figures with embeddings."""
        if not figures:
            return 0
        
        try:
            # Prepare figure data and texts for embedding
            texts_for_embedding = []
            figure_data = []
            
            for i, figure in enumerate(figures):
                # Prepare figure record (no embeddings for figures after cleanup)
                figure_record = {
                    'document_id': document_id,
                    'section_title': figure.get('section_title'),
                    'page_number': figure.get('page_number'),
                    'figure_index': i,
                    'extracted_data': figure.get('extracted_data'),
                    'metadata': figure.get('metadata', {})
                }
                figure_data.append(figure_record)
            
            # Store figures
            result = self.supabase.table('document_figures').insert(figure_data).execute()
            
            figures_stored = len(result.data) if result.data else 0
            self.logger.info(f"Stored {figures_stored} figures for document {document_id}")
            return figures_stored
            
        except Exception as e:
            self.logger.error(f"Error storing figures: {e}")
            return 0
    
    def _update_document_status(self, document_id: str, status: str) -> bool:
        """Update document processing status."""
        try:
            result = self.supabase.table('documents').update({
                'processing_status': status,
                'updated_at': 'now()'
            }).eq('id', document_id).execute()
            
            return bool(result.data)
            
        except Exception as e:
            self.logger.error(f"Error updating document status: {e}")
            return False
    
    def store_processing_result(
        self, 
        processing_info: Dict[str, Any], 
        document_id: str, 
        file_hash: str
    ) -> StorageResult:
        """
        Store processing results from UnifiedPDFProcessor in the database.
        
        Args:
            processing_info: Processing result from UnifiedPDFProcessor
            document_id: Document ID in database
            file_hash: SHA-256 hash of the file
            
        Returns:
            StorageResult with operation details
        """
        start_time = time.time()
        
        try:
            self.logger.info(f"Storing processing results for document {document_id}")
            
            # Extract basic info
            file_path = processing_info.get('input_path', '')
            base_name = processing_info.get('base_name', '')
            pages = processing_info.get('pages', 0)
            figures_count = processing_info.get('figures', 0)
            tables_count = processing_info.get('tables', 0)
            
            # Create basic document metadata if we don't have detailed structure
            metadata = DocumentMetadata(
                title=base_name,
                page_count=pages,
                file_size_bytes=0,  # Not available from processing_info
                extraction_method="unified_pdf_processor",
                processing_status="processing"
            )
            
            # Generate document chunks using StructureAwareChunker
            chunks = []
            markdown_path = processing_info.get('markdown_path')
            # Convert relative path to absolute
            if markdown_path and not Path(markdown_path).is_absolute():
                markdown_path = Path.cwd() / markdown_path
            if markdown_path and Path(markdown_path).exists():
                try:
                    # Read the markdown content
                    with open(markdown_path, 'r', encoding='utf-8') as f:
                        markdown_content = f.read()
                    
                    # Use StructureAwareChunker for intelligent chunking
                    from ..utils.document_chunker import StructureAwareChunker
                    
                    chunker = StructureAwareChunker(
                        chunk_size=int(os.getenv('CHUNK_SIZE', '512')),
                        chunk_overlap=int(os.getenv('CHUNK_OVERLAP', '50')),
                        tokenizer_name="tiktoken",
                        respect_section_boundaries=True,
                        preserve_tables=True,
                        preserve_formulas=True,
                        min_chunk_size=50,
                        max_chunk_size=1000
                    )
                    
                    # Try to use Docling document if available, otherwise use plain text
                    if processing_info.get('docling_document'):
                        chunks = chunker.chunk_document(
                            doc=processing_info['docling_document'],
                            document_id=base_name
                        )
                        self.logger.info(f"Generated {len(chunks)} chunks using Docling document structure")
                    else:
                        # Fallback to text-based chunking
                        chunks = chunker.chunk_text(
                            text=markdown_content,
                            document_id=base_name
                        )
                        self.logger.info(f"Generated {len(chunks)} chunks using text-based chunking")
                        
                except Exception as e:
                    self.logger.warning(f"Could not process markdown for chunking: {e}")
            
            # Process figures if available - prefer figures_metadata if provided
            figures = []
            if processing_info.get('figures_metadata'):
                try:
                    figures_metadata = processing_info['figures_metadata']
                    for i, fig_meta in enumerate(figures_metadata):
                        # Use the detailed figure metadata from processing
                        figure_data = {
                            'figure_caption': fig_meta.get('caption'),
                            'figure_description': fig_meta.get('ai_summary', f"Extracted figure from {base_name}"),
                            'figure_type': fig_meta.get('figure_type', 'unknown'),
                            'section_title': '',
                            'page_number': fig_meta.get('page_number', 1),
                            'figure_index': i,
                            'extracted_data': {
                                'figure_id': fig_meta.get('figure_id'),
                                'file_path': fig_meta.get('file_path'),
                                'bbox': fig_meta.get('bbox'),
                            },
                            'metadata': {
                                'processing_source': 'unified_pdf_processor',
                                'ai_summary_generated': bool(fig_meta.get('ai_summary'))
                            }
                        }
                        figures.append(figure_data)
                    
                    self.logger.info(f"Prepared {len(figures)} figures from metadata for storage")
                except Exception as e:
                    self.logger.warning(f"Could not process figures metadata: {e}")
            else:
                # Fallback: look for figure files in directory
                figures_dir = processing_info.get('figures_dir')
                # Convert relative path to absolute
                if figures_dir and not Path(figures_dir).is_absolute():
                    figures_dir = Path.cwd() / figures_dir
                if figures_dir and Path(figures_dir).exists():
                    try:
                        figure_files = list(Path(figures_dir).glob('*.png'))
                        for i, fig_file in enumerate(figure_files):
                            figure_data = {
                                'figure_caption': f"Figure {i+1}",
                                'figure_description': f"Extracted figure from {base_name}",
                                'figure_type': 'unknown',
                                'section_title': '',
                                'page_number': 1,
                                'figure_index': i,
                                'extracted_data': {'file_path': str(fig_file)},
                                'metadata': {'processing_source': 'unified_pdf_processor'}
                            }
                            figures.append(figure_data)
                        
                        self.logger.info(f"Prepared {len(figures)} figures from directory for storage")
                    except Exception as e:
                        self.logger.warning(f"Could not process figures directory: {e}")
            
            # Process tables if available in processing_info  
            tables = []
            if hasattr(processing_info, 'get') and processing_info.get('tables_metadata'):
                try:
                    tables_metadata = processing_info['tables_metadata']
                    for table_meta in tables_metadata:
                        table_data = {
                            'table_markdown': table_meta.get('table_markdown', ''),
                            'caption': table_meta.get('caption'),
                            'section_title': table_meta.get('section_title', ''),
                            'row_count': table_meta.get('row_count', 0),
                            'column_count': table_meta.get('column_count', 0),
                            'page_number': table_meta.get('page_number', 1),
                            'table_index': table_meta.get('table_index', 0),
                            'context': f"Table {table_meta.get('table_id', 'unknown')} from {base_name}"
                        }
                        tables.append(table_data)
                    
                    self.logger.info(f"Prepared {len(tables)} tables with structured data for storage")
                except Exception as e:
                    self.logger.warning(f"Could not process table metadata: {e}")
            elif tables_count > 0:
                self.logger.info(f"Document has {tables_count} tables, but structured data not available yet")
            
            # Store chunks, tables, and figures for existing document
            chunks_stored = 0
            tables_stored = 0
            figures_stored = 0
            
            try:
                # Store chunks with embeddings
                if chunks:
                    chunks_stored = self._store_chunks(document_id, chunks)
                    self.logger.info(f"Stored {chunks_stored} chunks for document {document_id}")
                
                # Store tables if provided
                if tables:
                    tables_stored = self._store_tables(document_id, tables)
                    self.logger.info(f"Stored {tables_stored} tables for document {document_id}")
                
                # Store figures if provided
                if figures:
                    figures_stored = self._store_figures(document_id, figures)
                    self.logger.info(f"Stored {figures_stored} figures for document {document_id}")
                
                # Create a successful result
                result = StorageResult(
                    success=True,
                    document_id=document_id,
                    chunks_stored=chunks_stored,
                    tables_stored=tables_stored,
                    figures_stored=figures_stored,
                    processing_time=0,  # Will be set below
                    error_message=None
                )
                
            except Exception as e:
                self.logger.error(f"Error storing document components: {e}")
                result = StorageResult(
                    success=False,
                    document_id=document_id,
                    error_message=f"Storage error: {str(e)}",
                    processing_time=0
                )
            
            # Update document with processing stats
            if result.success and result.document_id:
                try:
                    self.supabase.table('documents').update({
                        'page_count': pages,
                        'processing_status': 'completed',
                        'updated_at': 'now()'
                    }).eq('id', document_id).execute()
                    
                    self.logger.info(f"Updated document {document_id} with page count: {pages}")
                except Exception as e:
                    self.logger.warning(f"Could not update document page count: {e}")
            
            processing_time = time.time() - start_time
            self.logger.info(f"Processing result storage completed in {processing_time:.2f}s")
            
            return StorageResult(
                success=result.success,
                document_id=result.document_id,
                chunks_stored=result.chunks_stored,
                tables_stored=result.tables_stored,
                figures_stored=result.figures_stored,
                processing_time=processing_time,
                error_message=result.error_message
            )
            
        except Exception as e:
            error_msg = f"Error storing processing result: {e}"
            self.logger.error(error_msg)
            return StorageResult(
                success=False,
                error_message=error_msg,
                processing_time=time.time() - start_time
            )
    
    def search_documents(
        self, 
        query: str, 
        limit: int = 10,
        match_threshold: float = 0.7,
        search_type: str = 'hybrid'
    ) -> List[Dict[str, Any]]:
        """
        Search documents using vector similarity and/or full-text search.
        
        Args:
            query: Search query
            limit: Maximum number of results
            match_threshold: Minimum similarity threshold
            search_type: 'vector', 'text', or 'hybrid'
            
        Returns:
            List of matching document chunks
        """
        if not self.supabase:
            return []
        
        try:
            # Generate query embedding for vector search
            query_embedding = None
            if search_type in ['vector', 'hybrid']:
                query_embedding = self.embedding_generator.generate_embedding(query)
                if not query_embedding:
                    self.logger.warning("Failed to generate query embedding, falling back to text search")
                    search_type = 'text'
            
            if search_type == 'vector' and query_embedding:
                # Vector similarity search only
                result = self.supabase.rpc(
                    'search_document_chunks',
                    {
                        'query_embedding': query_embedding,
                        'match_threshold': match_threshold,
                        'match_count': limit
                    }
                ).execute()
                
            elif search_type == 'text':
                # Full-text search only - using ilike for compatibility
                result = self.supabase.from_('document_chunks').select(
                    '*, documents(title)'
                ).ilike(
                    'content', f'%{query}%'
                ).limit(limit).execute()
                
            elif search_type == 'hybrid' and query_embedding:
                # Hybrid search using the stored function
                result = self.supabase.rpc(
                    'search_document_chunks',
                    {
                        'query_embedding': query_embedding,
                        'search_text': query,
                        'match_threshold': match_threshold,
                        'match_count': limit
                    }
                ).execute()
            else:
                return []
            
            return result.data if result.data else []
            
        except Exception as e:
            self.logger.error(f"Error searching documents: {e}")
            return []
    
    def search_and_format_prompt(
        self,
        query: str,
        limit: int = 5,
        match_threshold: float = 0.7,
        search_type: str = 'hybrid',
        max_context_length: int = 4000
    ) -> Dict[str, Any]:
        """
        Search documents and format results into a structured prompt for AI agents.
        
        This method combines document search with prompt engineering best practices
        to create ready-to-use prompts for systems like Pydantic AI.
        
        Args:
            query: Search query
            limit: Maximum number of results to include
            match_threshold: Minimum similarity threshold for results
            search_type: 'vector', 'text', or 'hybrid'
            max_context_length: Maximum character length for context section
            
        Returns:
            Dict with formatted prompt, metadata, and source information:
            {
                "prompt": "Complete formatted prompt ready for AI agent",
                "context_count": 3,
                "max_similarity": 0.89,
                "sources": ["Doc1", "Doc2", "Doc3"],
                "truncated": False
            }
        """
        # Search for relevant documents
        search_results = self.search_documents(
            query=query,
            limit=limit,
            match_threshold=match_threshold,
            search_type=search_type
        )
        
        if not search_results:
            return {
                "prompt": f"""I don't have any relevant information in my knowledge base to answer the question: "{query}"

Please provide more context or rephrase your question, or search for documents that might contain relevant information.""",
                "context_count": 0,
                "max_similarity": 0.0,
                "sources": [],
                "truncated": False
            }
        
        # Format context sections
        context_parts = []
        sources = []
        max_similarity = 0.0
        current_length = 0
        truncated = False
        
        for i, result in enumerate(search_results, 1):
            # Track maximum similarity score
            similarity = result.get('similarity', 0.0)
            if similarity > max_similarity:
                max_similarity = similarity
            
            # Format source citation (simplified since we no longer have document titles)
            source_citation = f"[Source {i}: Document {result.get('document_id', 'Unknown')}]"
            
            # Get content
            content = result.get('content', '').strip()
            
            # Check if adding this content would exceed length limit
            new_content = f"{source_citation}\n{content}\n\n"
            if current_length + len(new_content) > max_context_length and len(context_parts) > 0:
                truncated = True
                break
            
            context_parts.append(new_content)
            sources.append(f"Document {result.get('document_id', 'Unknown')}")
            current_length += len(new_content)
        
        # Build the complete prompt
        context_section = "".join(context_parts).strip()
        
        prompt = f"""Based on the following research findings, answer the question accurately and comprehensively:

CONTEXT:
{context_section}

QUESTION: {query}

INSTRUCTIONS:
- Provide a precise answer based on the context above
- Cite sources using [Source X] format when referencing specific information
- If the context doesn't fully answer the question, clearly state what information is missing
- Maintain academic rigor and accuracy

ANSWER:"""
        
        return {
            "prompt": prompt,
            "context_count": len(context_parts),
            "max_similarity": round(max_similarity, 3),
            "sources": list(dict.fromkeys(sources)),  # Remove duplicates while preserving order
            "truncated": truncated
        }

    def get_document_status(self, file_hash: str) -> Optional[str]:
        """Check if a document has already been processed."""
        if not self.supabase:
            return None
        
        try:
            result = self.supabase.table('documents').select(
                'processing_status'
            ).eq('file_hash', file_hash).execute()
            
            if result.data:
                return result.data[0]['processing_status']
            else:
                return None
                
        except Exception as e:
            self.logger.error(f"Error checking document status: {e}")
            return None
    
    def store_structured_metadata(
        self, 
        document_id: str,
        metadata: Dict[str, Any]
    ) -> bool:
        """
        Store structured metadata for a document.
        
        Args:
            document_id: Database document ID
            metadata: Dictionary of structured metadata fields
            
        Returns:
            bool: Success status
        """
        if not self.supabase:
            self.logger.error("Supabase client not available")
            return False
        
        try:
            self.logger.info(f"Storing structured metadata for document {document_id}")
            
            # Prepare the update data with only non-None values
            update_data = {}
            
            # Core metadata fields
            if metadata.get('title'):
                update_data['title'] = metadata['title']
            if metadata.get('doi'):
                update_data['doi'] = metadata['doi']
            if metadata.get('pmid'):
                update_data['pmid'] = metadata['pmid']
            if metadata.get('arxiv_id'):
                update_data['arxiv_id'] = metadata['arxiv_id']
            if metadata.get('publication_year'):
                update_data['publication_year'] = metadata['publication_year']
            if metadata.get('publication_type'):
                update_data['publication_type'] = metadata['publication_type']
            
            # Author information (as JSONB)
            if metadata.get('authors'):
                update_data['authors'] = metadata['authors']
            if metadata.get('corresponding_author'):
                update_data['corresponding_author'] = metadata['corresponding_author']
            
            # Journal information (as JSONB)
            if metadata.get('journal'):
                update_data['journal'] = metadata['journal']
            
            # Content fields
            if metadata.get('abstract'):
                update_data['abstract'] = metadata['abstract']
            if metadata.get('keywords'):
                update_data['keywords'] = metadata['keywords']
            if metadata.get('subject_areas'):
                update_data['subject_areas'] = metadata['subject_areas']
            if metadata.get('research_domains'):
                update_data['research_domains'] = metadata['research_domains']
            
            # Citation information
            if metadata.get('citation_count') is not None:
                update_data['citation_count'] = metadata['citation_count']
            if metadata.get('references_count') is not None:
                update_data['references_count'] = metadata['references_count']
            
            # Additional metadata
            if metadata.get('language'):
                update_data['language'] = metadata['language']
            if metadata.get('license'):
                update_data['license'] = metadata['license']
            
            # Domain-specific fields for liquid biopsy research
            if metadata.get('technology'):
                update_data['technology'] = metadata['technology']
            if metadata.get('cancer_type'):
                update_data['cancer_type'] = metadata['cancer_type']
            
            # Update extraction status
            update_data['structured_extraction_status'] = 'completed'
            update_data['structured_metadata_extracted_at'] = 'now()'
            
            # Perform the update
            result = self.supabase.table('documents').update(
                update_data
            ).eq('id', document_id).execute()
            
            if result.data:
                self.logger.info(f"Successfully stored structured metadata for document {document_id}")
                
                # Log key extracted information
                tech_count = len(metadata.get('technology', []))
                cancer_count = len(metadata.get('cancer_type', []))
                self.logger.info(f"Extracted: title='{metadata.get('title', 'N/A')[:50]}...', "
                               f"year={metadata.get('publication_year', 'N/A')}, "
                               f"technologies={tech_count}, cancer_types={cancer_count}")
                
                return True
            else:
                self.logger.error(f"No data returned when updating structured metadata for document {document_id}")
                return False
                
        except Exception as e:
            self.logger.error(f"Error storing structured metadata for document {document_id}: {e}")
            
            # Try to update status to failed
            try:
                self.supabase.table('documents').update({
                    'structured_extraction_status': 'failed'
                }).eq('id', document_id).execute()
            except:
                pass  # Don't fail the main operation if status update fails
            
            return False
    
    def store_publication_type(self, document_id: str, classification_data: Dict[str, Any]) -> bool:
        """
        Store publication type classification results for a document.
        
        Args:
            document_id: Document ID to update
            classification_data: Dictionary containing classification results
                - publication_type: Category (Review, Clinical Research, etc.)
                - publication_type_confidence: Confidence score (0.0-1.0)
                - publication_type_keywords: List of keywords
                - publication_type_reasoning: Reasoning explanation
                
        Returns:
            bool: True if storage successful, False otherwise
        """
        if not self.supabase:
            self.logger.error("No Supabase client available for publication type storage")
            return False
        
        try:
            self.logger.info(f"Storing publication type classification for document {document_id}")
            
            # Prepare update data with validation
            update_data = {
                'publication_type': classification_data.get('publication_type'),
                'publication_type_confidence': float(classification_data.get('publication_type_confidence', 0.0)),
                'publication_type_keywords': classification_data.get('publication_type_keywords', []),
                'publication_type_reasoning': classification_data.get('publication_type_reasoning', ''),
                'publication_type_status': 'completed'
            }
            
            # Validate required fields
            if not update_data['publication_type']:
                self.logger.error("Publication type is required but not provided")
                return False
            
            # Validate category against allowed values
            allowed_categories = {
                'Review', 'Clinical Research', 'Case Report', 
                'Health Economic Publication', 'Other'
            }
            if update_data['publication_type'] not in allowed_categories:
                self.logger.warning(f"Invalid publication type '{update_data['publication_type']}', defaulting to 'Other'")
                update_data['publication_type'] = 'Other'
                update_data['publication_type_confidence'] = max(0.0, update_data['publication_type_confidence'] - 0.3)
            
            # Validate confidence range
            confidence = update_data['publication_type_confidence']
            if confidence < 0.0 or confidence > 1.0:
                self.logger.warning(f"Invalid confidence score {confidence}, clamping to [0.0, 1.0]")
                update_data['publication_type_confidence'] = max(0.0, min(1.0, confidence))
            
            # Ensure keywords is a list
            if not isinstance(update_data['publication_type_keywords'], list):
                update_data['publication_type_keywords'] = []
            
            # Limit keywords to reasonable number
            if len(update_data['publication_type_keywords']) > 10:
                update_data['publication_type_keywords'] = update_data['publication_type_keywords'][:10]
                self.logger.info("Truncated keywords list to 10 items")
            
            # Limit reasoning text length
            if len(update_data['publication_type_reasoning']) > 1000:
                update_data['publication_type_reasoning'] = update_data['publication_type_reasoning'][:1000]
                self.logger.info("Truncated reasoning text to 1000 characters")
            
            # Update document with publication type classification
            result = self.supabase.table('documents').update(update_data).eq('id', document_id).execute()
            
            if result.data:
                self.logger.info(f"Successfully stored publication type classification for document {document_id}")
                
                # Log classification details
                category = update_data['publication_type']
                confidence = update_data['publication_type_confidence']
                keyword_count = len(update_data['publication_type_keywords'])
                
                self.logger.info(f"Classification: category='{category}', confidence={confidence:.2f}, "
                               f"keywords={keyword_count}, reasoning_length={len(update_data['publication_type_reasoning'])}")
                
                return True
            else:
                self.logger.error(f"No data returned when updating publication type for document {document_id}")
                return False
                
        except Exception as e:
            self.logger.error(f"Error storing publication type for document {document_id}: {e}")
            
            # Try to update status to failed
            try:
                self.supabase.table('documents').update({
                    'publication_type_status': 'failed'
                }).eq('id', document_id).execute()
            except:
                pass  # Don't fail the main operation if status update fails
            
            return False


def create_document_storage(
    supabase_url: str,
    supabase_key: str,
    openai_api_key: Optional[str] = None
) -> DocumentStorage:
    """
    Convenience function to create a DocumentStorage instance.
    
    Args:
        supabase_url: Supabase project URL
        supabase_key: Supabase API key
        openai_api_key: OpenAI API key for embeddings
        
    Returns:
        DocumentStorage instance
    """
    return DocumentStorage(
        supabase_url=supabase_url,
        supabase_key=supabase_key,
        openai_api_key=openai_api_key
    )