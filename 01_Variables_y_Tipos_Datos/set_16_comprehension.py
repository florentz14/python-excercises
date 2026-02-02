"""
Conjuntos (set) - Ejemplo 16: Set comprehension
================================================
Tema: Conjuntos (01_Variables_y_Tipos_Datos)
Descripción: {x**2 for x in lista} crea un set; duplicados se eliminan automáticamente.
"""

print("Example 16: Set comprehension")
print("-" * 40)
numbers_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
squared_set = {x**2 for x in numbers_list}
print("Original numbers:", numbers_list)
print("Squared set (removes duplicates):", squared_set)
even_squared = {x**2 for x in numbers_list if x % 2 == 0}
print("Even squared set:", even_squared)
