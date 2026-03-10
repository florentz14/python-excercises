# -------------------------------------------------
# File Name: 48_remove_nodes_from_linked_list.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Remove nodes that have a greater value on the right.
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
    values = []
    while head:
        values.append(head.value)
        head = head.next
    return values


def reverse(head: Node | None) -> Node | None:
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


def remove_nodes(head: Node | None) -> Node | None:
    rev = reverse(head)
    max_seen = float("-inf")
    dummy = Node(0)
    tail = dummy

    current = rev
    while current:
        if current.value >= max_seen:
            max_seen = current.value
            tail.next = current
            tail = tail.next
        current = current.next

    tail.next = None
    return reverse(dummy.next)


def demo() -> None:
    title("REMOVE NODES FROM LINKED LIST")
    tests = [[5, 2, 13, 3, 8], [1, 1, 1, 1], [10, 9, 8]]
    for values in tests:
        head = build_linked_list(values)
        result = remove_nodes(head)
        print(f"  input={values} -> output={to_list(result)}")


if __name__ == "__main__":
    demo()
