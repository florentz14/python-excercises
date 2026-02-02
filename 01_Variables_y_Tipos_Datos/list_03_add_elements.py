"""
Listas - Ejemplo 3: Añadir elementos a una lista
================================================
Tema: Listas (01_Variables_y_Tipos_Datos)
Descripción: Usa append() para un elemento y extend() para añadir varios.
"""

print("Example 3: Add elements to a list")
print("-" * 40)
colors = ["red", "blue"]
print("Original list:", colors)
colors.append("green")  # Add one element
print("After append:", colors)
colors.extend(["yellow", "purple"])  # Add multiple elements
print("After extend:", colors)
