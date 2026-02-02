"""
Tuplas - Ejemplo 11: Inmutabilidad de las tuplas
===============================================
Tema: Tuplas (01_Variables_y_Tipos_Datos)
Descripción: Intentar modificar un elemento lanza TypeError.
"""

print("Example 11: Tuple immutability")
print("-" * 40)
my_tuple = (1, 2, 3)
print("Original tuple:", my_tuple)
try:
    my_tuple[0] = 10  # This will raise an error
except TypeError as e:
    print(f"Error: Tuples are immutable! - {e}")
