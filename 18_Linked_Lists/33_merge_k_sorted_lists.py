# -------------------------------------------------
# File Name: 33_merge_k_sorted_lists.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Merge k sorted linked lists using a min-heap.
# -------------------------------------------------

import heapq

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


def merge_k_lists(lists: list[Node | None]) -> Node | None:
    heap: list[tuple[int, int, Node]] = []
    uid = 0
    for node in lists:
        if node:
            heapq.heappush(heap, (node.value, uid, node))
            uid += 1

    dummy = Node(0)
    tail = dummy

    while heap:
        _, _, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(heap, (node.next.value, uid, node.next))
            uid += 1

    tail.next = None
    return dummy.next


def demo() -> None:
    title("MERGE K SORTED LISTS")
    lists = [
        build_linked_list([1, 4, 5]),
        build_linked_list([1, 3, 4]),
        build_linked_list([2, 6]),
    ]
    merged = merge_k_lists(lists)
    print(f"  merged={to_list(merged)}")


if __name__ == "__main__":
    demo()
