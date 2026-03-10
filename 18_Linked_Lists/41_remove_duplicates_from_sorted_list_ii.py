# -------------------------------------------------
# File Name: 41_remove_duplicates_from_sorted_list_ii.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Remove all duplicate values from a sorted linked list.
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


def delete_duplicates(head: Node | None) -> Node | None:
    dummy = Node(0, head)
    prev = dummy

    while head:
        if head.next and head.value == head.next.value:
            duplicate_value = head.value
            while head and head.value == duplicate_value:
                head = head.next
            prev.next = head
        else:
            prev = prev.next
            head = head.next

    return dummy.next


def demo() -> None:
    title("REMOVE DUPLICATES FROM SORTED LIST II")
    tests = [[1, 2, 3, 3, 4, 4, 5], [1, 1, 1, 2, 3], [1, 2, 2]]
    for values in tests:
        head = build_linked_list(values)
        result = delete_duplicates(head)
        print(f"  input={values} -> output={to_list(result)}")


if __name__ == "__main__":
    demo()
