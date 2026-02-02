"""
Diccionarios - Ejemplo 11: Copiar diccionario
=============================================
Tema: Diccionarios (01_Variables_y_Tipos_Datos)
Descripción: copy() crea una copia superficial; modificar la copia no afecta al original.
"""

print("Example 11: Copy dictionary")
print("-" * 40)
original = {"a": 1, "b": 2, "c": 3}
copy_dict = original.copy()
print("Original:", original)
print("Copy:", copy_dict)
copy_dict["a"] = 100
print("After modifying copy:")
print("Original:", original)
print("Copy:", copy_dict)
