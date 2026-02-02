"""
Números complejos en Python
===========================
Tema: Tipos numéricos - complex (01_Variables_y_Tipos_Datos)
Descripción: Crear números complejos (1+2j), partes real e imaginaria,
operaciones aritméticas, conjugate(), abs(), phase() y el módulo cmath.
"""
import cmath
# Examples of different numeric types in Python

x = 1
x = 1.1
x = 1+2j  # complex number with real part 1 and imaginary part 2
print(x)

# Display the real and imaginary parts of the complex number
print("Real part:", x.real)
print("Imaginary part:", x.imag)
# Perform and display various arithmetic operations
print("Addition:", x + (2 + 3j))
print("Subtraction:", x - (1 + 1j))
print("Multiplication:", x * (0 + 2j))
print("Division:", x / (1 + 0j))
print("Conjugate:", x.conjugate())
print("Magnitude:", abs(x))
print("Phase (angle):", cmath.phase(x))
