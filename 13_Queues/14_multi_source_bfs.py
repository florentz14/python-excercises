"""
13_Queues - Multi-Source BFS
=============================
BFS starting from multiple nodes simultaneously.
Applications: virus spread, fire in forest, rotting oranges.

Time: O(rows * cols)
"""

from collections import deque


def multi_source_bfs(grid: list[list[int]], sources: list[tuple]) -> list[list[int]]:
    """
    Returns distance from each cell to nearest source.
    grid: 0=empty, 1=obstacle. sources: list of (r, c).
    """
    rows, cols = len(grid), len(grid[0])
    dist = [[-1] * cols for _ in range(rows)]
    queue = deque()

    for r, c in sources:
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] != 1:
            dist[r][c] = 0
            queue.append((r, c))

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 1 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))
    return dist


def rotting_oranges(grid: list[list[int]]) -> int:
    """
    LeetCode 994. Minutes until all oranges rot.
    0=empty, 1=fresh, 2=rotten. Returns -1 if impossible.
    """
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:
        return 0
    minutes = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
        if queue:
            minutes += 1

    return minutes if fresh == 0 else -1


if __name__ == "__main__":
    print("=== Multi-Source BFS ===\n")

    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    dist = multi_source_bfs(grid, [(0, 0), (2, 2)])
    print("Distances from (0,0) and (2,2):")
    for row in dist:
        print(" ", row)

    print("\n=== Rotting Oranges ===")
    oranges = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    mins = rotting_oranges(oranges)
    print(f"Minutes to rot all: {mins}")
