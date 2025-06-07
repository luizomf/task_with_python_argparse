import argparse
from typing import Any

from rich.prompt import Prompt

from task.log import log_error, log_success, log_task_table
from task.repository import map_dict_to_task_params, task_repository


class DefaultRunner:
    def create(self, args: argparse.Namespace) -> None:
        arguments = vars(args)
        task_dict_param = map_dict_to_task_params(arguments)
        created = task_repository.create(task_dict_param)

        if created:
            log_task_table(task_repository.find_all())
            print()
            log_success("Created!")
        print()

    def all(self, *args: tuple[Any, ...], **kwargs: dict[Any, Any]) -> None:
        log_task_table(task_repository.find_all())
        print()

    def search(self, args: argparse.Namespace) -> None:
        arguments = vars(args)
        arguments.pop("command", None)

        search_title = ", ".join([f"{k}={v!r}" for k, v in arguments.items()])
        search_title = f"Search input: {search_title}"

        found = task_repository.find(**arguments)
        log_task_table(found, title=search_title)
        print()

    def delete(self, args: argparse.Namespace) -> None:
        force = args.force
        existing_task = task_repository.find_one(args.task_id)

        log_task_table(task_repository.find_all())
        print()

        if not existing_task:
            log_error("Task does not exist")
            return

        confirmed = False
        if not force:
            confirmed = (
                Prompt.ask(
                    f"Are you sure you want to delete task ID: {args.task_id}?",
                    choices=["y", "n"],
                )
                .lower()
                .startswith("y")
            )

        if not (force or confirmed):
            log_task_table(task_repository.find_all())
            print()
            log_success("Ok, nothing deleted!")
            return

        deleted = task_repository.delete(args.task_id)

        log_task_table(task_repository.find_all())
        log_task_table(deleted, icon="🔴 ", title="Deleted task:", show_header=False)
        print()
        log_success(f"Successfully deleted: {args.task_id}")
        print()

    def one(self, args: argparse.Namespace) -> None:
        log_task_table(task_repository.find_one(args.task_id))
        print()
