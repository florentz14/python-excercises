"""
Tuplas - Ejemplo 14: Convertir lista a tupla y viceversa
=========================================================
Tema: Tuplas (01_Variables_y_Tipos_Datos)
Descripción: tuple(lista) y list(tupla) para convertir entre tipos.
"""

print("Example 14: Convert list to tuple and vice versa")
print("-" * 40)
list_data = [10, 20, 30, 40]
tuple_data = tuple(list_data)
print("Original list:", list_data)
print("Converted to tuple:", tuple_data)
back_to_list = list(tuple_data)
print("Converted back to list:", back_to_list)
