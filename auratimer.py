import time
import argparse
import os
try:
    import winsound
except ImportError:
    winsound = None

from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn, TimeRemainingColumn
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.table import Table

console = Console()

ASCII_LOGO = """[cyan]
    ___                    VGltZXI=
   /   | __  ___________ _
  / /| |/ / / / ___/ __ `/
 / ___ / /_/ / /  / /_/ / 
/_/  |_\__,_/_/   \__,_/  
                          [magenta]Timer[/]
[/]"""

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_alert():
    if winsound:
        try:
            winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
        except:
            print("\a", end="")
    else:
        print("\a", end="")

def run_timer(minutes: int, session_type: str, color: str, task_name: str = None):
    seconds = minutes * 60
    
    header = Text()
    header.append(f"✦ {session_type} Session ✦\n", style=f"bold {color}")
    if task_name:
        header.append(f"Task: {task_name}", style="italic white")
        
    panel = Panel(Align.center(header), border_style=color, padding=(1, 2))
    
    clear_terminal()
    console.print(Align.center(ASCII_LOGO))
    console.print(panel)
    console.print()
    
    with Progress(
        SpinnerColumn(spinner_name="moon", style=color),
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
            
    play_alert()
    console.print()
    console.print(f"[{color} bold]✨ {session_type} Complete! ✨[/]")
    time.sleep(1.5)

def display_summary(work_mins: int, break_mins: int, cycles: int, task_name: str):
    clear_terminal()
    console.print(Align.center(ASCII_LOGO))
    
    total_work = work_mins * cycles
    total_break = break_mins * (cycles - 1) + (break_mins * 3)
    
    table = Table(title="📊 Session Summary", show_header=True, header_style="bold magenta")
    table.add_column("Metric", style="cyan")
    table.add_column("Details", style="green")
    
    table.add_row("Task Focus", task_name if task_name else "General Focus")
    table.add_row("Cycles Completed", str(cycles))
    table.add_row("Total Focus Time", f"{total_work} minutes")
    table.add_row("Total Break Time", f"{total_break} minutes")
    
    console.print(Align.center(table))
    console.print("\n[bold cyan]Great job today. See you next time![/]")

def main():
    parser = argparse.ArgumentParser(description="AuraTimer - Premium Terminal Pomodoro")
    parser.add_argument("-w", "--work", type=int, default=25, help="Work duration in minutes")
    parser.add_argument("-b", "--break_time", type=int, default=5, help="Break duration in minutes")
    parser.add_argument("-c", "--cycles", type=int, default=4, help="Number of cycles")
    parser.add_argument("-t", "--task", type=str, default="", help="Name of the task you are working on")
    
    args = parser.parse_args()
    
    try:
        for cycle in range(1, args.cycles + 1):
            console.rule(f"[bold cyan]Cycle {cycle}/{args.cycles}[/]")
            run_timer(args.work, "Focus", "cyan", args.task)
            
            if cycle < args.cycles:
                run_timer(args.break_time, "Break", "magenta", "Rest & Hydrate")
            else:
                run_timer(args.break_time * 3, "Long Break", "blue", "Deep Rest")
                
        display_summary(args.work, args.break_time, args.cycles, args.task)
        
    except KeyboardInterrupt:
        console.print("\n[bold red]Timer stopped by user.[/]")

if __name__ == "__main__":
    main()
