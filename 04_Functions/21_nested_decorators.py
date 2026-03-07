# -------------------------------------------------
# File: 21_anidadas_decoradores.py
# Description: Nested functions and decorators.
#              Function composition patterns.
# -------------------------------------------------

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
def decorador_simple(func):       # recibe una función como argumento
    def wrapper():                # función interna que "envuelve" a func
        print("Antes de la función")   # código antes de ejecutar func
        func()                    # ejecuta la función original
        print("Después de la función") # código después de ejecutar func
    return wrapper                # retorna la función modificada

@decorador_simple                 # aplica el decorador a decir_hola
def decir_hola():
    print("¡Hola!")

decir_hola()
print()
