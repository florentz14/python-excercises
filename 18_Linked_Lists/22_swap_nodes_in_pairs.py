# -------------------------------------------------
# File Name: 22_swap_nodes_in_pairs.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Swap every two adjacent nodes in a linked list.
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
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result


def swap_pairs(head: Node | None) -> Node | None:
    dummy = Node(0, head)
    prev = dummy
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first
    return dummy.next


def demo() -> None:
    title("SWAP NODES IN PAIRS")
    for values in ([1, 2, 3, 4], [1, 2, 3], [7]):
        head = build_linked_list(list(values))
        swapped = swap_pairs(head)
        print(f"  input={list(values)} -> swapped={to_list(swapped)}")


if __name__ == "__main__":
    demo()
