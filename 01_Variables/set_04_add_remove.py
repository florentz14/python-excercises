"""
Conjuntos (set) - Ejemplo 4: Añadir y eliminar elementos
========================================================
Tema: Conjuntos (01_Variables_y_Tipos_Datos)
Descripción: add(), remove() (error si no existe), discard() (sin error).
"""

print("Example 4: Add and remove elements")
print("-" * 40)
fruits = {"apple", "banana", "cherry"}
print("Original set:", fruits)
fruits.add("date")
print("After add('date'):", fruits)
fruits.remove("banana")
print("After remove('banana'):", fruits)
fruits.discard("grape")  # No error if element doesn't exist
print("After discard('grape'):", fruits)
