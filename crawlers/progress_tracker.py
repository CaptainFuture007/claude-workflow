"""
Progress Tracker - Comprehensive progress tracking for web crawling operations

Provides beautiful, real-time progress bars and status updates using the Rich library
for better user experience during long-running crawling operations.
"""

import time
from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass, field
from contextlib import contextmanager
from pathlib import Path

try:
    from rich.console import Console
    from rich.progress import (
        Progress, 
        TaskID, 
        BarColumn, 
        TextColumn, 
        TimeRemainingColumn, 
        TimeElapsedColumn,
        MofNCompleteColumn,
        SpinnerColumn,
        ProgressColumn
    )
    from rich.panel import Panel
    from rich.table import Table
    from rich.live import Live
    from rich.text import Text
    from rich.layout import Layout
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    # Fallback imports
    import sys


@dataclass
class ProgressStats:
    """Statistics for tracking crawling progress."""
    total_discovered: int = 0
    total_processed: int = 0
    successful: int = 0
    failed: int = 0
    skipped: int = 0
    current_url: str = ""
    stage: str = ""
    start_time: float = field(default_factory=time.time)
    
    @property
    def processing_rate(self) -> float:
        """Calculate processing rate in items per second."""
        elapsed = time.time() - self.start_time
        return self.total_processed / elapsed if elapsed > 0 else 0.0
    
    @property
    def success_rate(self) -> float:
        """Calculate success rate as percentage."""
        return (self.successful / self.total_processed * 100) if self.total_processed > 0 else 0.0
    
    @property
    def eta_seconds(self) -> Optional[float]:
        """Estimate time remaining in seconds."""
        if self.total_discovered > 0 and self.processing_rate > 0:
            remaining = self.total_discovered - self.total_processed
            return remaining / self.processing_rate
        return None


class SpeedColumn(ProgressColumn):
    """Custom column showing processing speed."""
    
    def render(self, task) -> Text:
        """Render the speed column."""
        speed = task.speed or 0
        if speed > 1:
            return Text(f"{speed:.1f} it/s", style="progress.data.speed")
        elif speed > 0:
            return Text(f"{1/speed:.1f}s/it", style="progress.data.speed")
        else:
            return Text("--", style="progress.data.speed")


class ProgressTracker:
    """
    Comprehensive progress tracking for web crawling operations.
    
    Features:
    - Multi-stage progress tracking
    - Real-time statistics
    - Beautiful Rich-based UI with fallback
    - Async-compatible progress updates
    """
    
    def __init__(self, console: Optional[Console] = None, enable_rich: bool = True):
        """
        Initialize the progress tracker.
        
        Args:
            console: Rich console instance (created if None)
            enable_rich: Whether to use Rich formatting (falls back if not available)
        """
        self.use_rich = RICH_AVAILABLE and enable_rich
        self.console = console or (Console() if self.use_rich else None)
        
        # Progress tracking
        self.stats = ProgressStats()
        self.active_tasks: Dict[str, TaskID] = {}
        self.stage_history: List[str] = []
        
        # Rich components
        if self.use_rich:
            self.progress = Progress(
                SpinnerColumn(),
                TextColumn("[bold blue]{task.description}"),
                BarColumn(),
                MofNCompleteColumn(),
                TextColumn("•"),
                TimeElapsedColumn(),
                TextColumn("•"),
                SpeedColumn(),
                TextColumn("•"),
                TimeRemainingColumn(),
                console=self.console,
                expand=True
            )
            self.live = None
        else:
            self.progress = None
    
    def start(self) -> 'ProgressTracker':
        """Start the progress tracker."""
        if self.use_rich:
            self.progress.start()
        return self
    
    def stop(self):
        """Stop the progress tracker."""
        if self.use_rich and self.progress:
            self.progress.stop()
        if self.live:
            self.live.stop()
    
    def __enter__(self) -> 'ProgressTracker':
        """Context manager entry."""
        return self.start()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.stop()
    
    def create_task(
        self, 
        name: str, 
        description: str, 
        total: Optional[int] = None,
        start: bool = True
    ) -> str:
        """
        Create a new progress task.
        
        Args:
            name: Unique task identifier
            description: Human-readable task description
            total: Total number of items to process (None for indefinite)
            start: Whether to start the task immediately
        
        Returns:
            Task identifier for updates
        """
        if self.use_rich:
            task_id = self.progress.add_task(
                description=description,
                total=total,
                start=start
            )
            self.active_tasks[name] = task_id
        else:
            self._fallback_log(f"Starting: {description}")
        
        return name
    
    def update_task(
        self,
        name: str,
        advance: int = 1,
        description: Optional[str] = None,
        total: Optional[int] = None,
        current_item: Optional[str] = None,
        **kwargs
    ):
        """
        Update an existing task's progress.
        
        Args:
            name: Task identifier
            advance: Number of items to advance by
            description: New description (optional)
            total: New total count (optional)
            current_item: Current item being processed
            **kwargs: Additional progress arguments
        """
        if current_item:
            self.stats.current_url = current_item
        
        if self.use_rich and name in self.active_tasks:
            task_id = self.active_tasks[name]
            
            update_kwargs = {"advance": advance}
            if description is not None:
                update_kwargs["description"] = description
            if total is not None:
                update_kwargs["total"] = total
            update_kwargs.update(kwargs)
            
            self.progress.update(task_id, **update_kwargs)
        else:
            if current_item:
                self._fallback_log(f"Processing: {current_item}")
    
    def complete_task(self, name: str, description: Optional[str] = None):
        """
        Mark a task as completed.
        
        Args:
            name: Task identifier
            description: Final description (optional)
        """
        if self.use_rich and name in self.active_tasks:
            task_id = self.active_tasks[name]
            if description:
                self.progress.update(task_id, description=description)
            self.progress.update(task_id, completed=True)
            # Don't remove the task - let it show as completed
        else:
            final_desc = description or f"Completed: {name}"
            self._fallback_log(f"✅ {final_desc}")
    
    def fail_task(self, name: str, error: str):
        """
        Mark a task as failed.
        
        Args:
            name: Task identifier
            error: Error description
        """
        if self.use_rich and name in self.active_tasks:
            task_id = self.active_tasks[name]
            self.progress.update(
                task_id, 
                description=f"[red]Failed: {error}[/red]"
            )
        else:
            self._fallback_log(f"❌ Failed: {error}")
    
    def update_stats(
        self,
        total_discovered: Optional[int] = None,
        total_processed: Optional[int] = None,
        successful: Optional[int] = None,
        failed: Optional[int] = None,
        skipped: Optional[int] = None,
        stage: Optional[str] = None
    ):
        """Update overall statistics."""
        if total_discovered is not None:
            self.stats.total_discovered = total_discovered
        if total_processed is not None:
            self.stats.total_processed = total_processed
        if successful is not None:
            self.stats.successful = successful
        if failed is not None:
            self.stats.failed = failed
        if skipped is not None:
            self.stats.skipped = skipped
        if stage is not None:
            self.stats.stage = stage
            self.stage_history.append(stage)
    
    def increment_stats(
        self,
        processed: int = 0,
        successful: int = 0,
        failed: int = 0,
        skipped: int = 0
    ):
        """Increment statistics counters."""
        self.stats.total_processed += processed
        self.stats.successful += successful
        self.stats.failed += failed
        self.stats.skipped += skipped
    
    def log(self, message: str, level: str = "info"):
        """
        Log a message with appropriate styling.
        
        Args:
            message: Message to log
            level: Log level (info, success, warning, error)
        """
        if self.use_rich:
            if level == "success":
                self.console.print(f"✅ {message}", style="green")
            elif level == "warning":
                self.console.print(f"⚠️  {message}", style="yellow")
            elif level == "error":
                self.console.print(f"❌ {message}", style="red")
            else:
                self.console.print(f"ℹ️  {message}")
        else:
            prefix = {"success": "✅", "warning": "⚠️", "error": "❌"}.get(level, "ℹ️")
            self._fallback_log(f"{prefix} {message}")
    
    def print_stage_header(self, stage: str, description: str = ""):
        """Print a formatted stage header."""
        self.stats.stage = stage
        
        if self.use_rich:
            header_text = f"🚀 {stage}"
            if description:
                header_text += f": {description}"
            
            panel = Panel(
                header_text,
                style="bold blue",
                padding=(0, 1)
            )
            self.console.print(panel)
        else:
            separator = "=" * 60
            self._fallback_log(f"\n{separator}")
            self._fallback_log(f"🚀 {stage}")
            if description:
                self._fallback_log(f"   {description}")
            self._fallback_log(separator)
    
    def print_summary(self):
        """Print a final summary of the crawling session."""
        elapsed = time.time() - self.stats.start_time
        
        if self.use_rich:
            # Create summary table
            table = Table(title="🏁 Crawling Session Summary", show_header=True)
            table.add_column("Metric", style="cyan", width=20)
            table.add_column("Value", style="magenta")
            
            table.add_row("Total Discovered", str(self.stats.total_discovered))
            table.add_row("Total Processed", str(self.stats.total_processed))
            table.add_row("Successful", f"[green]{self.stats.successful}[/green]")
            table.add_row("Failed", f"[red]{self.stats.failed}[/red]")
            table.add_row("Skipped", f"[yellow]{self.stats.skipped}[/yellow]")
            table.add_row("Success Rate", f"{self.stats.success_rate:.1f}%")
            table.add_row("Processing Rate", f"{self.stats.processing_rate:.2f} items/sec")
            table.add_row("Total Time", f"{elapsed:.1f} seconds")
            
            self.console.print(table)
        else:
            self._fallback_log("\n" + "="*50)
            self._fallback_log("🏁 CRAWLING SESSION SUMMARY")
            self._fallback_log("="*50)
            self._fallback_log(f"Total Discovered: {self.stats.total_discovered}")
            self._fallback_log(f"Total Processed: {self.stats.total_processed}")
            self._fallback_log(f"✅ Successful: {self.stats.successful}")
            self._fallback_log(f"❌ Failed: {self.stats.failed}")
            self._fallback_log(f"⚠️  Skipped: {self.stats.skipped}")
            self._fallback_log(f"Success Rate: {self.stats.success_rate:.1f}%")
            self._fallback_log(f"Processing Rate: {self.stats.processing_rate:.2f} items/sec")
            self._fallback_log(f"Total Time: {elapsed:.1f} seconds")
            self._fallback_log("="*50)
    
    def _fallback_log(self, message: str):
        """Fallback logging when Rich is not available."""
        print(message, flush=True)
    
    @contextmanager
    def stage(self, name: str, description: str = ""):
        """
        Context manager for tracking a stage of work.
        
        Args:
            name: Stage name
            description: Stage description
        """
        self.print_stage_header(name, description)
        try:
            yield self
        finally:
            pass
    
    def create_subtask_tracker(self, name: str, description: str, total: int) -> 'SubTaskTracker':
        """
        Create a subtask tracker for fine-grained progress.
        
        Args:
            name: Subtask name
            description: Subtask description  
            total: Total items to process
        
        Returns:
            SubTaskTracker instance
        """
        task_id = self.create_task(name, description, total)
        return SubTaskTracker(self, task_id, name)


class SubTaskTracker:
    """Helper class for tracking subtasks."""
    
    def __init__(self, tracker: ProgressTracker, task_id: str, task_name: str):
        self.tracker = tracker
        self.task_id = task_id
        self.task_name = task_name
        self.processed = 0
    
    def update(self, advance: int = 1, current_item: str = "", **kwargs):
        """Update the subtask progress."""
        self.processed += advance
        self.tracker.update_task(
            self.task_name,
            advance=advance,
            current_item=current_item,
            **kwargs
        )
    
    def complete(self, description: Optional[str] = None):
        """Mark the subtask as completed."""
        self.tracker.complete_task(self.task_name, description)
    
    def fail(self, error: str):
        """Mark the subtask as failed."""
        self.tracker.fail_task(self.task_name, error)


# Convenience function for simple progress tracking
def create_progress_tracker(enable_rich: bool = True) -> ProgressTracker:
    """
    Create a progress tracker instance.
    
    Args:
        enable_rich: Whether to enable Rich formatting
    
    Returns:
        ProgressTracker instance
    """
    return ProgressTracker(enable_rich=enable_rich)