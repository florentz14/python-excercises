# -------------------------------------------------
# File Name: 50_insert_into_a_sorted_circular_linked_list.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Insert a value into a sorted circular linked list.
# -------------------------------------------------

SEPARATOR = "=" * 62


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


class Node:
    def __init__(self, value: int, next_node: "Node | None" = None) -> None:
        self.value = value
        self.next = next_node


def insert(head: Node | None, insert_val: int) -> Node:
    new_node = Node(insert_val)
    if not head:
        new_node.next = new_node
        return new_node

    current = head
    while True:
        next_node = current.next

        # Normal sorted place.
        if current.value <= insert_val <= next_node.value:
            break

        # Rotation point between max and min.
        if current.value > next_node.value:
            if insert_val >= current.value or insert_val <= next_node.value:
                break

        current = next_node
        if current is head:
            break

    new_node.next = current.next
    current.next = new_node
    return head


def circular_to_list(head: Node, limit: int = 12) -> list[int]:
    values = []
    current = head
    for _ in range(limit):
        values.append(current.value)
        current = current.next
        if current is head:
            break
    return values


def demo() -> None:
    title("INSERT INTO A SORTED CIRCULAR LINKED LIST")

    n1 = Node(1)
    n3 = Node(3)
    n4 = Node(4)
    n1.next = n3
    n3.next = n4
    n4.next = n1

    head = insert(n1, 2)
    head = insert(head, 5)
    head = insert(head, 0)
    print(f"  circular list sample: {circular_to_list(head)}")


if __name__ == "__main__":
    demo()
