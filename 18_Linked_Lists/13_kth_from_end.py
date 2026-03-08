# -------------------------------------------------
# File Name: 13_kth_from_end.py
# Author: Florentino Báez
# Date: 18_Linked_Lists
# Description: Find kth node from the end of linked list.
# -------------------------------------------------

from typing import Any, Optional


class Node:
    """Node for singly linked list."""

    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional["Node"] = None


class SinglyLinkedList:
    """Singly Linked List with kth from end operation."""

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.size: int = 0

    def is_empty(self) -> bool:
        return self.head is None

    def display(self):
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

    def find_kth_from_end(self, k: int) -> Any:
        """Find kth node from the end using two pointers. O(n) time, O(1) space"""
        if self.is_empty() or k <= 0:
            return None

        # First pointer moves k steps ahead
        fast = self.head
        for i in range(k):
            if fast is None:
                return None  # k is larger than list length
            fast = fast.next

        # Second pointer starts from head
        slow = self.head

        # Move both pointers until fast reaches end
        while fast:
            slow = slow.next
            fast = fast.next

        return slow.data if slow else None

    def find_kth_from_end_naive(self, k: int) -> Any:
        """Naive approach: count length first. O(n) time, O(1) space"""
        if self.is_empty() or k <= 0:
            return None

        # Count total nodes
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next

        if k > length:
            return None

        # Find (length - k + 1)th node from start
        target_position = length - k
        current = self.head
        assert current is not None
        for i in range(target_position):
            current = current.next
        assert current is not None
        return current.data


# Demonstration
if __name__ == "__main__":
    sll = SinglyLinkedList()

    print("=== Find Kth From End Demo ===\n")

    # Create list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
    for i in range(1, 8):
        sll.append(i)

    print("List:")
    sll.display()
    print(f"Size: {sll.size}")

    # Test different k values
    test_cases = [1, 2, 3, 4, 5, 7, 8, 0, -1]

    for k in test_cases:
        result_two_pointer = sll.find_kth_from_end(k)
        result_naive = sll.find_kth_from_end_naive(k)
        print(
            f"{k}th from end: {result_two_pointer} (two pointers), {result_naive} (naive)")

    print("\nExplanation:")
    print("For k=1: last element (7)")
    print("For k=2: second last (6)")
    print("For k=3: third last (5)")
    print("etc.")

    # Edge cases
    print("\n=== Edge Cases ===")

    # Empty list
    empty_list = SinglyLinkedList()
    print(f"Empty list, k=1: {empty_list.find_kth_from_end(1)}")

    # Single element
    single_list = SinglyLinkedList()
    single_list.append(42)
    print(f"Single element, k=1: {single_list.find_kth_from_end(1)}")
    print(f"Single element, k=2: {single_list.find_kth_from_end(2)}")
