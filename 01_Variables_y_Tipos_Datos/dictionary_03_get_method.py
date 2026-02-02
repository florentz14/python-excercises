"""
Diccionarios - Ejemplo 3: Método get()
======================================
Tema: Diccionarios (01_Variables_y_Tipos_Datos)
Descripción: get(clave) y get(clave, valor_por_defecto) para evitar KeyError.
"""

print("Example 3: Use get() method")
print("-" * 40)
user = {"username": "johndoe", "email": "john@example.com", "active": True}
print("Dictionary:", user)
print("Username:", user.get("username"))
print("Phone (not exists):", user.get("phone", "Not provided"))
