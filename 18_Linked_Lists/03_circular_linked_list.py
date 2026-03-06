# -------------------------------------------------
# File: 03_circular_linked_list.py
# Description: Circular Linked List implementation.
#              Last node points back to first node.
# -------------------------------------------------


class Node:
    """Node for circular linked list."""
    def __init__(self, data):
        self.data = data          # stores the value
        self.next = None          # pointer to next node


class CircularLinkedList:
    """Circular Linked List implementation."""
    
    def __init__(self):
        self.head = None          # first node
        self.size = 0             # number of nodes
    
    def is_empty(self):
        """Check if list is empty."""
        return self.head is None
    
    def append(self, data):
        """Add node at the end."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head  # point to itself
        else:
            current = self.head
            while current.next != self.head:  # traverse to last node
                current = current.next
            current.next = new_node
            new_node.next = self.head  # complete the circle
        self.size += 1
    
    def prepend(self, data):
        """Add node at the beginning."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            # Find last node
            current = self.head
            while current.next != self.head:
                current = current.next
            
            new_node.next = self.head
            current.next = new_node
            self.head = new_node
        self.size += 1
    
    def delete(self, data):
        """Delete first occurrence of data."""
        if self.is_empty():
            return False
        
        # Case: single node
        if self.head.data == data and self.head.next == self.head:
            self.head = None
            self.size -= 1
            return True
        
        # Case: head node
        if self.head.data == data:
            # Find last node
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            self.size -= 1
            return True
        
        # Case: other nodes
        current = self.head
        while current.next != self.head:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False
    
    def search(self, data):
        """Search for data, return position or -1."""
        if self.is_empty():
            return -1
        
        current = self.head
        position = 0
        while True:
            if current.data == data:
                return position
            current = current.next
            position += 1
            if current == self.head:
                break
        return -1
    
    def display(self):
        """Display all elements."""
        if self.is_empty():
            return "Empty list"
        
        elements = []
        current = self.head
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        return " -> ".join(elements) + " -> (back to head)"
    
    def traverse(self, times=1):
        """Traverse the circular list multiple times."""
        if self.is_empty():
            return []
        
        result = []
        current = self.head
        for _ in range(self.size * times):
            result.append(current.data)
            current = current.next
        return result
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        return self.display()


# Example usage
if __name__ == "__main__":
    print("=" * 50)
    print("CIRCULAR LINKED LIST")
    print("=" * 50)
    
    # Create list
    cll = CircularLinkedList()
    
    # Append elements
    print("\n1. Appending elements: 10, 20, 30")
    cll.append(10)
    cll.append(20)
    cll.append(30)
    print(f"   List: {cll}")
    
    # Prepend element
    print("\n2. Prepending 5:")
    cll.prepend(5)
    print(f"   List: {cll}")
    
    # Search
    print("\n3. Searching:")
    print(f"   Position of 20: {cll.search(20)}")
    print(f"   Position of 100: {cll.search(100)}")
    
    # Circular traversal
    print("\n4. Circular traversal (2 times around):")
    print(f"   Elements: {cll.traverse(2)}")
    
    # Delete
    print("\n5. Deleting 20:")
    cll.delete(20)
    print(f"   List: {cll}")
    
    # Size
    print(f"\n6. Size: {len(cll)}")
    
    # Verify circularity
    print("\n7. Verifying circularity:")
    current = cll.head
    for i in range(len(cll) + 2):
        print(f"   Step {i}: {current.data}")
        current = current.next
