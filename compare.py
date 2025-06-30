import os
import json
from rich.console import Console
from rich.table import Table

SNAPSHOT_DIR = "snapshots"
console = Console()

def load_snapshot(filename):
    path = os.path.join(SNAPSHOT_DIR, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Snapshot file '{filename}' not found in '{SNAPSHOT_DIR}/'")
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def compare_snapshots(snap1_file, snap2_file):
    console.print(f"\n[bold cyan]Comparing snapshots:[/bold cyan] {snap1_file} ⟷ {snap2_file}\n")

    snap1 = load_snapshot(snap1_file)
    snap2 = load_snapshot(snap2_file)

    files1 = set(snap1.keys())
    files2 = set(snap2.keys())

    added = files2 - files1
    removed = files1 - files2
    modified = []

    for path in files1 & files2:
        file1 = snap1[path]
        file2 = snap2[path]
        if file1["sha256"] != file2["sha256"] or file1["size"] != file2["size"]:
            modified.append(path)

    def print_list(title, items, color):
        if items:
            console.print(f"\n[bold {color}]{title} ({len(items)}):[/bold {color}]")
            for item in sorted(items):
                console.print(f"• {item}")
        else:
            console.print(f"\n[dim]{title}: none[/dim]")

    print_list("🟢 Added files", added, "green")
    print_list("🔴 Removed files", removed, "red")
    print_list("🟡 Modified files", modified, "yellow")

    if not (added or removed or modified):
        console.print("\n[bold green]✅ No differences found. Snapshots are identical.[/bold green]")

