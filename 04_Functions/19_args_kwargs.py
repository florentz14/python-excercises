# -------------------------------------------------
# File: 19_args_kwargs.py
# Description: Variable arguments (*args, **kwargs).
#              Flexible function parameters.
# -------------------------------------------------

print("=== *args y **kwargs ===\n")

# Función con argumentos variables (*args)
print("=== Argumentos Variables (*args) ===")
def sumar_numeros(*args):
    return sum(args)

print(f"sumar_numeros(1, 2, 3) = {sumar_numeros(1, 2, 3)}")
print(f"sumar_numeros(1, 2, 3, 4, 5) = {sumar_numeros(1, 2, 3, 4, 5)}\n")

# Función con keyword arguments (**kwargs)
print("=== Keyword Arguments (**kwargs) ===")
def imprimir_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"  {clave}: {valor}")

print("Información:")
imprimir_info(nombre="Juan", edad=25, ciudad="Madrid")
print()
