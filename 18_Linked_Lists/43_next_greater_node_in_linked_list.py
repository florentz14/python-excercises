# -------------------------------------------------
# File Name: 43_next_greater_node_in_linked_list.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Find next greater value for each linked list node.
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


def next_larger_nodes(head: Node | None) -> list[int]:
    values = []
    while head:
        values.append(head.value)
        head = head.next

    result = [0] * len(values)
    stack = []
    for i, value in enumerate(values):
        while stack and values[stack[-1]] < value:
            idx = stack.pop()
            result[idx] = value
        stack.append(i)
    return result


def demo() -> None:
    title("NEXT GREATER NODE IN LINKED LIST")
    tests = [[2, 1, 5], [2, 7, 4, 3, 5], [1, 7, 5, 1, 9, 2, 5, 1]]
    for values in tests:
        head = build_linked_list(values)
        print(f"  input={values} -> output={next_larger_nodes(head)}")


if __name__ == "__main__":
    demo()
