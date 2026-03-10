# -------------------------------------------------
# File Name: 26_rotate_list.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Rotate linked list to the right by k steps.
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


def rotate_right(head: Node | None, k: int) -> Node | None:
    if not head or not head.next or k == 0:
        return head

    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    k %= length
    if k == 0:
        return head

    # Create a cycle and cut at the new tail position.
    tail.next = head
    steps_to_new_tail = length - k - 1
    new_tail = head
    for _ in range(steps_to_new_tail):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head


def demo() -> None:
    title("ROTATE LIST")
    tests = [
        ([1, 2, 3, 4, 5], 2),
        ([0, 1, 2], 4),
    ]
    for values, k in tests:
        head = build_linked_list(values)
        rotated = rotate_right(head, k)
        print(f"  values={values}, k={k} -> {to_list(rotated)}")


if __name__ == "__main__":
    demo()
