"""
Diccionarios - Ejemplo 16: Método setdefault()
==============================================
Tema: Diccionarios (01_Variables_y_Tipos_Datos)
Descripción: setdefault(clave, valor) inserta solo si la clave no existe y devuelve el valor.
"""

print("Example 16: Dictionary methods")
print("-" * 40)
employee = {"id": 101, "name": "Bob", "department": "IT"}
print("Original:", employee)
print("setdefault('salary', 50000):", employee.setdefault("salary", 50000))
print("After setdefault:", employee)
print("setdefault('name', 'Unknown'):", employee.setdefault("name", "Unknown"))
print("Final dictionary:", employee)
