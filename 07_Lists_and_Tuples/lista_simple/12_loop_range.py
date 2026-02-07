# ---------------------------------------------------------------------------
# Lista Simple - 12: Recorrer con range() e Indices
# ---------------------------------------------------------------------------
# Descripcion: Recorrer una lista usando range(len(lista)) permite acceder
#              a los elementos por su indice numerico. Es util cuando se
#              necesita el indice para modificar la lista o comparar
#              elementos adyacentes.
# Sintaxis:    for i in range(len(lista)):
# ---------------------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "pineapple", "grape"]

# --- Recorrer usando indices ---
print("=== Loop with indices ===")
for i in range(len(fruits)):
    print(f"  Index {i}: {fruits[i]}")
# Output:
#   Index 0: apple
#   Index 1: banana
#   Index 2: cherry
#   Index 3: pineapple
#   Index 4: grape

# --- Modificar elementos durante el recorrido ---
numeros = [1, 2, 3, 4, 5]
print("\nOriginal:", numeros)

for i in range(len(numeros)):
    numeros[i] = numeros[i] * 2  # Duplicar cada elemento

print("Duplicados:", numeros)
# Output: [2, 4, 6, 8, 10]

# --- Recorrer en reversa ---
print("\n=== Reverse loop ===")
for i in range(len(fruits) - 1, -1, -1):
    print(f"  Index {i}: {fruits[i]}")
# Output:
#   Index 4: grape
#   Index 3: pineapple
#   Index 2: cherry
#   Index 1: banana
#   Index 0: apple

# --- Comparar elementos adyacentes ---
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nLista: {numeros}")
print("Pares adyacentes donde el segundo es mayor:")
for i in range(len(numeros) - 1):
    if numeros[i] < numeros[i + 1]:
        print(f"  {numeros[i]} < {numeros[i + 1]} (indices {i} y {i + 1})")

# --- Recorrer cada 2 elementos (paso) ---
print("\n=== Cada 2 elementos ===")
letras = ["a", "b", "c", "d", "e", "f"]
for i in range(0, len(letras), 2):
    print(f"  Indice {i}: {letras[i]}")
# Output:
#   Indice 0: a
#   Indice 2: c
#   Indice 4: e

# ---------------------------------------------------------------------------
# Nota: Para simple iteracion, prefiere 'for x in lista' (mas limpio).
#       Usa 'for i in range(len(lista))' cuando NECESITES el indice.
#       O mejor aun, usa enumerate() para tener ambos.
# ---------------------------------------------------------------------------
