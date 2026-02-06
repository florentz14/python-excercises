"""
Tuplas - Ejemplo 10: Tupla de un solo elemento
==============================================
Tema: Tuplas (01_Variables_y_Tipos_Datos)
Descripción: La coma es obligatoria: (42,) es tupla; (42) es int.
"""

print("Example 10: Single element tuple")
print("-" * 40)
single = (42,)  # Note the comma is required
print("Single element tuple:", single)
print("Type:", type(single))
not_tuple = (42)  # Without comma, it's just an integer
print("Without comma:", not_tuple)
print("Type:", type(not_tuple))
