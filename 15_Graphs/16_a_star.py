"""
15_Graphs - A* (A-Star) algorithm
==================================
Shortest path with heuristic. Used in: pathfinding, games, robotics.
Requires admissible heuristic h(n) <= actual cost to goal.
"""

import heapq


def a_star(start: tuple[int, int], goal: tuple[int, int], grid: list[list[int]]) -> list[tuple[int, int]] | None:
    """
    Grid: 0 = passable, 1 = wall. Returns path or None.
    Uses Manhattan distance as heuristic.
    """
    rows, cols = len(grid), len(grid[0])
    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return None

    def h(r, c):
        return abs(r - goal[0]) + abs(c - goal[1])

    heap = [(h(*start), 0, start, [start])]
    seen = {start}

    while heap:
        _, g, (r, c), path = heapq.heappop(heap)
        if (r, c) == goal:
            return path
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in seen:
                seen.add((nr, nc))
                ng = g + 1
                heapq.heappush(heap, (ng + h(nr, nc), ng, (nr, nc), path + [(nr, nc)]))
    return None


if __name__ == "__main__":
    print("=== A* (pathfinding with heuristic) ===\n")
    grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ]
    path = a_star((0, 0), (2, 3), grid)
    print(f"Path from (0,0) to (2,3): {path}")
