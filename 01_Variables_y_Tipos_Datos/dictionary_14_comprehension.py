"""
Diccionarios - Ejemplo 14: Dictionary comprehension
===================================================
Tema: Diccionarios (01_Variables_y_Tipos_Datos)
Descripción: {x: x**2 for x in lista} y con condición if.
"""

print("Example 14: Dictionary comprehension")
print("-" * 40)
numbers = [1, 2, 3, 4, 5]
squared = {x: x**2 for x in numbers}
print("Numbers:", numbers)
print("Squared dictionary:", squared)
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print("Even squared dictionary:", even_squares)
