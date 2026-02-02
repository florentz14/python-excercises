"""
Tuplas - Ejemplo 13: Tuplas anidadas
====================================
Tema: Tuplas (01_Variables_y_Tipos_Datos)
Descripción: Tuplas dentro de tuplas; acceso con [i][j].
"""

print("Example 13: Nested tuples")
print("-" * 40)
nested = ((1, 2), ("a", "b"), (True, False))
print("Nested tuple:", nested)
print("First inner tuple:", nested[0])
print("First element of first inner tuple:", nested[0][0])
