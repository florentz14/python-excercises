# -------------------------------------------------
# File Name: 12_intersection_of_lists.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Find intersection point of two linked lists.
# -------------------------------------------------

from typing import Any, Optional


class Node:
    """Node for singly linked list."""

    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional['Node'] = None


class SinglyLinkedList:
    """Singly Linked List with intersection finding."""

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

    def append(self, data: Any) -> Node:
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
        return new_node

    def get_length(self) -> int:
        """Get length of the list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def find_intersection(self, other: "SinglyLinkedList") -> Any:
        """Find intersection point of two linked lists. O(m+n) time, O(1) space"""
        if not self.head or not other.head:
            return None

        # Get lengths
        len1 = self.get_length()
        len2 = other.get_length()

        # Align the starting points
        current1 = self.head
        current2 = other.head

        # Move the longer list's pointer ahead by the difference
        if len1 > len2:
            for i in range(len1 - len2):
                assert current1 is not None
                current1 = current1.next
        else:
            for i in range(len2 - len1):
                assert current2 is not None
                current2 = current2.next

        # Move both pointers until they meet
        while current1 and current2:
            if current1 == current2:  # Same node reference
                return current1.data
            current1 = current1.next
            current2 = current2.next

        return None  # No intersection


# Demonstration
if __name__ == "__main__":
    print("=== Find Intersection of Two Lists Demo ===\n")

    # Create intersecting lists
    # List 1: 1 -> 2 -> 3 -> 4 -> 5
    # List 2: 6 -> 7 -> 4 -> 5
    # Intersection at node with value 4

    list1 = SinglyLinkedList()
    list2 = SinglyLinkedList()

    # Common tail: 4 -> 5
    common_node = list1.append(4)
    list1.append(5)

    # List 1 prefix: 1 -> 2 -> 3
    list1.head = Node(1)
    list1.head.next = Node(2)
    list1.head.next.next = Node(3)
    list1.head.next.next.next = common_node
    list1.size = 5

    # List 2 prefix: 6 -> 7
    list2.head = Node(6)
    list2.head.next = Node(7)
    list2.head.next.next = common_node
    list2.size = 4

    print("List 1:")
    list1.display()
    print("List 2:")
    list2.display()

    intersection = list1.find_intersection(list2)
    if intersection:
        print(f"Intersection found at node with value: {intersection}")
    else:
        print("No intersection found")

    # Test 2: No intersection
    print("\n=== Test 2: No intersection ===")
    list3 = SinglyLinkedList()
    list4 = SinglyLinkedList()

    for val in [1, 2, 3]:
        list3.append(val)

    for val in [4, 5, 6]:
        list4.append(val)

    print("List 3:")
    list3.display()
    print("List 4:")
    list4.display()

    intersection2 = list3.find_intersection(list4)
    if intersection2:
        print(f"Intersection found at node with value: {intersection2}")
    else:
        print("No intersection found")

    # Test 3: One empty list
    print("\n=== Test 3: One empty list ===")
    empty_list = SinglyLinkedList()
    intersection3 = list3.find_intersection(empty_list)
    print(f"Intersection with empty list: {intersection3}")
