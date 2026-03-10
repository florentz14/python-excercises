# -------------------------------------------------
# File Name: 36_reverse_nodes_in_even_length_groups.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Reverse nodes in even-length natural groups.
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
    arr = []
    while head:
        arr.append(head.value)
        head = head.next
    return arr


def reverse_segment(head: Node, k: int) -> tuple[Node, Node, Node | None]:
    prev = None
    current = head
    while k > 0 and current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
        k -= 1
    return prev, head, current


def reverse_even_length_groups(head: Node | None) -> Node | None:
    if not head:
        return head

    dummy = Node(0, head)
    prev_group_tail = dummy
    group_size = 1

    while prev_group_tail.next:
        # Count actual nodes in this group.
        count = 0
        group_head = prev_group_tail.next
        cursor = group_head
        while count < group_size and cursor:
            count += 1
            cursor = cursor.next

        if count % 2 == 0:
            new_head, new_tail, next_group = reverse_segment(group_head, count)
            prev_group_tail.next = new_head
            new_tail.next = next_group
            prev_group_tail = new_tail
        else:
            for _ in range(count):
                prev_group_tail = prev_group_tail.next

        group_size += 1

    return dummy.next


def demo() -> None:
    title("REVERSE NODES IN EVEN LENGTH GROUPS")
    values = [1, 1, 0, 6, 5, 4, 3, 2, 7]
    head = build_linked_list(values)
    updated = reverse_even_length_groups(head)
    print(f"  input={values}")
    print(f"  output={to_list(updated)}")


if __name__ == "__main__":
    demo()
