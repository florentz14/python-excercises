# -------------------------------------------------
# File Name: 11_remove_duplicates.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Remove duplicates from singly linked list.
# -------------------------------------------------

from typing import Any, Optional


class Node:
    """Node for singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next: Optional['Node'] = None


class SinglyLinkedList:
    """Singly Linked List with duplicate removal."""

    def __init__(self):
        self.head: Optional[Node] = None
        self.size = 0

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

    def remove_duplicates_sorted(self) -> None:
        """Remove duplicates from sorted linked list. O(n) time"""
        if self.is_empty():
            return

        current = self.head
        assert current is not None

        while current and current.next:
            if current.data == current.next.data:
                # Skip the duplicate
                current.next = current.next.next
                self.size -= 1
            else:
                current = current.next

        print("Duplicates removed from sorted list")

    def remove_duplicates_unsorted(self) -> None:
        """Remove duplicates from unsorted linked list using hash set. O(n) time, O(n) space"""
        if self.is_empty():
            return

        seen = set()
        current = self.head
        prev = None

        while current:
            if current.data in seen:
                # Remove duplicate (prev is not None: we've seen at least one unique node)
                assert prev is not None
                prev.next = current.next
                self.size -= 1
            else:
                seen.add(current.data)
                prev = current
            current = current.next

        print("Duplicates removed from unsorted list")

    def remove_duplicates_no_extra_space(self) -> None:
        """Remove duplicates without extra space (brute force). O(n^2) time, O(1) space"""
        if self.is_empty():
            return

        current = self.head
        assert current is not None

        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                    self.size -= 1
                else:
                    runner = runner.next
            current = current.next

        print("Duplicates removed (no extra space)")


# Demonstration
if __name__ == "__main__":
    print("=== Remove Duplicates Demo ===\n")

    # Test 1: Sorted list with duplicates
    print("Test 1: Sorted list with duplicates")
    sorted_list = SinglyLinkedList()
    for val in [1, 1, 2, 3, 3, 3, 4, 5, 5]:
        sorted_list.append(val)

    print("Original:")
    sorted_list.display()
    sorted_list.remove_duplicates_sorted()
    print("After removing duplicates:")
    sorted_list.display()

    # Test 2: Unsorted list with duplicates
    print("\nTest 2: Unsorted list with duplicates")
    unsorted_list = SinglyLinkedList()
    for val in [3, 1, 2, 3, 4, 2, 1, 5]:
        unsorted_list.append(val)

    print("Original:")
    unsorted_list.display()
    unsorted_list.remove_duplicates_unsorted()
    print("After removing duplicates:")
    unsorted_list.display()

    # Test 3: No extra space approach
    print("\nTest 3: No extra space (brute force)")
    brute_list = SinglyLinkedList()
    for val in [1, 2, 2, 3, 1, 4]:
        brute_list.append(val)

    print("Original:")
    brute_list.display()
    brute_list.remove_duplicates_no_extra_space()
    print("After removing duplicates:")
    brute_list.display()

    # Test 4: No duplicates
    print("\nTest 4: List with no duplicates")
    no_dup_list = SinglyLinkedList()
    for val in [1, 2, 3, 4, 5]:
        no_dup_list.append(val)

    print("Original:")
    no_dup_list.display()
    no_dup_list.remove_duplicates_unsorted()
    print("After (no change expected):")
    no_dup_list.display()
