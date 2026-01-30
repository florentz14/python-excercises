# Matrix / List of Lists Program
# This program demonstrates basic matrix and 2D list operations in Python

# Example 1: Create and display a matrix
print("Example 1: Create and display a matrix")
print("-" * 40)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix:")
for row in matrix:
    print(row)

# Example 2: Access matrix elements
print("\nExample 2: Access matrix elements")
print("-" * 40)
print("Element at row 0, col 0:", matrix[0][0])
print("Element at row 1, col 2:", matrix[1][2])
print("Element at row 2, col 1:", matrix[2][1])

# Example 3: Modify matrix elements
print("\nExample 3: Modify matrix elements")
print("-" * 40)
matrix[1][1] = 50
print("Modified matrix (changed [1][1] to 50):")
for row in matrix:
    print(row)

# Example 4: Get matrix dimensions
print("\nExample 4: Get matrix dimensions")
print("-" * 40)
rows = len(matrix)
cols = len(matrix[0])
print(f"Rows: {rows}, Columns: {cols}")

# Example 5: Create a matrix with specific values
print("\nExample 5: Create a matrix with zeros")
print("-" * 40)
zero_matrix = [[0 for _ in range(3)] for _ in range(3)]
print("Zero matrix (3x3):")
for row in zero_matrix:
    print(row)

# Example 6: Create identity matrix
print("\nExample 6: Create identity matrix")
print("-" * 40)
identity = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
print("Identity matrix (3x3):")
for row in identity:
    print(row)

# Example 7: Matrix transposition
print("\nExample 7: Matrix transposition")
print("-" * 40)
original = [
    [1, 2, 3],
    [4, 5, 6]
]
print("Original matrix (2x3):")
for row in original:
    print(row)
transposed = [[original[i][j]
               for i in range(len(original))] for j in range(len(original[0]))]
print("Transposed matrix (3x2):")
for row in transposed:
    print(row)

# Example 8: Add two matrices
print("\nExample 8: Add two matrices")
print("-" * 40)
matrix_a = [
    [1, 2],
    [3, 4]
]
matrix_b = [
    [5, 6],
    [7, 8]
]
print("Matrix A:")
for row in matrix_a:
    print(row)
print("Matrix B:")
for row in matrix_b:
    print(row)
matrix_sum = [[matrix_a[i][j] + matrix_b[i][j]
               for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
print("Sum (A + B):")
for row in matrix_sum:
    print(row)

# Example 9: Scalar multiplication
print("\nExample 9: Scalar multiplication")
print("-" * 40)
scalar = 2
matrix_data = [[1, 2], [3, 4]]
print("Original matrix:")
for row in matrix_data:
    print(row)
print(f"Multiply by {scalar}:")
result = [[element * scalar for element in row] for row in matrix_data]
for row in result:
    print(row)

# Example 10: Get row and column
print("\nExample 10: Get specific row and column")
print("-" * 40)
data_matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print("Matrix:")
for row in data_matrix:
    print(row)
print("Row 1:", data_matrix[1])
print("Column 1:", [row[1] for row in data_matrix])

# Example 11: Find sum of all elements
print("\nExample 11: Sum of all matrix elements")
print("-" * 40)
matrix_nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix:")
for row in matrix_nums:
    print(row)
total_sum = sum(sum(row) for row in matrix_nums)
print(f"Sum of all elements: {total_sum}")

# Example 12: Find maximum and minimum
print("\nExample 12: Find max and min elements")
print("-" * 40)
print("Matrix:")
for row in matrix_nums:
    print(row)
flat_list = [element for row in matrix_nums for element in row]
print(f"Maximum element: {max(flat_list)}")
print(f"Minimum element: {min(flat_list)}")

# Example 13: Print matrix as grid
print("\nExample 13: Print matrix as formatted grid")
print("-" * 40)
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix grid:")
for row in grid:
    print(" ".join(str(x) for x in row))

# Example 14: Matrix with different data types
print("\nExample 14: Matrix with mixed data types")
print("-" * 40)
mixed_matrix = [
    ["name", "age", "city"],
    ["Alice", 25, "NYC"],
    ["Bob", 30, "LA"],
    ["Charlie", 28, "Chicago"]
]
print("Mixed matrix:")
for row in mixed_matrix:
    print(row)

# Example 15: Check if matrix is square
print("\nExample 15: Check if matrix is square")
print("-" * 40)
square_matrix = [[1, 2], [3, 4]]
rectangular_matrix = [[1, 2, 3], [4, 5, 6]]
print("Square matrix:")
for row in square_matrix:
    print(row)
is_square = len(square_matrix) == len(square_matrix[0])
print(f"Is square? {is_square}")
print("\nRectangular matrix:")
for row in rectangular_matrix:
    print(row)
is_square = len(rectangular_matrix) == len(rectangular_matrix[0])
print(f"Is square? {is_square}")

# Example 16: Rotate matrix 90 degrees
print("\nExample 16: Rotate matrix 90 degrees clockwise")
print("-" * 40)
rotate_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Original matrix:")
for row in rotate_matrix:
    print(row)
rotated = [[rotate_matrix[len(rotate_matrix)-1-j][i]
            for j in range(len(rotate_matrix))] for i in range(len(rotate_matrix[0]))]
print("Rotated 90° clockwise:")
for row in rotated:
    print(row)

# Example 17: Check main diagonal
print("\nExample 17: Get main diagonal elements")
print("-" * 40)
diag_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix:")
for row in diag_matrix:
    print(row)
diagonal = [diag_matrix[i][i]
            for i in range(min(len(diag_matrix), len(diag_matrix[0])))]
print("Main diagonal:", diagonal)

# Example 18: Nested loop traversal
print("\nExample 18: Traverse matrix with nested loops")
print("-" * 40)
traverse_matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
print("Matrix elements:")
for i in range(len(traverse_matrix)):
    for j in range(len(traverse_matrix[i])):
        print(f"[{i}][{j}] = {traverse_matrix[i][j]}", end="  ")
    print()

# Example 19: Matrix comprehension
print("\nExample 19: Create matrix using comprehension")
print("-" * 40)
# Create 4x4 matrix with multiplication table
mult_matrix = [[i * j for j in range(1, 5)] for i in range(1, 5)]
print("Multiplication table (4x4):")
for row in mult_matrix:
    print(row)

# Example 20: Practical example - Store student grades
print("\nExample 20: Practical example - Student grades")
print("-" * 40)
grades = [
    ["Math", "Science", "English"],
    ["Alice", 85, 90],
    ["Bob", 78, 88],
    ["Charlie", 92, 95]
]
print("Student grades:")
for row in grades:
    print(row)
print("\nAccess specific data:")
print(f"Grade of Bob in Math: {grades[2][1]}")
print(f"All of Charlie's grades: {grades[3][1:]}")
