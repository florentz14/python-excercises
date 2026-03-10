# -------------------------------------------------
# File Name: 34_remove_zero_sum_consecutive_nodes.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Remove consecutive nodes whose sum equals zero.
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


def remove_zero_sum_sublists(head: Node | None) -> Node | None:
    dummy = Node(0, head)
    prefix_sum = 0
    last_seen = {}

    current = dummy
    while current:
        prefix_sum += current.value
        last_seen[prefix_sum] = current
        current = current.next

    prefix_sum = 0
    current = dummy
    while current:
        prefix_sum += current.value
        current.next = last_seen[prefix_sum].next
        current = current.next

    return dummy.next


def demo() -> None:
    title("REMOVE ZERO SUM CONSECUTIVE NODES")
    tests = [
        [1, 2, -3, 3, 1],
        [1, 2, 3, -3, 4],
        [1, 2, 3, -3, -2],
    ]
    for values in tests:
        head = build_linked_list(values)
        result = remove_zero_sum_sublists(head)
        print(f"  input={values} -> output={to_list(result)}")


if __name__ == "__main__":
    demo()
