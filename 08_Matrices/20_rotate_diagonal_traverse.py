# ------------------------------------------------------------
# File: 20_rotate_diagonal_traverse.py
# Purpose: Rotate 90°, main diagonal, index traverse.
# Description: Clockwise rotation, diagonal extraction, element-by-element.
# ------------------------------------------------------------

# Rotate 90° clockwise
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Original:")
for row in M:
    print(row)

n = len(M)
# rotated[i][j] = M[n-1-j][i]
rotated = [[M[n - 1 - j][i] for j in range(n)] for i in range(n)]
print("Rotated 90° clockwise:")
for row in rotated:
    print(row)

# Main diagonal: M[0][0], M[1][1], ...
diagonal = [M[i][i] for i in range(min(len(M), len(M[0])))]
print("\nMain diagonal:", diagonal)

# Traverse with indices
M2 = [[1, 2], [3, 4], [5, 6]]
print("\nIndex traverse [i][j]:")
for i in range(len(M2)):
    for j in range(len(M2[i])):
        print(f"  [{i}][{j}] = {M2[i][j]}", end="")
    print()
