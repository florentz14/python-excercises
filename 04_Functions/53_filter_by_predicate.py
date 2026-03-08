# -------------------------------------------------
# File Name: 53_filter_by_predicate.py
# Description: Filter list by boolean function (filter)
# -------------------------------------------------

from typing import Callable, TypeVar

T = TypeVar("T")


def filter_by_predicate(items: list[T], predicate: Callable[[T], bool]) -> list[T]:
    """Return elements for which predicate(x) is True."""
    return [x for x in items if predicate(x)]


if __name__ == "__main__":
    print(filter_by_predicate([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))
    print(filter_by_predicate(["a", "ab", "abc", "abcd"], lambda s: len(s) > 2))
    print(filter_by_predicate([0, 1, "", "x", None, 42], bool))
