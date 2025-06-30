import typer
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import os
import sys

from snapshot import take_snapshot
from compare import compare_snapshots
from utils import load_banner

app = typer.Typer()
console = Console()

SNAPSHOT_DIR = "snapshots"
os.makedirs(SNAPSHOT_DIR, exist_ok=True)

def interactive_mode():
    console.print(load_banner(), style="cyan")

    while True:
        console.print("\n[bold]What do you want to do?[/bold]")
        console.print("1. 📸 Take a directory snapshot")
        console.print("2. 🔍 Compare two snapshots")
        console.print("3. ❌ Exit")

        choice = Prompt.ask("Enter your choice (1/2/3 or 'exit')").strip().lower()

        if choice in ['3', 'exit', 'quit', 'q']:
            console.print("👋 Exiting. See you!")
            sys.exit()
        elif choice == '1':
            path = Prompt.ask("Enter the path to the folder to scan")
            if not os.path.isdir(path):
                console.print("[red]Invalid path. Please try again.[/red]")
                continue
            take_snapshot(path)
        elif choice == '2':
            snap1 = Prompt.ask("Enter the first snapshot filename (.json)")
            snap2 = Prompt.ask("Enter the second snapshot filename (.json)")
            try:
                compare_snapshots(snap1, snap2)
            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")
        else:
            console.print("[red]Invalid choice. Please select 1, 2, or 3.[/red]")

@app.command()
def snapshot(path: str):
    """Take a snapshot of a directory"""
    take_snapshot(path)

@app.command()
def compare(snap1: str, snap2: str):
    """Compare two snapshot files"""
    compare_snapshots(snap1, snap2)

@app.command()
def interactive():
    """Run the interactive terminal interface"""
    interactive_mode()

if __name__ == "__main__":
    app()
