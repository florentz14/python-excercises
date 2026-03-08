# -------------------------------------------------
# File Name: 12_bloom_filter.py
# Author: Florentino Báez
# Date: 19_Hash_Tables
# Description: Probabilistic membership with multiple hash functions.
# -------------------------------------------------


class BloomFilter:
    """Probabilistic set: may have false positives, no false negatives.
    Uses multiple hash variants (Python built-in) for independence."""

    def __init__(self, size=1000, num_hashes=3):
        self.size = size
        self.num_hashes = num_hashes
        self.bits = [False] * size

    def _hashes(self, key):
        s = str(key)
        return [(hash(s + str(i) + "salt") % self.size + i * 31) % self.size for i in range(self.num_hashes)]

    def add(self, key):
        for i in self._hashes(key):
            self.bits[i] = True

    def __contains__(self, key):
        return all(self.bits[i] for i in self._hashes(key))


if __name__ == "__main__":
    bf = BloomFilter(size=100, num_hashes=3)

    print("=" * 50)
    print("BLOOM FILTER (probabilistic membership)")
    print("=" * 50)

    for w in ["apple", "banana", "cherry"]:
        bf.add(w)

    print("Added: apple, banana, cherry")
    print(f"'apple' in bf: {'apple' in bf}")
    print(f"'mango' in bf: {'mango' in bf}")
    print("(mango may be false positive; apple/cherry are definitely in)")
