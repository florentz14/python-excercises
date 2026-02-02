"""
Diccionarios - Ejemplo 15: Lista de tuplas a diccionario
========================================================
Tema: Diccionarios (01_Variables_y_Tipos_Datos)
Descripción: dict([(k1,v1), (k2,v2), ...]) construye el diccionario.
"""

print("Example 15: Convert list of tuples to dictionary")
print("-" * 40)
pairs = [("name", "Alice"), ("age", 30), ("city", "Boston")]
person_dict = dict(pairs)
print("List of tuples:", pairs)
print("Converted to dictionary:", person_dict)
