# -------------------------------------------------
# File Name: 28_flatten_multilevel_doubly_linked_list.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Flatten a multilevel doubly linked list.
# -------------------------------------------------

SEPARATOR = "=" * 62


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.prev: "Node | None" = None
        self.next: "Node | None" = None
        self.child: "Node | None" = None


def flatten(head: Node | None) -> Node | None:
    if not head:
        return head

    stack = [head]
    prev = None

    while stack:
        current = stack.pop()
        if prev:
            prev.next = current
            current.prev = prev

        if current.next:
            stack.append(current.next)
        if current.child:
            stack.append(current.child)
            current.child = None

        prev = current

    return head


def to_list(head: Node | None) -> list[int]:
    values = []
    cur = head
    while cur:
        values.append(cur.value)
        cur = cur.next
    return values


def demo() -> None:
    title("FLATTEN MULTILEVEL DOUBLY LINKED LIST")

    # Build example:
    # 1 - 2 - 3 - 4
    #         |
    #         7 - 8
    n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
    n7, n8 = Node(7), Node(8)
    n1.next, n2.prev = n2, n1
    n2.next, n3.prev = n3, n2
    n3.next, n4.prev = n4, n3
    n7.next, n8.prev = n8, n7
    n3.child = n7

    flat_head = flatten(n1)
    print(f"  Flattened order: {to_list(flat_head)}")


if __name__ == "__main__":
    demo()
