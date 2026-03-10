# -------------------------------------------------
# File Name: 05_insert_operations.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Insert operations in singly linked list.
# -------------------------------------------------

from typing import Any, Optional


class Node:
    """Node for singly linked list."""

    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional['Node'] = None


class SinglyLinkedList:
    """Singly Linked List with insert operations."""

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

    # Insert operations

    def insert_at_beginning(self, data):
        """Insert node at the beginning. O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        print(f"Inserted {data} at beginning")

    def insert_at_end(self, data: Any) -> None:
        """Insert node at the end. O(n)"""
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
        print(f"Inserted {data} at end")

    def insert_at_position(self, data, position):
        """Insert node at specific position. O(n)"""
        if position < 0 or position > self.size:
            print("Invalid position")
            return

        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            assert current is not None
            for i in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.size += 1
        print(f"Inserted {data} at position {position}")

    def insert_after_node(self, prev_data: Any, data: Any) -> None:
        """Insert node after a specific node value. O(n)"""
        current = self.head
        while current:
            if current.data == prev_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                self.size += 1
                print(f"Inserted {data} after {prev_data}")
                return
            current = current.next
        print(f"Node with data {prev_data} not found")


# Demonstration
if __name__ == "__main__":
    sll = SinglyLinkedList()

    print("=== Insert Operations Demo ===\n")

    # Insert at beginning
    sll.insert_at_beginning(10)
    sll.display()

    sll.insert_at_beginning(5)
    sll.display()

    # Insert at end
    sll.insert_at_end(20)
    sll.display()

    sll.insert_at_end(30)
    sll.display()

    # Insert at position
    sll.insert_at_position(15, 2)  # Between 10 and 20
    sll.display()

    # Insert after node
    sll.insert_after_node(20, 25)
    sll.display()

    print(f"\nFinal size: {sll.size}")
