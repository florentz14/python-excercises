# Tabla de multiplicación interactiva
# El usuario elige qué tabla de multiplicación desea ver (1-12)

print("=" * 50)
print("TABLA DE MULTIPLICACIÓN INTERACTIVA")
print("=" * 50)

# Solicitar al usuario el número de la tabla que desea
while True:
    try:
        # Pedir al usuario que ingrese un número entre 1 y 12
        number = int(input("\n¿Qué tabla de multiplicación deseas? (1-12): "))
        
        # Validar que el número esté entre 1 y 12
        if number < 1 or number > 12:
            print("Por favor, ingresa un número entre 1 y 12")
            continue
        
        # Si el número es válido, salir del loop
        break
    
    except ValueError:
        # Si el usuario no ingresa un número válido
        print("Por favor, ingresa un número válido")

# Mostrar la tabla de multiplicación elegida
print(f"\nTabla de Multiplicación del {number}")
print("=" * 40)

# Loop para multiplicar desde 1 hasta 12
for i in range(1, 13):
    resultado = number * i
    print(f"{number} x {i:2d} = {resultado:3d}")

print("=" * 40)
