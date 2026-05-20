import time
import argparse
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn, TimeRemainingColumn
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
import os

console = Console()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_timer(minutes: int, session_type: str, color: str):
    seconds = minutes * 60
    
    title = Text(f"🍅 {session_type} Session 🍅", style=f"bold {color}")
    panel = Panel(Align.center(title), border_style=color, padding=(1, 2))
    
    clear_terminal()
    console.print(panel)
    console.print()
    
    with Progress(
        SpinnerColumn(spinner_name="dots", style=color),
        TextColumn(f"[{color}]{session_type}..."),
        BarColumn(complete_style=color, finished_style="green"),
        TaskProgressColumn(),
        TimeRemainingColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("Working...", total=seconds)
        
        while not progress.finished:
            time.sleep(1)
            progress.update(task, advance=1)
            
    console.print()
    console.print(f"[{color} bold]✨ Session Complete! ✨[/]")
    time.sleep(1)

def main():
    parser = argparse.ArgumentParser(description="Terminal Pomodoro Timer")
    parser.add_argument("-w", "--work", type=int, default=25, help="Work duration in minutes")
    parser.add_argument("-b", "--break_time", type=int, default=5, help="Break duration in minutes")
    parser.add_argument("-c", "--cycles", type=int, default=4, help="Number of cycles")
    
    args = parser.parse_args()
    
    try:
        for cycle in range(1, args.cycles + 1):
            console.rule(f"[bold cyan]Cycle {cycle}/{args.cycles}[/]")
            run_timer(args.work, "Focus", "red")
            
            if cycle < args.cycles:
                run_timer(args.break_time, "Break", "blue")
            else:
                run_timer(args.break_time * 3, "Long Break", "magenta")
                
        console.rule("[bold green]🎉 All Cycles Complete! Great job! 🎉[/]")
        
    except KeyboardInterrupt:
        console.print("\n[bold red]Timer stopped by user.[/]")

if __name__ == "__main__":
    main()
