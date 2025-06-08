import argparse
import textwrap

import rich_argparse

from task.runners import DefaultRunner
from task.settings import clear
from task.validation import validate_positive_int, validate_str


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="task",
        description=textwrap.dedent("""
            Task Manager helps you organize your tasks directly from the terminal.

            You can create, search, list, and delete tasks with ease - all from
            your CLI. No need for web apps, mouse clicks or distractions.
            Just productivity.
        """),
        epilog=textwrap.dedent("""
            This will be shown below all arguments and can be used to add
            copyright or other complex examples.
        """),
        formatter_class=rich_argparse.RawDescriptionRichHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    ### PARSER CREATE
    create_parser = subparsers.add_parser(
        "create",
        aliases=["new", "add"],
        description=textwrap.dedent("""
            Use this command to create a new task quickly and efficiently.

            Provide a title, optional tags, priority, and mark it as done if needed.
            Whether you're planning your day or dumping ideas into the terminal,
            this is your entry point.
        """),
        epilog=textwrap.dedent("""
            Examples:

              task create -t "Buy groceries"
              task create -t "Study argparse" --tag python --tag cli --priority high
              task create -t "Walk the dog" --done

            You can also combine options freely to match your workflow.
            Tags help with filtering later. Priorities can be: low, medium, high.
        """),
        formatter_class=rich_argparse.RawDescriptionRichHelpFormatter,
    )
    create_parser.set_defaults(command="create")

    create_parser.add_argument(
        "-t",
        "--task",
        dest="task",
        type=validate_str,
        help="Describes your task",
        required=True,
        metavar="Task",
    )

    create_parser.add_argument(
        "--done",
        help="Marks a task as complete",
        action=argparse.BooleanOptionalAction,
        default=False,
    )

    create_parser.add_argument(
        "--tag",
        help="Adds tags to your tasks for organization",
        action="extend",
        type=validate_str,
        nargs="*",  # zero ou muitos
        default=[],
        dest="tags",
    )

    create_parser.add_argument(
        "-p",
        "--priority",
        choices=["low", "medium", "high"],
        default="medium",
        help="Sets the priority for your task",
    )

    ### PARSER ALL
    subparsers.add_parser(
        "all",
        help="Shows all tasks",
        description=textwrap.dedent("""Shows all tasks"""),
        formatter_class=rich_argparse.RawDescriptionRichHelpFormatter,
    )

    ### PARSER SEARCH
    search_parser = subparsers.add_parser(
        "search",
        aliases=["find"],
        description=textwrap.dedent("""
            Search through your tasks with surgical precision.

            Use this command to filter tasks by title, tags, status or priority.
            Whether you're reviewing your day or trying to find that one todo
            you swore you wrote down, this is the command that brings order to the chaos.
        """),
        epilog=textwrap.dedent("""
            Examples:

              task search --tag python
              task search -t "groceries" --done
              task search --priority high --limit 5

            You can combine multiple options for refined results.
            The search is non-destructive and works with partial information.

            All arguments are optional – filter as much or as little as you want.
        """),
        formatter_class=rich_argparse.RawDescriptionRichHelpFormatter,
    )
    search_parser.set_defaults(command="search")

    search_parser.add_argument(
        "-t",
        "--task",
        type=validate_str,
        help="Searches for your task description (regular expression allowed)",
    )

    search_parser.add_argument(
        "--done",
        help="Finds tasks with `--done` (completed) or `--no-done` (not completed)",
        action=argparse.BooleanOptionalAction,
    )

    search_parser.add_argument(
        "--tag",
        help="Adds tags to your tasks for organization",
        action="extend",
        type=validate_str,
        nargs="*",  # zero ou muitos
        default=None,
        dest="tags",
    )

    search_parser.add_argument(
        "-p",
        "--priority",
        choices=["low", "medium", "high"],
        default=None,
        help="Sets the priority for your task",
    )

    search_parser.add_argument(
        "-l",
        "--limit",
        help="Limits the number of tasks per search",
        default=10,
        type=validate_positive_int,
    )

    ### PARSER DELETE
    delete_parser = subparsers.add_parser(
        "delete",
        description="Deletes one task by id",
        help="Deletes one task by id",
        formatter_class=rich_argparse.RawDescriptionRichHelpFormatter,
    )

    delete_parser.add_argument(
        "-i", "--task-id", help="Task ID", required=True, type=validate_positive_int
    )

    delete_parser.add_argument(
        "-f",
        "--force",
        help="Removes the confirmation when deleting tasks",
        action="store_true",
    )

    ### PARSER ONE
    one_parser = subparsers.add_parser(
        "one",
        description="Finds one task by id",
        help="Finds one task by id",
        formatter_class=rich_argparse.RawDescriptionRichHelpFormatter,
    )

    one_parser.add_argument(
        "-i", "--task-id", help="Task ID", required=True, type=validate_positive_int
    )  # Task ID is required and must be an integer

    return parser


def run() -> None:
    clear()
    parser = build_parser()

    args = parser.parse_args()

    default_runner = DefaultRunner()
    getattr(default_runner, args.command)(args)


if __name__ == "__main__":
    run()
