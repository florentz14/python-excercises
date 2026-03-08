# -------------------------------------------------
# File Name: 23_multi_source_bfs.py
# Author: Florentino Báez
# Date: 15_Graphs
# Description: 15_Graphs - Multi-Source BFS ============================== BFS starting from multiple sources (e.g. LeetCode 994 Rotting Oranges).
# -------------------------------------------------

from collections import deque


def multi_source_bfs(grid: list[list[int]], sources: list[tuple[int, int]], empty: int = 0) -> list[list[int]]:
    """
    Returns distance grid from nearest source. -1 for unreachable.
    sources: [(r, c), ...] starting cells.
    """
    rows, cols = len(grid), len(grid[0])
    dist = [[-1] * cols for _ in range(rows)]
    q = deque()
    for r, c in sources:
        dist[r][c] = 0
        q.append((r, c))

    while q:
        r, c = q.popleft()
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1 and grid[nr][nc] != empty:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return dist


def rotting_oranges(grid: list[list[int]]) -> int:
    """
    LeetCode 994. 0=empty, 1=fresh, 2=rotten.
    Returns minutes to rot all, or -1 if impossible.
    """
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:
        return 0
    minutes = 0
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
        minutes += 1
    return minutes - 1 if fresh == 0 else -1


if __name__ == "__main__":
    print("=== Multi-Source BFS / Rotting Oranges ===\n")
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    mins = rotting_oranges([row[:] for row in grid])
    print(f"Grid: [[2,1,1],[1,1,0],[0,1,1]]")
    print(f"Minutes to rot all: {mins}")
