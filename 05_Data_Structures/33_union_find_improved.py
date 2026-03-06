# -------------------------------------------------
# File: 33_union_find_mejorado.py (Union-Find / Disjoint Set Union)
# -------------------------------------------------
# Author: Florentino Báez
# Module: Data Structures - Advanced Structures
#
# Description:
#   Union-Find with path compression and union by rank.
#   Amortized O(α(n)) ≈ constant. Used for cycles, connected components.
# -------------------------------------------------


class UnionFind:
    """
    Union-Find with path compression and union by rank.
    Complexity: O(α(n)) ≈ constant in practice.
    """

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
        self.num_components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.num_components -= 1
        return True

    def same_set(self, x, y):
        return self.find(x) == self.find(y)

    def component_size(self, x):
        return self.size[self.find(x)]

    def get_components(self):
        comp = {}
        for i in range(len(self.parent)):
            r = self.find(i)
            if r not in comp:
                comp[r] = []
            comp[r].append(i)
        return comp


if __name__ == "__main__":
    print("=== Advanced: Union-Find (Disjoint Set) ===\n")

    uf = UnionFind(10)
    print("Unions:")
    pairs = [(0, 1), (2, 3), (4, 5), (6, 7), (0, 2), (4, 6), (1, 3)]
    for x, y in pairs:
        uf.union(x, y)
        print(f"  Union {x} & {y}: components = {uf.num_components}")

    print(f"\nNumber of components: {uf.num_components}")
    print(f"0 and 3 in same set? {uf.same_set(0, 3)}")
    print(f"Component size of 0: {uf.component_size(0)}")
    print(f"Components: {uf.get_components()}")
