"""
Tuplas - Ejemplo 12: Tupla con tipos mezclados
=============================================
Tema: Tuplas (01_Variables_y_Tipos_Datos)
Descripción: Una tupla puede contener int, str, float, bool, None; se recorre con enumerate().
"""

print("Example 12: Tuple with mixed data types")
print("-" * 40)
mixed = (10, "hello", 3.14, True, None)
print("Mixed tuple:", mixed)
for index, item in enumerate(mixed):
    print(f"Index {index}: {item} (type: {type(item).__name__})")
