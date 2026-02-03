# 05_Estructuras_de_Datos

Matrices, **métodos de ordenamiento** y **algoritmos de búsqueda**.

## Métodos de ordenamiento

| Archivo | Contenido |
|---------|-----------|
| `ordenamiento_00_utilidades.py` | `esta_ordenada()`, `generar_lista_aleatoria()` |
| `ordenamiento_01_bubble.py` | Bubble Sort y versión optimizada |
| `ordenamiento_02_selection.py` | Selection Sort |
| `ordenamiento_03_insertion.py` | Insertion Sort |
| `ordenamiento_04_merge.py` | Merge Sort y `merge()` |
| `ordenamiento_05_quick.py` | Quick Sort y Quick Sort in-place |
| `ordenamiento_06_heap.py` | Heap Sort y `heapify()` |
| `ordenamiento_07_counting.py` | Counting Sort (rango pequeño) |
| `ordenamiento_08_comparacion.py` | Compara tiempos de todos los métodos |
| `ordenamiento_09_complejidad.py` | Tabla de complejidad (mejor/promedio/peor) |
| `ordenamiento_10_casos_especiales.py` | Casos: ordenada, inversa, iguales, vacía |
| `ordenamiento_11_resumen.py` | Recomendaciones de uso |

**Dependencias:** 08 importa de 00–07; 10 importa de 00 y 04. Ejecutar desde la carpeta `05_Estructuras_de_Datos` para que los imports funcionen.

```bash
cd 05_Estructuras_de_Datos
python ordenamiento_00_utilidades.py
python ordenamiento_01_bubble.py
python ordenamiento_08_comparacion.py
python ordenamiento_09_complejidad.py
python ordenamiento_10_casos_especiales.py
python ordenamiento_11_resumen.py
```

## Algoritmos de búsqueda

| Archivo | Contenido |
|---------|-----------|
| `busqueda_00_lineal.py` | Búsqueda lineal, optimizada, todas las ocurrencias |
| `busqueda_01_binaria.py` | Búsqueda binaria (iterativa, recursiva, primera/última ocurrencia) |
| `busqueda_02_strings.py` | Búsqueda de patrón en texto (fuerza bruta) |
| `busqueda_03_kmp.py` | Algoritmo KMP (Knuth-Morris-Pratt) |
| `busqueda_04_comparacion.py` | Compara lineal vs binaria y bruta vs KMP |
| `busqueda_05_utilidades.py` | Posición de inserción, conteo de ocurrencias en lista ordenada |
| `busqueda_06_resumen.py` | Resumen y recomendaciones |

**Dependencias:** 04 importa de 00, 01, 02, 03; 05 importa de 01. Ejecutar desde `05_Estructuras_de_Datos`.

```bash
cd 05_Estructuras_de_Datos
python busqueda_00_lineal.py
python busqueda_01_binaria.py
python busqueda_02_strings.py
python busqueda_03_kmp.py
python busqueda_04_comparacion.py
python busqueda_05_utilidades.py
python busqueda_06_resumen.py
```

## Algoritmos Greedy (42_xx)

| Archivo | Contenido |
|---------|-----------|
| `42_01_mochila_fraccionaria.py` | Mochila fraccionaria (valor/peso, O(n log n)) |
| `42_02_seleccion_actividades.py` | Selección de actividades (orden por fin, O(n log n)) |
| `42_03_kruskal.py` | MST con Kruskal (Union-Find, O(E log E)) |
| `42_04_huffman.py` | Codificación de Huffman (heap, O(n log n)) |
| `42_05_cambio_monedas.py` | Cambio de monedas greedy (solo sistemas canónicos) |
| `42_06_interval_scheduling.py` | Interval scheduling con pesos (versión simplificada) |
| `42_07_resumen.py` | Resumen de algoritmos greedy |

Ejecutar desde la raíz del proyecto o desde `05_Estructuras_de_Datos`:

```bash
python 05_Estructuras_de_Datos/42_01_mochila_fraccionaria.py
python 05_Estructuras_de_Datos/42_04_huffman.py
```

## Algoritmos avanzados de strings (44_xx)

| Archivo | Contenido |
|---------|-----------|
| `44_01_rabin_karp.py` | Rabin-Karp (búsqueda con rolling hash, O(n+m) promedio) |
| `44_02_z_algorithm.py` | Z-Algorithm (Z-array y búsqueda de patrón, O(n+m)) |
| `44_03_longest_common_substring.py` | Subcadena común más larga (DP, O(m*n)) |
| `44_04_edit_distance.py` | Distancia de Levenshtein (insertar/eliminar/sustituir, O(m*n)) |
| `44_05_longest_palindromic_substring.py` | Subcadena palindrómica más larga (expansión centro, O(n²)) |
| `44_06_anagramas_permutaciones.py` | Anagramas, agrupación, permutaciones |
| `44_07_resumen.py` | Resumen de algoritmos de strings |

```bash
python 05_Estructuras_de_Datos/44_01_rabin_karp.py
python 05_Estructuras_de_Datos/44_04_edit_distance.py
```

## Algoritmos matemáticos (45_xx)

| Archivo | Contenido |
|---------|-----------|
| `45_01_pascal.py` | Triángulo de Pascal, coeficientes binomiales, fila n |
| `45_02_euclides.py` | MCD (iterativo/recursivo), MCM, Euclides extendido |
| `45_03_eratostenes.py` | Criba de Eratóstenes, `es_primo_optimizado` |
| `45_04_exponenciacion_modular.py` | Exponenciación modular rápida (base^exp mod m) |
| `45_05_fibonacci_matematico.py` | Fibonacci: Binet y exponenciación de matrices |
| `45_06_factorizacion.py` | Factorización en primos, factores únicos, contar divisores |
| `45_07_conversion_bases.py` | Conversión entre bases (decimal, binario, octal, hex) |
| `45_08_resumen.py` | Resumen de algoritmos matemáticos |

```bash
python 05_Estructuras_de_Datos/45_01_pascal.py
python 05_Estructuras_de_Datos/45_02_euclides.py
```

## Backtracking (47_xx)

| Archivo | Contenido |
|---------|-----------|
| `47_01_n_reinas.py` | N-Reinas: colocar N reinas sin que se ataquen |
| `47_02_sudoku.py` | Solucionador de Sudoku 9x9 |
| `47_03_laberinto.py` | Resolución de laberintos (camino inicio–destino) |
| `47_04_permutaciones_backtracking.py` | Generación de permutaciones |
| `47_05_combinaciones_backtracking.py` | Generación de combinaciones de k en n |
| `47_06_subset_sum.py` | Subset Sum (subconjuntos que sumen objetivo) |
| `47_07_resumen.py` | Resumen de backtracking |

```bash
python 05_Estructuras_de_Datos/47_01_n_reinas.py
python 05_Estructuras_de_Datos/47_04_permutaciones_backtracking.py
```

## Estructuras de datos avanzadas (48_xx)

| Archivo | Contenido |
|---------|-----------|
| `48_01_trie.py` | Trie (árbol de prefijos): insertar, buscar, autocompletar |
| `48_02_segment_tree.py` | Segment Tree: consulta/actualización de rango (suma, mín, máx) |
| `48_03_fenwick_tree.py` | Fenwick Tree (BIT): sumas de prefijos y rango |
| `48_04_union_find_mejorado.py` | Union-Find con path compression y union by rank |
| `48_05_resumen.py` | Resumen y complejidades |

```bash
python 05_Estructuras_de_Datos/48_01_trie.py
python 05_Estructuras_de_Datos/48_03_fenwick_tree.py
```

## Otros archivos

- `count.py` – conteos.  
  (El contenido de `matrix.py` y `matrix_operations.py` se movió a **08_Matrices** en archivos `matrix_07_*` … `matrix_20_*`.)
