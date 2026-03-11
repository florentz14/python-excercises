# -------------------------------------------------
# File Name: 31_segment_tree.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: Segment tree for range queries and updates. O(log n) per operation.
# -------------------------------------------------

print("=== 2. Segment Tree ===\n")


class SegmentTree:
    """
    Segment Tree for range queries.
    Complexity: O(log n) query and update.
    """

    def __init__(self, arr, funcion=sum):
        self.n = len(arr)
        self.funcion = funcion
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [0] * (2 * self.size)

        for i in range(self.n):
            self.tree[self.size + i] = arr[i]

        if funcion == min:
            for i in range(self.size + self.n, 2 * self.size):
                self.tree[i] = float('inf')

        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self._apply_function(
                self.tree[2 * i],
                self.tree[2 * i + 1]
            )

    def _apply_function(self, a, b):
        if self.funcion == sum:
            return a + b
        if self.funcion == min:
            return min(a, b)
        if self.funcion == max:
            return max(a, b)
        return self.funcion([a, b])

    def query_range(self, l, r):
        """Query range [l, r) (l included, r excluded)."""
        l += self.size
        r += self.size
        result = 0 if self.funcion == sum else None
        if self.funcion == min:
            result = float('inf')
        elif self.funcion == max:
            result = float('-inf')

        while l < r:
            if l % 2 == 1:
                result = self._apply_function(result, self.tree[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                result = self._apply_function(result, self.tree[r])
            l //= 2
            r //= 2
        return result

    def update(self, index, value):
        index += self.size
        self.tree[index] = value
        index //= 2
        while index >= 1:
            self.tree[index] = self._apply_function(
                self.tree[2 * index],
                self.tree[2 * index + 1]
            )
            index //= 2


if __name__ == "__main__":
    arr_seg = [1, 3, 5, 7, 9, 11]
    print(f"Array: {arr_seg}")

    seg_tree_sum = SegmentTree(arr_seg, sum)
    print(f"Sum [1, 4): {seg_tree_sum.query_range(1, 4)}")
    print(f"Sum [0, 6): {seg_tree_sum.query_range(0, 6)}")

    seg_tree_min = SegmentTree(arr_seg, min)
    print(f"Minimum [1, 4): {seg_tree_min.query_range(1, 4)}")

    seg_tree_sum.update(2, 10)
    print(f"After updating index 2 to 10: {seg_tree_sum.query_range(0, 6)}")


# Backward-compatible aliases.
SegmentTree.consultar_rango = SegmentTree.query_range
SegmentTree.actualizar = SegmentTree.update
SegmentTree._aplicar_funcion = SegmentTree._apply_function
