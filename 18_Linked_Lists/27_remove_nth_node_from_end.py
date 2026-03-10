# -------------------------------------------------
# File Name: 27_remove_nth_node_from_end.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Remove the n-th node from the end of a linked list.
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
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result


def remove_nth_from_end(head: Node | None, n: int) -> Node | None:
    dummy = Node(0, head)
    fast = dummy
    slow = dummy

    for _ in range(n):
        if fast.next is None:
            return head
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next if slow.next else None
    return dummy.next


def demo() -> None:
    title("REMOVE NTH NODE FROM END")
    tests = [
        ([1, 2, 3, 4, 5], 2),
        ([1], 1),
        ([1, 2], 1),
    ]
    for values, n in tests:
        head = build_linked_list(values)
        updated = remove_nth_from_end(head, n)
        print(f"  values={values}, n={n} -> {to_list(updated)}")


if __name__ == "__main__":
    demo()
