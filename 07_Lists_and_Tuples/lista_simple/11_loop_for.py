# ---------------------------------------------------------------------------
# Lista Simple - 11: Recorrer con for (Iteracion Directa)
# ---------------------------------------------------------------------------
# Descripcion: La forma mas pytonica de recorrer una lista es iterar
#              directamente sobre sus elementos usando un bucle for.
#              No se necesita usar indices.
# Sintaxis:    for elemento in lista:
# ---------------------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "pineapple", "grape", "blueberry"]

# --- Recorrer e imprimir cada elemento ---
print("=== Direct loop ===")
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry
# pineapple
# grape
# blueberry

# --- Recorrer con formato personalizado ---
print("\n=== Formatted ===")
for fruit in fruits:
    print(f"  - {fruit.upper()}")
# Output:
#   - APPLE
#   - BANANA
#   - CHERRY
#   - PINEAPPLE
#   - GRAPE
#   - BLUEBERRY

# --- Recorrer y aplicar una condicion ---
print("\n=== Fruits with more than 5 letters ===")
for fruit in fruits:
    if len(fruit) > 5:
        print(f"  {fruit} ({len(fruit)} letters)")
# Output:
#   banana (6 letters)
#   cherry (6 letters)
#   pineapple (9 letters)
#   blueberry (9 letters)

# --- Recorrer y acumular un resultado ---
numeros = [10, 20, 30, 40, 50]
suma = 0
for num in numeros:
    suma += num
print(f"\nSuma de {numeros} = {suma}")
# Output: Suma de [10, 20, 30, 40, 50] = 150

# ---------------------------------------------------------------------------
# Usar enumerate() para obtener indice Y valor al mismo tiempo
# ---------------------------------------------------------------------------
print("\n=== With enumerate() ===")
for i, fruit in enumerate(fruits):
    print(f"  [{i}] {fruit}")
# Output:
#   [0] apple
#   [1] banana
#   [2] cherry
#   [3] pineapple
#   [4] grape
#   [5] blueberry

# enumerate con indice inicial personalizado
print("\n=== enumerate starting at 1 ===")
for num, fruit in enumerate(fruits, start=1):
    print(f"  {num}. {fruit}")
# Output:
#   1. apple
#   2. banana
#   3. cherry
#   4. pineapple
#   5. grape
#   6. blueberry
