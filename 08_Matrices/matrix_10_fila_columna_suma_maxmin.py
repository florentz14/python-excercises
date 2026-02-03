"""
08_Matrices - Fila, columna, suma total y máximo/mínimo
========================================================
Ejemplos 10-12: obtener fila/columna, suma de elementos, max y min.
"""

M = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
]
print("Matriz:")
for row in M:
    print(row)
print("Fila 1:", M[1])
print("Columna 1:", [row[1] for row in M])

# Suma de todos los elementos
nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nMatriz:", nums)
print("Suma de todos los elementos:", sum(sum(row) for row in nums))

# Máximo y mínimo
flat = [x for row in nums for x in row]
print("Máximo:", max(flat))
print("Mínimo:", min(flat))
