# -------------------------------------------------
# File Name: 10_merge_two_sorted_lists.py
# Author: Florentino Báez
# Date: 18_Linked_Lists
# Description: Merge two sorted singly linked lists.
# -------------------------------------------------

from typing import Any, Optional


class Node:
    """Node for singly linked list."""

    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional['Node'] = None


class SinglyLinkedList:
    """Singly Linked List with merge operations."""

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

    def merge_sorted(self, other: "SinglyLinkedList") -> "SinglyLinkedList":
        """Merge two sorted linked lists. Returns new merged list."""
        # Create dummy node for easy handling
        dummy = Node(0)
        current = dummy

        # Pointers for both lists
        p1 = self.head
        p2 = other.head

        # Merge while both lists have nodes
        while p1 and p2:
            if p1.data <= p2.data:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next

        # Attach remaining nodes
        if p1:
            current.next = p1
        if p2:
            current.next = p2

        # Create new list with merged result
        merged_list = SinglyLinkedList()
        merged_list.head = dummy.next

        # Calculate size
        temp = merged_list.head
        while temp:
            merged_list.size += 1
            temp = temp.next

        return merged_list

    def merge_sorted_in_place(self, other: "SinglyLinkedList") -> None:
        """Merge two sorted lists in-place, modifying self."""
        if not other.head:
            return
        if not self.head:
            self.head = other.head
            self.size = other.size
            return

        # Determine which list starts smaller
        if self.head.data > other.head.data:
            self.head, other.head = other.head, self.head

        current = self.head

        while current.next and other.head:
            if current.next.data > other.head.data:
                # Insert other node here
                temp = other.head
                other.head = other.head.next
                temp.next = current.next
                current.next = temp
                self.size += 1
            current = current.next

        # Attach remaining nodes from other list
        if other.head:
            assert current is not None
            current.next = other.head
            # Update size
            temp = other.head
            while temp:
                self.size += 1
                temp = temp.next


# Demonstration
if __name__ == "__main__":
    print("=== Merge Two Sorted Lists Demo ===\n")

    # Create first sorted list
    list1 = SinglyLinkedList()
    for val in [1, 3, 5, 7]:
        list1.append(val)

    print("List 1:")
    list1.display()

    # Create second sorted list
    list2 = SinglyLinkedList()
    for val in [2, 4, 6, 8]:
        list2.append(val)

    print("List 2:")
    list2.display()

    # Merge using new list approach
    merged = list1.merge_sorted(list2)
    print("Merged (new list):")
    merged.display()

    print(f"Merged size: {merged.size}")

    # Test in-place merge
    print("\n=== In-place merge test ===")
    list3 = SinglyLinkedList()
    for val in [1, 4, 7]:
        list3.append(val)

    list4 = SinglyLinkedList()
    for val in [2, 3, 5, 6]:
        list4.append(val)

    print("List 3:")
    list3.display()
    print("List 4:")
    list4.display()

    list3.merge_sorted_in_place(list4)
    print("After in-place merge (list3):")
    list3.display()
    print(f"Final size: {list3.size}")
