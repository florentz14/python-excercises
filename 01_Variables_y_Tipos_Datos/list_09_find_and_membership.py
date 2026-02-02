"""
Listas - Ejemplo 9: Buscar elemento y comprobar pertenencia
============================================================
Tema: Listas (01_Variables_y_Tipos_Datos)
Descripción: Usa 'in' / 'not in' e index() para buscar en la lista.
"""

print("Example 9: Find element and check membership")
print("-" * 40)
items = ["pen", "pencil", "eraser", "ruler", "notebook"]
print("List:", items)
if "pen" in items:
    print("'pen' is in the list")
    print("Index of 'pen':", items.index("pen"))
if "marker" not in items:
    print("'marker' is not in the list")
