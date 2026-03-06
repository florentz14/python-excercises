# -------------------------------------------------
# File Name: 03_kruskal.py
# Author: Florentino Báez
# Date: Data Structures - Greedy Algorithms
# Description: Kruskal's Algorithm for Minimum Spanning Tree (MST).
#              Finds the minimum spanning tree of an undirected
#              weighted graph. Sorts edges by weight and adds
#              those that don't form cycles using Union-Find.
#              Complexity: O(E log E) where E = number of edges.
# -------------------------------------------------

print("=== 3. Algoritmo de Kruskal (MST) ===\n")


class UnionFind:
    """Union-Find structure to detect cycles in Kruskal's algorithm."""

    def __init__(self, n):
        self.padre = list(range(n))  # Each node is its own parent initially
        self.rango = [0] * n         # Rank for union by rank

    def encontrar(self, x):
        """Finds the root of the set with path compression."""
        if self.padre[x] != x:
            self.padre[x] = self.encontrar(self.padre[x])  # Path compression
        return self.padre[x]

    def unir(self, x, y):
        """Merges two sets using union by rank."""
        raiz_x = self.encontrar(x)
        raiz_y = self.encontrar(y)
        if raiz_x == raiz_y:
            return False  # Already in the same set (would form a cycle)
        # Union by rank: shorter tree joins the taller one
        if self.rango[raiz_x] < self.rango[raiz_y]:
            self.padre[raiz_x] = raiz_y
        elif self.rango[raiz_x] > self.rango[raiz_y]:
            self.padre[raiz_y] = raiz_x
        else:
            self.padre[raiz_y] = raiz_x
            self.rango[raiz_x] += 1  # Increase rank if they were equal
        return True


def kruskal(nodos, aristas):
    """
    Minimum Spanning Tree using Kruskal's algorithm.
    Strategy: Sort edges by weight and add those that don't form cycles.
    Complexity: O(E log E)
    """
    # Step 1: Sort all edges by weight (ascending)
    aristas.sort(key=lambda x: x[2])
    uf = UnionFind(nodos)  # Structure to detect cycles
    mst = []               # Edges of the minimum spanning tree
    peso_total = 0

    # Step 2: Iterate edges and add if they don't form a cycle
    for u, v, peso in aristas:
        if uf.unir(u, v):  # If u and v are in different sets
            mst.append((u, v, peso))
            peso_total += peso
            if len(mst) == nodos - 1:
                break  # MST complete: has V-1 edges

    return mst, peso_total


if __name__ == "__main__":
    nodos_kruskal = 4
    aristas_kruskal = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]

    print(f"Grafo con {nodos_kruskal} nodos y {len(aristas_kruskal)} aristas:")
    for u, v, peso in aristas_kruskal:
        print(f"  {u} --{peso}-- {v}")

    mst, peso_total = kruskal(nodos_kruskal, aristas_kruskal)
    print(f"\nMinimum Spanning Tree (peso total: {peso_total}):")
    for u, v, peso in mst:
        print(f"  {u} --{peso}-- {v}")
