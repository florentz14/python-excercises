"""
Conjuntos (set) - Ejemplo 15: min, max y pop
============================================
Tema: Conjuntos (01_Variables_y_Tipos_Datos)
Descripción: max(), min() sobre el set; pop() quita y devuelve un elemento arbitrario.
"""

print("Example 15: Find and remove elements")
print("-" * 40)
num_set = {50, 10, 40, 20, 30}
print("Original set:", num_set)
print("Max element:", max(num_set))
print("Min element:", min(num_set))
popped = num_set.pop()  # Remove and return an arbitrary element
print(f"Popped element: {popped}")
print("After pop:", num_set)
