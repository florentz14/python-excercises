# -------------------------------------------------
# File Name: 23_reverse_nodes_in_k_group.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Reverse linked list nodes in groups of size k.
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
    cur = head
    while cur:
        out.append(cur.value)
        cur = cur.next
    return out


def reverse_k_group(head: Node | None, k: int) -> Node | None:
    if k <= 1 or not head:
        return head

    dummy = Node(0, head)
    group_prev = dummy

    while True:
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if kth is None:
                return dummy.next

        group_next = kth.next

        # Reverse exactly k nodes.
        prev = group_next
        cur = group_prev.next
        while cur is not group_next:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        new_group_head = kth
        old_group_head = group_prev.next
        group_prev.next = new_group_head
        group_prev = old_group_head


def demo() -> None:
    title("REVERSE NODES IN K GROUP")
    values = [1, 2, 3, 4, 5, 6, 7]
    for k in (2, 3, 4):
        head = build_linked_list(values)
        result = reverse_k_group(head, k)
        print(f"  values={values}, k={k} -> {to_list(result)}")


if __name__ == "__main__":
    demo()
