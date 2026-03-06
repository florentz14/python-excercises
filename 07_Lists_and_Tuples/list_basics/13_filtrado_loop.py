# ---------------------------------------------------------------------------
# Lista Simple - 13: Filtrado con Bucle for
# ---------------------------------------------------------------------------
# Descripcion: Crear una nueva lista filtrando elementos de otra lista
#              usando un bucle for tradicional con una condicion if.
#              Es la forma clasica antes de aprender list comprehension.
# Patron:      nueva_lista = []
#              for x in lista:
#                  if condicion:
#                      nueva_lista.append(x)
# ---------------------------------------------------------------------------

# --- Filter fruits that contain the letter "a" ---
fruits = ["apple", "banana", "cherry", "kiwi", "mango", "grape", "pear", "peach"]

new_list = []
for fruit in fruits:
    if "a" in fruit:
        new_list.append(fruit)

print("Fruits with 'a':", new_list)
# Output: ['banana', 'mango', 'grape', 'pear', 'peach']

# --- Filtrar numeros pares ---
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)

print("Numeros pares:", pares)
# Output: [2, 4, 6, 8, 10]

# --- Filtrar strings con longitud mayor a 5 ---
palabras = ["sol", "computadora", "rio", "programacion", "luz", "python"]

largas = []
for palabra in palabras:
    if len(palabra) > 5:
        largas.append(palabra)

print("Palabras largas:", largas)
# Output: ['computadora', 'programacion', 'python']

# --- Filtrar y transformar al mismo tiempo ---
# Obtener el cuadrado de los numeros positivos
datos = [-3, 5, -1, 8, 0, -7, 4, 2]

cuadrados_positivos = []
for n in datos:
    if n > 0:
        cuadrados_positivos.append(n ** 2)

print("Cuadrados de positivos:", cuadrados_positivos)
# Output: [25, 64, 16, 4]

# --- Filtrar eliminando duplicados (mantener orden) ---
con_duplicados = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

sin_duplicados = []
for n in con_duplicados:
    if n not in sin_duplicados:
        sin_duplicados.append(n)

print("Sin duplicados:", sin_duplicados)
# Output: [3, 1, 4, 5, 9, 2, 6]

# ---------------------------------------------------------------------------
# Nota: Este patron es funcional pero verboso. En el siguiente archivo
#       veremos como simplificarlo usando List Comprehension.
# ---------------------------------------------------------------------------
