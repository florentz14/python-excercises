# -------------------------------------------------
# File: 09_cycle_detection_floyd.py
# Description: Detect cycle in singly linked list.
#              Using Floyd's Tortoise and Hare algorithm.
# -------------------------------------------------

from typing import Any, Optional


class Node:
    """Node for singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next: Optional['Node'] = None


class SinglyLinkedList:
    """Singly Linked List with cycle detection."""

    def __init__(self):
        self.head: Optional[Node] = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.head is None

    def display(self):
        """Display the linked list (limited to prevent infinite loop)."""
        if self.is_empty():
            print("List is empty")
            return

        current = self.head
        count = 0
        while current and count < 20:  # Prevent infinite loop
            print(current.data, end=" -> ")
            current = current.next
            count += 1

        if current:
            print("... (cycle detected or long list)")
        else:
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
        return new_node  # Return node for cycle creation

    def detect_cycle(self) -> bool:
        """Detect cycle using Floyd's Tortoise and Hare algorithm. O(n) time, O(1) space"""
        if self.is_empty():
            return False

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next          # Move slow by 1
            fast = fast.next.next     # Move fast by 2

            if slow == fast:          # Cycle detected
                return True

        return False

    def create_cycle(self, position: int) -> None:
        """Create a cycle for testing (connect last node to node at position)."""
        if position < 0 or position >= self.size:
            print("Invalid position for cycle")
            return

        if self.size < 2:
            print("Need at least 2 nodes to create cycle")
            return

        # Find last node
        assert self.head is not None
        last = self.head
        while last.next:
            last = last.next

        # Find node at position
        cycle_node = self.head
        for i in range(position):
            cycle_node = cycle_node.next
        assert cycle_node is not None

        # Create cycle
        last.next = cycle_node
        print(
            f"Created cycle: last node -> node at position {position} ({cycle_node.data})")


# Demonstration
if __name__ == "__main__":
    print("=== Cycle Detection Demo ===\n")

    # Test 1: No cycle
    print("Test 1: List without cycle")
    sll1 = SinglyLinkedList()
    for i in [1, 2, 3, 4, 5]:
        sll1.append(i)

    sll1.display()
    print(f"Has cycle: {sll1.detect_cycle()}")

    # Test 2: With cycle
    print("\nTest 2: List with cycle")
    sll2 = SinglyLinkedList()
    nodes = []
    for i in [1, 2, 3, 4, 5]:
        node = sll2.append(i)
        nodes.append(node)

    sll2.create_cycle(2)  # Connect last to node with value 3
    print("List with cycle (display limited):")
    sll2.display()
    print(f"Has cycle: {sll2.detect_cycle()}")

    # Test 3: Single node (no cycle)
    print("\nTest 3: Single node")
    sll3 = SinglyLinkedList()
    sll3.append(42)
    sll3.display()
    print(f"Has cycle: {sll3.detect_cycle()}")

    # Test 4: Empty list
    print("\nTest 4: Empty list")
    sll4 = SinglyLinkedList()
    print(f"Has cycle: {sll4.detect_cycle()}")
