# 12_04_anidadas_decoradores.py - Funciones anidadas y decoradores

print("=== Funciones Anidadas y Decoradores ===\n")

# Función dentro de función
print("=== Función Anidada ===")
def funcion_externa(x):
    def funcion_interna(y):
        return y * 2
    return funcion_interna(x) + 10

resultado = funcion_externa(5)
print(f"función_externa(5) = {resultado}\n")

# Decoradores (concepto básico)
print("=== Decoradores ===")
def decorador_simple(func):
    def wrapper():
        print("Antes de la función")
        func()
        print("Después de la función")
    return wrapper

@decorador_simple
def decir_hola():
    print("¡Hola!")

decir_hola()
print()
