# -------------------------------------------------
# File Name: 32_odd_even_linked_list.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Group odd-indexed nodes followed by even-indexed nodes.
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


def odd_even_list(head: Node | None) -> Node | None:
    if head is None or head.next is None:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head
    return head


def demo() -> None:
    title("ODD EVEN LINKED LIST")
    for values in ([1, 2, 3, 4, 5], [2, 1, 3, 5, 6, 4, 7]):
        head = build_linked_list(values)
        print(f"  input={values} -> output={to_list(odd_even_list(head))}")


if __name__ == "__main__":
    demo()
