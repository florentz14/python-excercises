"""
15_Graphs - Prim's MST Algorithm
===================================
Minimum Spanning Tree using Prim's algorithm.
Greedy: grow tree by adding minimum-weight edge from tree to non-tree.
Complexity: O(V^2) simple, O(E log V) with heap.
"""

import heapq
from collections import defaultdict


def prim(num_nodes: int, edges: list[tuple[int, int, int]], start: int = 0) -> tuple[list[tuple[int, int, int]], int]:
    """
    Prim's MST. Returns (mst_edges, total_weight).
    edges: [(u, v, w), ...] undirected.
    """
    adj: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    in_mst = [False] * num_nodes
    min_edge = [(float("inf"), -1, -1)] * num_nodes  # (weight, from, to)
    min_edge[start] = (0, -1, start)
    heap = [(0, start, -1)]  # (weight, node, from)
    mst_edges = []
    total = 0

    while heap:
        w, u, from_node = heapq.heappop(heap)
        if in_mst[u]:
            continue
        in_mst[u] = True
        total += w
        if from_node >= 0:
            mst_edges.append((from_node, u, w))
        for v, w2 in adj[u]:
            if not in_mst[v] and w2 < min_edge[v][0]:
                min_edge[v] = (w2, u, v)
                heapq.heappush(heap, (w2, v, u))

    return mst_edges, total


if __name__ == "__main__":
    print("=== Prim's MST ===\n")
    # Graph: 0-1:2, 0-3:6, 1-2:3, 1-3:8, 1-4:5, 2-4:7, 3-4:9
    edges = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]
    mst, total = prim(5, edges)
    print(f"MST edges: {mst}")
    print(f"Total weight: {total}")
