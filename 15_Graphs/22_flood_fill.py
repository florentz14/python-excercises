"""
15_Graphs - Flood Fill (LeetCode 733)
======================================
Replace connected region of same color. DFS/BFS on grid.
"""

from collections import deque


def flood_fill_dfs(grid: list[list[int]], sr: int, sc: int, new_color: int) -> list[list[int]]:
    """Flood fill using DFS. Modifies grid in place, returns it."""
    rows, cols = len(grid), len(grid[0])
    old_color = grid[sr][sc]
    if old_color == new_color:
        return grid

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != old_color:
            return
        grid[r][c] = new_color
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(r + dr, c + dc)

    dfs(sr, sc)
    return grid


def flood_fill_bfs(grid: list[list[int]], sr: int, sc: int, new_color: int) -> list[list[int]]:
    """Flood fill using BFS."""
    rows, cols = len(grid), len(grid[0])
    old_color = grid[sr][sc]
    if old_color == new_color:
        return grid

    q = deque([(sr, sc)])
    grid[sr][sc] = new_color
    while q:
        r, c = q.popleft()
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == old_color:
                grid[nr][nc] = new_color
                q.append((nr, nc))
    return grid


if __name__ == "__main__":
    print("=== Flood Fill ===\n")
    grid = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    result = flood_fill_bfs([row[:] for row in grid], 1, 1, 2)
    print("Original: [[1,1,1],[1,1,0],[1,0,1]]")
    print(f"After flood_fill(1,1,2): {result}")
