"""
14_Trees - Segment Tree
========================
Range queries: sum, min, max over array intervals.
Build O(n), query/update O(log n).
Used in competitive programming, interval analysis.
"""


class SegmentTree:
    """Segment tree for range queries (sum, min, max)."""

    def __init__(self, arr, op=sum, default=0):
        self.n = len(arr)
        self.op = op
        self.default = default
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [default] * (2 * self.size)
        for i in range(self.n):
            self.tree[self.size + i] = arr[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = op([self.tree[2 * i], self.tree[2 * i + 1]])

    def query(self, left, right):
        """Query range [left, right] (inclusive)."""
        left += self.size
        right += self.size
        result = self.default
        while left <= right:
            if left % 2 == 1:
                result = self.op([result, self.tree[left]])
                left += 1
            if right % 2 == 0:
                result = self.op([result, self.tree[right]])
                right -= 1
            left //= 2
            right //= 2
        return result

    def update(self, idx, value):
        """Update element at idx."""
        idx += self.size
        self.tree[idx] = value
        idx //= 2
        while idx:
            self.tree[idx] = self.op([
                self.tree[2 * idx],
                self.tree[2 * idx + 1]
            ])
            idx //= 2


if __name__ == "__main__":
    print("=== Segment Tree (Range Queries) ===\n")
    arr = [1, 3, 5, 7, 9, 11]
    print(f"Array: {arr}")

    st_sum = SegmentTree(arr, op=sum, default=0)
    print(f"Sum [2, 4]: {st_sum.query(2, 4)}")  # 5+7+9 = 21

    st_min = SegmentTree(arr, op=min, default=float("inf"))
    print(f"Min [1, 5]: {st_min.query(1, 5)}")  # 3

    st_max = SegmentTree(arr, op=max, default=float("-inf"))
    print(f"Max [0, 3]: {st_max.query(0, 3)}")  # 7

    st_sum.update(3, 10)
    print(f"After update arr[3]=10, sum [2,4]: {st_sum.query(2, 4)}")
