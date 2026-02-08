# Listas - filter(): filtrar elementos
print("=== filter - filtrar elementos ===")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Numeros: {numeros}")
print(f"Pares (filter): {pares}")

# Más ejemplos de filter
print("\n=== Más ejemplos ===")
impares = list(filter(lambda x: x % 2 != 0, numeros))
print(f"Impares: {impares}")

mayores_5 = list(filter(lambda x: x > 5, numeros))
print(f"Mayores que 5: {mayores_5}")

# filter con función definida
def es_positivo(x):
    return x > 0

numeros = [-3, -1, 0, 2, 5, -4, 8]
positivos = list(filter(es_positivo, numeros))
print(f"Numeros: {numeros}")
print(f"Positivos: {positivos}")
