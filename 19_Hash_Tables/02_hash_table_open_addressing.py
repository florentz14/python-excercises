# -------------------------------------------------
# File: 02_hash_table_open_addressing.py
# Description: Hash Table with Open Addressing.
#              Linear probing for collision handling.
# -------------------------------------------------


class HashTableOpenAddressing:
    """Hash Table using open addressing (linear probing)."""
    
    EMPTY = None
    DELETED = "<DELETED>"
    
    def __init__(self, size=10):
        self.size = size
        self.keys = [self.EMPTY] * size
        self.values = [self.EMPTY] * size
        self.count = 0
    
    def _hash(self, key):
        """Primary hash function."""
        if isinstance(key, int):
            return key % self.size
        hash_value = 0
        for char in str(key):
            hash_value += ord(char)
        return hash_value % self.size
    
    def _probe(self, index):
        """Linear probing: next index."""
        return (index + 1) % self.size
    
    def insert(self, key, value):
        """Insert or update key-value pair."""
        if self.count >= self.size:
            raise Exception("Hash table is full")
        
        index = self._hash(key)
        original_index = index
        
        while self.keys[index] not in (self.EMPTY, self.DELETED):
            if self.keys[index] == key:
                # Update existing key
                self.values[index] = value
                return
            index = self._probe(index)
            if index == original_index:
                raise Exception("Hash table is full")
        
        self.keys[index] = key
        self.values[index] = value
        self.count += 1
    
    def get(self, key):
        """Get value by key."""
        index = self._hash(key)
        original_index = index
        
        while self.keys[index] != self.EMPTY:
            if self.keys[index] == key:
                return self.values[index]
            index = self._probe(index)
            if index == original_index:
                break
        
        raise KeyError(f"Key '{key}' not found")
    
    def remove(self, key):
        """Remove key-value pair."""
        index = self._hash(key)
        original_index = index
        
        while self.keys[index] != self.EMPTY:
            if self.keys[index] == key:
                self.keys[index] = self.DELETED
                self.values[index] = self.EMPTY
                self.count -= 1
                return True
            index = self._probe(index)
            if index == original_index:
                break
        
        return False
    
    def contains(self, key):
        """Check if key exists."""
        try:
            self.get(key)
            return True
        except KeyError:
            return False
    
    def display(self):
        """Display hash table structure."""
        print(f"Hash Table (size={self.size}, count={self.count}):")
        for i in range(self.size):
            if self.keys[i] == self.EMPTY:
                print(f"  [{i}]: empty")
            elif self.keys[i] == self.DELETED:
                print(f"  [{i}]: <deleted>")
            else:
                print(f"  [{i}]: {self.keys[i]} -> {self.values[i]}")
    
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
    print("HASH TABLE WITH OPEN ADDRESSING")
    print("=" * 50)
    
    # Create hash table
    ht = HashTableOpenAddressing(size=11)
    
    # Insert elements
    print("\n1. Inserting elements:")
    data = [
        (10, "ten"),
        (21, "twenty-one"),   # Will collide with 10 (both % 11 = 10)
        (32, "thirty-two"),   # Will collide again
        (5, "five"),
        (16, "sixteen"),      # Will collide with 5
    ]
    
    for key, value in data:
        ht.insert(key, value)
        print(f"   Inserted: {key} -> {value}")
    
    # Display structure
    print("\n2. Hash table structure (showing collisions):")
    ht.display()
    
    # Get values
    print("\n3. Getting values:")
    print(f"   ht[10] = {ht[10]}")
    print(f"   ht[21] = {ht[21]}")
    print(f"   ht[32] = {ht[32]}")
    
    # Check contains
    print("\n4. Contains check:")
    print(f"   10 in ht: {10 in ht}")
    print(f"   99 in ht: {99 in ht}")
    
    # Remove element
    print("\n5. Removing key 21:")
    ht.remove(21)
    ht.display()
    
    # Can still find 32 after deleting 21
    print(f"\n6. ht[32] after deletion: {ht[32]}")
    
    # Statistics
    print(f"\n7. Statistics:")
    print(f"   Size: {len(ht)}")
    print(f"   Load factor: {ht.load_factor():.2f}")
