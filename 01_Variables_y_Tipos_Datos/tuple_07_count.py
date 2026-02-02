"""
Tuplas - Ejemplo 7: Contar ocurrencias
======================================
Tema: Tuplas (01_Variables_y_Tipos_Datos)
Descripción: Usa count() para contar cuántas veces aparece un valor.
"""

print("Example 7: Count occurrences")
print("-" * 40)
repeated_tuple = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
print("Tuple:", repeated_tuple)
print("Count of 2:", repeated_tuple.count(2))
print("Count of 4:", repeated_tuple.count(4))
