# -------------------------------------------------
# File Name: 29_sort_list_merge_sort.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Sort a linked list using merge sort.
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
        if not head:
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


def merge(left: Node | None, right: Node | None) -> Node | None:
    dummy = Node(0)
    tail = dummy
    while left and right:
        if left.value <= right.value:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    tail.next = left if left else right
    return dummy.next


def sort_list(head: Node | None) -> Node | None:
    if not head or not head.next:
        return head

    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = sort_list(head)
    right = sort_list(mid)
    return merge(left, right)


def demo() -> None:
    title("SORT LIST WITH MERGE SORT")
    tests = [[4, 2, 1, 3], [-1, 5, 3, 4, 0]]
    for values in tests:
        head = build_linked_list(values)
        sorted_head = sort_list(head)
        print(f"  input={values} -> sorted={to_list(sorted_head)}")


if __name__ == "__main__":
    demo()
