# -------------------------------------------------
# File: 14_partition_list.py
# Description: Partition linked list around a value.
#              All nodes < pivot come before nodes >= pivot.
# -------------------------------------------------

from typing import Optional, Any


class Node:
    """Node for singly linked list."""

    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional["Node"] = None


class SinglyLinkedList:
    """Singly Linked List with partition operation."""

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

    def append(self, data):
        """Helper method to add nodes."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def partition(self, pivot: Any) -> None:
        """Partition list around pivot value. O(n) time, O(1) space"""
        if self.is_empty():
            return

        # Create two dummy nodes for less and greater/equal lists
        less_head = Node(0)
        greater_head = Node(0)

        less_tail = less_head
        greater_tail = greater_head

        current = self.head

        # Traverse and partition
        while current:
            if current.data < pivot:
                less_tail.next = current
                less_tail = less_tail.next
            else:
                greater_tail.next = current
                greater_tail = greater_tail.next
            current = current.next

        # Connect less list to greater list
        less_tail.next = greater_head.next
        greater_tail.next = None  # End the greater list

        # Update head
        self.head = less_head.next


# Demonstration
if __name__ == "__main__":
    print("=== Partition List Demo ===\n")

    # Example from problem description
    sll = SinglyLinkedList()
    values = [3, 5, 8, 5, 10, 2, 1]
    for val in values:
        sll.append(val)

    print("Original list:")
    sll.display()

    pivot = 5
    print(f"\nPartitioning around {pivot}...")
    sll.partition(pivot)

    print("After partition:")
    sll.display()
    print("Note: All values < 5 come before values >= 5")

    # Another example
    print("\n=== Another Example ===")
    sll2 = SinglyLinkedList()
    values2 = [1, 4, 3, 2, 5, 2]
    for val in values2:
        sll2.append(val)

    print("Original list:")
    sll2.display()

    pivot2 = 3
    print(f"\nPartitioning around {pivot2}...")
    sll2.partition(pivot2)

    print("After partition:")
    sll2.display()

    # Edge cases
    print("\n=== Edge Cases ===")

    # All elements < pivot
    sll3 = SinglyLinkedList()
    for val in [1, 2, 3, 4]:
        sll3.append(val)
    print("All < 5:")
    sll3.display()
    sll3.partition(5)
    sll3.display()

    # All elements >= pivot
    sll4 = SinglyLinkedList()
    for val in [5, 6, 7, 8]:
        sll4.append(val)
    print("All >= 5:")
    sll4.display()
    sll4.partition(5)
    sll4.display()

    # Empty list
    sll5 = SinglyLinkedList()
    print("Empty list:")
    sll5.display()
    sll5.partition(5)
    sll5.display()
