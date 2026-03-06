# -------------------------------------------------
# File: 02_doubly_linked_list.py
# Description: Doubly Linked List implementation.
#              Nodes with prev and next pointers.
# -------------------------------------------------


class Node:
    """Node for doubly linked list."""
    def __init__(self, data):
        self.data = data          # stores the value
        self.prev = None          # pointer to previous node
        self.next = None          # pointer to next node


class DoublyLinkedList:
    """Doubly Linked List implementation."""
    
    def __init__(self):
        self.head = None          # first node
        self.tail = None          # last node
        self.size = 0             # number of nodes
    
    def is_empty(self):
        """Check if list is empty."""
        return self.head is None
    
    def append(self, data):
        """Add node at the end."""
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def prepend(self, data):
        """Add node at the beginning."""
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    
    def insert(self, data, position):
        """Insert node at specific position."""
        if position < 0 or position > self.size:
            raise IndexError("Position out of range")
        
        if position == 0:
            self.prepend(data)
            return
        if position == self.size:
            self.append(data)
            return
        
        new_node = Node(data)
        current = self.head
        for _ in range(position):
            current = current.next
        
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node
        self.size += 1
    
    def delete(self, data):
        """Delete first occurrence of data."""
        if self.is_empty():
            return False
        
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
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
    
    def display_forward(self):
        """Display list from head to tail."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "None <-> " + " <-> ".join(elements) + " <-> None"
    
    def display_backward(self):
        """Display list from tail to head."""
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.data))
            current = current.prev
        return "None <-> " + " <-> ".join(elements) + " <-> None"
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        return self.display_forward()


# Example usage
if __name__ == "__main__":
    print("=" * 50)
    print("DOUBLY LINKED LIST")
    print("=" * 50)
    
    # Create list
    dll = DoublyLinkedList()
    
    # Append elements
    print("\n1. Appending elements: 10, 20, 30")
    dll.append(10)
    dll.append(20)
    dll.append(30)
    print(f"   Forward:  {dll.display_forward()}")
    print(f"   Backward: {dll.display_backward()}")
    
    # Prepend element
    print("\n2. Prepending 5:")
    dll.prepend(5)
    print(f"   Forward:  {dll.display_forward()}")
    
    # Insert at position
    print("\n3. Inserting 15 at position 2:")
    dll.insert(15, 2)
    print(f"   Forward:  {dll.display_forward()}")
    
    # Search
    print("\n4. Searching:")
    print(f"   Position of 20: {dll.search(20)}")
    print(f"   Position of 100: {dll.search(100)}")
    
    # Delete
    print("\n5. Deleting 15:")
    dll.delete(15)
    print(f"   Forward:  {dll.display_forward()}")
    
    # Size
    print(f"\n6. Size: {len(dll)}")
    
    # Traverse both directions
    print("\n7. Bidirectional traversal:")
    print(f"   Head: {dll.head.data}")
    print(f"   Tail: {dll.tail.data}")
