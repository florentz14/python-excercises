# -------------------------------------------------
# File Name: 38_delete_the_middle_node.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Delete the middle node of a singly linked list.
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


def delete_middle(head: Node | None) -> Node | None:
    if not head or not head.next:
        return None

    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next
    return head


def demo() -> None:
    title("DELETE THE MIDDLE NODE")
    tests = [[1, 3, 4, 7, 1, 2, 6], [1, 2, 3, 4], [2, 1]]
    for values in tests:
        head = build_linked_list(values)
        updated = delete_middle(head)
        print(f"  input={values} -> output={to_list(updated)}")


if __name__ == "__main__":
    demo()
