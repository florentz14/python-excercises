# -------------------------------------------------
# File Name: 30_linked_list_cycle_ii.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Find the node where a linked list cycle begins.
# -------------------------------------------------

SEPARATOR = "=" * 62


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


class Node:
    def __init__(self, value: int, next_node: "Node | None" = None) -> None:
        self.value = value
        self.next = next_node


def detect_cycle_start(head: Node | None) -> Node | None:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None

    ptr = head
    while ptr is not slow:
        ptr = ptr.next
        slow = slow.next
    return ptr


def build_sample_cycle() -> Node:
    # Build list 3 -> 2 -> 0 -> -4 and connect tail to node with value 2.
    n1 = Node(3)
    n2 = Node(2)
    n3 = Node(0)
    n4 = Node(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2
    return n1


def demo() -> None:
    title("LINKED LIST CYCLE II")
    head = build_sample_cycle()
    cycle_start = detect_cycle_start(head)
    print(f"  Cycle starts at node value: {cycle_start.value if cycle_start else None}")


if __name__ == "__main__":
    demo()
