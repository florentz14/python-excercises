# Triángulo de Pascal
# El usuario define cuántas filas desea ver del triángulo de Pascal
# Cada número es la suma de los dos números superiores

print("=" * 50)
print("TRIÁNGULO DE PASCAL")
print("=" * 50)

# Solicitar al usuario cuántas filas desea
while True:
    try:
        rows = int(
            input("\n¿Cuántas filas del triángulo de Pascal deseas? (1-15): "))

        # Validar que el número sea positivo
        if rows < 1:
            print("Por favor, ingresa un número mayor que 0")
            continue

        if rows > 15:
            print("Por favor, ingresa un número máximo de 15")
            continue

        break

    except ValueError:
        print("Por favor, ingresa un número válido")

print(f"\nTriángulo de Pascal ({rows} filas)")
print("=" * 50)

# Loop externo: itera sobre cada fila
for i in range(rows):
    # Espacios en blanco para centrar el triángulo
    for space in range(rows - i - 1):
        print(" ", end="  ")

    # Calcular los números de la fila actual
    # Usamos la propiedad de que cada número es combinación
    number = 1

    # Loop interno: calcula cada número de la fila
    for j in range(i + 1):
        print(number, end="  ")
        # Calcular el siguiente número de la fila
        # Usando la fórmula: siguiente = actual * (i - j) / (j + 1)
        number = number * (i - j) // (j + 1)

    # Nueva línea después de cada fila
    print()

print("=" * 50)
