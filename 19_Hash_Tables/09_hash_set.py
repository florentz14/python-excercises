# -------------------------------------------------
# File Name: 09_hash_set.py
# Author: Florentino Báez
# Date: 19_Hash_Tables
# Description: HashSet implementation (keys only), duplicate detection, membership.
# -------------------------------------------------

class HashSet:
    """HashSet: keys only, no values. For membership and duplicate detection."""

    def __init__(self, size=16):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        if isinstance(key, int):
            return key % self.size
        return sum(ord(c) for c in str(key)) % self.size

    def add(self, key):
        index = self._hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)
            self.count += 1

    def remove(self, key):
        index = self._hash(key)
        if key in self.table[index]:
            self.table[index].remove(key)
            self.count -= 1
            return True
        return False

    def __contains__(self, key):
        index = self._hash(key)
        return key in self.table[index]

    def __len__(self):
        return self.count

    def __iter__(self):
        for chain in self.table:
            for k in chain:
                yield k


if __name__ == "__main__":
    print("=" * 50)
    print("HASH SET (keys only)")
    print("=" * 50)

    hs = HashSet()
    words = ["apple", "banana", "apple", "cherry", "banana", "date"]
    for w in words:
        hs.add(w)

    print(f"Added: {words}")
    print(f"Unique: {list(hs)}")
    print(f"Size: {len(hs)}")
    print(f"'apple' in hs: {'apple' in hs}")
    print(f"'mango' in hs: {'mango' in hs}")
    hs.remove("banana")
    print(f"After remove 'banana': {list(hs)}")
