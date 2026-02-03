"""
08_Matrices - Matriz de ceros y matriz identidad
=================================================
Ejemplos 5-6: crear matriz de ceros e identidad con listas.
"""

# Matriz de ceros 3x3
zeros = [[0 for _ in range(3)] for _ in range(3)]
print("Matriz de ceros (3x3):")
for row in zeros:
    print(row)

# Matriz identidad 3x3
identidad = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
print("\nMatriz identidad (3x3):")
for row in identidad:
    print(row)
