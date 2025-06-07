from __future__ import annotations

from typing import Any, Literal, NamedTuple, NotRequired, TypedDict, overload

TypePriority = Literal["low", "medium", "high"]


class TaskParamData(TypedDict):
    task: str
    done: NotRequired[bool]
    tags: NotRequired[tuple[str, ...]]
    priority: NotRequired[TypePriority]


class Task(NamedTuple):
    id: int = 0
    task: str = ""
    done: bool = False
    tags: tuple[str, ...] = ()
    priority: Literal[TypePriority] = "medium"

    @overload
    def get(self, attr: Literal["id"]) -> int: ...
    @overload
    def get(self, attr: Literal["task"]) -> str: ...
    @overload
    def get(self, attr: Literal["done"]) -> bool: ...
    @overload
    def get(self, attr: Literal["tags"]) -> tuple[str, ...]: ...
    @overload
    def get(self, attr: Literal["priority"]) -> Literal[TypePriority]: ...
    @overload
    def get[T](self, attr: str, default: T = None) -> T: ...

    def get[T](self, attr: str, default: T = None) -> T | Any:
        return getattr(self, attr, default)
