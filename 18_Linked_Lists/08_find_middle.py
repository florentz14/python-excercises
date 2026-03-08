# -------------------------------------------------
# File Name: 08_find_middle.py
# Author: Florentino Báez
# Date: 18_Linked_Lists
# Description: Find middle node of singly linked list.
# -------------------------------------------------

from typing import Any, Optional


class Node:
    """Node for singly linked list."""

    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional['Node'] = None


class SinglyLinkedList:
    """Singly Linked List with middle finding operation."""

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

    def find_middle(self) -> Any:
        """Find middle node using slow and fast pointers. O(n) time, O(1) space"""
        if self.is_empty():
            return None

        assert self.head is not None
        slow: Optional[Node] = self.head
        fast: Optional[Node] = self.head

        # Fast moves 2 steps, slow moves 1 step
        while fast and fast.next:
            slow = slow.next if slow else None
            fast = fast.next.next if fast and fast.next else None

        assert slow is not None
        return slow.data

    def find_middle_naive(self) -> Any:
        """Naive approach: count nodes first, then traverse. O(n) time, O(1) space"""
        if self.is_empty():
            return None

        # Count total nodes
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next

        # Find middle
        middle_index = count // 2
        current = self.head
        assert current is not None
        for i in range(middle_index):
            current = current.next
        assert current is not None
        return current.data


# Demonstration
if __name__ == "__main__":
    sll = SinglyLinkedList()

    print("=== Find Middle Node Demo ===\n")

    # Test with odd number of nodes
    print("Odd number of nodes:")
    for i in [1, 2, 3, 4, 5]:
        sll.append(i)

    sll.display()
    print(f"Middle (slow/fast): {sll.find_middle()}")
    print(f"Middle (naive): {sll.find_middle_naive()}")

    print("\nEven number of nodes:")
    sll.append(6)
    sll.display()
    # Returns 3rd node (0-based index 2)
    print(f"Middle (slow/fast): {sll.find_middle()}")
    print(f"Middle (naive): {sll.find_middle_naive()}")

    print("\nSingle node:")
    single_list = SinglyLinkedList()
    single_list.append(42)
    single_list.display()
    print(f"Middle: {single_list.find_middle()}")

    print("\nEmpty list:")
    empty_list = SinglyLinkedList()
    print(f"Middle: {empty_list.find_middle()}")
