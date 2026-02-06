# -------------------------------------------------
# File: 01_hash_table_chaining.py
# Description: Hash Table with Chaining.
#              Collision handling using linked lists.
# -------------------------------------------------


class HashTable:
    """Hash Table implementation using chaining for collisions."""
    
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # list of lists (chains)
        self.count = 0
    
    def _hash(self, key):
        """Simple hash function."""
        if isinstance(key, int):
            return key % self.size
        # String hash
        hash_value = 0
        for char in str(key):
            hash_value += ord(char)
        return hash_value % self.size
    
    def insert(self, key, value):
        """Insert or update key-value pair."""
        index = self._hash(key)
        
        # Check if key exists, update if so
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        
        # Key doesn't exist, add new pair
        self.table[index].append((key, value))
        self.count += 1
    
    def get(self, key):
        """Get value by key."""
        index = self._hash(key)
        
        for k, v in self.table[index]:
            if k == key:
                return v
        
        raise KeyError(f"Key '{key}' not found")
    
    def remove(self, key):
        """Remove key-value pair."""
        index = self._hash(key)
        
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                self.count -= 1
                return True
        
        return False
    
    def contains(self, key):
        """Check if key exists."""
        index = self._hash(key)
        
        for k, v in self.table[index]:
            if k == key:
                return True
        return False
    
    def keys(self):
        """Return all keys."""
        all_keys = []
        for chain in self.table:
            for k, v in chain:
                all_keys.append(k)
        return all_keys
    
    def values(self):
        """Return all values."""
        all_values = []
        for chain in self.table:
            for k, v in chain:
                all_values.append(v)
        return all_values
    
    def items(self):
        """Return all key-value pairs."""
        all_items = []
        for chain in self.table:
            for k, v in chain:
                all_items.append((k, v))
        return all_items
    
    def display(self):
        """Display hash table structure."""
        print(f"Hash Table (size={self.size}, count={self.count}):")
        for i, chain in enumerate(self.table):
            if chain:
                print(f"  [{i}]: {chain}")
            else:
                print(f"  [{i}]: empty")
    
    def load_factor(self):
        """Calculate load factor."""
        return self.count / self.size
    
    def __len__(self):
        return self.count
    
    def __setitem__(self, key, value):
        self.insert(key, value)
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __contains__(self, key):
        return self.contains(key)


# Example usage
if __name__ == "__main__":
    print("=" * 50)
    print("HASH TABLE WITH CHAINING")
    print("=" * 50)
    
    # Create hash table
    ht = HashTable(size=7)
    
    # Insert elements
    print("\n1. Inserting elements:")
    data = [
        ("apple", 5),
        ("banana", 3),
        ("cherry", 8),
        ("date", 2),
        ("elderberry", 7),
        ("fig", 4),
        ("grape", 6)
    ]
    
    for key, value in data:
        ht.insert(key, value)
        print(f"   Inserted: {key} -> {value}")
    
    # Display structure
    print("\n2. Hash table structure:")
    ht.display()
    
    # Get values
    print("\n3. Getting values:")
    print(f"   ht['apple'] = {ht['apple']}")
    print(f"   ht['cherry'] = {ht['cherry']}")
    
    # Check contains
    print("\n4. Contains check:")
    print(f"   'banana' in ht: {'banana' in ht}")
    print(f"   'mango' in ht: {'mango' in ht}")
    
    # Update value
    print("\n5. Updating 'apple' to 10:")
    ht['apple'] = 10
    print(f"   ht['apple'] = {ht['apple']}")
    
    # Remove element
    print("\n6. Removing 'date':")
    ht.remove('date')
    print(f"   Keys: {ht.keys()}")
    
    # Statistics
    print(f"\n7. Statistics:")
    print(f"   Size: {len(ht)}")
    print(f"   Load factor: {ht.load_factor():.2f}")
