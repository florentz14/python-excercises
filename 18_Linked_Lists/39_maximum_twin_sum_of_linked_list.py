# -------------------------------------------------
# File Name: 39_maximum_twin_sum_of_linked_list.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Find maximum twin sum in an even-length linked list.
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


def pair_sum(head: Node | None) -> int:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    answer = 0
    left = head
    right = prev
    while right:
        answer = max(answer, left.value + right.value)
        left = left.next
        right = right.next
    return answer


def demo() -> None:
    title("MAXIMUM TWIN SUM OF LINKED LIST")
    tests = [[5, 4, 2, 1], [4, 2, 2, 3], [1, 100000]]
    for values in tests:
        head = build_linked_list(values)
        print(f"  input={values} -> max_twin_sum={pair_sum(head)}")


if __name__ == "__main__":
    demo()
