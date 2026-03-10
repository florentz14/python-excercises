# -------------------------------------------------
# File Name: 40_insert_greatest_common_divisors.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Insert GCD nodes between adjacent linked list nodes.
# -------------------------------------------------

from math import gcd

SEPARATOR = "=" * 62


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


class Node:
    def __init__(self, value: int, next_node: "Node | None" = None) -> None:
        self.value = value
        self.next = next_node


def build_linked_list(values: list[int]) -> Node | None:
    head = None
    tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def to_list(head: Node | None) -> list[int]:
    arr = []
    while head:
        arr.append(head.value)
        head = head.next
    return arr


def insert_greatest_common_divisors(head: Node | None) -> Node | None:
    current = head
    while current and current.next:
        g = gcd(current.value, current.next.value)
        inserted = Node(g, current.next)
        current.next = inserted
        current = inserted.next
    return head


def demo() -> None:
    title("INSERT GREATEST COMMON DIVISORS")
    tests = [[18, 6, 10, 3], [7], [42, 56]]
    for values in tests:
        head = build_linked_list(values)
        updated = insert_greatest_common_divisors(head)
        print(f"  input={values} -> output={to_list(updated)}")


if __name__ == "__main__":
    demo()
