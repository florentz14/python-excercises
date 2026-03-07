# -------------------------------------------------
# File: 07_reverse_linked_list.py
# Description: Reverse a singly linked list.
#              Classic algorithm using iterative approach.
# -------------------------------------------------

from typing import Any, Optional


class Node:
    """Node for singly linked list."""

    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional["Node"] = None


class SinglyLinkedList:
    """Singly Linked List with reverse operation."""

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.size: int = 0

    def is_empty(self) -> bool:
        return self.head is None

    def display(self) -> None:
        """Display the linked list."""
        if self.is_empty():
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def append(self, data: Any) -> None:
        """Helper method to add nodes."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            assert current is not None
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def reverse(self) -> None:
        """Reverse the linked list iteratively. O(n) time, O(1) space"""
        prev = None
        current = self.head

        while current:
            next_node = current.next  # Save next node
            current.next = prev       # Reverse the link
            prev = current            # Move prev forward
            current = next_node       # Move current forward

        self.head = prev  # Update head to new first node

    def reverse_recursive(self, node: Optional[Node]) -> Optional[Node]:
        """Helper method for recursive reverse."""
        if node is None or node.next is None:
            return node

        # Recursively reverse the rest of the list
        reversed_head = self.reverse_recursive(node.next)

        # Reverse the current node's link
        node.next.next = node
        node.next = None

        return reversed_head

    def reverse_recursive_wrapper(self) -> None:
        """Wrapper for recursive reverse."""
        self.head = self.reverse_recursive(self.head)


# Demonstration
if __name__ == "__main__":
    sll = SinglyLinkedList()

    print("=== Reverse Linked List Demo ===\n")

    # Create initial list
    for i in [1, 2, 3, 4, 5]:
        sll.append(i)

    print("Original list:")
    sll.display()

    # Reverse iteratively
    sll.reverse()
    print("After iterative reverse:")
    sll.display()

    # Reverse again to show it works both ways
    sll.reverse()
    print("Reversed back:")
    sll.display()

    # Reverse recursively
    sll.reverse_recursive_wrapper()
    print("After recursive reverse:")
    sll.display()

    print(f"\nSize: {sll.size}")
