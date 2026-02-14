"""
Constantes y asignación múltiple
=================================
Tema: Variables (01_Variables_y_Tipos_Datos)
Descripción: Constantes (UPPER_CASE), asignación múltiple, intercambio de variables.
"""
# Constantes: convención UPPER_CASE para valores que no cambian
PI = 3.14159
IVA = 0.16
MAX_INTENTOS = 3

print("Constantes:")
print(f"PI = {PI}")
print(f"IVA = {IVA * 100}%")

# Asignación múltiple
x, y = 10, 20
print(f"\nAsignación múltiple: x, y = 10, 20 -> x={x}, y={y}")

# Misma valor a varias variables
a = b = c = 0
print(f"Mismo valor: a = b = c = 0 -> a={a}, b={b}, c={c}")

# Intercambio de variables (swap) sin variable temporal
a, b = 5, 10
print(f"\nAntes del swap: a={a}, b={b}")
a, b = b, a
print(f"Después del swap: a={a}, b={b}")
