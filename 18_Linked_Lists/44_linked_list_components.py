# -------------------------------------------------
# File Name: 44_linked_list_components.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Count connected components in a linked list subset.
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


def num_components(head: Node | None, nums: list[int]) -> int:
    allowed = set(nums)
    count = 0
    current = head
    while current:
        if current.value in allowed and (current.next is None or current.next.value not in allowed):
            count += 1
        current = current.next
    return count


def demo() -> None:
    title("LINKED LIST COMPONENTS")
    values = [0, 1, 2, 3]
    head = build_linked_list(values)
    nums = [0, 1, 3]
    print(f"  list={values}, subset={nums} -> components={num_components(head, nums)}")


if __name__ == "__main__":
    demo()
