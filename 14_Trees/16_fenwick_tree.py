"""
14_Trees - Fenwick Tree (Binary Indexed Tree)
==============================================
Simpler than Segment Tree for prefix sums and point updates.
Prefix sum, range sum, point update: O(log n).
Used for prefix queries, inversions count, range updates.
"""


class FenwickTree:
    """Fenwick Tree (Binary Indexed Tree) for prefix sums."""

    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (self.n + 1)
        for i, v in enumerate(arr):
            self._update(i + 1, v)

    def _update(self, idx, delta):
        """Internal: add delta to tree at idx."""
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & (-idx)

    def prefix_sum(self, idx):
        """Sum of elements [0, idx] (0-indexed)."""
        s = 0
        idx += 1
        while idx > 0:
            s += self.tree[idx]
            idx -= idx & (-idx)
        return s

    def range_sum(self, left, right):
        """Sum of elements [left, right] (inclusive)."""
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

    def update(self, idx, new_value, old_value=None):
        """Update element at idx. Pass old_value if known for efficiency."""
        if old_value is None:
            # Would need to store original array for full update
            delta = new_value
        else:
            delta = new_value - old_value
        self._update(idx + 1, delta)


if __name__ == "__main__":
    print("=== Fenwick Tree (Binary Indexed Tree) ===\n")
    arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Array: {arr}")

    ft = FenwickTree(arr)
    print(f"Prefix sum [0..5]: {ft.prefix_sum(5)}")  # 2+1+1+3+2+3 = 12
    print(f"Range sum [3..7]: {ft.range_sum(3, 7)}")  # 3+2+3+4+5 = 17
