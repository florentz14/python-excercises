"""
Operadores de comparación en Python
====================================
Tema: Variables (01_Variables_y_Tipos_Datos)
Descripción: ==, !=, <, >, <=, >= para comparar valores.
Retornan True o False (tipo bool).
"""
# Operadores de comparación
a = 10
b = 5

print("a =", a, ", b =", b)
print("a == b (igual):", a == b)
print("a != b (diferente):", a != b)
print("a < b (menor):", a < b)
print("a > b (mayor):", a > b)
print("a <= b (menor o igual):", a <= b)
print("a >= b (mayor o igual):", a >= b)

# Comparaciones con strings (orden lexicográfico)
s1 = "abc"
s2 = "abd"
print("\nStrings: s1 =", s1, ", s2 =", s2)
print("s1 < s2:", s1 < s2)

# Comparaciones encadenadas
x = 5
print("\n1 < x < 10:", 1 < x < 10)
print("1 < x < 3:", 1 < x < 3)
