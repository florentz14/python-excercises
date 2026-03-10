# -------------------------------------------------
# File Name: 15_lru_cache_simulation.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Simulate LRU Cache using doubly linked list + hashmap.
# -------------------------------------------------

from typing import Optional, Any, Dict


class Node:
    """Node for doubly linked list."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """LRU Cache implementation using doubly linked list and hashmap."""
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> node
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        """Remove node from linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_front(self, node: Node) -> None:
        """Add node right after head (most recently used)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key: Any) -> Any:
        """Get value by key. O(1) time"""
        if key in self.cache:
            node = self.cache[key]
            # Move to front (most recently used)
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return -1  # Not found
    
    def put(self, key, value):
        """Put key-value pair. O(1) time"""
        if key in self.cache:
            # Update existing
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            # Add new
            if len(self.cache) >= self.capacity:
                # Remove least recently used (tail.prev)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
            
            # Add new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)
    
    def display(self) -> None:
        """Display current cache state (for debugging)."""
        print("Cache contents (MRU to LRU):", end=" ")
        current = self.head.next
        while current != self.tail:
            print(f"({current.key}:{current.value})", end=" ")
            current = current.next
        print()


# Demonstration
if __name__ == "__main__":
    print("=== LRU Cache Simulation Demo ===\n")
    
    # Create LRU cache with capacity 3
    cache = LRUCache(3)
    
    print("Capacity: 3")
    print("Operations:")
    
    # Put operations
    print("\nPut(1, 10)")
    cache.put(1, 10)
    cache.display()
    
    print("Put(2, 20)")
    cache.put(2, 20)
    cache.display()
    
    print("Put(3, 30)")
    cache.put(3, 30)
    cache.display()
    
    # Get operation (moves to front)
    print("Get(2) ->", cache.get(2))
    cache.display()
    
    # Put when at capacity (removes LRU)
    print("Put(4, 40) - should evict key 1")
    cache.put(4, 40)
    cache.display()
    
    # Update existing
    print("Put(3, 35) - update existing")
    cache.put(3, 35)
    cache.display()
    
    # Get non-existent
    print("Get(1) ->", cache.get(1), "(should be -1)")
    
    print("\nFinal state:")
    cache.display()
    
    print("\n=== Explanation ===")
    print("LRU Cache maintains order: Most Recently Used -> Least Recently Used")
    print("When capacity exceeded, least recently used item is evicted")
    print("Get/Put operations move items to front (most recently used)")
