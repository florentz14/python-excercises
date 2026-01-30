# Matrix Operations Program
# This program demonstrates matrix arithmetic operations

# Helper function to print a matrix
def print_matrix(matrix, name="Matrix"):
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


# Example 1: Matrix Addition
print("Example 1: Matrix Addition")
print("=" * 50)
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print_matrix(matrix_a, "Matrix A")
print_matrix(matrix_b, "Matrix B")

# Add matrices
matrix_sum = [[matrix_a[i][j] + matrix_b[i][j]
               for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
print_matrix(matrix_sum, "A + B")

# Example 2: Matrix Subtraction
print("Example 2: Matrix Subtraction")
print("=" * 50)
# Subtract matrices
matrix_diff = [[matrix_a[i][j] - matrix_b[i][j]
                for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
print_matrix(matrix_diff, "A - B")

# Example 3: Scalar Multiplication
print("Example 3: Scalar Multiplication")
print("=" * 50)
scalar = 2
print(f"Matrix A multiplied by {scalar}:")
scalar_result = [[element * scalar for element in row] for row in matrix_a]
print_matrix(scalar_result, f"A × {scalar}")

# Example 4: Matrix Multiplication
print("Example 4: Matrix Multiplication")
print("=" * 50)
matrix_c = [
    [1, 2],
    [3, 4],
    [5, 6]
]
matrix_d = [
    [7, 8, 9],
    [10, 11, 12]
]

print_matrix(matrix_c, "Matrix C (3x2)")
print_matrix(matrix_d, "Matrix D (2x3)")

# Multiply matrices C (3x2) × D (2x3) = Result (3x3)
result = []
for i in range(len(matrix_c)):
    row = []
    for j in range(len(matrix_d[0])):
        sum_product = 0
        for k in range(len(matrix_d)):
            sum_product += matrix_c[i][k] * matrix_d[k][j]
        row.append(sum_product)
    result.append(row)

print_matrix(result, "C × D (Result: 3x3)")

# Example 5: Element-wise Multiplication (Hadamard Product)
print("Example 5: Element-wise Multiplication (Hadamard Product)")
print("=" * 50)
matrix_e = [
    [1, 2, 3],
    [4, 5, 6]
]
matrix_f = [
    [2, 3, 4],
    [5, 6, 7]
]

print_matrix(matrix_e, "Matrix E")
print_matrix(matrix_f, "Matrix F")

hadamard = [[matrix_e[i][j] * matrix_f[i][j]
             for j in range(len(matrix_e[0]))] for i in range(len(matrix_e))]
print_matrix(hadamard, "E ⊙ F (Hadamard Product)")

# Example 6: Matrix Transpose
print("Example 6: Matrix Transpose")
print("=" * 50)
matrix_g = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print_matrix(matrix_g, "Matrix G (3x4)")

transpose = [[matrix_g[i][j]
              for i in range(len(matrix_g))] for j in range(len(matrix_g[0]))]
print_matrix(transpose, "G^T (Transpose: 4x3)")

# Example 7: Matrix Division by Scalar
print("Example 7: Matrix Division by Scalar")
print("=" * 50)
scalar_div = 2
print(f"Matrix A divided by {scalar_div}:")
div_result = [[element / scalar_div for element in row] for row in matrix_a]
print_matrix(div_result, f"A ÷ {scalar_div}")

# Example 8: Matrix Negation
print("Example 8: Matrix Negation")
print("=" * 50)
print_matrix(matrix_a, "Original Matrix A")
negation = [[-element for element in row] for row in matrix_a]
print_matrix(negation, "-A (Negation)")

# Example 9: Identity Matrix and Multiplication
print("Example 9: Identity Matrix and Multiplication")
print("=" * 50)
identity_2x2 = [
    [1, 0],
    [0, 1]
]
matrix_h = [
    [5, 6],
    [7, 8]
]

print_matrix(identity_2x2, "Identity Matrix (2x2)")
print_matrix(matrix_h, "Matrix H")

# Multiply H × I (should equal H)
identity_mult = []
for i in range(len(matrix_h)):
    row = []
    for j in range(len(identity_2x2[0])):
        sum_product = 0
        for k in range(len(identity_2x2)):
            sum_product += matrix_h[i][k] * identity_2x2[k][j]
        row.append(sum_product)
    identity_mult.append(row)

print_matrix(identity_mult, "H × I (Should equal H)")

# Example 10: Trace of a Matrix (sum of diagonal elements)
print("Example 10: Trace of a Matrix")
print("=" * 50)
square_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix(square_matrix, "Square Matrix")
trace = sum(square_matrix[i][i] for i in range(len(square_matrix)))
print(f"Trace (sum of diagonal elements): {trace}")
print()

# Example 11: Determinant of 2x2 Matrix
print("Example 11: Determinant of 2x2 Matrix")
print("=" * 50)
matrix_2x2 = [
    [4, 7],
    [2, 6]
]

print_matrix(matrix_2x2, "2x2 Matrix")
determinant_2x2 = (matrix_2x2[0][0] * matrix_2x2[1]
                   [1]) - (matrix_2x2[0][1] * matrix_2x2[1][0])
print(f"Determinant = (4 × 6) - (7 × 2) = {determinant_2x2}")
print()

# Example 12: Sum of all elements
print("Example 12: Sum of all elements")
print("=" * 50)
print_matrix(matrix_a, "Matrix A")
total = sum(sum(row) for row in matrix_a)
print(f"Sum of all elements: {total}")
print()

# Example 13: Matrix row sum and column sum
print("Example 13: Row sums and Column sums")
print("=" * 50)
print_matrix(matrix_a, "Matrix A")

row_sums = [sum(row) for row in matrix_a]
print(f"Row sums: {row_sums}")

col_sums = [sum(matrix_a[i][j] for i in range(len(matrix_a)))
            for j in range(len(matrix_a[0]))]
print(f"Column sums: {col_sums}")
print()

# Example 14: Matrix Division (Element-wise)
print("Example 14: Element-wise Division")
print("=" * 50)
numerator = [
    [10, 20, 30],
    [40, 50, 60]
]
denominator = [
    [2, 5, 5],
    [8, 10, 6]
]

print_matrix(numerator, "Matrix Numerator")
print_matrix(denominator, "Matrix Denominator")

division = [[numerator[i][j] / denominator[i][j]
             for j in range(len(numerator[0]))] for i in range(len(numerator))]
print_matrix(division, "Element-wise Division")

# Example 15: Power of a Matrix (multiply by itself)
print("Example 15: Power of a Matrix (Square)")
print("=" * 50)
matrix_i = [
    [1, 2],
    [3, 4]
]

print_matrix(matrix_i, "Matrix I")

# I^2 = I × I
matrix_squared = []
for i in range(len(matrix_i)):
    row = []
    for j in range(len(matrix_i[0])):
        sum_product = 0
        for k in range(len(matrix_i)):
            sum_product += matrix_i[i][k] * matrix_i[k][j]
        row.append(sum_product)
    matrix_squared.append(row)

print_matrix(matrix_squared, "I² (I squared)")

# Example 16: Practical example - Image brightness adjustment
print("Example 16: Practical example - Image brightness adjustment")
print("=" * 50)
image_matrix = [
    [100, 150, 200],
    [120, 180, 220],
    [140, 190, 240]
]

print_matrix(image_matrix, "Original image pixel values (0-255)")

brightness_factor = 0.8
darkened = [[int(pixel * brightness_factor) for pixel in row]
            for row in image_matrix]
print_matrix(darkened, f"Darkened by factor {brightness_factor}")

# Example 17: Practical example - Sales matrix operations
print("Example 17: Practical example - Sales analysis")
print("=" * 50)
q1_sales = [
    [1000, 1200, 1100],  # Region A, B, C
    [1500, 1600, 1400]   # Product X, Y
]
q2_sales = [
    [1200, 1400, 1300],
    [1600, 1800, 1500]
]

print_matrix(q1_sales, "Q1 Sales")
print_matrix(q2_sales, "Q2 Sales")

total_sales = [[q1_sales[i][j] + q2_sales[i][j]
                for j in range(len(q1_sales[0]))] for i in range(len(q1_sales))]
print_matrix(total_sales, "Total Sales (Q1 + Q2)")

growth = [[q2_sales[i][j] - q1_sales[i][j]
           for j in range(len(q1_sales[0]))] for i in range(len(q1_sales))]
print_matrix(growth, "Growth (Q2 - Q1)")

print("\nEnd of Matrix Operations Examples")
