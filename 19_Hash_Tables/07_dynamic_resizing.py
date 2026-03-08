# -------------------------------------------------
# File Name: 07_dynamic_resizing.py
# Author: Florentino Báez
# Date: 19_Hash_Tables
# Description: Dynamic resizing, load factor, rehashing.
# -------------------------------------------------

class HashTableDynamic:
    """Hash Table with automatic resizing when load_factor > threshold."""

    def __init__(self, initial_size=8, load_threshold=0.7):
        self.size = initial_size
        self.threshold = load_threshold
        self.table = [[] for _ in range(self.size)]
        self.count = 0

    def _hash(self, key):
        if isinstance(key, int):
            return key % self.size
        return sum(ord(c) for c in str(key)) % self.size

    def _rehash(self):
        """Expand table and reinsert all elements."""
        old_table = self.table
        self.size = 2 * self.size
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        for chain in old_table:
            for k, v in chain:
                self._insert_internal(k, v)

        print(f"  [rehash] new size = {self.size}")

    def _insert_internal(self, key, value):
        """Insert without triggering rehash."""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
        self.count += 1

    def insert(self, key, value):
        if self.load_factor() >= self.threshold:
            self._rehash()
        self._insert_internal(key, value)

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found")

    def load_factor(self):
        return self.count / self.size

    def __len__(self):
        return self.count

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.insert(key, value)


if __name__ == "__main__":
    print("=" * 50)
    print("DYNAMIC RESIZING (load_factor > 0.7 -> expand)")
    print("=" * 50)

    ht = HashTableDynamic(initial_size=4, load_threshold=0.7)

    for i in range(10):
        ht[f"key_{i}"] = i
        print(f"Insert key_{i}: size={ht.size}, count={len(ht)}, load={ht.load_factor():.2f}")

    print(f"\nFinal: size={ht.size}, count={len(ht)}")
    print(f"ht['key_5'] = {ht['key_5']}")
