# -------------------------------------------------
# File Name: 47_double_a_number_represented_as_linked_list.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Double a number stored in forward-order linked list.
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


def reverse(head: Node | None) -> Node | None:
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


def double_it(head: Node | None) -> Node | None:
    rev = reverse(head)
    carry = 0
    current = rev
    prev = None
    while current:
        total = current.value * 2 + carry
        current.value = total % 10
        carry = total // 10
        prev = current
        current = current.next

    if carry:
        prev.next = Node(carry)

    return reverse(rev)


def demo() -> None:
    title("DOUBLE A NUMBER REPRESENTED AS LINKED LIST")
    tests = [[1, 8, 9], [9, 9, 9], [0]]
    for digits in tests:
        head = build_linked_list(digits)
        doubled = double_it(head)
        print(f"  input={digits} -> output={to_list(doubled)}")


if __name__ == "__main__":
    demo()
