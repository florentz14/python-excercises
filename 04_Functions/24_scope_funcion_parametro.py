# -------------------------------------------------
# File: 24_scope_funcion_parametro.py
# Description: Variable scope and higher-order functions.
#              Local/global scope and functions as parameters.
# -------------------------------------------------

print("=== Scope y Función como Parámetro ===\n")

# Scope (ámbito) de variables
print("=== Scope de Variables ===")
variable_global = "Soy global"

def funcion_scope():
    variable_local = "Soy local"
    print(f"Dentro de la función: {variable_local}")
    print(f"Variable global: {variable_global}")

funcion_scope()
print(f"Fuera de la función: {variable_global}\n")

# Función como parámetro
print("=== Función como Parámetro ===")
def aplicar_funcion(func, valor):
    return func(valor)

def doble(x):
    return x * 2

def triple(x):
    return x * 3

print(f"aplicar_funcion(doble, 5) = {aplicar_funcion(doble, 5)}")
print(f"aplicar_funcion(triple, 5) = {aplicar_funcion(triple, 5)}")
