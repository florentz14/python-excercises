"""
Diccionarios - Ejemplo 9: Comprobar si existe una clave
======================================================
Tema: Diccionarios (01_Variables_y_Tipos_Datos)
Descripción: Usa 'in' y 'not in' para comprobar pertenencia de claves.
"""

print("Example 9: Check if key exists")
print("-" * 40)
settings = {"theme": "dark", "language": "English", "notifications": True}
print("Dictionary:", settings)
if "theme" in settings:
    print("'theme' is in the dictionary")
if "password" not in settings:
    print("'password' is not in the dictionary")
