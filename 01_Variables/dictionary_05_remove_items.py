"""
Diccionarios - Ejemplo 5: Eliminar elementos
============================================
Tema: Diccionarios (01_Variables_y_Tipos_Datos)
Descripción: pop(clave) devuelve el valor y lo elimina; del dic[clave] también elimina.
"""

print("Example 5: Remove items from dictionary")
print("-" * 40)
inventory = {"apple": 10, "banana": 5, "orange": 8, "grape": 12}
print("Original:", inventory)
removed = inventory.pop("banana")  # Remove and return value
print(f"Removed banana: {removed}")
print("After pop:", inventory)
del inventory["grape"]  # Delete an item
print("After del grape:", inventory)
