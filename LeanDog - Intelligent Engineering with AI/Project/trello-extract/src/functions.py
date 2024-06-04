from typing import Iterator, Optional, TypeVar

T = TypeVar("T")


def first(iterable: Iterator[T], default: Optional[T] = None) -> Optional[T]:
    for item in iterable:
        return item
    return default
