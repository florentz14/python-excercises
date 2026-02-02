"""
Tuplas - Ejemplo 6: Buscar elemento y comprobar pertenencia
=============================================================
Tema: Tuplas (01_Variables_y_Tipos_Datos)
Descripción: Usa 'in', 'not in' e index() en tuplas.
"""

print("Example 6: Find element and check membership")
print("-" * 40)
items = ("pen", "pencil", "eraser", "ruler", "notebook")
print("Tuple:", items)
if "pen" in items:
    print("'pen' is in the tuple")
    print("Index of 'pen':", items.index("pen"))
if "marker" not in items:
    print("'marker' is not in the tuple")
