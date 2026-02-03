"""
Conjuntos (set) - Ejemplo 6: Recorrer un set con for
====================================================
Tema: Conjuntos (01_Variables_y_Tipos_Datos)
Descripción: Itera sobre los elementos (el orden no está garantizado).
"""

print("Example 6: Loop through a set")
print("-" * 40)
animals = {"cat", "dog", "bird", "fish"}
print("Set:", animals)
for animal in animals:
    print(animal)
