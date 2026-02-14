"""
Operaciones aritméticas y lógicas en Python
============================================
Tema: Variables (01_Variables_y_Tipos_Datos)
Descripción: +, -, *, /, //, %, ** y operadores lógicos and, or, not.
"""
# Operadores aritméticos
a = 15
b = 4

print("a =", a, ", b =", b)
print("Suma (a + b):", a + b)
print("Resta (a - b):", a - b)
print("Multiplicación (a * b):", a * b)
print("División (a / b):", a / b)
print("División entera (a // b):", a // b)
print("Módulo/resto (a % b):", a % b)
print("Potencia (a ** 2):", a ** 2)

# Operadores de asignación compuesta
x = 10
x += 5   # x = x + 5
print("\nx += 5 ->", x)
x *= 2   # x = x * 2
print("x *= 2 ->", x)

# Operadores lógicos (and, or, not)
p = True
q = False
print("\np =", p, ", q =", q)
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)

# Aplicación práctica
edad = 25
tiene_licencia = True
puede_conducir = edad >= 18 and tiene_licencia
print("\nEdad:", edad, ", Licencia:", tiene_licencia)
print("Puede conducir:", puede_conducir)
