# -------------------------------------------------
# File Name: 31_reverse_linked_list_ii.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Reverse a linked list between positions left and right.
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
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result


def reverse_between(head: Node | None, left: int, right: int) -> Node | None:
    if head is None or left == right:
        return head

    dummy = Node(0, head)
    prev = dummy
    for _ in range(left - 1):
        prev = prev.next

    current = prev.next
    for _ in range(right - left):
        nxt = current.next
        current.next = nxt.next
        nxt.next = prev.next
        prev.next = nxt

    return dummy.next


def demo() -> None:
    title("REVERSE LINKED LIST II")
    values = [1, 2, 3, 4, 5]
    head = build_linked_list(values)
    updated = reverse_between(head, 2, 4)
    print(f"  input={values}, left=2, right=4 -> {to_list(updated)}")


if __name__ == "__main__":
    demo()
