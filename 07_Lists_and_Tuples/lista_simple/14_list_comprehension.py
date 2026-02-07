# ---------------------------------------------------------------------------
# Lista Simple - 14: List Comprehension
# ---------------------------------------------------------------------------
# Descripcion: List comprehension es una sintaxis compacta para crear listas
#              a partir de iterables existentes. Combina el bucle for y la
#              condicion if en UNA sola linea.
# Sintaxis:    [expresion for elemento in iterable]
#              [expresion for elemento in iterable if condicion]
#              [expr_true if condicion else expr_false for elemento in iterable]
# ---------------------------------------------------------------------------

# --- Filter fruits that contain "a" (compare with previous file) ---
fruits = ["apple", "banana", "cherry", "kiwi", "mango", "grape", "pear", "peach"]

# Con bucle (forma clasica):
# new_list = []
# for fruit in fruits:
#     if "a" in fruit:
#         new_list.append(fruit)

# Con list comprehension (forma pytonica):
new_list = [fruit for fruit in fruits if "a" in fruit]
print("Fruits with 'a':", new_list)
# Output: ['banana', 'mango', 'grape', 'pear', 'peach']

# --- Crear lista de cuadrados ---
cuadrados = [x ** 2 for x in range(1, 11)]
print("Cuadrados:", cuadrados)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# --- Filtrar numeros pares ---
pares = [x for x in range(1, 21) if x % 2 == 0]
print("Pares del 1-20:", pares)
# Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# --- Transformar: convertir a mayusculas ---
uppercased = [fruit.upper() for fruit in fruits]
print("Uppercased:", uppercased)
# Output: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO', 'GRAPE', 'PEAR', 'PEACH']

# --- Condicional con if-else (sin filtrar, transforma todos) ---
clasificacion = ["par" if x % 2 == 0 else "impar" for x in range(1, 6)]
print("Clasificacion:", clasificacion)
# Output: ['impar', 'par', 'impar', 'par', 'impar']

# --- Comprehension anidado (aplanar lista de listas) ---
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
plana = [num for fila in matriz for num in fila]
print("Aplanada:", plana)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- Filtrar y transformar en un paso ---
# Obtener longitudes de palabras que tienen mas de 4 letras
palabras = ["hola", "mundo", "sol", "programacion", "py"]
longitudes = [len(p) for p in palabras if len(p) > 4]
print("Longitudes (>4 letras):", longitudes)
# Output: [5, 12]

# ---------------------------------------------------------------------------
# Comparacion de rendimiento:
# List comprehension es generalmente mas rapido que el bucle for
# equivalente porque esta optimizado internamente por Python.
#
# Regla: Si la comprehension se vuelve dificil de leer, usa un bucle for.
# ---------------------------------------------------------------------------
