# -------------------------------------------------
# File Name: 42_swap_nodes_in_linked_list.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Swap values of k-th node from start and end.
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


def swap_nodes(head: Node | None, k: int) -> Node | None:
    first = head
    for _ in range(k - 1):
        first = first.next

    fast = first
    second = head
    while fast.next:
        fast = fast.next
        second = second.next

    first.value, second.value = second.value, first.value
    return head


def demo() -> None:
    title("SWAP NODES IN LINKED LIST")
    tests = [([1, 2, 3, 4, 5], 2), ([7, 9, 6, 6, 7, 8, 3, 0, 9, 5], 5)]
    for values, k in tests:
        head = build_linked_list(values)
        swap_nodes(head, k)
        print(f"  input={values}, k={k} -> output={to_list(head)}")


if __name__ == "__main__":
    demo()
