# 05_Estructuras_de_Datos

Algoritmos de ordenamiento, búsqueda, greedy, strings, matemáticos, backtracking y estructuras avanzadas.

## Algoritmos Greedy (01-07)

| Archivo | Contenido |
|---------|-----------|
| `01_mochila_fraccionaria.py` | Mochila fraccionaria (valor/peso, O(n log n)) |
| `02_seleccion_actividades.py` | Selección de actividades (orden por fin, O(n log n)) |
| `03_kruskal.py` | MST con Kruskal (Union-Find, O(E log E)) |
| `04_huffman.py` | Codificación de Huffman (heap, O(n log n)) |
| `05_cambio_monedas.py` | Cambio de monedas greedy (solo sistemas canónicos) |
| `06_interval_scheduling.py` | Interval scheduling con pesos (versión simplificada) |
| `07_resumen.py` | Resumen de algoritmos greedy |

## Algoritmos de Strings (08-14)

| Archivo | Contenido |
|---------|-----------|
| `08_rabin_karp.py` | Rabin-Karp (búsqueda con rolling hash, O(n+m) promedio) |
| `09_z_algorithm.py` | Z-Algorithm (Z-array y búsqueda de patrón, O(n+m)) |
| `10_longest_common_substring.py` | Subcadena común más larga (DP, O(m*n)) |
| `11_edit_distance.py` | Distancia de Levenshtein (insertar/eliminar/sustituir, O(m*n)) |
| `12_longest_palindromic_substring.py` | Subcadena palindrómica más larga (expansión centro, O(n²)) |
| `13_anagramas_permutaciones.py` | Anagramas, agrupación, permutaciones |
| `14_resumen.py` | Resumen de algoritmos de strings |

## Algoritmos Matemáticos (15-22)

| Archivo | Contenido |
|---------|-----------|
| `15_pascal.py` | Triángulo de Pascal, coeficientes binomiales, fila n |
| `16_euclides.py` | MCD (iterativo/recursivo), MCM, Euclides extendido |
| `17_eratostenes.py` | Criba de Eratóstenes, `es_primo_optimizado` |
| `18_exponenciacion_modular.py` | Exponenciación modular rápida (base^exp mod m) |
| `19_fibonacci_matematico.py` | Fibonacci: Binet y exponenciación de matrices |
| `20_factorizacion.py` | Factorización en primos, factores únicos, contar divisores |
| `21_conversion_bases.py` | Conversión entre bases (decimal, binario, octal, hex) |
| `22_resumen.py` | Resumen de algoritmos matemáticos |

## Backtracking (23-29)

| Archivo | Contenido |
|---------|-----------|
| `23_n_reinas.py` | N-Reinas: colocar N reinas sin que se ataquen |
| `24_sudoku.py` | Solucionador de Sudoku 9x9 |
| `25_laberinto.py` | Resolución de laberintos (camino inicio–destino) |
| `26_permutaciones_backtracking.py` | Generación de permutaciones |
| `27_combinaciones_backtracking.py` | Generación de combinaciones de k en n |
| `28_subset_sum.py` | Subset Sum (subconjuntos que sumen objetivo) |
| `29_resumen.py` | Resumen de backtracking |

## Estructuras de Datos Avanzadas (30-34)

| Archivo | Contenido |
|---------|-----------|
| `30_trie.py` | Trie (árbol de prefijos): insertar, buscar, autocompletar |
| `31_segment_tree.py` | Segment Tree: consulta/actualización de rango (suma, mín, máx) |
| `32_fenwick_tree.py` | Fenwick Tree (BIT): sumas de prefijos y rango |
| `33_union_find_mejorado.py` | Union-Find con path compression y union by rank |
| `34_resumen.py` | Resumen y complejidades |

## Algoritmos de Búsqueda (35-41)

| Archivo | Contenido |
|---------|-----------|
| `35_lineal.py` | Búsqueda lineal, optimizada, todas las ocurrencias |
| `36_binaria.py` | Búsqueda binaria (iterativa, recursiva, primera/última ocurrencia) |
| `37_strings.py` | Búsqueda de patrón en texto (fuerza bruta) |
| `38_kmp.py` | Algoritmo KMP (Knuth-Morris-Pratt) |
| `39_comparacion.py` | Compara lineal vs binaria y bruta vs KMP |
| `40_utilidades.py` | Posición de inserción, conteo de ocurrencias en lista ordenada |
| `41_resumen.py` | Resumen y recomendaciones |

**Dependencias:** 39 importa de 35, 36, 37, 38; 40 importa de 36.

## Otros (42)

| Archivo | Contenido |
|---------|-----------|
| `42_dataclass_inventory.py` | Ejemplo de dataclass para inventario |

## Métodos de Ordenamiento (43-53)

| Archivo | Contenido |
|---------|-----------|
| `43_utilidades.py` | `esta_ordenada()`, `generar_lista_aleatoria()` |
| `44_bubble.py` | Bubble Sort y versión optimizada |
| `45_selection.py` | Selection Sort |
| `46_insertion.py` | Insertion Sort |
| `47_merge.py` | Merge Sort y `merge()` |
| `48_quick.py` | Quick Sort y Quick Sort in-place |
| `49_heap.py` | Heap Sort y `heapify()` |
| `50_counting.py` | Counting Sort (rango pequeño) |
| `51_comparacion.py` | Compara tiempos de todos los métodos |
| `52_complejidad.py` | Tabla de complejidad (mejor/promedio/peor) |
| `53_casos_especiales.py` | Casos: ordenada, inversa, iguales, vacía |

**Dependencias:** 51 importa de 43–50; 53 importa de 43 y 47.

## Resumen de Ordenamiento

| Método | Complejidad | Notas |
|--------|-------------|-------|
| Bubble Sort | O(n²) | Simple, estable |
| Selection Sort | O(n²) | Simple, no estable |
| Insertion Sort | O(n²) peor, O(n) mejor | Estable, bueno para listas casi ordenadas |
| Merge Sort | O(n log n) | Estable, usa memoria extra |
| Quick Sort | O(n log n) promedio | In-place, no estable |
| Heap Sort | O(n log n) | In-place, no estable |
| Counting Sort | O(n + k) | Rango pequeño conocido |
| Python `sorted()` | O(n log n) | Timsort (híbrido) |

### Recomendaciones de uso

1. **Listas pequeñas (< 50):** Insertion Sort o Bubble Sort
2. **Listas medianas (50-1000):** Quick Sort o Merge Sort
3. **Listas grandes (> 1000):** Quick Sort, Merge Sort, Heap Sort o `sorted()`
4. **Rango de valores pequeño conocido:** Counting Sort
5. **Necesitas estabilidad:** Merge, Insertion, Bubble, Counting (evitar Quick, Heap)
6. **Poco espacio (in-place):** Quick Sort, Heap Sort, Insertion Sort (evitar Merge)
