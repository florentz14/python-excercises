# ---------------------------------------------------------------------------
# Lista Simple - 15: Metodo sort() - Ordenamiento
# ---------------------------------------------------------------------------
# Descripcion: El metodo sort() ordena la lista IN-PLACE (modifica la lista
#              original). Por defecto ordena en orden ascendente.
#              Puede ordenar strings (A-Z), numeros (menor a mayor), y
#              acepta parametros para personalizar el orden.
# Sintaxis:    lista.sort()                   -> ascendente
#              lista.sort(reverse=True)        -> descendente
#              lista.sort(key=funcion)         -> con clave personalizada
# Complejidad: O(n log n) - usa Timsort internamente
# ---------------------------------------------------------------------------

# --- Ordenar strings alfabeticamente (A-Z) ---
fruits = ["orange", "mango", "kiwi", "pineapple", "banana", "grape", "apple"]
print("Original:", fruits)

fruits.sort()
print("sort():", fruits)
# Output: ['apple', 'banana', 'grape', 'kiwi', 'mango', 'orange', 'pineapple']

# --- Ordenar numeros en orden ascendente ---
numeros = [100, 50, 65, 82, 23]
print("\nOriginal:", numeros)

numeros.sort()
print("sort():", numeros)
# Output: [23, 50, 65, 82, 100]

# --- Ordenar en orden descendente (reverse=True) ---
fruits2 = ["orange", "mango", "kiwi", "pineapple", "banana", "grape"]
fruits2.sort(reverse=True)
print("\nsort(reverse=True):", fruits2)
# Output: ['pineapple', 'orange', 'mango', 'kiwi', 'grape', 'banana']

numeros2 = [100, 50, 65, 82, 23]
numeros2.sort(reverse=True)
print("sort(reverse=True):", numeros2)
# Output: [100, 82, 65, 50, 23]

# --- Ordenar con clave personalizada (key) ---
# Ordenar por longitud del string
palabras = ["python", "es", "un", "lenguaje", "increible"]
palabras.sort(key=len)
print("\nOrdenado por longitud:", palabras)
# Output: ['es', 'un', 'python', 'increible', 'lenguaje']

# Ordenar ignorando mayusculas/minusculas
mixed = ["Banana", "apple", "Cherry", "blueberry", "Mango"]
mixed.sort(key=str.lower)
print("Sorted case-insensitive:", mixed)
# Output: ['apple', 'Banana', 'blueberry', 'Cherry', 'Mango']

# --- Diferencia entre sort() y sorted() ---
# sort()   -> modifica la lista original, retorna None
# sorted() -> retorna una NUEVA lista ordenada, no modifica la original

original = [3, 1, 4, 1, 5, 9, 2, 6]
nueva_ordenada = sorted(original)
print(f"\nOriginal intacto: {original}")
print(f"sorted() retorna: {nueva_ordenada}")
# Output: Original: [3, 1, 4, 1, 5, 9, 2, 6]
# Output: sorted(): [1, 1, 2, 3, 4, 5, 6, 9]

# ---------------------------------------------------------------------------
# Nota: sort() solo funciona cuando todos los elementos son comparables
#       entre si. No se puede ordenar una lista mixta como [1, "texto"].
# ---------------------------------------------------------------------------
try:
    mixta = [1, "texto", 3]
    mixta.sort()
except TypeError as e:
    print(f"\nError con lista mixta: {e}")
# Output: Error: '<' not supported between instances of 'str' and 'int'
