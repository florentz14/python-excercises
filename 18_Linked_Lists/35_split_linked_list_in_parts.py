# -------------------------------------------------
# File Name: 35_split_linked_list_in_parts.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Split a linked list into k consecutive parts.
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
    arr = []
    while head:
        arr.append(head.value)
        head = head.next
    return arr


def split_list_to_parts(head: Node | None, k: int) -> list[Node | None]:
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    base_size, extra = divmod(length, k)
    parts = []
    current = head

    for i in range(k):
        part_head = current
        part_size = base_size + (1 if i < extra else 0)

        for _ in range(part_size - 1):
            if current:
                current = current.next

        if current:
            nxt = current.next
            current.next = None
            current = nxt

        parts.append(part_head)

    return parts


def demo() -> None:
    title("SPLIT LINKED LIST IN PARTS")
    head = build_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    parts = split_list_to_parts(head, 3)
    print("  parts:")
    for i, part_head in enumerate(parts, start=1):
        print(f"    part {i}: {to_list(part_head)}")


if __name__ == "__main__":
    demo()
