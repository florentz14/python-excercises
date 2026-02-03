# 12_03_multiple_return_lambda.py - Retorno múltiple y funciones lambda

print("=== Retorno Múltiple y Lambda ===\n")

# Función que retorna múltiples valores
print("=== Retornar Múltiples Valores ===")
def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None
    return suma, resta, multiplicacion, division

s, r, m, d = operaciones(10, 5)
print(f"Operaciones con 10 y 5:")
print(f"  Suma: {s}")
print(f"  Resta: {r}")
print(f"  Multiplicación: {m}")
print(f"  División: {d}\n")

# Funciones lambda (anónimas)
print("=== Funciones Lambda ===")
cuadrado = lambda x: x**2
print(f"cuadrado(5) = {cuadrado(5)}")

numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(f"Cuadrados de {numeros}: {cuadrados}\n")
