# -------------------------------------------------
# File Name: 28_practical_examples.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Pixel scaling, Q1+Q2 sales, growth calculation.
# -------------------------------------------------

def print_matrix(matrix, name="Matrix"):
    """Print matrix with aligned columns."""
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


# Image brightness (pixels 0-255)
pixels = [[100, 150, 200], [120, 180, 220], [140, 190, 240]]
print_matrix(pixels, "Original pixels (0-255)")
factor = 0.8
darkened = [[int(p * factor) for p in row] for row in pixels]
print_matrix(darkened, f"Darkened (factor {factor})")

# Sales Q1 and Q2 by region/product
q1 = [[1000, 1200, 1100], [1500, 1600, 1400]]
q2 = [[1200, 1400, 1300], [1600, 1800, 1500]]
print_matrix(q1, "Q1")
print_matrix(q2, "Q2")
total = [[q1[i][j] + q2[i][j] for j in range(len(q1[0]))] for i in range(len(q1))]
print_matrix(total, "Total (Q1 + Q2)")
growth = [[q2[i][j] - q1[i][j] for j in range(len(q1[0]))] for i in range(len(q1))]
print_matrix(growth, "Growth (Q2 - Q1)")
