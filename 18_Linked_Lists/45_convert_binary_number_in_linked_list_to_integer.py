# -------------------------------------------------
# File Name: 45_convert_binary_number_in_linked_list_to_integer.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Convert a binary number in linked list form to integer.
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


def get_decimal_value(head: Node | None) -> int:
    result = 0
    while head:
        result = (result << 1) | head.value
        head = head.next
    return result


def demo() -> None:
    title("CONVERT BINARY NUMBER IN LINKED LIST TO INTEGER")
    tests = [[1, 0, 1], [0], [1, 1, 1, 1], [1, 0, 0, 1, 1]]
    for bits in tests:
        head = build_linked_list(bits)
        print(f"  bits={bits} -> decimal={get_decimal_value(head)}")


if __name__ == "__main__":
    demo()
