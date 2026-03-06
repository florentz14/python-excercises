# -------------------------------------------------
# File: 20_multiple_return_lambda.py
# Description: Multiple return values and lambdas.
#              Anonymous functions and tuple returns.
# -------------------------------------------------

print("=== Retorno Múltiple y Lambda ===\n")

# Función que retorna múltiples valores
print("=== Retornar Múltiples Valores ===")
def operaciones(a, b):            # función con dos parámetros
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None  # evita división por cero
    return suma, resta, multiplicacion, division  # retorna tupla con 4 valores

s, r, m, d = operaciones(10, 5)   # desempaqueta los 4 valores en variables
print(f"Operaciones con 10 y 5:")
print(f"  Suma: {s}")
print(f"  Resta: {r}")
print(f"  Multiplicación: {m}")
print(f"  División: {d}\n")

# Funciones lambda (anónimas)
print("=== Funciones Lambda ===")
cuadrado = lambda x: x**2         # función anónima: recibe x, retorna x²
print(f"cuadrado(5) = {cuadrado(5)}")

numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))  # map aplica lambda a cada elemento
print(f"Cuadrados de {numeros}: {cuadrados}\n")
