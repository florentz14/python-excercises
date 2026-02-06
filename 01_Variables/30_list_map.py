# Listas - map(): aplicar función a cada elemento
print("=== map - aplicar funcion ===")
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(f"Numeros: {numeros}")
print(f"Cuadrados (map): {cuadrados}")

# Más ejemplos de map
print("\n=== Más ejemplos ===")
nombres = ["ana", "juan", "pedro"]
mayusculas = list(map(str.upper, nombres))
print(f"Nombres: {nombres}")
print(f"Mayúsculas: {mayusculas}")

# map con función definida
def duplicar(x):
    return x * 2

numeros = [1, 2, 3, 4, 5]
duplicados = list(map(duplicar, numeros))
print(f"Duplicados: {duplicados}")
