"""
08_Matrices - Rotar 90°, diagonal principal y recorrido por índices
=====================================================================
Ejemplos 16-18.
"""

# Rotar 90° en sentido horario
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matriz original:")
for row in M:
    print(row)
n = len(M)
rotada = [[M[n - 1 - j][i] for j in range(n)] for i in range(n)]
print("Rotada 90° horario:")
for row in rotada:
    print(row)

# Diagonal principal
print("\nMatriz:")
for row in M:
    print(row)
diagonal = [M[i][i] for i in range(min(len(M), len(M[0])))]
print("Diagonal principal:", diagonal)

# Recorrido con índices
M2 = [[1, 2], [3, 4], [5, 6]]
print("\nRecorrido [i][j]:")
for i in range(len(M2)):
    for j in range(len(M2[i])):
        print(f"  [{i}][{j}] = {M2[i][j]}", end="")
    print()
