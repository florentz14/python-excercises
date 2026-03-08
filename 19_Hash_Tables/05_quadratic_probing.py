# -------------------------------------------------
# File Name: 05_quadratic_probing.py
# Author: Florentino Báez
# Date: 19_Hash_Tables
# Description: Open addressing with quadratic probing: i + 1², i + 2², i + 3²...
# -------------------------------------------------

class HashTableQuadratic:
    """Hash Table using quadratic probing to avoid linear clustering."""

    EMPTY = None
    DELETED = "<DELETED>"

    def __init__(self, size=11):
        self.size = size
        self.keys = [self.EMPTY] * size
        self.values = [self.EMPTY] * size
        self.count = 0

    def _hash(self, key):
        if isinstance(key, int):
            return key % self.size
        return sum(ord(c) for c in str(key)) % self.size

    def _probe(self, index, i):
        """Quadratic: index + i² (i = 0, 1, 2, ...)"""
        return (index + i * i) % self.size

    def insert(self, key, value):
        if self.count >= self.size:
            raise Exception("Hash table is full")

        index = self._hash(key)
        for i in range(self.size):
            idx = self._probe(index, i)
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
        index = self._hash(key)
        for i in range(self.size):
            idx = self._probe(index, i)
            if self.keys[idx] == self.EMPTY:
                raise KeyError(f"Key '{key}' not found")
            if self.keys[idx] == key:
                return self.values[idx]
        raise KeyError(f"Key '{key}' not found")

    def remove(self, key):
        index = self._hash(key)
        for i in range(self.size):
            idx = self._probe(index, i)
            if self.keys[idx] == self.EMPTY:
                return False
            if self.keys[idx] == key:
                self.keys[idx] = self.DELETED
                self.values[idx] = self.EMPTY
                self.count -= 1
                return True
        return False

    def display(self):
        print(f"Quadratic Probing (size={self.size}, count={self.count}):")
        for i in range(self.size):
            if self.keys[i] == self.EMPTY:
                print(f"  [{i}]: empty")
            elif self.keys[i] == self.DELETED:
                print(f"  [{i}]: <deleted>")
            else:
                print(f"  [{i}]: {self.keys[i]} -> {self.values[i]}")


if __name__ == "__main__":
    print("=" * 50)
    print("QUADRATIC PROBING (avoids linear clustering)")
    print("=" * 50)

    ht = HashTableQuadratic(size=11)
    for k, v in [(10, "a"), (21, "b"), (32, "c"), (5, "d"), (16, "e")]:
        ht.insert(k, v)
        print(f"Inserted {k} -> {v}")

    print("\nStructure:")
    ht.display()
    print(f"\nht[32] = {ht.get(32)}")
    print(f"ht[21] = {ht.get(21)}")
