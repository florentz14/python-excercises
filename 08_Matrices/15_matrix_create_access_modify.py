# ------------------------------------------------------------
# File: 15_matrix_create_access_modify.py
# Purpose: Create, access, and modify matrix elements.
# Description: Indexing, element update, dimensions.
# ------------------------------------------------------------

# Create matrix as list of lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("Matrix:")
for row in matrix:
    print(row)

# Access by index [row][col]
print("\nElement [0][0]:", matrix[0][0])
print("Element [1][2]:", matrix[1][2])
print("Element [2][1]:", matrix[2][1])

# Modify element
matrix[1][1] = 50
print("\nAfter setting [1][1] = 50:")
for row in matrix:
    print(row)

# Dimensions
rows, cols = len(matrix), len(matrix[0])
print(f"\nRows: {rows}, Columns: {cols}")
