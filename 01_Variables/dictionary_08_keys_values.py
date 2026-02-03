"""
Diccionarios - Ejemplo 8: Obtener todas las claves y valores
============================================================
Tema: Diccionarios (01_Variables_y_Tipos_Datos)
Descripción: keys(), values() devuelven vistas; list() para convertirlas en lista.
"""

print("Example 8: Get all keys and values")
print("-" * 40)
courses = {"Math": "A", "Science": "B", "English": "A"}
print("Dictionary:", courses)
print("Keys:", list(courses.keys()))
print("Values:", list(courses.values()))
