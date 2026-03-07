"""
15_Graphs - Floyd-Warshall algorithm
=======================================
All-pairs shortest path. Works with negative weights (no negative cycles).
Used in: transitive closure, shortest path between all pairs.
Complexity: O(V^3)
"""


def floyd_warshall(n: int, edges: list[tuple[int, int, float]]) -> list[list[float]]:
    """Returns n x n matrix of shortest distances. edges: (u, v, weight)."""
    INF = float("inf")
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


if __name__ == "__main__":
    print("=== Floyd-Warshall (all-pairs shortest path) ===\n")
    n = 4
    edges = [(0, 1, 3), (0, 3, 7), (1, 0, 8), (1, 2, 2), (2, 0, 5), (2, 3, 1), (3, 0, 2)]
    dist = floyd_warshall(n, edges)
    print("Distance matrix:")
    for i, row in enumerate(dist):
        print(f"  {i}: {row}")
