import re
from typing import Any, cast

from tinydb import Query, TinyDB
from tinydb.table import Document

from task.log import log_error
from task.models import Task, TaskParamData, TypePriority
from task.settings import DB_FILE


class TinyDbRepository:
    def __init__(self, db: TinyDB) -> None:
        self.db = db

    def find_all(self) -> list[Task]:
        return self._get_tasks()

    def find_one(self, task_id: int) -> Task | None:
        task_data: TaskParamData = self.db.get(doc_id=task_id)  # pyright: ignore
        return Task(id=task_id, **task_data) if task_data else None

    def find(
        self,
        *,
        task: str | None = None,
        done: bool | None = None,
        tags: tuple[str, ...] = (),
        priority: TypePriority | None = None,
        limit: int = 10,
    ) -> list[Task]:
        q = Query()
        no_q = q.noop()
        done_t = done is True
        done_f = done is False
        q_done_t = q.done == True  # noqa: E712
        q_done_f = q.done == False  # noqa: E712

        kwargs = {
            "task": lambda: q.task.search(task, re.I) if task else no_q,
            "done": lambda: q_done_t if done_t else q_done_f if done_f else no_q,
            "tags": lambda: q.tags.any(list(tags)) if tags else no_q,
            "priority": lambda: q.priority.search(priority, re.I) if priority else no_q,
        }
        queries = (
            kwargs["task"]()
            & kwargs["done"]()
            & kwargs["tags"]()
            & kwargs["priority"]()
        )

        result = self.db.search(queries)
        return map_tinydb_docs_to_tasks(result)[:limit]

    def create(self, task_data: TaskParamData) -> Task | None:
        existing_task = self.find(task=task_data["task"])

        if existing_task:
            log_error("Task description already exist")
            return None

        task_data["tags"] = tuple(set(task_data.get("tags", ())))
        task_id = self.db.insert(task_data)  # pyright: ignore
        return Task(
            id=task_id,
            task=task_data["task"],
            priority=task_data.get("priority", "medium"),
            done=task_data.get("done", False),
            tags=task_data.get("tags", ()),
        )

    def delete(self, task_id: int) -> Task | None:
        task = self.find_one(task_id)

        if not task:
            log_error("Task does not exist")
            return None

        self.db.remove(doc_ids=[task_id])
        return task

    def _get_tasks(self) -> list[Task]:
        db_tasks = self.db.all()
        return map_tinydb_docs_to_tasks(db_tasks)


def map_tinydb_docs_to_tasks(doc_tasks: list[Document]) -> list[Task]:
    return [map_tinydb_doc_to_task(task) for task in doc_tasks]


def map_tinydb_doc_to_task(doc_task: Document) -> Task:
    return Task(id=doc_task.doc_id, **doc_task)


def map_dict_to_task_params(data: dict[str, Any]) -> TaskParamData:
    mapped_data = cast(
        "TaskParamData", {k: data.get(k) for k in Task._fields if k in data}
    )
    return TaskParamData(mapped_data)


db = TinyDB(DB_FILE)
db.default_table_name = "tasks"
task_repository = TinyDbRepository(db)
