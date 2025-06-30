import os
import hashlib
import json
from pathlib import Path
from datetime import datetime
from rich.console import Console
from utils import compute_file_hash

console = Console()
SNAPSHOT_DIR = "snapshots"

def take_snapshot(directory_path):
    directory = Path(directory_path)
    if not directory.exists() or not directory.is_dir():
        console.print(f"[red]Error: Directory '{directory_path}' does not exist or is not a folder.[/red]")
        return

    snapshot = {}
    console.print(f"\n[bold]Scanning directory:[/bold] {directory.resolve()}\n")

    for file_path in directory.rglob('*'):
        if file_path.is_file():
            rel_path = str(file_path.relative_to(directory))
            try:
                file_info = {
                    "size": file_path.stat().st_size,
                    "modified": file_path.stat().st_mtime,
                    "sha256": compute_file_hash(file_path)
                }
                snapshot[rel_path] = file_info
            except Exception as e:
                console.print(f"[yellow]Warning: Failed to process '{file_path}': {e}[/yellow]")

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    snapshot_filename = f"snapshot_{timestamp}.json"
    snapshot_path = os.path.join(SNAPSHOT_DIR, snapshot_filename)

    with open(snapshot_path, 'w', encoding='utf-8') as f:
        json.dump(snapshot, f, indent=2)

    console.print(f"[green]Snapshot saved as:[/green] {snapshot_filename}")
    return snapshot_filename
