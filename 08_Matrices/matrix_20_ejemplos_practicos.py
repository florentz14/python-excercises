"""
08_Matrices - Ejemplos prácticos: brillo de imagen y análisis de ventas
========================================================================
Ejemplos 16-17: ajuste de brillo (píxeles), ventas Q1+Q2 y crecimiento.
"""


def print_matrix(matrix, name="Matrix"):
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


# Brillo de imagen (valores 0-255)
pixels = [[100, 150, 200], [120, 180, 220], [140, 190, 240]]
print_matrix(pixels, "Pixels originales (0-255)")
factor = 0.8
oscurecido = [[int(p * factor) for p in row] for row in pixels]
print_matrix(oscurecido, f"Oscurecido (factor {factor})")

# Ventas Q1 y Q2 por región/producto
q1 = [[1000, 1200, 1100], [1500, 1600, 1400]]
q2 = [[1200, 1400, 1300], [1600, 1800, 1500]]
print_matrix(q1, "Q1")
print_matrix(q2, "Q2")
total = [[q1[i][j] + q2[i][j] for j in range(len(q1[0]))] for i in range(len(q1))]
print_matrix(total, "Total (Q1 + Q2)")
crecimiento = [[q2[i][j] - q1[i][j] for j in range(len(q1[0]))] for i in range(len(q1))]
print_matrix(crecimiento, "Crecimiento (Q2 - Q1)")
