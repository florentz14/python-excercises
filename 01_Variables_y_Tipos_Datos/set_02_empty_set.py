"""
Conjuntos (set) - Ejemplo 2: Crear un set vacío
===============================================
Tema: Conjuntos (01_Variables_y_Tipos_Datos)
Descripción: set() para conjunto vacío; {} es un diccionario vacío, no un set.
"""

print("Example 2: Create an empty set")
print("-" * 40)
empty_set = set()  # Must use set() for empty set
print("Empty set:", empty_set)
print("Type:", type(empty_set))
not_a_set = {}  # This creates an empty dictionary, not a set
print("Empty dict:", not_a_set)
print("Type:", type(not_a_set))
