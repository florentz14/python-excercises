# ---------------------------------------------------------------------------
# Debugging Assignment - Tuplas (corregido)
# Las tuplas son INMUTABLES: no se pueden modificar elementos.
# ---------------------------------------------------------------------------

numbers = (4, 8, 12, 16, 20, 24, 28, 32)

print("Using for loop")

for i in range(len(numbers)):
    # Las tuplas no se pueden modificar:numbers[i] = numbers[i] + 1 no se puede hacer porque es una tupla inmutable, da error TypeError
    # Imprimimos el valor + 1 sin modificar la tupla
    print(numbers[i] + 1)

print("Using while loop")
i = 0
total = 0
while i < len(numbers):  # i <= len() causaría IndexError (índice 8 no existe)
    total = total + numbers[i]
    i += 1  # Incrementar i para evitar bucle infinito
print("Total:", total)
