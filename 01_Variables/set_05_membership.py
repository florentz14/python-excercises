"""
Conjuntos (set) - Ejemplo 5: Comprobar pertenencia
==================================================
Tema: Conjuntos (01_Variables_y_Tipos_Datos)
Descripción: 'in' y 'not in' para saber si un elemento está en el set.
"""

print("Example 5: Check membership")
print("-" * 40)
colors = {"red", "green", "blue", "yellow"}
print("Set:", colors)
if "red" in colors:
    print("'red' is in the set")
if "purple" not in colors:
    print("'purple' is not in the set")
