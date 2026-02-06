# 12_01_basica_parametros.py - Funciones básicas, con parámetros y por defecto

print("=== Funciones: Básica, Parámetros y Por Defecto ===\n")

# Función básica
print("=== Función Básica ===")
def saludar():
    return "¡Hola!"

mensaje = saludar()
print(f"Resultado: {mensaje}\n")

# Función con parámetros
print("=== Función con Parámetros ===")
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(f"sumar(5, 3) = {resultado}\n")

# Función con parámetros por defecto
print("=== Parámetros por Defecto ===")
def saludar_persona(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}!"

print(saludar_persona("Juan"))
print(saludar_persona("María", "Buenos días"))
print()
