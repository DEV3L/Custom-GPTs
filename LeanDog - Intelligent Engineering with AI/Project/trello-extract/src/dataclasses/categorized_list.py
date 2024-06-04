from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class CategorizedLists(Generic[T]):
    planning: list[T] = field(default_factory=list)
    todo: list[T] = field(default_factory=list)
    doing: list[T] = field(default_factory=list)
    done: list[T] = field(default_factory=list)
    users: list[T] = field(default_factory=list)
    team: list[T] = field(default_factory=list)