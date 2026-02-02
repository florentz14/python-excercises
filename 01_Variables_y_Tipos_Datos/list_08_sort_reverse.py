"""
Listas - Ejemplo 8: Ordenar y revertir
=======================================
Tema: Listas (01_Variables_y_Tipos_Datos)
Descripción: Ordena la lista in-place con sort() y la invierte con reverse().
"""

print("Example 8: Sort and reverse")
print("-" * 40)
unsorted = [50, 10, 40, 20, 30]
print("Original list:", unsorted)
unsorted.sort()
print("Sorted list:", unsorted)
unsorted.reverse()
print("Reversed list:", unsorted)
