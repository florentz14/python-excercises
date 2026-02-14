# 07 - Listas y Tuplas

Ejercicios de listas y tuplas en Python, organizados en subcarpetas por tema.

## Estructura

```
07_Lists_and_Tuples/
|-- lista_simple/          (26 archivos)  Metodos basicos de listas
|-- tuplas/                (21 archivos)  Ejercicios de tuplas
|-- listas_anidadas/       (40 archivos)  Listas anidadas y matrices
|-- busqueda_y_filtrado/   (64 archivos)  Busqueda, filtrado y conteo
|-- ordenamiento/          (10 archivos)  Ordenamiento y organizacion
|-- matematicas/           (25 archivos)  Operaciones matematicas
|-- funcional_y_avanzado/  (11 archivos)  Programacion funcional y avanzada
|-- ejercicios_generales/  (133 archivos) Manipulacion y ejercicios variados
```

## Subcarpetas

### `lista_simple/` - Metodos Basicos (25 archivos)

Archivos individuales que demuestran cada metodo y operacion de las listas:
`append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`, `copy()`,
`extend()`, `count()`, `index()`, `clear()`, slicing, loops, list comprehension,
`del`, `len()`, `in`, `min/max/sum`, concatenacion y mas.

### `tuplas/` - Ejercicios de Tuplas (21 archivos)

Operaciones con tuplas: creacion, inmutabilidad, acceso, conversion a lista,
operador `in`, concatenacion, repeticion, unpacking, ordenamiento por elemento,
extraccion de elementos, productos min/max, y conversion a strings.

### `listas_anidadas/` - Listas Anidadas y Matrices (40 archivos)

Ejercicios con listas de listas, matrices 2D/3D: aplanar (flatten), sublistas,
columnas, diagonales, matrices de ceros, grids, frecuencias en anidadas,
ordenar por suma de filas, extraer columnas, y deep flatten.

### `busqueda_y_filtrado/` - Busqueda y Filtrado (64 archivos)

Buscar elementos, filtrar por condiciones, contar ocurrencias, encontrar
indices, elementos comunes entre listas, duplicados, frecuencias, valores
unicos, verificar primos, y operaciones con funciones de filtrado.

### `ordenamiento/` - Ordenamiento (10 archivos)

Ordenar listas por diferentes criterios: alfabetico, numerico, por longitud,
por otro lista, mezclar (shuffle), verificar si esta ordenada, y ordenar
listas mixtas.

### `matematicas/` - Operaciones Matematicas (25 archivos)

Sumas, productos, promedios, maximos/minimos, segundo mas grande/pequeno,
criba de Eratostenes, rangos, promedios ponderados, y operaciones con
funciones de mapeo.

### `funcional_y_avanzado/` - Programacion Funcional (11 archivos)

Permutaciones, combinaciones, powerset, agrupacion por funcion, diferencia/
union/interseccion con funciones personalizadas, y verificaciones con
predicados (`all`, `any`).

### `ejercicios_generales/` - Ejercicios Generales (133 archivos)

Manipulacion general de listas: modificar, insertar, eliminar, rotar,
intercalar, codificacion run-length, operaciones con diccionarios en listas,
conversion de tipos, iteracion ciclica, bigrams, fibonacci, y muchos mas
ejercicios variados.

## Resumen

| Subcarpeta | Archivos | Tema |
|------------|----------|------|
| `lista_simple/` | 26 | Metodos basicos de listas |
| `tuplas/` | 21 | Ejercicios de tuplas |
| `listas_anidadas/` | 40 | Listas anidadas y matrices |
| `busqueda_y_filtrado/` | 64 | Busqueda, filtrado y conteo |
| `ordenamiento/` | 10 | Ordenamiento y organizacion |
| `matematicas/` | 25 | Operaciones matematicas |
| `funcional_y_avanzado/` | 11 | Programacion funcional |
| `ejercicios_generales/` | 133 | Manipulacion y ejercicios variados |
| **Total** | **332** | |

## Como ejecutar

Cada archivo se puede ejecutar de forma independiente:

```bash
cd 07_Lists_and_Tuples
python lista_simple/01_crear_lista.py
python tuplas/001_colors.py
python matematicas/034_sieve_eratosthenes.py
```

## Requisitos

- Python 3.x
- No requiere librerias externas
