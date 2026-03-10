# -------------------------------------------------
# File Name: 46_merge_in_between_linked_lists.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Replace nodes from index a to b with another list.
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


def merge_in_between(list1: Node | None, a: int, b: int, list2: Node | None) -> Node | None:
    dummy = Node(0, list1)
    prev_a = dummy
    for _ in range(a):
        prev_a = prev_a.next

    after_b = prev_a.next
    for _ in range(b - a + 1):
        after_b = after_b.next

    prev_a.next = list2
    tail2 = list2
    while tail2 and tail2.next:
        tail2 = tail2.next
    if tail2:
        tail2.next = after_b
    else:
        prev_a.next = after_b

    return dummy.next


def demo() -> None:
    title("MERGE IN BETWEEN LINKED LISTS")
    list1 = build_linked_list([0, 1, 2, 3, 4, 5])
    list2 = build_linked_list([1000000, 1000001, 1000002])
    merged = merge_in_between(list1, 3, 4, list2)
    print(f"  output={to_list(merged)}")


if __name__ == "__main__":
    demo()
