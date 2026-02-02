"""
Conjuntos (set) - Ejemplo 7: Unión de conjuntos
===============================================
Tema: Conjuntos (01_Variables_y_Tipos_Datos)
Descripción: set1 | set2 o set1.union(set2) combina todos los elementos.
"""

print("Example 7: Set union (combine sets)")
print("-" * 40)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Set 1:", set1)
print("Set 2:", set2)
union = set1 | set2  # or set1.union(set2)
print("Union (set1 | set2):", union)
