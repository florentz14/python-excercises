"""
15_Graphs - Union-Find (Disjoint Set Union)
=============================================
Used in: Kruskal MST, cycle detection, connected components.
Amortized O(α(n)) ≈ constant. Essential for Kruskal.
"""


class UnionFind:
    """Union-Find with path compression and union by rank."""

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True

    def same_set(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


if __name__ == "__main__":
    print("=== Union-Find (Disjoint Set) ===\n")
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)
    print(f"same_set(0, 2): {uf.same_set(0, 2)}")
    print(f"same_set(0, 4): {uf.same_set(0, 4)}")
