# -------------------------------------------------
# File: 01_singly_linked_list.py
# Description: Singly Linked List implementation.
#              Basic node-based linear data structure.
# -------------------------------------------------


class Node:
    """Node for singly linked list."""
    def __init__(self, data):
        self.data = data          # stores the value
        self.next = None          # pointer to next node


class SinglyLinkedList:
    """Singly Linked List implementation."""
    
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
        else:
            current = self.head
            while current.next:   # traverse to last node
                current = current.next
            current.next = new_node
        self.size += 1
    
    def prepend(self, data):
        """Add node at the beginning."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert(self, data, position):
        """Insert node at specific position."""
        if position < 0 or position > self.size:
            raise IndexError("Position out of range")
        
        if position == 0:
            self.prepend(data)
            return
        
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete(self, data):
        """Delete first occurrence of data."""
        if self.is_empty():
            return False
        
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False
    
    def search(self, data):
        """Search for data, return position or -1."""
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1
    
    def get(self, position):
        """Get data at position."""
        if position < 0 or position >= self.size:
            raise IndexError("Position out of range")
        
        current = self.head
        for _ in range(position):
            current = current.next
        return current.data
    
    def display(self):
        """Display all elements."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) + " -> None"
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        return self.display()


# Example usage
if __name__ == "__main__":
    print("=" * 50)
    print("SINGLY LINKED LIST")
    print("=" * 50)
    
    # Create list
    sll = SinglyLinkedList()
    
    # Append elements
    print("\n1. Appending elements: 10, 20, 30")
    sll.append(10)
    sll.append(20)
    sll.append(30)
    print(f"   List: {sll}")
    
    # Prepend element
    print("\n2. Prepending 5:")
    sll.prepend(5)
    print(f"   List: {sll}")
    
    # Insert at position
    print("\n3. Inserting 15 at position 2:")
    sll.insert(15, 2)
    print(f"   List: {sll}")
    
    # Search
    print("\n4. Searching:")
    print(f"   Position of 20: {sll.search(20)}")
    print(f"   Position of 100: {sll.search(100)}")
    
    # Get element
    print("\n5. Getting elements:")
    print(f"   Element at position 0: {sll.get(0)}")
    print(f"   Element at position 3: {sll.get(3)}")
    
    # Delete
    print("\n6. Deleting 15:")
    sll.delete(15)
    print(f"   List: {sll}")
    
    # Size
    print(f"\n7. Size: {len(sll)}")
