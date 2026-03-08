# -------------------------------------------------
# File Name: 06_double_hashing.py
# Author: Florentino Báez
# Date: 19_Hash_Tables
# Description: Collision resolution: index = (h1(key) + i * h2(key)) % size.
# -------------------------------------------------

class HashTableDoubleHashing:
    """Hash Table using double hashing: h1 + i * h2."""

    EMPTY = None
    DELETED = "<DELETED>"

    def __init__(self, size=11):
        self.size = size
        self.keys = [self.EMPTY] * size
        self.values = [self.EMPTY] * size
        self.count = 0

    def _h1(self, key):
        """Primary hash function."""
        if isinstance(key, int):
            return key % self.size
        return sum(ord(c) for c in str(key)) % self.size

    def _h2(self, key):
        """Secondary hash function. Must be coprime to size; return 1 + (key % (size-1))."""
        if isinstance(key, int):
            h = key
        else:
            h = sum(ord(c) for c in str(key))
        return 1 + (h % (self.size - 1))  # ensures h2 != 0 and varies

    def _probe(self, index, step, i):
        """index = (h1 + i * h2) % size"""
        return (index + i * step) % self.size

    def insert(self, key, value):
        if self.count >= self.size:
            raise Exception("Hash table is full")

        h1 = self._h1(key)
        h2 = self._h2(key)

        for i in range(self.size):
            idx = self._probe(h1, h2, i)
            if self.keys[idx] in (self.EMPTY, self.DELETED):
                self.keys[idx] = key
                self.values[idx] = value
                self.count += 1
                return
            if self.keys[idx] == key:
                self.values[idx] = value
                return
        raise Exception("Hash table is full")

    def get(self, key):
        h1 = self._h1(key)
        h2 = self._h2(key)
        for i in range(self.size):
            idx = self._probe(h1, h2, i)
            if self.keys[idx] == self.EMPTY:
                raise KeyError(f"Key '{key}' not found")
            if self.keys[idx] == key:
                return self.values[idx]
        raise KeyError(f"Key '{key}' not found")

    def display(self):
        print(f"Double Hashing (size={self.size}, count={self.count}):")
        for i in range(self.size):
            if self.keys[i] == self.EMPTY:
                print(f"  [{i}]: empty")
            elif self.keys[i] == self.DELETED:
                print(f"  [{i}]: <deleted>")
            else:
                print(f"  [{i}]: {self.keys[i]} -> {self.values[i]}")


if __name__ == "__main__":
    print("=" * 50)
    print("DOUBLE HASHING: index = (h1 + i * h2) % size")
    print("=" * 50)

    ht = HashTableDoubleHashing(size=11)
    for k, v in [(10, "a"), (21, "b"), (32, "c"), (5, "d"), (16, "e"), (27, "f")]:
        ht.insert(k, v)
        print(f"Inserted {k} -> {v}")

    print("\nStructure:")
    ht.display()
    print(f"\nht[27] = {ht.get(27)}")
