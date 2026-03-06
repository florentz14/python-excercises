# -------------------------------------------------
# File: 04_linked_list_operations.py
# Description: Common Linked List operations.
#              Reverse, merge, detect cycle, find middle.
# -------------------------------------------------


class Node:
    """Node for singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Linked List with common operations."""
    
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Add node at the end."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def display(self):
        """Display list."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) + " -> None"
    
    # ===============================
    # COMMON OPERATIONS
    # ===============================
    
    def reverse(self):
        """Reverse the linked list in-place."""
        prev = None
        current = self.head
        while current:
            next_node = current.next  # save next
            current.next = prev       # reverse pointer
            prev = current            # move prev forward
            current = next_node       # move current forward
        self.head = prev
    
    def find_middle(self):
        """Find middle element using slow/fast pointers."""
        if not self.head:
            return None
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next          # moves 1 step
            fast = fast.next.next     # moves 2 steps
        
        return slow.data
    
    def detect_cycle(self):
        """Detect if list has a cycle (Floyd's algorithm)."""
        if not self.head:
            return False
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def remove_duplicates(self):
        """Remove duplicate elements."""
        if not self.head:
            return
        
        seen = set()
        current = self.head
        seen.add(current.data)
        
        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.data)
                current = current.next
    
    def get_nth_from_end(self, n):
        """Get nth element from the end."""
        if not self.head or n <= 0:
            return None
        
        first = self.head
        second = self.head
        
        # Move first n nodes ahead
        for _ in range(n):
            if not first:
                return None
            first = first.next
        
        # Move both until first reaches end
        while first:
            first = first.next
            second = second.next
        
        return second.data
    
    def to_list(self):
        """Convert to Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


def merge_sorted_lists(list1, list2):
    """Merge two sorted linked lists."""
    dummy = Node(0)
    current = dummy
    
    p1 = list1.head
    p2 = list2.head
    
    while p1 and p2:
        if p1.data <= p2.data:
            current.next = p1
            p1 = p1.next
        else:
            current.next = p2
            p2 = p2.next
        current = current.next
    
    # Attach remaining nodes
    current.next = p1 if p1 else p2
    
    result = LinkedList()
    result.head = dummy.next
    return result


# Example usage
if __name__ == "__main__":
    print("=" * 50)
    print("LINKED LIST OPERATIONS")
    print("=" * 50)
    
    # Create list
    ll = LinkedList()
    for val in [1, 2, 3, 4, 5]:
        ll.append(val)
    
    print(f"\n1. Original list: {ll.display()}")
    
    # Find middle
    print(f"\n2. Middle element: {ll.find_middle()}")
    
    # Get nth from end
    print(f"\n3. 2nd element from end: {ll.get_nth_from_end(2)}")
    
    # Reverse
    ll.reverse()
    print(f"\n4. Reversed list: {ll.display()}")
    
    # Reverse back
    ll.reverse()
    
    # Remove duplicates
    print("\n5. Remove duplicates:")
    ll2 = LinkedList()
    for val in [1, 2, 2, 3, 3, 3, 4]:
        ll2.append(val)
    print(f"   Before: {ll2.display()}")
    ll2.remove_duplicates()
    print(f"   After:  {ll2.display()}")
    
    # Detect cycle (no cycle)
    print(f"\n6. Has cycle: {ll.detect_cycle()}")
    
    # Merge sorted lists
    print("\n7. Merge sorted lists:")
    list_a = LinkedList()
    list_b = LinkedList()
    for val in [1, 3, 5, 7]:
        list_a.append(val)
    for val in [2, 4, 6, 8]:
        list_b.append(val)
    print(f"   List A: {list_a.display()}")
    print(f"   List B: {list_b.display()}")
    merged = merge_sorted_lists(list_a, list_b)
    print(f"   Merged: {merged.display()}")
    
    # Convert to list
    print(f"\n8. As Python list: {ll.to_list()}")
