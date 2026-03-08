# -------------------------------------------------
# File Name: 14_bellman_ford.py
# Author: Florentino Báez
# Date: 15_Graphs
# Description: 15_Graphs - Bellman-Ford algorithm ===================================== Shortest path with negative edge weights. Detects negative cycles.
# -------------------------------------------------

def bellman_ford(n: int, edges: list[tuple[int, int, float]], start: int) -> tuple[dict[int, float], bool]:
    """
    Returns (distances, has_negative_cycle).
    edges: list of (u, v, weight).
    """
    dist = {i: float("inf") for i in range(n)}
    dist[start] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative cycle
    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            return dist, True
    return dist, False


if __name__ == "__main__":
    print("=== Bellman-Ford (negative weights OK) ===\n")
    n = 5
    edges = [(0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)]
    dist, neg_cycle = bellman_ford(n, edges, 0)
    print(f"Distances from 0: {dist}")
    print(f"Negative cycle: {neg_cycle}")
