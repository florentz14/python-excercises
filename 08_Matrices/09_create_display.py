# ------------------------------------------------------------
# File: 09_create_display.py
# Purpose: Create and display a matrix (list of lists).
# Description: Represent matrix as rows; show dimensions and element access.
# ------------------------------------------------------------

# Matrix 2x3: 2 rows, 3 columns
A = [
    [1, 2, 3],
    [4, 5, 6],
]

print("Matrix A (2x3):")
for row in A:
    print(" ", row)
print("Rows:", len(A))
print("Columns:", len(A[0]))
# Element at row 1, column 2 (0-based)
print("Element A[1][2] =", A[1][2])
