# -------------------------------------------------
# File Name: 24_add_two_numbers_linked_list.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Add two numbers represented by linked lists.
# -------------------------------------------------

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
    out = []
    while head:
        out.append(head.value)
        head = head.next
    return out


def add_two_numbers(l1: Node | None, l2: Node | None) -> Node | None:
    carry = 0
    dummy = Node(0)
    tail = dummy

    while l1 or l2 or carry:
        v1 = l1.value if l1 else 0
        v2 = l2.value if l2 else 0
        total = v1 + v2 + carry
        carry = total // 10
        tail.next = Node(total % 10)
        tail = tail.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


def demo() -> None:
    title("ADD TWO NUMBERS (LINKED LIST)")
    tests = [
        ([2, 4, 3], [5, 6, 4]),
        ([9, 9, 9, 9], [1]),
        ([0], [0]),
    ]
    for a, b in tests:
        l1 = build_linked_list(a)
        l2 = build_linked_list(b)
        result = add_two_numbers(l1, l2)
        print(f"  {a} + {b} -> {to_list(result)}")


if __name__ == "__main__":
    demo()
