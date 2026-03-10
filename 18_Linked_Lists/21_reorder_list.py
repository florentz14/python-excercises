# -------------------------------------------------
# File Name: 21_reorder_list.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Reorder list as L0->Ln->L1->Ln-1...
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
    for value in reversed(values):
        head = Node(value, head)
    return head


def to_list(head: Node | None) -> list[int]:
    out = []
    current = head
    while current:
        out.append(current.value)
        current = current.next
    return out


def reorder_list(head: Node | None) -> Node | None:
    if not head or not head.next:
        return head

    # Find the middle node.
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half.
    prev = None
    current = slow.next
    slow.next = None
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt

    # Merge first and second half alternately.
    first = head
    second = prev
    while second:
        f_next = first.next
        s_next = second.next
        first.next = second
        second.next = f_next
        first = f_next
        second = s_next

    return head


def demo() -> None:
    title("REORDER LIST")
    for values in ([1, 2, 3, 4], [1, 2, 3, 4, 5]):
        head = build_linked_list(list(values))
        reorder_list(head)
        print(f"  input={list(values)} -> reordered={to_list(head)}")


if __name__ == "__main__":
    demo()
