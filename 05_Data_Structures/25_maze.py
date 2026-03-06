# -------------------------------------------------
# File: 25_laberinto.py (Maze Solving - Backtracking)
# -------------------------------------------------
# Author: Florentino Báez
# Module: Data Structures - Backtracking
#
# Description:
#   Maze pathfinding via backtracking. 0 = open, 1 = wall. Explores
#   the 4 directions (right, down, left, up) and backtracks on dead ends.
#
# Returns: path list if found, None otherwise.
# -------------------------------------------------


def solve_maze(maze, start, goal):
    """Returns path from start to goal, or None if no path exists."""
    n, m = len(maze), len(maze[0])
    visited = [[False] * m for _ in range(n)]
    path = []

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_valid(x, y):
        return (0 <= x < n and 0 <= y < m and
                maze[x][y] == 0 and not visited[x][y])

    def backtrack(x, y):
        if (x, y) == goal:
            path.append((x, y))
            return True
        visited[x][y] = True
        path.append((x, y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and backtrack(nx, ny):
                return True
        path.pop()
        return False

    if backtrack(start[0], start[1]):
        return path
    return None


def print_maze_with_path(maze, path):
    """Prints maze with path marked (S=start, E=end, *=path)."""
    n, m = len(maze), len(maze[0])
    grid = [[' ' if maze[i][j] == 0 else '#' for j in range(m)] for i in range(n)]
    for x, y in path:
        grid[x][y] = '*'
    if path:
        grid[path[0][0]][path[0][1]] = 'S'
        grid[path[-1][0]][path[-1][1]] = 'E'
    print("  " + "".join(str(i % 10) for i in range(m)))
    for i, row in enumerate(grid):
        print(f"{i % 10} " + "".join(row))


if __name__ == "__main__":
    print("=== Backtracking: Maze Solving ===\n")

    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    start, goal = (0, 0), (4, 4)

    print("Maze (0=open, 1=wall):")
    for row in maze:
        print(f"  {row}")

    path = solve_maze(maze, start, goal)
    if path:
        print(f"\nPath found ({len(path)} steps):")
        print_maze_with_path(maze, path)
    else:
        print("\nNo path found")
