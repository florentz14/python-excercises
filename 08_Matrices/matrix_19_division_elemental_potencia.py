"""
08_Matrices - División elemento a elemento y potencia (matriz al cuadrado)
===========================================================================
Ejemplos 14-15.
"""


def print_matrix(matrix, name="Matrix"):
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


# División elemento a elemento
num = [[10, 20, 30], [40, 50, 60]]
den = [[2, 5, 5], [8, 10, 6]]
print_matrix(num, "Numerador")
print_matrix(den, "Denominador")
division = [[num[i][j] / den[i][j] for j in range(len(num[0]))] for i in range(len(num))]
print_matrix(division, "Division elemento a elemento")

# Matriz al cuadrado (I^2 = I × I)
I = [[1, 2], [3, 4]]
print_matrix(I, "I")
I2 = []
for i in range(len(I)):
    row = []
    for j in range(len(I[0])):
        row.append(sum(I[i][k] * I[k][j] for k in range(len(I))))
    I2.append(row)
print_matrix(I2, "I^2")
