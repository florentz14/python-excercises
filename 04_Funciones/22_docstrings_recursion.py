# 12_05_docstrings_recursion.py - Docstrings y funciones recursivas

print("=== Docstrings y Recursión ===\n")

# Funciones con documentación (docstrings)
print("=== Funciones con Documentación ===")
def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    Parámetros:
    base (float): La base del rectángulo
    altura (float): La altura del rectángulo

    Retorna:
    float: El área del rectángulo
    """
    return base * altura

area = calcular_area_rectangulo(5, 3)
print(f"Área del rectángulo (5x3): {area}")
print(f"Documentación: {calcular_area_rectangulo.__doc__}\n")

# Función recursiva
print("=== Función Recursiva ===")
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"factorial(5) = {factorial(5)}")
print(f"factorial(0) = {factorial(0)}\n")
