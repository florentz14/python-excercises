# ---------------------------------------------------------------------------
# Lista Simple - 24: Funciones min(), max() y sum()
# ---------------------------------------------------------------------------
# Descripcion: Python incluye funciones integradas para obtener el valor
#              minimo, maximo y la suma total de los elementos de una lista.
# Sintaxis:    min(lista)   -> retorna el menor
#              max(lista)   -> retorna el mayor
#              sum(lista)   -> retorna la suma de todos
# ---------------------------------------------------------------------------

numeros = [34, 12, 89, 5, 67, 23, 45]
print("Lista:", numeros)

# --- min(): obtener el menor ---
print(f"Minimo: {min(numeros)}")
# Output: 5

# --- max(): obtener el mayor ---
print(f"Maximo: {max(numeros)}")
# Output: 89

# --- sum(): obtener la suma total ---
print(f"Suma: {sum(numeros)}")
# Output: 275

# --- Calcular el promedio ---
promedio = sum(numeros) / len(numeros)
print(f"Promedio: {promedio:.2f}")
# Output: 39.29

# --- Con strings: min y max usan orden alfabetico ---
fruits = ["mango", "banana", "cherry", "apple", "grape", "pineapple"]
print(f"\nMin (alphabetical): {min(fruits)}")   # apple
print(f"Max (alphabetical): {max(fruits)}")     # pineapple

# --- min/max con key personalizada ---
palabras = ["python", "es", "un", "lenguaje", "genial"]
mas_corta = min(palabras, key=len)
mas_larga = max(palabras, key=len)
print(f"\nPalabra mas corta: '{mas_corta}' ({len(mas_corta)} letras)")
print(f"Palabra mas larga: '{mas_larga}' ({len(mas_larga)} letras)")

# --- sum() con valor inicial ---
numeros2 = [1, 2, 3, 4, 5]
total_con_base = sum(numeros2, 100)  # Empieza sumando desde 100
print(f"\nsum([1,2,3,4,5], 100) = {total_con_base}")
# Output: 115

# ---------------------------------------------------------------------------
# Error: estas funciones no funcionan con listas vacias (excepto sum)
# ---------------------------------------------------------------------------
try:
    min([])
except ValueError as e:
    print(f"\nError min([]): {e}")

# sum() si funciona con lista vacia
print(f"sum([]) = {sum([])}")
# Output: 0
