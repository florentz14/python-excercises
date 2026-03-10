# -------------------------------------------------
# File Name: 20_palindrome_linked_list.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Check if a singly linked list is a palindrome.
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
    current = head
    while current:
        values.append(current.value)
        current = current.next
    return values


def is_palindrome(head: Node | None) -> bool:
    values = to_list(head)
    return values == values[::-1]


def demo() -> None:
    title("PALINDROME LINKED LIST")
    tests = [
        [1, 2, 2, 1],
        [1, 2, 3, 2, 1],
        [1, 2, 3],
    ]
    for values in tests:
        head = build_linked_list(values)
        print(f"  list={values} -> palindrome={is_palindrome(head)}")


if __name__ == "__main__":
    demo()
