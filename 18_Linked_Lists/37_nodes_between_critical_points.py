# -------------------------------------------------
# File Name: 37_nodes_between_critical_points.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Min and max distance between linked list critical points.
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


def nodes_between_critical_points(head: Node | None) -> list[int]:
    if not head or not head.next or not head.next.next:
        return [-1, -1]

    positions = []
    index = 1
    prev = head
    curr = head.next

    while curr.next:
        nxt = curr.next
        is_peak = curr.value > prev.value and curr.value > nxt.value
        is_valley = curr.value < prev.value and curr.value < nxt.value
        if is_peak or is_valley:
            positions.append(index)
        prev = curr
        curr = nxt
        index += 1

    if len(positions) < 2:
        return [-1, -1]

    min_dist = min(positions[i] - positions[i - 1] for i in range(1, len(positions)))
    max_dist = positions[-1] - positions[0]
    return [min_dist, max_dist]


def demo() -> None:
    title("NODES BETWEEN CRITICAL POINTS")
    tests = [
        [3, 1],
        [5, 3, 1, 2, 5, 1, 2],
        [1, 3, 2, 2, 3, 2, 2, 2, 7],
    ]
    for values in tests:
        head = build_linked_list(values)
        print(f"  input={values} -> {nodes_between_critical_points(head)}")


if __name__ == "__main__":
    demo()
