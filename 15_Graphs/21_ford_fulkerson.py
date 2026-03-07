"""
15_Graphs - Ford-Fulkerson Max Flow
=====================================
Maximum flow from source to sink using DFS to find augmenting paths.
Edmonds-Karp (BFS) is a variant. Used in: network routing, bipartite matching.
"""

from collections import defaultdict


def ford_fulkerson(n: int, edges: list[tuple[int, int, int]], source: int, sink: int) -> int:
    """
    Returns maximum flow from source to sink.
    edges: [(u, v, capacity), ...] directed.
    """
    adj: dict[int, list[int]] = defaultdict(list)
    capacity = defaultdict(lambda: defaultdict(int))
    for u, v, cap in edges:
        adj[u].append(v)
        adj[v].append(u)
        capacity[u][v] += cap

    def dfs_find_path(s, t, visited, path, min_cap):
        if s == t:
            return min_cap
        visited.add(s)
        for v in adj[s]:
            if v not in visited and capacity[s][v] > 0:
                flow = dfs_find_path(v, t, visited, path + [v], min(min_cap, capacity[s][v]))
                if flow > 0:
                    capacity[s][v] -= flow
                    capacity[v][s] += flow
                    return flow
        return 0

    max_flow = 0
    while True:
        flow = dfs_find_path(source, sink, set(), [source], float("inf"))
        if flow == 0:
            break
        max_flow += flow
    return max_flow


if __name__ == "__main__":
    print("=== Ford-Fulkerson Max Flow ===\n")
    # Source 0, Sink 3. 0->1:10, 0->2:5, 1->2:15, 1->3:10, 2->3:10
    edges = [(0, 1, 10), (0, 2, 5), (1, 2, 15), (1, 3, 10), (2, 3, 10)]
    flow = ford_fulkerson(4, edges, 0, 3)
    print(f"Maximum flow from 0 to 3: {flow}")
