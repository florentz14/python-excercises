# -------------------------------------------------
# File: 06_delete_operations.py
# Description: Delete operations in singly linked list.
#              Delete head, tail, by value, by position.
# -------------------------------------------------

from typing import Any, Optional


class Node:
    """Node for singly linked list."""

    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional["Node"] = None


class SinglyLinkedList:
    """Singly Linked List with delete operations."""

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
            assert current is not None
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    # Delete operations

    def delete_head(self) -> None:
        """Delete node at the beginning. O(1)"""
        if self.is_empty():
            print("List is empty")
            return

        deleted_data = self.head.data
        self.head = self.head.next
        self.size -= 1
        print(f"Deleted head: {deleted_data}")

    def delete_tail(self):
        """Delete node at the end. O(n)"""
        if self.is_empty():
            print("List is empty")
            return
        assert self.head is not None
        if self.head.next is None:  # Only one node
            deleted_data = self.head.data
            self.head = None
        else:
            current = self.head
            assert current is not None
            while current.next and current.next.next:  # Go to second last
                current = current.next
            assert current.next is not None
            deleted_data = current.next.data
            current.next = None

        self.size -= 1
        print(f"Deleted tail: {deleted_data}")

    def delete_by_value(self, value: Any) -> None:
        """Delete first occurrence of a value. O(n)"""
        if self.is_empty():
            print("List is empty")
            return
        assert self.head is not None
        if self.head.data == value:
            self.head = self.head.next
            self.size -= 1
            print(f"Deleted value: {value}")
            return

        current = self.head
        assert current is not None
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                self.size -= 1
                print(f"Deleted value: {value}")
                return
            current = current.next

        print(f"Value {value} not found")

    def delete_by_position(self, position: int) -> None:
        """Delete node at specific position. O(n)"""
        if self.is_empty():
            print("List is empty")
            return

        if position < 0 or position >= self.size:
            print("Invalid position")
            return

        assert self.head is not None
        if position == 0:
            deleted_data = self.head.data
            self.head = self.head.next
        else:
            current = self.head
            for i in range(position - 1):
                current = current.next
            assert current is not None and current.next is not None
            deleted_data = current.next.data
            current.next = current.next.next

        self.size -= 1
        print(f"Deleted at position {position}: {deleted_data}")


# Demonstration
if __name__ == "__main__":
    sll = SinglyLinkedList()

    print("=== Delete Operations Demo ===\n")

    # Create initial list
    for i in [10, 20, 30, 40, 50]:
        sll.append(i)

    print("Initial list:")
    sll.display()

    # Delete head
    sll.delete_head()
    sll.display()

    # Delete tail
    sll.delete_tail()
    sll.display()

    # Delete by value
    sll.delete_by_value(30)
    sll.display()

    # Delete by position
    sll.delete_by_position(1)  # Should delete 40
    sll.display()

    print(f"\nFinal size: {sll.size}")
