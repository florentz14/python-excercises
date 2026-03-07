# ------------------------------------------------------------
# File: 19_grid_types_square.py
# Purpose: Grid display, mixed types, square check.
# Description: Print as grid, mixed type matrix, is_square check.
# ------------------------------------------------------------

# Print as grid (space-separated)
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix as grid:")
for row in grid:
    print(" ".join(str(x) for x in row))

# Mixed types (e.g. table with header)
mixed = [
    ["name", "age", "city"],
    ["Alice", 25, "NYC"],
    ["Bob", 30, "LA"],
    ["Charlie", 28, "Chicago"],
]
print("\nMixed-type matrix:")
for row in mixed:
    print(row)

# Square check: rows == columns
square = [[1, 2], [3, 4]]
rect = [[1, 2, 3], [4, 5, 6]]
print("\nSquare matrix:", square, "→ is_square:", len(square) == len(square[0]))
print("Rectangular:", rect, "→ is_square:", len(rect) == len(rect[0]))
