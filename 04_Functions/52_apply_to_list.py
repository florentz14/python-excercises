# -------------------------------------------------
# File Name: 52_apply_to_list.py
# Description: Apply function to each element of list (map)
# -------------------------------------------------

from typing import Callable, TypeVar

T = TypeVar("T")
U = TypeVar("U")


def apply_to_list(items: list[T], func: Callable[[T], U]) -> list[U]:
    """Apply func to each element, return new list."""
    return [func(x) for x in items]


if __name__ == "__main__":
    print(apply_to_list([1, 2, 3, 4], lambda x: x * 2))
    print(apply_to_list(["a", "bb", "ccc"], len))
    print(apply_to_list([2.1, 3.7, 1.2], int))
