# ------------------------------------------------------------
# File: 14_matrix_vector_product.py
# Purpose: Matrix times column vector.
# Description: A(m×n) * v(n×1) = vector of m components. Each row of A · v.
# ------------------------------------------------------------

A = [[1, 2], [3, 4], [5, 6]]  # 3x2
v = [7, 8]  # 2-component vector

# Result: for each row i, sum A[i][j] * v[j]
result = [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]

print("A =")
for row in A:
    print(" ", row)
print("v =", v)
print("A * v =", result)
