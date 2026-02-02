"""
Diccionarios - Ejemplo 4: Añadir y modificar valores
====================================================
Tema: Diccionarios (01_Variables_y_Tipos_Datos)
Descripción: Asignación dic[clave] = valor para añadir o modificar.
"""

print("Example 4: Add and modify values")
print("-" * 40)
car = {"brand": "Toyota", "color": "red"}
print("Original:", car)
car["year"] = 2023  # Add new key-value pair
print("After adding year:", car)
car["color"] = "blue"  # Modify existing value
print("After modifying color:", car)
