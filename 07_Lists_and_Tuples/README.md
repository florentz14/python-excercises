# 07 - Lists and Tuples

List and tuple exercises in Python, organized by topic in subfolders.

## Structure

```
07_Lists_and_Tuples/
|-- list_basics/           (26 files)  Basic list methods
|-- tuples/                (21 files)  Tuple exercises
|-- list_nested/           (40 files)  Nested lists and matrices
|-- list_search_filter/    (64 files)  Search, filter and count
|-- list_sorting/          (10 files)  Sorting and organization
|-- list_math/             (25 files)  Mathematical operations
|-- list_functional/       (11 files)  Functional programming
|-- list_integrative/      (133 files) Integrative list exercises
```

## Subfolders

### `list_basics/` - Basic Methods (26 files)

Archivos individuales que demuestran cada metodo y operacion de las listas:
`append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`, `copy()`,
`extend()`, `count()`, `index()`, `clear()`, slicing, loops, list comprehension,
`del`, `len()`, `in`, `min/max/sum`, concatenacion y mas.

### `tuples/` - Tuple Exercises (21 files)

Operations with tuples: creation, immutability, access, conversion to list,
operador `in`, concatenacion, repeticion, unpacking, ordenamiento por elemento,
extraccion de elementos, productos min/max, y conversion a strings.

### `list_nested/` - Nested Lists and Matrices (40 files)

Exercises with lists of lists, 2D/3D matrices: aplanar (flatten), sublistas,
columnas, diagonales, matrices de ceros, grids, frecuencias en anidadas,
ordenar por suma de filas, extraer columnas, y deep flatten.

### `list_search_filter/` - Search and Filter (64 files)

Search elements, filter by conditions, count occurrences, find
indices, elementos comunes entre listas, duplicados, frecuencias, valores
unicos, verificar primos, y operaciones con funciones de filtrado.

### `list_sorting/` - Sorting (10 files)

Sort lists by different criteria: alfabetico, numerico, por longitud,
por otro lista, mezclar (shuffle), verificar si esta ordenada, y ordenar
listas mixtas.

### `list_math/` - Mathematical Operations (25 files)

Sums, products, averages, max/min, segundo mas grande/pequeno,
criba de Eratostenes, rangos, promedios ponderados, y operaciones con
funciones de mapeo.

### `list_functional/` - Functional Programming (11 files)

Permutations, combinations, powerset, grouping by function, diferencia/
union/interseccion con funciones personalizadas, y verificaciones con
predicados (`all`, `any`).

### `list_integrative/` - Integrative Exercises (133 files)

General list manipulation: modify, insert, delete, rotate,
intercalar, codificacion run-length, operaciones con diccionarios en listas,
conversion de tipos, iteracion ciclica, bigrams, fibonacci, y muchos mas
ejercicios variados.

## Resumen

| Subcarpeta | Archivos | Tema |
|------------|----------|------|
| `list_basics/` | 26 | Basic list methods |
| `tuples/` | 21 | Tuple exercises |
| `list_nested/` | 40 | Nested lists and matrices |
| `list_search_filter/` | 64 | Search, filter and count |
| `list_sorting/` | 10 | Sorting and organization |
| `list_math/` | 25 | Mathematical operations |
| `list_functional/` | 11 | Functional programming |
| `list_integrative/` | 133 | Integrative list exercises |
| **Total** | **332** | |

## How to run

Cada archivo se puede ejecutar de forma independiente:

```bash
cd 07_Lists_and_Tuples
python list_basics/01_crear_lista.py
python tuples/001_colors.py
python list_math/034_sieve_eratosthenes.py
```

## Requisitos

- Python 3.x
- No requiere librerias externas
