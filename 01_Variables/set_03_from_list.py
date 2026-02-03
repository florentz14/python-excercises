"""
Conjuntos (set) - Ejemplo 3: Crear set desde una lista
=====================================================
Tema: Conjuntos (01_Variables_y_Tipos_Datos)
Descripción: set(lista) elimina duplicados y crea un conjunto.
"""

print("Example 3: Create set from list")
print("-" * 40)
list_data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print("List with duplicates:", list_data)
unique_set = set(list_data)
print("Converted to set (removes duplicates):", unique_set)
