from rich import print as rprint
from rich.console import Console
from rich.table import Table

from task.models import Task

console = Console()


def info(msg: str) -> None:
    rprint(f"[bold cyan][ info ][/bold cyan] {msg}")


def success(msg: str) -> None:
    rprint(f"[bold green][ success ][/bold green] {msg}")


def warning(msg: str) -> None:
    rprint(f"[bold yellow][ warning ][/bold yellow] {msg}")


def error(msg: str) -> None:
    rprint(f"[bold red][ error ][/bold red] {msg}")


def debug(msg: str) -> None:
    rprint(f"[dim][ debug ][/dim] {msg}")


def info_bool(*, value: bool) -> str:
    return f"{'[green]enabled[/green]' if value else '[red]disabled[/red]'}"


def log_success(msg: str) -> None:
    success(f"🟢 {msg}")
    print()


def log_error(msg: str) -> None:
    error(f"🔴 {msg}")
    print()


console = Console()


def log_task_table(
    tasks: list[Task] | Task | None,
    *,
    icon: str = "",
    show_header: bool = True,
    title: str = "Tasks",
) -> None:
    if tasks is None or (not isinstance(tasks, list) and not tasks):
        print()
        log_error("No tasks found")
        return

    if not isinstance(tasks, list):
        tasks = [tasks]

    if not tasks:
        print()
        log_error("No tasks found")
        return

    console.print(f"\n[bold cyan]{title}[/bold cyan]\n")

    table = Table(
        show_header=show_header, header_style="bold magenta", border_style="dim"
    )

    table.add_column("ID", style="dim", justify="right")
    table.add_column("Task", style="white")
    table.add_column("Done", justify="center")
    table.add_column("Priority", justify="center")
    table.add_column("Tags", style="yellow")

    for task in tasks:
        done = "[green]✔[/green]" if task.done else "[red]✘[/red]"

        priority_color = {
            "low": "blue",
            "medium": "yellow",
            "high": "red",
        }.get(task.priority, "white")

        priority = f"[{priority_color}]{task.priority}[/]"

        tags = ", ".join(task.tags)
        task_text = f"{icon}{task.task}"

        table.add_row(
            str(task.id),
            task_text,
            done,
            priority,
            tags,
        )

    console.print(table)
