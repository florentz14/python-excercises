"""
Diccionarios - Ejemplo 13: Diccionarios anidados
================================================
Tema: Diccionarios (01_Variables_y_Tipos_Datos)
Descripción: Valores pueden ser otros diccionarios; acceso con dic["a"]["b"].
"""

print("Example 13: Dictionary with nested structures")
print("-" * 40)
nested = {
    "user1": {"name": "John", "age": 25},
    "user2": {"name": "Jane", "age": 23}
}
print("Nested dictionary:", nested)
print("User 1 name:", nested["user1"]["name"])
print("User 2 age:", nested["user2"]["age"])
