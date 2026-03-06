# ---------------------------------------------------------------------------
# Lista Simple - 16: Metodo reverse() - Invertir Lista
# ---------------------------------------------------------------------------
# Descripcion: El metodo reverse() invierte el orden de los elementos de la
#              lista IN-PLACE (modifica la lista original). No ordena, solo
#              invierte la posicion de los elementos.
# Sintaxis:    lista.reverse()
# Complejidad: O(n)
# ---------------------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "pineapple", "grape", "mango"]
print("Original:", fruits)

fruits.reverse()
print("reverse():", fruits)
# Output: ['mango', 'grape', 'pineapple', 'cherry', 'banana', 'apple']

# --- Con numeros ---
numeros = [1, 2, 3, 4, 5]
numeros.reverse()
print("\nNumeros invertidos:", numeros)
# Output: [5, 4, 3, 2, 1]

# ---------------------------------------------------------------------------
# Alternativas para invertir una lista
# ---------------------------------------------------------------------------

original = [10, 20, 30, 40, 50]

# Metodo 1: reverse() (modifica la original)
copia1 = original.copy()
copia1.reverse()
print("\nreverse():", copia1)

# Metodo 2: slicing [::-1] (crea una nueva lista)
invertida = original[::-1]
print("[::-1]:", invertida)
print("Original intacto:", original)

# Metodo 3: reversed() (retorna un iterador, no modifica)
invertida2 = list(reversed(original))
print("reversed():", invertida2)

# ---------------------------------------------------------------------------
# Diferencia entre reverse() y sort(reverse=True)
# ---------------------------------------------------------------------------
# reverse()          -> Solo invierte el orden actual (no ordena)
# sort(reverse=True) -> Ordena de mayor a menor

ejemplo = [3, 1, 4, 1, 5]
print(f"\nOriginal: {ejemplo}")

r1 = ejemplo.copy()
r1.reverse()
print(f"reverse():          {r1}")   # [5, 1, 4, 1, 3]

r2 = ejemplo.copy()
r2.sort(reverse=True)
print(f"sort(reverse=True): {r2}")   # [5, 4, 3, 1, 1]
