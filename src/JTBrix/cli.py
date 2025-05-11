"""Console script for JTBrix."""
import subprocess
import typer
from rich.console import Console

app = typer.Typer()
console = Console()

@app.command()
def main():
    """Runs the Flask app defined in app.py"""
    console.print("[bold green]Starting the JTBrix app...[/bold green]")
    subprocess.run(["python", "src/JTBrix/app.py"])

if __name__ == "__main__":
    app()