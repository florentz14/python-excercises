# -------------------------------------------------
# File Name: 17_kd_tree.py
# Author: Florentino Báez
# Date: 14_Trees
# Description: KD-Tree for multidimensional data and nearest neighbor search.
# -------------------------------------------------

class KDNode:
    """Node for KD-Tree."""

    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right


class KDTree:
    """KD-Tree for k-dimensional points."""

    def __init__(self, points):
        self.k = len(points[0]) if points else 0
        self.root = self._build(points, 0)

    def _build(self, points, depth):
        if not points:
            return None
        axis = depth % self.k
        points_sorted = sorted(points, key=lambda p: p[axis])
        mid = len(points_sorted) // 2
        return KDNode(
            points_sorted[mid],
            self._build(points_sorted[:mid], depth + 1),
            self._build(points_sorted[mid + 1:], depth + 1),
        )

    def nearest(self, target):
        """Find nearest point to target (simplified, no full backtracking)."""
        if self.root is None:
            return None
        best = [None, float("inf")]

        def _search(node, depth):
            if node is None:
                return
            d = sum((a - b) ** 2 for a, b in zip(node.point, target))
            if d < best[1]:
                best[0] = node.point
                best[1] = d
            axis = depth % self.k
            if target[axis] < node.point[axis]:
                _search(node.left, depth + 1)
                _search(node.right, depth + 1)
            else:
                _search(node.right, depth + 1)
                _search(node.left, depth + 1)

        _search(self.root, 0)
        return best[0]


if __name__ == "__main__":
    print("=== KD-Tree (K-Dimensional) ===\n")
    points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
    print(f"Points: {points}")

    kdt = KDTree(points)
    target = (6, 5)
    nearest = kdt.nearest(target)
    print(f"Nearest to {target}: {nearest}")
