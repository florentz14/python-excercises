# -------------------------------------------------
# File Name: 03_kruskal.py
# Author: Florentino Báez
# Date: 05_Data_Structures
# Description: Kruskal's algorithm for Minimum Spanning Tree. Uses Union-Find to detect cycles. Sorts edges by weight; adds each if it doesn't form a cycle. O(E log E).
# -------------------------------------------------

class UnionFind:
    """Union-Find (disjoint set) for cycle detection in Kruskal's algorithm."""

    def __init__(self, n):
        self.parent = list(range(n))  # Each node is its own parent initially
        self.rank = [0] * n           # Rank for union-by-rank optimization

    def find(self, x):
        """Find root with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Merge sets containing x and y. Returns False if already in same set."""
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False  # Same set → would form a cycle
        # Union by rank: attach smaller tree under larger
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True


def kruskal(num_nodes, edges):
    """
    Returns (mst_edges, total_weight) for the minimum spanning tree.
    edges: list of (u, v, weight) tuples.
    """
    # Sort edges by weight ascending
    edges = sorted(edges, key=lambda x: x[2])
    uf = UnionFind(num_nodes)
    mst = []
    total_weight = 0

    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            total_weight += w
            if len(mst) == num_nodes - 1:
                break  # MST has V-1 edges

    return mst, total_weight


if __name__ == "__main__":
    print("=== Greedy Algorithms: Kruskal's MST ===\n")

    n_nodes = 4
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]

    print(f"Graph with {n_nodes} nodes and {len(edges)} edges:")
    for u, v, w in edges:
        print(f"  {u} --{w}-- {v}")

    mst, total = kruskal(n_nodes, edges)
    print(f"\nMinimum Spanning Tree (total weight: {total}):")
    for u, v, w in mst:
        print(f"  {u} --{w}-- {v}")
