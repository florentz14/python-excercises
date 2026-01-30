# Matriz de pares e impares
# Crear una matriz y clasificar sus elementos en pares e impares

print("Clasificar Matriz 2D en Pares e Impares")
print("=" * 45)

# Definir una matriz
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Listas para almacenar pares e impares
even_numbers = []
odd_numbers = []

print("Matriz:")
for row in matrix:
    print(row)

print("\nClasificando elementos...")

# Loop externo: itera sobre cada fila
for row in matrix:
    # Loop interno: itera sobre cada elemento
    for num in row:
        # Verificar si es par o impar
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

print(f"\nNúmeros pares: {even_numbers}")
print(f"Números impares: {odd_numbers}")
print(f"Total de pares: {len(even_numbers)}")
print(f"Total de impares: {len(odd_numbers)}")
