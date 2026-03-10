# -------------------------------------------------
# File Name: 49_delete_nodes_from_linked_list_present_in_array.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Remove linked list nodes whose values are in an array.
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


def modified_list(nums: list[int], head: Node | None) -> Node | None:
    banned = set(nums)
    dummy = Node(0, head)
    current = dummy

    while current and current.next:
        if current.next.value in banned:
            current.next = current.next.next
        else:
            current = current.next

    return dummy.next


def demo() -> None:
    title("DELETE NODES PRESENT IN ARRAY")
    nums = [1, 2, 3]
    values = [1, 2, 3, 4, 5]
    head = build_linked_list(values)
    updated = modified_list(nums, head)
    print(f"  values={values}, nums={nums} -> output={to_list(updated)}")


if __name__ == "__main__":
    demo()
