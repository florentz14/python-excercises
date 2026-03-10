# -------------------------------------------------
# File Name: 13_bfs_shortest_path.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: BFS shortest path. Unweighted graph shortest path.
# -------------------------------------------------

from collections import deque


def bfs_shortest_path(graph: dict, start: str, end: str) -> list | None:
    """
    Returns shortest path from start to end using BFS.
    graph: adjacency list {node: [neighbors]}
    """
    if start == end:
        return [start]
    if start not in graph:
        return None

    visited = {start}
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor == end:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None


def bfs_shortest_path_grid(grid: list[list[int]], start: tuple, end: tuple) -> int:
    """
    Shortest path length on a 2D grid (0=empty, 1=wall).
    Returns -1 if no path exists.
    """
    rows, cols = len(grid), len(grid[0])
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return -1

    visited = {start}
    queue = deque([(start[0], start[1], 0)])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        r, c, dist = queue.popleft()
        if (r, c) == end:
            return dist
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    return -1


if __name__ == "__main__":
    print("=== BFS Shortest Path ===\n")

    # Graph example
    graph = {"A": ["B", "C"], "B": ["A", "D", "E"], "C": ["A", "F"], "D": ["B"], "E": ["B", "F"], "F": ["C", "E"]}
    path = bfs_shortest_path(graph, "A", "F")
    print(f"Graph: A->F shortest path: {path}")

    # Grid/maze example
    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    length = bfs_shortest_path_grid(grid, (0, 0), (2, 2))
    print(f"Grid (0,0)->(2,2) shortest length: {length}")
