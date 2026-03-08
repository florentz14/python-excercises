# -------------------------------------------------
# File Name: 18_kruskal.py
# Author: Florentino Báez
# Date: 15_Graphs
# Description: 15_Graphs - Kruskal's MST algorithm ===================================== Minimum Spanning Tree. Sort edges by weight, add if no cycle (Union-Find).
# -------------------------------------------------

from adjacency_list import GrafoListaAdyacencia


def kruskal_mst(grafo: GrafoListaAdyacencia) -> tuple[list[tuple], float]:
    """Returns (mst_edges, total_weight)."""
    edges = []
    nodes = grafo.obtener_nodos()
    node_to_idx = {n: i for i, n in enumerate(nodes)}
    n = len(nodes)

    for u in nodes:
        for v, w in grafo.obtener_vecinos(u):
            if node_to_idx[u] < node_to_idx[v]:
                edges.append((node_to_idx[u], node_to_idx[v], w))

    edges.sort(key=lambda e: e[2])
    uf = __import__("17_union_find").UnionFind(n)
    mst = []
    total = 0.0

    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((nodes[u], nodes[v], w))
            total += w
    return mst, total


if __name__ == "__main__":
    print("=== Kruskal MST ===\n")
    g = GrafoListaAdyacencia(dirigido=False)
    g.agregar_arista("A", "B", 4)
    g.agregar_arista("A", "C", 2)
    g.agregar_arista("B", "C", 1)
    g.agregar_arista("B", "D", 5)
    g.agregar_arista("C", "D", 8)
    g.agregar_arista("C", "E", 10)
    g.agregar_arista("D", "E", 2)
    mst, total = kruskal_mst(g)
    print(f"MST edges: {mst}")
    print(f"Total weight: {total}")
