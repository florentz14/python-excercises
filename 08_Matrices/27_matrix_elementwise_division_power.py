# ------------------------------------------------------------
# File: 27_matrix_elementwise_division_power.py
# Purpose: Element-wise division and matrix power.
# Description: A/B element-wise, I² = I × I (matrix squared).
# ------------------------------------------------------------


def print_matrix(matrix, name="Matrix"):
    """Print matrix with aligned columns."""
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


# Element-wise division
num = [[10, 20, 30], [40, 50, 60]]
den = [[2, 5, 5], [8, 10, 6]]
print_matrix(num, "Numerator")
print_matrix(den, "Denominator")
divided = [[num[i][j] / den[i][j] for j in range(len(num[0]))] for i in range(len(num))]
print_matrix(divided, "Element-wise division")

# Matrix squared: I² = I × I
I = [[1, 2], [3, 4]]
print_matrix(I, "I")
I2 = [[sum(I[i][k] * I[k][j] for k in range(len(I))) for j in range(len(I[0]))] for i in range(len(I))]
print_matrix(I2, "I²")
